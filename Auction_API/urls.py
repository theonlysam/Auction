from django.urls import path
from Auction_API import views

urlpatterns = [
    path('auction/',views.AuctionsList.as_view()),
]
