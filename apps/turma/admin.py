from django.contrib import admin
from.models import Turma


class Turmaadmin(admin.ModelAdmin):
    list_display = ('turma','catequista')


admin.site.register(Turma, Turmaadmin)