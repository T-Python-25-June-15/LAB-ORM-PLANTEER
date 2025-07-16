from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def main_page(request: HttpRequest):

  return render(request, "main/index.html")