#encoding: utf-8
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from ACTP.auth_checks import is_superuser
from clubs.forms import ClubForm
from clubs.models import Club

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def home(request):
	clubs = Club.objects.all().order_by('foundation')
	return render_to_response('clubs_index.html', {'clubs':clubs}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def create_club(request):
	if request.method == 'GET':
		form = ClubForm()
		return render_to_response('club.html', {'form': form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = ClubForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse_lazy('clubs:home'))

		return render_to_response('club.html', {'form': form}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def read_club(request, club_id):
    club = Club.objects.get(id=club_id)
    return render_to_response('club_detail.html', {'club':club}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def update_club(request, club_id):
	club = Club.objects.get(id=club_id)

	if request.method == 'GET':
		form = ClubForm(instance=club)
		return render_to_response('club.html', {
			'form': form, 'editing':True, 'logo': club.logo, 'heading':club.header_image, 'name':club.name
		}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = ClubForm(request.POST, request.FILES, instance=club)
		if form.is_valid():
			form.save()
			return redirect(reverse_lazy('clubs:home'))

		return render_to_response('club.html', {
			'form': form, 'editing':True, 'logo': club.logo, 'heading':club.header_image, 'name': club.name
		}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def toggle_status(request, club_id):
	club = Club.objects.get(id=club_id)
	club.is_active = not club.is_active
	club.save()
	return redirect(reverse_lazy('clubs:home'))
