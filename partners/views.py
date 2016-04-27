from _ast import Set
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from partners.forms import PartnerForm, EditPartnerForm, PasswordForm
from partners.models import Partner
from django.http.response import HttpResponse
from qrcode import *


def home(request):
	partners = Partner.objects.all().order_by('-date_joined')
	return render_to_response('partners_index.html', {'partners': partners}, context_instance=RequestContext(request))


def create_partner(request):
	if request.method == 'GET':
		form = PartnerForm()
		return render_to_response('partner.html', {'form': form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PartnerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse_lazy('partners:home'))

		return render_to_response('partner.html', {'form': form}, context_instance=RequestContext(request))


def update_partner(request, partner_id):
	pass_change = False
	if request.session.get('pass_changed'):
		pass_change = True
		del request.session['pass_changed']

	partner = Partner.objects.get(id=partner_id)

	if request.method == 'GET':
		form = EditPartnerForm(instance=partner)
		return render_to_response('partner.html', {
			'form': form, 'pass':pass_change, 'editing':True, 'partner':partner
		}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = EditPartnerForm(request.POST, request.FILES, instance=partner)
		if form.is_valid():
			form.save()
			return redirect(reverse_lazy('partners:home'))
		return render_to_response('partner.html', {
			'form': form, 'pass':pass_change, 'editing':True, 'partner':partner
		}, context_instance=RequestContext(request))


def update_password(request, partner_id):
	user = Partner.objects.get(id=partner_id)

	if request.method == 'GET':
		form = PasswordForm(user, None)
		return render_to_response('update_password.html', {'form':form, 'editing':True, 'site_user':user}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PasswordForm(user,request.POST)
		if form.is_valid():
			form.save()
			request.session['pass_changed']=True
			return redirect('partners:edit', partner_id=partner_id)

		return render_to_response('update_password.html', {'form':form, 'editing':True, 'site_user':user}, context_instance=RequestContext(request))







def get_qr(request):
    text = request.GET.get('data')
    qr = generate_qr_code(text, 10, 2)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response


def generate_qr_code(data, size=10, border=0):
	qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=size, border=border)
	qr.add_data(data)
	qr.make(fit=True)
	return qr.make_image()