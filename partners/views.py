#encoding: utf-8
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from django.utils import timezone
from ACTP.auth_checks import is_superuser
from partners.forms import PartnerForm, EditPartnerForm, PasswordForm
from partners.models import Partner
from django.http.response import HttpResponse
from qrcode import *

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate_objects(page, objects, per_page=10):
    paginator = Paginator(objects,per_page)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def home(request):
    if request.method == 'GET':
        partners = Partner.objects.all().order_by('-date_joined')
        count = partners.count()
        page = request.GET.get('page')
        partners = paginate_objects(page,partners)

    return render_to_response('partners_index.html', {'count':count,'partners': partners}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
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


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def read_partner(request, partner_id):
	partner = Partner.objects.get(id=partner_id)
	return render_to_response('partner_detail.html', {'partner': partner}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
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


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
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




@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def accept_member(request, partner_id):
	partner = Partner.objects.get(id=partner_id)
	partner.is_approved = True
	partner.member_since = timezone.now()
	partner.save()
	return redirect('partners:view', partner_id=partner_id)



@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def toggle_status(request, partner_id):
	partner = Partner.objects.get(id=partner_id)
	partner.is_active = not partner.is_active
	partner.save()
	return redirect(reverse_lazy('partners:home'))



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


def report(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    xlsx_data = WriteToExcel()
    response.write(xlsx_data)
    return response


import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.contrib.auth.models import User
 
def WriteToExcel():
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
 
    # Here we will adding the code to add data
    worksheet_s = workbook.add_worksheet("Summary")
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    cell = workbook.add_format({
        'bg_color': '#FFFFFF',
        'color': 'black',
        'align': 'justify',
        'valign': 'middle',
        'border': 1
    })

    cell_center = workbook.add_format({
        'bg_color': '#FFFFFF',
        'color': 'black',
        'align': 'center',
        'valign': 'middle',
        'border': 1
    })



    title_text = u"Reporte de inscritos al Primer Torneo Nacional de FT 2017 - Sutamarchán"
    worksheet_s.merge_range('A2:D2', title_text, title)

    worksheet_s.write(4, 0, ugettext("#"), header)
    worksheet_s.write(4, 1, ugettext("Documento"), header)
    worksheet_s.write(4, 2, ugettext("Nombre completo"), header)
    worksheet_s.write(4, 3, ugettext("Club"), header)

    worksheet_s.set_column('B:B', 13)
    worksheet_s.set_column('C:C', 40)
    worksheet_s.set_column('D:D', 30)
    worksheet_s.set_row(4, 28)
    
    # the rest of the headers from the HTML file

    partners = User.objects.filter(suscribed=True)    

    for idx, partner in enumerate(partners):
        row = 5 + idx
        worksheet_s.write_number(row, 0, idx + 1, cell_center)
        worksheet_s.write_string(row, 1, str(partner.doc_id), cell)
        worksheet_s.write_string(row, 2, partner.get_full_name(), cell)
        worksheet_s.write(row, 3, partner.club.name, cell_center)
        # the rest of the data

 
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data
