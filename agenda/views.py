from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from agenda.forms import RegistrationForm, LoginForm, MessageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Contacts, FriendsRequest, ListMessages

# Create your views here.

def inicio(request):
    
    usuario_actual = request.user

    contactos = Contacts.objects.filter(belongs_to = usuario_actual)

    return render(request, 'index.html', {
        'contacts': contactos
    })

def loginRegister(request):

    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:  # Si se envió el formulario de inicio de sesión
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
                else:
                    messages.warning(request, 'Usuario o contraseña inválidos')
        elif 'register_submit' in request.POST:  # Si se envió el formulario de registro
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                messages.success(request, 'Te has registrado correctamente')
                return redirect('inicio')
        else:
            login_form = LoginForm()
            registration_form = RegistrationForm()
 
    return render(request, 'loginRegister.html', {
        'login_form': login_form,
        'registration_form': registration_form
    })

@login_required(login_url='login-register')
def logout_user(request):
    logout(request)
    return redirect('inicio')

@login_required(login_url='login-register')
def search_friends(request):
    
    if request.method == 'POST':
        search = request.POST['search']

        usuario_actual = request.user

        searched = User.objects.filter(username__contains = search.strip()).exclude(id = usuario_actual.id)
        
        contactos = Contacts.objects.filter(belongs_to = usuario_actual)

        lista_contactos = [contacto.username for contacto in contactos]

        solicitudes = FriendsRequest.objects.filter(username = usuario_actual)

        lista_solictudes = [solicitud.id_requested for solicitud in solicitudes]

        return render(request, 'search_friends.html', {
            'search': search,
            'searched': searched,
            'contactos': contactos,
            'lista_contactos': lista_contactos,
            'lista_solictudes': lista_solictudes,
            'solicitudes': solicitudes
            }
        )
    else:
        return render(request, 'search_friends.html')

@login_required(login_url='login-register')
def send_request(request, requested):

    usuario_actual = request.user

    id_actual = usuario_actual.id

    username = usuario_actual

    solicitud = FriendsRequest(
        user_id = id_actual,
        username = username,
        id_requested = requested
    )

    solicitud.save()
    
    messages.success(request, 'Solicitud de amistad enviada')

    return redirect('inicio')

@login_required(login_url='login-register')
def delete_friend(request, id_deleted):

    usuario_actual = request.user

    usuario_eliminado = User.objects.get(id = id_deleted)

    contacto_usuario_actual = Contacts.objects.filter(belongs_to = usuario_actual).get(username = usuario_eliminado.username)

    contacto_usuario_actual.delete()

    contacto_usuario_eliminado = Contacts.objects.filter(username = usuario_actual).get(belongs_to= usuario_eliminado.username)

    contacto_usuario_eliminado.delete()

    messages.success(request, 'Contacto eliminado')

    return redirect('inicio')

@login_required(login_url='login-register')
def friends_request(request):

    usuario_actual = request.user
    
    solicitudes = FriendsRequest.objects.filter(id_requested = usuario_actual.id).order_by('-id')

    return render(request, 'friends-request.html',{
        'solicitudes': solicitudes
    })

@login_required(login_url='login-register')
def accept_request(request, user_id):

    usuario_actual = request.user

    usuario_solicitado = User.objects.filter(id = user_id).get()

    contacto = Contacts(
        user_id = user_id,
        username = usuario_solicitado.username,
        belongs_to = usuario_actual
    )
    
    contacto.save()

    contacto = Contacts(
        user_id = usuario_actual.id,
        username = usuario_actual,
        belongs_to = usuario_solicitado.username
    )
    
    contacto.save()

    solicitudes = FriendsRequest.objects.filter(id_requested = usuario_actual.id).filter(user_id = user_id)

    solicitudes.delete()

    messages.success(request, 'Solicitud aceptada con éxito')

    return redirect('inicio')

@login_required(login_url='login-register')
def reject_request(request, user_id):

    usuario_actual = request.user

    solicitudes = FriendsRequest.objects.filter(id_requested = usuario_actual.id).filter(user_id = user_id)

    solicitudes.delete()

    messages.success(request, 'Solicitud rechazada con éxito')
    
    return redirect('inicio')

@login_required(login_url='login-register')
def messages_list(request):

    usuario_actual = request.user

    list_messages = ListMessages.objects.filter(receiver = usuario_actual).order_by('-id')

    return render(request, 'messages.html',{
        'messages': list_messages
    })

@login_required(login_url='login-register')
def sent_messages(request):

    usuario_actual = request.user

    sents = ListMessages.objects.filter(sender = usuario_actual)

    return render(request, 'sent_messages.html',{
        'sents': sents
    })

@login_required(login_url='login-register')
def send_message(request, user_destination):

    usuario_actual = request.user

    usuario_destino = user_destination

    formulario = MessageForm(request.POST)

    if request.method == 'POST':

        formulario = MessageForm(request.POST)

        usuario_actual = request.user
        
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            issue = data_form['issue']
            content = data_form['content']

            nuevo_mensaje = ListMessages(
                sender = usuario_actual,
                receiver = user_destination,
                issue = issue,
                content = content
            )

            nuevo_mensaje.save()

            messages.success(request, 'El mesaje ha sido enviado con éxito')

            return redirect('inicio')
    else:
        return render(request, 'send_message.html',{
            'usuario_actual': usuario_actual,
            'usuario_destino': usuario_destino,
            'formulario': formulario
        })
    
@login_required(login_url='login-register')
def individual_message(request, id_message):

    read_message = ListMessages.objects.get(id = id_message)

    read_message.state = False

    read_message.save()
    
    message = ListMessages.objects.filter(id = id_message)

    return render(request, 'individual_message.html',{
        'message' : message
    })
