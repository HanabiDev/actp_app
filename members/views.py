from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from partners.models import Equipment


@login_required(login_url=reverse_lazy('backend_login'))
def home(request):
	return render_to_response('partners_index.html', {}, context_instance=RequestContext(request))
