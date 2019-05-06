from django.shortcuts import render
from Auction_API.models import Auction
from Auction_API.models import Comment
from Auction_API.models import Bid
from django.contrib.auth.models import User
from rest_framework import generics
from Auction_API.serializers import UserSerializer
from Auction_API.serializers import AuctionSerializer
from Auction_API.serializers import CommentSerializer
from Auction_API.serializers import BidSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
"""
class AuctionsList(generics.ListCreateAPIView):
    'List all Auctions, or create a new auction'
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class AuctionsDetail(generics.RetrieveUpdateDestroyAPIView):
    'Process specific Auction'
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

"""
class AuctionsList(APIView):
    'List all Auctions, or create a new auction'

    def get(self,request):
        'Process GET request'
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)

    def post(self,request):
        'Process POST request'
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""
def AuctionList(request):
    return HttpResponse("test")
"""
