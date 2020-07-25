from django.shortcuts import render

def search(request):
    return render(request, 'findaridepublic/search.html')