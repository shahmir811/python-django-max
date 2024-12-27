from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "This world is full of challenges. But we are here to face them all. Let us start with the first one. The first challenge is to create a Django project and run it on the server. Let us see if you can do it. Good luck!",
    "february": "This is the challenge for February. The challenge is to create a Django app and run it on the server. Let us see if you can do it. Good luck!",
    "march": "This is the challenge for March. The challenge is to create a Django model and run it on the server. Let us see if you can do it. Good luck!",
    "april": "This is the challenge for April. The challenge is to create a Django view and run it on the server. Let us see if you can do it. Good luck!",
    "may": "This is the challenge for May. The challenge is to create a Django template and run it on the server. Let us see if you can do it. Good luck!",
    "june": "This is the challenge for June. The challenge is to create a Django URL and run it on the server. Let us see if you can do it. Good luck!",
    "july": "This is the challenge for July. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
    "august": "This is the challenge for August. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
    "september": "This is the challenge for September. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
    "october": "This is the challenge for October. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
    "november": "This is the challenge for November. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
    "december": "This is the challenge for December. The challenge is to create a Django model form and run it on the server. Let us see if you can do it. Good luck!",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    
    response_date = f"<ul>{list_items}</ul>"
    return HttpResponse(response_date)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        response_date = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_date)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")