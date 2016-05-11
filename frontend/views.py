#encoding: utf-8

from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext, Context
from django.template.loader import render_to_string
from frontend.forms import AffiliationForm


def home(request):
    return render_to_response('index.html', request.session, context_instance=RequestContext(request))


def affiliation(request):

    if request.method == 'GET':
        form = AffiliationForm()
        return render_to_response('affiliation.html', {'form':form}, context_instance=RequestContext(request))

    if request.method == 'POST':
        form = AffiliationForm(request.POST, request.FILES)
        if form.is_valid():
            partner = form.save()
            send_webmail(partner.id)
            send_confirmation(partner)
            return redirect(reverse_lazy('frontend:affiliation_success'))
        return render_to_response('affiliation.html', {'form':form}, context_instance=RequestContext(request))


def affiliation_success(request):
    return render_to_response('affiliation_success.html', {}, context_instance=RequestContext(request))

def send_confirmation(user):
    data = Context({ 'name': user.first_name})
    text_template = render_to_string('confirmation.txt', data)
    html_template = render_to_string('confirmation.html', data)

    send_mail(
        subject=u'Se ha registrado su solicitud en ACTP', message=text_template,
        html_message=html_template, from_email='Web ACTP <web@actp.com.co>',
        recipient_list=[user.email,], fail_silently=False
    )


def send_webmail(id):
    data = Context({ 'id': id})
    text_template = render_to_string('email.txt', data)
    html_template = render_to_string('email.html', data)

    send_mail(
        subject=u'Solicitud a través de sitio Web', message=text_template,
        html_message=html_template, from_email='Web ACTP <web@actp.com.co>',
        recipient_list=['admin@actp.com.co',], fail_silently=False
    )
