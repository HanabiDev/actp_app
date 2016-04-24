from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from partners.forms import PartnerForm
from partners.models import Partner


def home(request):
	partners = Partner.objects.all().order_by('-date_joined')
	return render_to_response('partners_index.html', {'clubs':partners}, context_instance=RequestContext(request))

def create_partner(request):
	if request.method == 'GET':
		form = PartnerForm()
		return render_to_response('partner.html', {'form': form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PartnerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse_lazy('clubs:home'))

		return render_to_response('partner.html', {'form': form}, context_instance=RequestContext(request))