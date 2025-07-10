from django.shortcuts import render
from django.views import View
from .services import ServicoResposta

class AvaliaRespostaView(View):
    def get(self, request, *args, **kwargs):
        servico = ServicoResposta()
        id_resposta = kwargs['id_resposta']
        obj = servico.recupera_resposta(id_resposta)
        contexto = {'resposta': obj}
        return render(request, 'cpp/avalia_resposta.html', contexto)
