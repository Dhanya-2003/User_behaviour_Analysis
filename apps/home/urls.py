# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('add_rows/', views.add_rows, name='add_rows'),
    
    path('table_view/', views.table_view, name='table_view'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
