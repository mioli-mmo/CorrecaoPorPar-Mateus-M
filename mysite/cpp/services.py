from .models import Resposta, CorrecaoPorPar

class ServicoResposta():

    def recupera_resposta(self, id_resposta):
        obj = Resposta.objects.get(pk = id_resposta)
        return obj

class ServicoCorrecao():

    def salvar_correcao(self, id_resp, id_aluno, nota, comentario):
        srv = ServicoResposta()
        resp = srv.recupera_resposta(id_resp)
        if (resp and nota):
            novo = CorrecaoPorPar(
                aluno_id=id_aluno, nota=nota, comentarios=comentario
            )
            novo.save()
            resp.set_correcao(novo)
            resp.save()
        return resp.avaliacao.id
