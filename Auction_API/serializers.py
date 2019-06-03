from rest_framework import serializers
from django.contrib.auth.models import User
from Auction_API.models import Auction
from Auction_API.models import Comment
from Auction_API.models import Bid
 

class UserSerializer(serializers.ModelSerializer):
    'Serialize user objects'
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)

    def create(self, validated_data):
        'Hash user password'
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

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


'''
To update password will need to override the update method
https://stackoverflow.com/questions/50755874/put-method-makes-invalid-password-format-or-unknown-hashing-algorithm-drf/50756429
'''