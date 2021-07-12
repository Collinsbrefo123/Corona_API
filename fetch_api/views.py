import requests as rq
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def fetchapi(request):

    # if request.method == 'P0ST':
    #     search_query = request.GET.get('search', '')



    response = rq.get('https://corona-api.com/countries', ).json()

    response_data = response['data']
    count = len(response_data)
    print(count)
    #searching for the name
    search_query = request.GET.get('search', '').capitalize()
    print(search_query)
    if search_query:
        for idx,num in enumerate(response_data):
            if num['name'] == search_query:
                print(num['name'])
                print(response_data[idx])
                response_data =[response_data[idx]]


    page_number = request.GET.get('page', 1)
    paginator = Paginator(response_data, 10)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    # print(paginator.page_range)

    return render(request, 'fetch.html',
                  {'response': page.object_list, 'pages': page, 'next_url': next_url, 'prev_url': prev_url, 'count':count})


def fetchcountry(request, code):
    country_Code = code
    country_Code.upper()
    responseCountry = rq.get('https://corona-api.com/countries/' + country_Code + '', ).json()
    print(responseCountry['data']['name'])

    return render(request, 'fetchcountry.html', {'countrydata': responseCountry['data']})
