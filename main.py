# -*- coding: utf-8 -*-
## ----------------------------------------------------------
## Importação dos módulos padrões
## ----------------------------------------------------------
import os, pymongo
from flask import Flask, jsonify, request, render_template
from flask_json_schema import JsonSchema, JsonValidationError

## ----------------------------------------------------------
## Instanciando a API
## ----------------------------------------------------------
app = Flask("n-server")
app.config.from_object('settings')


## ----------------------------------------------------------
## Tratamento de erros na validação
## ----------------------------------------------------------
@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'Erro': e.message, 'Errors': [validation_error.message for validation_error in e.errors]})


## ----------------------------------------------------------
## Rotas padrões
## ----------------------------------------------------------
##
## @pessoa_blue.route: A rota do endpoint
## ----------------------------------------------------------

##Definição do endpoint
@app.route("/panic", methods=['GET'])
def nao_entre_em_panico():
    return jsonify({"message": "Nao entre em panico, isso é soh um retorno padrao"})

## ----------------------------------------------------------
## Endpoint index
## ----------------------------------------------------------
@app.route("/")
def index():
    return jsonify({"message": "servidor do auditor"})
