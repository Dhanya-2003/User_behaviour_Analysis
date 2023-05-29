from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import pandas as pd
import json
import requests
from django.shortcuts import render

# from apps.home.models import MyModel # replace with your own model

def getRandomName():
    names = ['John', 'Jane', 'Alice', 'Bob', 'Chris']
    return names[0]

def table_view(request):
    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)
    data = response.json()

    context = {
        'data': data
    }

    return render(request, 'home/iTable.html', context)
# def my_view(request):
#     api_url = "https://jsonplaceholder.typicode.com/users"
#     response = requests.get(api_url)
#     data = response.json()
#     context = {'data': data}
#     return render(request, 'home/iTable.html', context)


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    




def add_rows(request):
    # Get the list of people from the database or wherever else you're getting it from
    new_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 40},
    ]
    
    # Get the existing list of people from the database or wherever else you're getting it from
    existing_people = [
        {'name': 'David', 'age': 35},
        {'name': 'Emily', 'age': 28},
    ]
    
    # Combine the existing and new lists of people
    people = existing_people + new_people
    
    # Render the template with the updated list of people
    return render(request, 'home/tables.html', {'people': people})
def df_create(api_url):
    response = requests.get(api_url)
    json_data = response.json()

    # Convert JSON data to a Python object
    py_obj = json.dumps(json_data)
    data = json.loads(py_obj)

    if 'features' in data:
        df = pd.json_normalize(data, record_path=['features'])
        return df
    else:
        return pd.DataFrame()
    
# def my_view(request):
#     lst =['1', '2', '3', '5', '12']
#     final_df = pd.DataFrame()

#     for x in lst:
#         url = "https://b.maps.owm.io/weather/cities/" + x + "/" + x + "/" + x + ".geojson?appid=b1b15e88fa797225412429c1c50c122a1"
#         df = df_create(url)
#         final_df = pd.concat([final_df, df])
#     html_table = final_df.to_html()
#     context = {'my_table': html_table}
#     return render(request, 'home/iTable.html', context)
