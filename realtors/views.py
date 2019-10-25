from django.shortcuts import render
from django.http import HttpResponse
def realtors(req):
    return render(req, "realtors/realtors.html")