from typing import ChainMap
from django.http.response import HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string #allows use of HTML docs by converting them to str
from django.http import Http404
# Create your views here.

# def jan(request):
#     return HttpResponse("Request Accepted  for Jan.")
# # This function is created to handle url requests

# def feb(request):
#     return HttpResponse("February works baby!")


# dictionary URL
m_challenges = { 
    "january": "Jan is the goat",
    "february": "Feb is the cat",
    "march": "Ye-yeah!",
    "april": "Yoyo!",
    "may": "Forgot about MAY!",
    "june": None,
    "july": None,
    "august": None,
    "september": None,
    "october": None,
    "november": None,
    "december": None
}


# def index(request): #standard name for homepage func
#     # Inefficient way of creating index func
#     list_items = ""
#     months = list(m_challenges.keys())
    
#     for month in months:
#         capital_month = month.capitalize()
#         month_path = reverse("month-challenge", args =[month])
#         list_items += f"<li><a href=\"{month_path}\">{capital_month}</a></li>" # dont fucking forget {} for paths!!

#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)

def index(request): 
    # Standard index func
    months = list(m_challenges.keys())
    return render(request, "challenges/index.html", {
        "month_list": months 
    })

def monthpages_by_number(request, month):
# redirects numerical URLs to corresponding month
    months = list(m_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("number invalid, b*tch")
   
    redirect_months = months[month-1] # the -1 aligns the index 
    redirect_path = reverse("month-challenge", args =[redirect_months])
    
    return HttpResponseRedirect(redirect_path)
    

def monthpages(request, month): # second arg is the <placeholder> mentioned in urls
    # http response func receives request, lookup dictionary value then returns response
    try:
        challenge_text = m_challenges[month] # square brackets cite item inside dictionary
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        }) #shorthanded version of above 2 comments
    except:
        # response_data = render_to_string("404.html") 
        #return HttpResponseNotFound(response_data) # Obsolete command. Instead we raise the class 404 by importing http404
        raise Http404() # automatically looks for 404.html in root template folder.
                        # This is useful when deving since you get the bultin errors when urls dont work helping you troubleshoot
    
# The objective of your views.py is to keep the functions as lean as possible and avoid any hardcoded html.
#  Leave all html for the actual html documents


