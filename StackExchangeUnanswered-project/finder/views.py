from django.shortcuts import render
import json
import requests


def home(request):
    response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
    return render(request, "finder/home.html")