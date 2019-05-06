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
from django.http import Http404


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

class AuctionsDetail(APIView):
    'Retrieve, update or delete an Auction'

    def get_object(self, pk):
        try:
            return Auction.objects.get(pk=pk)
        except Auction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        auction = self.get_object(pk)
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)

    def put(self, request, pk):
        auction = self.get_object(pk)
        serializer = AuctionSerializer(auction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        auction = self.get_object(pk)
        serializer = AuctionSerializer(auction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        auction = self.get_object(pk)
        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class AuctionBidList(APIView):
    'List all bids related to an auction'
    def get(self,request,pk):
        bids = Bid.objects.filter(auction=pk)
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data)

class AuctionCommentList(APIView):
    'List all comments related to an auction'
    def get(self,request,pk):
        comments = Comment.objects.filter(auction=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class BidPost(APIView):
    'Create Bid'
    def post(self, request):
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class BidDelete(APIView):
    'Delete Bid'
    def get_object(request, pk):
        try:
            return Bid.objects.get(pk=pk)
        except Bid.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        bid = self.get_object(pk)
        bid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)