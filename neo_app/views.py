from django.shortcuts import render, get_object_or_404
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
    # Add user's days coverage
    user_end_date_with_coverage = user_end_date + timedelta(days=int(user_day_coverage))
    user_end_date_sanityze = str(user_end_date_with_coverage)[0:10]

    # pull data from NASA rest api & convert reponse data into json format
    response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={user_start_date}&end_date={user_end_date_sanityze}&api_key=axrQkb17JHVEoxlaXS5H8em4lERotAP0ESB6pG2d')
   
    neos_api_object = response.json()
    neo_object_without_hearder = neos_api_object["near_earth_objects"]

    # append response in a list of objects
    neos_list = []
    for neo in neo_object_without_hearder[user_start_date]:
        neos_list.append(neo)
    # print(neos_list)

    return render(request,'neo_app/neo_result.html',
                  {'user_start_date':user_start_date,
                   'user_day_coverage':user_day_coverage,
                   'user_end_date_sanityze':user_end_date_sanityze,
                   'neos_api_object':neos_api_object,
                   'neo_object_without_hearder':neo_object_without_hearder,
                   'neos_list':neos_list })

def neo_detail(request, neoId):

    # pull data from NASA rest api & convert reponse data into json format
    response = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/{neoId}?api_key=axrQkb17JHVEoxlaXS5H8em4lERotAP0ESB6pG2d')
    neo_details = response.json()
    print(neo_details)

    return render(request,'neo_app/neo_detail.html',{'neoId':neoId})

