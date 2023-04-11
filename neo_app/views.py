from django.shortcuts import render


def neo_home(request):
    return render(request,'neo_app/neo_home.html')

def neo_search(request):
    return render(request,'neo_app/neo_search.html')

def neo_result(request):
    user_start_date = request.GET.get('start_date')
    user_end_date = request.GET.get('end_date')
    return render(request,'neo_app/neo_result.html',{'user_start_date':user_start_date, 'user_end_date':user_end_date})