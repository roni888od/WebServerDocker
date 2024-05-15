from django.shortcuts import render
from .models import MyModel

def index(request):
    my_objects = MyModel.objects.all()
    return render(request, 'index.html', {'my_objects': my_objects})