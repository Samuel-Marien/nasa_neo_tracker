from django.shortcuts import render
import requests


def neo_home(request):
    return render(request,'neo_app/neo_home.html')

def neo_search(request):
    return render(request,'neo_app/neo_search.html')

def neo_result(request):
    user_start_date = request.GET.get('start_date')
    user_end_date = request.GET.get('end_date')
    # Expected format (yyyy-mm-dd)
    #pull data from NASA rest api
    response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={user_start_date}-09-07&end_date=2016-09-08&api_key=axrQkb17JHVEoxlaXS5H8em4lERotAP0ESB6pG2d')
    #convert reponse data into json
    neo_api_object = response.json()
    print(neo_api_object)
    return render(request,'neo_app/neo_result.html',{'user_start_date':user_start_date, 'user_end_date':user_end_date})