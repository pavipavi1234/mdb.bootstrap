from django.shortcuts import render

# Create your views here.
def mdb(request):
    return render(request,'mdb.html')
def bg(request):
    return  render(request,'bg.html')