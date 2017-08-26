from django.shortcuts import render
#from django.http import HttpResponse
#from AppTwo.models import User
from AppTwo.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')


def user(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("error form invalid")

    return render(request,'AppTwo/user.html',{'form':form})
    #userlist = User.objects.order_by('firstname')
    ##user_dict={'user_list':userlist}
    #return render(request,'AppTwo/user.html',context=user_dict)
