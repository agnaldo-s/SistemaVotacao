from django.contrib import admin
from .models import Enquete, Voto

class VotoInline(admin.TabularInline):
    model = Voto
    extra = 1

class EnqueteAdmin(admin.ModelAdmin):
    list_display = ["id", "pergunta"]
    search_fields = ["pergunta"]
    inlines = [VotoInline]

    def get_criador_da_enquete(self, obj):
        return obj.criador_da_enquete.username

    get_criador_da_enquete.short_description = 'Criador da Enquete'

class VotoAdmin(admin.ModelAdmin):
    list_display = ["id", "enquete", "resposta", "get_usuario_votante"]
    search_fields = ["enquete__pergunta", "usuario_votante__username"]

    def get_usuario_votante(self, obj):
        return obj.usuario_votante.username

    get_usuario_votante.short_description = 'Usuário Votante'

admin.site.register(Enquete, EnqueteAdmin)
admin.site.register(Voto, VotoAdmin)
