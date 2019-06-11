from django.urls import path
from Auction_UI import views

urlpatterns = [
    path('', views.auction_list.as_view(), name='auctions'),
    path('search/', views.search_auction.as_view(), name='search'),
    path('<int:pk>/', views.auction_detail.as_view(), name='auction_detail'),
    path('auction_signup/', views.auction_signup.as_view(), name='auction_signup'),
    path('auction_login/', views.auction_login.as_view(), name="auction_login"),
    path('auction_new/', views.auction_new.as_view(), name="auction_new"),
]