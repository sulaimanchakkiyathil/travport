from django.shortcuts import render

# Create your views here.
def Main_Page(request):
    user=request.user
    print(user)

    return render(request,'index.html',{'user':user})
