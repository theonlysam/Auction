from rest_framework import serializers
from django.contrib.auth.models import User
from Auction_API.models import Auction
from Auction_API.models import Comment
from Auction_API.models import Bid
 

class UserSerializer(serializers.ModelSerializer):
    'Serialize user objects'
    class Meta:
        model = User
        fields = ('username',)

class AuctionSerializer(serializers.ModelSerializer):
    'Serializer Auction objects'
    class Meta:
        model = Auction
        fields = '__all__'
        
class AuctionImageSerializer(serializers.ModelSerializer):
    'Serialize Auction Image'
    class Meta:
        model = Auction
        fields = ('image_url',)

class CommentSerializer(serializers.ModelSerializer):
    'Serialize Comments'
    class Meta:
        model = Comment
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    'Serialize Bids'
    class Meta:
        model = Bid
        fields = '__all__'