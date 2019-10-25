from django.shortcuts import render
from django.http import HttpResponse
def listings(req):
    
    return render(req, 'listings/listings.html')

def listing(req):
    return render(req, 'listings/listing.html')