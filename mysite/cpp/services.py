from .models import Resposta

class ServicoResposta():

    def recupera_resposta(self, id_resposta):
        obj = Resposta.objects.get(id_resposta)
        return obj