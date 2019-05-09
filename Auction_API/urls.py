from django.urls import path
from Auction_API import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auction/',views.AuctionsList.as_view()),
    path('auction/<int:pk>/', views.AuctionsDetail.as_view()),
    path('auction/<int:pk>/bids/', views.AuctionBidList.as_view()),
    path('auction/<int:pk>/comments/', views.AuctionCommentList.as_view()),
    path('bids/', views.BidPost.as_view()),
    path('bids/<int:pk>/', views.BidDelete.as_view()),
    path('comments/', views.CommentPost.as_view()),
    path('comments/<int:pk>/', views.CommentDelete.as_view()),
    path('signup/', views.CreateUser.as_view()),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]
