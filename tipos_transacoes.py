from datetime import datetime

class Tipos_Transacoes:
  def __init__(self):
    self.transacoes = []

  def log_cadastro_usuario(self, dados, t = ""):
    
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    formato_log = {
      "tipo_log": "cadastro_inicial",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    
    self.transacoes.append(formato_log)

