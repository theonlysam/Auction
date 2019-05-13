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
        bids = auctions.filter()
        '''for auction in auctions:
            #self.stdout.write(auction)
            bid = Bid.objects.filter(auction=auction)
            print(bid)
         '''   
        #$time = timezone.now().strftime('%X')
        #self.stdout.write("It's now %s" % time)