from django.shortcuts import render
from .models import banner
# Create your views here.

def index(req):
    all_banner = banner.objects
    return render(req , 'index.html',{'all_banner':all_banner})