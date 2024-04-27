from django.db import models
from django import forms

# Create your models here.
class Contacts(models.Model):
    user_id = models.IntegerField(verbose_name="Id de usuario")
    username = models.CharField(verbose_name="Nombre de usuario", max_length=52)
    belongs_to = models.CharField(verbose_name="Pertenece a", max_length=52, null=True)
    created_at = models.DateField(verbose_name="Amigos desde", auto_now_add=True)

class FriendsRequest(models.Model):
    username = models.CharField(verbose_name="Nombre de usuario", max_length=52)
    created_at = models.DateField(verbose_name="Enviado el", auto_now_add=True)
    id_requested = models.IntegerField(verbose_name="A quien", null=True)

class ListMessages(models.Model):
    sender = models.CharField(verbose_name="Remitente", max_length=100)
    receiver = models.CharField(verbose_name="Destinatario", max_length=100)
    issue = models.CharField(verbose_name="Asunto", max_length=150)
    content = models.TextField(verbose_name="Contenido")
    state = models.BooleanField(verbose_name="Estado", default=True)
    date_sent = models.DateTimeField(verbose_name="Enviado el", auto_now_add=True)

class Meta:
        model = ListMessages
        fields = '__all__'
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'textarea-input', 'rows': 5}),
        }