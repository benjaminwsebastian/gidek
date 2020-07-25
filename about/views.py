from django.shortcuts import render

def team(request):
    return render(request, 'about/our_team.html')

def plan(request):
    return render(request, 'about/our_plan.html')