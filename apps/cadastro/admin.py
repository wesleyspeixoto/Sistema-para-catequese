from django.contrib import admin
from.models import Cadastro


class Cadastroadmin(admin.ModelAdmin):
    list_display = ('nome','pai','mae')


admin.site.register(Cadastro, Cadastroadmin)