from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def reverse(request):
    djtext = request.GET.get("reverse","default")

    final_text = djtext[::-1]

    para = {
        "answer":final_text,
        "purpose":"reversed"
    }
    return render(request,"base.html",para)


def removepunc(request):
    djtext = request.GET.get("removepunc","default")


    mark = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+",",","<",">",".","/","?","{","}","[","]","'",'"']
    ans = ""
    for i in djtext:
        if i not in mark:
            ans += i

    para = {
        "answer":ans,
        "purpose":"punctuation markless"
    }

    return render(request,"base.html",para)


def countChar(request):
    djtext = request.GET.get("countChar","default")
    ans = len(djtext)

    para = {
        "answer":ans,
        "purpose":"charactor count of your"
    }
    return render(request,"base.html",para)


def CapChar(request):
    djtext = request.GET.get("CapChar","default")
    ans = djtext.upper()

    para = {
        "answer":ans,
        "purpose":"capitalized"
    }
    return render(request,"base.html",para)
    