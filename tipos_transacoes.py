from datetime import datetime

class Tipos_Transacoes:
  def __init__(self):
    self.transacoes = []


  # --------------------------------------------------------------------------
  # Logs acionados por acões em sistemas da aplicação
  # --------------------------------------------------------------------------
  def log_interno_cadastro_inicial_usuario(self, dados, t = ""):
    
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    formato_log = {
      "tipo_log": "interno_cadastro_inicial",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    
    self.transacoes.append(formato_log)

  def log_interno_login_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "login_interno_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_consulta_dados_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "interno_consulta_dados_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_adicao_dados_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "adicao_dados_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_alteracao_dados_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "alteracao_dados_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_exclusao_dados_usuario(self, dados, t = ""): 
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "exclusao_dados_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    } 
    self.transacoes.append(formato_log)

  def log_solicitacao_exclusao_usuario(self, dados, t = ""):
    
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    formato_log = {
      "tipo_log": "solicitacao_exclusao_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    
    self.transacoes.append(formato_log)

  def log_interno_criacao_vinculo(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "cadastro_inicial",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_exclusao_vinculo(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "cadastro_inicial",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)


  # --------------------------------------------------------------------------
  # Logs acionados por acões em sistemas externos a aplicação
  # --------------------------------------------------------------------------
  def log_externo_login_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_login_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_consulta_dados_usuario(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_consulta_dados_usuario",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_criacao_vinculo(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_criacao_vinculo",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_exclusao_vinculo(self, dados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_exclusao_vinculo",
      "id_usuario": dados["id"],
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)