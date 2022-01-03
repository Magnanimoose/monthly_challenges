from django.urls import path
from . import views # the "." means from same current folder
from django.urls import reverse

"""This is the URL config the order the paths are listed is important"""
urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthpages_by_number),
    path("<str:month>", views.monthpages, name="month-challenge") # this is a dynamic path and segment, prevents long list of paths. Good for writing blogs
    
]

# name=monthly-challenge is added to create a reverse path for url challenge (as opposed to challenge(s) this is to avoid dev probs in the long term)
# if request january is made, execute fuction index from views