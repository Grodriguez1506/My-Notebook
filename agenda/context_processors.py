from .models import FriendsRequest, ListMessages

def get_request(request):

    usuario_actual = request.user

    solicitudes = FriendsRequest.objects.filter(id_requested = usuario_actual.id)
    
    conteo_solicitudes = 0

    for solicitud in solicitudes:
        conteo_solicitudes += 1

    return {
        'conteo_solicitudes': conteo_solicitudes
    }

def get_messages(request):

    usuario_actual = request.user

    list_messages = ListMessages.objects.filter(receiver = usuario_actual).filter(state = True)
    
    conteo_mensajes = 0

    for message in list_messages:
        conteo_mensajes += 1

    return {
        'conteo_mensajes': conteo_mensajes
    }
