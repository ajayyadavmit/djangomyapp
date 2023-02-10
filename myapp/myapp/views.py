from django.http import HttpResponse
from django.shortcuts import render
from mobile.models import Mobile

def laptopproduct(request):    
    print(dir(HttpResponse))
    print("##"*22, dir(request))
    return HttpResponse(" THese are the laptop products")


def laptoplist(request):
    print("LLL"*44)

    if request.method == 'GET': 
        n = request.GET.get('mobilename')
        c = int(request.GET.get('cost'))
        l = request.GET.get('location')
        print(n,c,l, sep='\t\t')
## Steps are .. >> Call Database,, Write query, Save query and Save the data in DB .... 
# create DB 
        m1 = Mobile()
        m1.name = n
        m1.cost = c
        m1.location = l
        m1.save()
        print("Success DB Insertedd Here >>")
        m2 = Mobile.objects.all()



    return render(request, "laptop.html", {'m2': m2})

def dynamic(request,routevalue):
    print(routevalue)
    print(type(routevalue))

    return HttpResponse(routevalue)

#slug cannot take the value of @ or special characters excpet _ underscore values.. 

def notype(request,ntype):
    print("NO TYPE OF Specific Data types INT STR SLUG NOTYPE <>  <int: value> ")
    print(type(ntype))
    return HttpResponse(ntype)