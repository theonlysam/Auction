from django.urls import path
from Auction_UI import views

urlpatterns = [
    path('', views.auction_list, name='auctions'),
    path('search/', views.search_auction, name='search'),
    path('<int:pk>/', views.auction_detail, name='auction_detail'),
]