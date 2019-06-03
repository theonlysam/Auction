from __future__ import unicode_literals

from django.shortcuts import render
import requests.exceptions
from django.views import View

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

def get_url(url):
    'Query url and return json response/data'
    try:
        response = requests.get(url)
    except:
        pass
    else:        
        return response.json()
    

def auction_detail(request, pk):
    'Display the detail for the individual Auction items'
    auction_detail_endpoint = url+'auction/'+ str(pk) + '/'
    auction_bid_endpoint = auction_detail_endpoint + 'bids/'
    auction_comment_endpoint = auction_detail_endpoint + 'comments/'
    
    auction = get_url(auction_detail_endpoint)    
    auction_bids = get_url(auction_bid_endpoint)
    auction_comments = get_url(auction_comment_endpoint)

    return render(request, 'Auction_UI/auction_detail.html', {'auction': auction,
                                                            'auction_bids': auction_bids,
                                                            'auction_comments': auction_comments
                                                            })


class auction_signup(View):
    'Displays and handles the sign up form'

    def get(self, request):
        'Display the sign up form'
        return render(request, 'Auction_UI/auction_signup.html', {})

    def post(self, request):
        'Process the submitted data'
        pass

class auction_login(View):
    'Display and handles the login form'

    def get(self, request):
        'Display the login form'
        return render(request, 'Auction_UI/auction_login.html',{})

    def post(self, request):
        'Process the login info'
        pass



