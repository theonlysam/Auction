from django.db import models

from django.contrib.auth import get_user_model

def upload_image_path(instance, filename):
        'File will be uploaded to MEDIA_ROOT/auction_<id>/filename'
        return 'Auction/%Y/%m/%d/{}'.format(filename)

class Auction(models.Model):
    'Model to store items for auction'
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image_url = models.FileField(upload_to=upload_image_path) #blank=False, null=False)
    base_price = models.DecimalField(max_digits=19, decimal_places=0)
    start_datetime = models.DateTimeField("Start Date/Time", auto_now=False, auto_now_add=False)
    end_datetime = models.DateTimeField("End Date/Time", auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('start_datetime',)

    def __str__(self):
        return '{} by {}'.format(self.title, self.owner)

    

'''
class Images(model.Model):
    'Model to store Auction Images'
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    image_url = models.FileField(blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.image_url)
'''

class Comment(models.Model):
    'Model to store user comments'
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    message = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.message)
        


class Bid(models.Model):
    'Bids made by users'
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount_offered = models.DecimalField(max_digits=19, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} who bid ${}'.format(self.user, self.amount_offered)
