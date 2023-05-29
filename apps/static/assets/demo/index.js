try{
    // $(document).ready(function () {
    //     // Javascript method's body can be found in assets/js/demos.js
    //     demo.initDashboardPageCharts();
    // });

} catch(error){
    console.error('Error in index.html page', error);
}

try{
    + function(l, y, t, i, c, s) {
        l['LocalyticsGlobal'] = i;
        l[i] = function() {
            (l[i].q = l[i].q || []).push(arguments)
        };
        l[i].t = +new Date;
        (s = y.createElement(t)).type = 'text/javascript';
        s.src = '//web.localytics.com/v4/localytics.min.js';
        (c = y.getElementsByTagName(t)[0]).parentNode.insertBefore(s, c);
        ll('init', '6ad135797500443614cb908-60a48cae-d47c-11ed-c697-007c928ca240', {} /* Options */ );
        console.log("connection successful");
        

    }(window, document, 'script', 'll');
} catch(error){
    console.log('Error connecting to Localytics');
}