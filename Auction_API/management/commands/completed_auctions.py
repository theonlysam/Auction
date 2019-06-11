from django.core.management.base import BaseCommand
from Auction_API.models import Auction
from Auction_API.models import Bid
from datetime import datetime
from django.db.models import Max
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        auctions = Auction.objects.filter(end_datetime__lte=datetime.now())         
        for auction in auctions:  
            bids = auction.bid_set.all().order_by('-amount_offered').first()
            print('Highest bidder for {} was  {}'.format(auction,bids))
            
      