from django.contrib import admin
from Auction_API.models import Auction
from Auction_API.models import Comment
from Auction_API.models import Bid

# Register your models here.
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Bid)
