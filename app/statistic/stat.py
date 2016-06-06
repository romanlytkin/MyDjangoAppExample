
import json
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from app.models import Region, City, Comments
from django.db.models import Count

# Create your views here.
def index(request):
    satistics = Region.objects.select_related().values('id', 'region_name', 'comments__region_id').annotate(count=Count('comments__region_id')).filter(count__gt=5)
    return render_to_response(
        'stat.html',
        {
            'satistics': satistics
        },
        context_instance=RequestContext(request)
    )

def statbyregion(request, region_id):
    satistics = City.objects.select_related().filter(comments__region_id=region_id).values('id', 'city_name', 'comments__city_id').annotate(count=Count('comments__city_id'))
    return render_to_response(
        'statbyregion.html',
        {
            'region_id': region_id,
            'satistics': satistics
        },
        context_instance=RequestContext(request)
    )

def statbycity(request, region_id, city_id):
    comments = Comments.objects.filter(region_id=region_id, city_id=city_id)
    return render_to_response(
        'view.html',
        {
            'comments': comments
        },
        context_instance=RequestContext(request)
    )
