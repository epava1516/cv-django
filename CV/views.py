from multiprocessing import context
from django.shortcuts import render
import yaml

# Create your views here.
def index_html(request):
  with open('variables.yml') as info:
    context = yaml.load(info)

  return render(request, "index.html", context)

def edit_html(request):
    return render(request, "edit.html")
