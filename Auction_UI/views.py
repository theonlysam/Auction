from __future__ import unicode_literals

from django.shortcuts import render
import requests.exceptions
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

url = 'http://127.0.0.1:8000/api/'
 
def get_url(url, params=None):
    'Query url and return json response/data'
    try:
        response = requests.get(url, params)
    except:
        pass
    else:        
        return response.json()

def post_url(url, data=None):
    try:
        response = requests.post(url, data)
    except:
        pass
    else:        
        return response.json()

class auction_list(View):

    def get(self, request):
        'Display list of Auctions'
        endpoint = 'auction/'

        auction_list = get_url(url+endpoint)
        return render(request, 'Auction_UI/auction_list.html', 
                                {'auction_list': auction_list})

class search_auction(View):

    def get(self,request):
        'Display records matching search criteria'
        endpoint = 'auction/'
        search_text = request.GET.get('search')
        params = {'search': search_text }

        auction_list = get_url(url+endpoint,params)     
        return render(request, 'Auction_UI/auction_list.html', 
                                {'auction_list': auction_list,
                                'search_text': search_text})
    
class auction_detail(View):

    def get(self,request, pk):
        'Display the detail for the individual Auction items'
        auction_detail_endpoint = url+'auction/'+ str(pk) + '/'
        auction_bid_endpoint = auction_detail_endpoint + 'bids/'
        auction_comment_endpoint = auction_detail_endpoint + 'comments/'

        auction = get_url(auction_detail_endpoint)    
        auction_bids = get_url(auction_bid_endpoint)
        auction_comments = get_url(auction_comment_endpoint)

        return render(request, 'Auction_UI/auction_detail.html', 
                                            {'auction': auction,
                                            'auction_bids': auction_bids,
                                            'auction_comments': auction_comments})


class auction_signup(View):
    'Displays and handle the sign up form'

    def get(self, request):
        'Display the sign up form'
        return render(request, 'Auction_UI/auction_signup.html')

    def post(self, request):
        'Process the submitted data'
        endpoint = 'signup/'
        data = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'password': request.POST.get('password'),
                }
        response = post_url(url+endpoint, data)        
        if response:
            ###Todo
            #log in the user 
            #redirect to auction_list
            #auction_login.post()
            return redirect('../auction_login')
        else:
            return redirect('../auction_signup')

        

class auction_login(View):
    'Display and handle the login form'

    def get(self, request):
        'Display the login form'
        return render(request, 'Auction_UI/auction_login.html')

    def post(self, request):
        'Process the login info'
        
        obtainJWT = 'login/'
        refreshJWT = 'login/refresh/'        
        data = {
                'username': request.POST.get('username'), 
                'password': request.POST.get('password') 
                }        
        # login not working for incorrect passwords
        # what to check for in the return
        response = post_url(url+obtainJWT,data)
        if response['detail'] == 'No active account found with the given credentials':    
            return redirect('../auction_login')            
        else:
            response = post_url(url+refreshJWT, data={'refresh': response['refresh']})
            #Set the authenticated variable 
            #Store the access_token for use by other urls
            #redirect to the auction list page            
            access_token = response['access']
            return render(request, 'Auction_UI/test_login.html', {'response': response})        
            


class auction_new(View):
    'Display and handle the new item form'

    def get(self, request):
        'Display the new auction item form'
        return render(request, 'Auction_UI/auction_new.html')

    def post(self, request):
        'Process the new auction item form'
        endpoint = 'auction_new/'
        data = {
                'item': request.POST.get(''),
                'email': request.POST.get('email'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'password': request.POST.get('password'),
                }
        response = post_url(url+endpoint, data)        
        if response:
            ###Todo
            #log in the user 
            #redirect to auction_list
            #auction_login.post()
            return redirect('../auction_login')
        else:
            return redirect('../auction_signup')
        


