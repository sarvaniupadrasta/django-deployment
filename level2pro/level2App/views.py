from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict ={'insert_content':"hello level2"}
    return render(request,'level2App/index.html',context=my_dict)
