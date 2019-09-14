import base64 
from datetime import datetime
from AESCipher import AESCipher
import ast

class Bloco:

  def __init__(self, transacoes, bloco_ant, next_block = ''):

    bloco_anterior_formatado = '{}'.format(
      bloco_ant
    )    

    self._bloco_ant = bloco_ant
    self._transacoes = AESCipher(bloco_anterior_formatado).encrypt(transacoes)
    # self._next_block = next_block

  @property
  def bloco_ant(self):
    return self._bloco_ant

  @property
  def transacoes(self):
    bloco_anterior_formatado = '{}'.format(
      self.bloco_ant
    )  
    return ast.literal_eval(AESCipher(bloco_anterior_formatado).decrypt(self._transacoes))