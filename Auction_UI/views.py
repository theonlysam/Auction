from __future__ import unicode_literals

from django.shortcuts import render
import requests.exceptions

url = 'http://127.0.0.1:8000/api/'

def auction_list(request):
    'Display list of Auctions'
    endpoint = 'auction/'
    try:
        response = requests.get(url+endpoint)
    except:
    #except requests.exceptions.RequestException:
        pass

    else:
        return render(request, 'Auction_UI/auction_list.html', {'auction_list': response.json()})


def search_auction(request):
    'Display records matching search criteria'
    return render(request, 'Auction_UI/auction_list.html', {})

def auction_detail(request, pk):
    'Display the detail for the individual Auction items'
    endpoint = 'auction/'+ str(pk) + '/'
    try:
        response = requests.get(url+endpoint)
    except:
        pass
    else:
        return render(request, 'Auction_UI/auction_detail.html', {'auction': response.json()})
