
import json
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from app.models import Comments

# Create your views here.
def index(request):
    try:
        comments = Comments.objects.all().select_related()
    except:
        comments = None
    return render_to_response(
        'view.html',
        {
            'comments': comments
        },
        context_instance=RequestContext(request)
    )

def delcomment(request):
    if request.POST:
        comment = Comments.objects.get(id=int(request.POST.get('id')))
        comment.delete()
        return HttpResponse(json.dumps(""))
    else:
        raise Http404
