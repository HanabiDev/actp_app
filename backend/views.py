#encoding: utf-8

# Create your views here.
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from ACTP.auth_checks import is_superuser


def login_user(request):
    logout(request)
    username = password = ''
    error = False
    next = ""

    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and user.is_superuser:
                    login(request, user)
                    if next == "":
                        return redirect(reverse_lazy('admin_home'))
                    else:
                        return redirect(next)
                else:
                    if not user.is_superuser:
                        error = 'No posee permisos de administrador'
                    else:
                        error = 'Usuario no activo'
            else:
                error = 'Credenciales no válidas'
        else:
            error = 'Usuario y contraseña requeridos'
    return render_to_response('admin_login.html', {'error':error, 'next':next, 'site_user':username}, context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('backend_login'))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def home(request):
    return render_to_response('backend_index.html', request.session, context_instance=RequestContext(request))
