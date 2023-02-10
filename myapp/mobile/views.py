from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render 

def mobilelist(request):
    print("MMMMMMM")
    l1 = [34,2,55,12,78,90,35]
    s1 = "ramkumari yadav"
    t1 = (2,3,4,5,89,99)
    data = {
        'l1': l1,
        's1': s1,
        't1': t1,
        'v1': False,
        "name" : {"subject": "english", "marks" : [34,23,45]},

    }
    # return HttpResponse(" List o f  mobile phones")
    return render(request, "mobile.html", data)


