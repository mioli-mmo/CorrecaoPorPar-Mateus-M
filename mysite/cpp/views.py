from django.shortcuts import render
from django.views import View
from .services import ServicoResposta

class AvaliaRespostaView(View):
    def get(self, request, *args, **kwargs):
        srv = ServicoResposta()
        id_resposta = kwargs.get('id_resposta', '')
        obj = srv.recupera_resposta(id_resposta)
        contexto = {'resposta': obj}
        return render(request, 'cpp/avalia_resposta.html', contexto)
