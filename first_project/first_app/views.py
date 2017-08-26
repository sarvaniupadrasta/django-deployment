from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Webpage,Topic

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    ##mydict = {'insert_me':'yo yo url'}
    return render(request,'first_app/index.html',context=date_dict)
    
