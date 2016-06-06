
import json
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponse
from app.models import Region, City, Comments, RegionCity

# Create your views here.
def index(request):
    region = Region.objects.all()
    city = City.objects.all()
    return render_to_response(
        'comment.html',
        {
            'regions': region,
            'cities': city
        },
        context_instance=RequestContext(request)
    )

def addcomment(request):
    if request.POST:
        comment = Comments()
        comment.fname = request.POST.get('firstname')
        comment.name = request.POST.get('lastname')
        comment.lname = request.POST.get('secondname')
        comment.region_id = int(request.POST.get('region'))
        comment.city_id = int(request.POST.get('city'))
        comment.phone = request.POST.get('phone')
        comment.email = request.POST.get('email')
        comment.comment = request.POST.get('comment')
        comment.save()
        return HttpResponse(json.dumps(""))
    else:
        raise Http404

def selectregion(request):
    if request.POST:
        id = int(request.POST.get('id'))
        if id == 0:
            cities = City.objects.all()
        else:
            cities = City.objects.select_related().filter(regioncity__region=id)
        template = render_to_response(
            'selectorcity.html',
            {
                'cities': cities
            },
            context_instance=RequestContext(request)
        )
        del template['Content-Type']
        del template['charset']
        data = {'template' : "%s" % template}
        return HttpResponse(json.dumps(data))
    else:
        raise Http404

def selectorcity(request):
    if request.POST:
        id = int(request.POST.get('id'))
        selectid = 0
        if id != 0:
            region = Region.objects.select_related().get(regioncity__city=id)
            selectid = region.id
        return HttpResponse(selectid)
    else:
        raise Http404
