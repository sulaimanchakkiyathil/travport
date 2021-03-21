from django.shortcuts import render

# Create your views here.
def Main_Page(request):

    return render(request,'index.html')
