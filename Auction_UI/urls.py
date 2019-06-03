from django.urls import path
from Auction_UI import views

urlpatterns = [
    path('', views.auction_list, name='auctions'),
    path('search/', views.search_auction, name='search'),
    path('<int:pk>/', views.auction_detail, name='auction_detail'),
    path('auction_signup/', views.auction_signup.as_view(), name='auction_signup'),
    path('auction_login/', views.auction_login.as_view(), name="auction_login"),
]