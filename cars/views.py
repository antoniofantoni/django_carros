from django.shortcuts import render

# Create your views here.
def cars_views(request):
    return render(request, 'cars.html')
