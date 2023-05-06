from django.shortcuts import render
import datetime


def index(request):
    date = datetime.datetime.now().date()
    name = "Andrew"
    context = {"date": date, "name": name}
    return render(request, "index.html", context=context)
