from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext


def home(request):
	return render_to_response('index.html', request.session, context_instance=RequestContext(request))