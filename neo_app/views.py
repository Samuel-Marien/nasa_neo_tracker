from django.shortcuts import render
import datetime
from datetime import datetime, timedelta

import requests


def neo_home(request):
    return render(request,'neo_app/neo_home.html')

def neo_search(request):
    return render(request,'neo_app/neo_search.html')

def neo_result(request):
    user_start_date = request.GET.get('start_date')
    user_day_coverage = request.GET.get('day_coverage')

    # Expected format (yyyy-mm-dd)
    user_start_date_stringified = str(user_start_date)
    user_end_date = datetime.strptime(user_start_date_stringified, '%Y-%m-%d')
    user_end_date_with_coverage = user_end_date + timedelta(days=int(user_day_coverage))
    user_end_date_sanityze = str(user_end_date_with_coverage)[0:10]

    # pull data from NASA rest api & convert reponse data into json
    response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={user_start_date}&end_date={user_end_date_sanityze}&api_key=axrQkb17JHVEoxlaXS5H8em4lERotAP0ESB6pG2d')
    neo_api_object = response.json()
    print(neo_api_object)

    return render(request,'neo_app/neo_result.html',{'user_start_date':user_start_date, 'user_end_date':user_end_date,'user_day_coverage':user_day_coverage, 'user_end_date_sanityze':user_end_date_sanityze})