from django.shortcuts import render, redirect
from django.views import View
from .services import ServicoResposta, ServicoCorrecao

class AvaliaRespostaView(View):
    def get(self, request, *args, **kwargs):
        srv = ServicoResposta()
        id_resposta = kwargs.get('id_resposta', '')
        obj = srv.recupera_resposta(id_resposta)
        contexto = {'resposta': obj}
        return render(request, 'cpp/avalia_resposta.html', contexto)

    def post(self, request, *args, **kwargs):
        srv = ServicoCorrecao()
        id_resposta = kwargs.get('id_resposta', '')
        #if request.user.is_authenticated and request.user.aluno:
        id_aluno = 1
        nota = request.POST.get('nota','')
        comentario = request.POST.get('comentario', '')
        id_aval = srv.salvar_correcao(id_resposta, id_aluno, nota, comentario)
        return redirect('/avaliacao/{}/'.format(id_aval))

