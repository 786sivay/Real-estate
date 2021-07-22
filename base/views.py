from django.shortcuts import render
from listings.models import listing1


# Create your views here.

def index(request):
    Listing=listing1.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings': Listing
    }
    return render(request,"pages/index.html",context)


def about(request):
    return render(request,"pages/about.html")


