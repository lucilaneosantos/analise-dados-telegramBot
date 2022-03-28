"Biblioteca responsavel pelo carregamento das variaveis de ambiante interna"
from email import message
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv() # pega as variáveis ​​de ambiente de .env.


class TelegramBot:
    def __init__(self):
        TOKEN = os.getenv("CHAVE_ACESSO_BOT") # receber variavel do env
        self.url = f"https://api.telegram.org/bot{TOKEN}/" # Conexão da chave com o site para controle do bot
    
    def iniciar(self): # rensponsavel por iniciar o bot
        update_id= None
        while True:
            update = self.pegar_mensagem(update_id)
            messages =  update['result']
            if messages :
                for message in messages :
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        mensagem_texto =  message['message']['text']
                        resposta_bot = self.criar_pergunta(mensagem_texto)
                        self.enviar_resposta(chat_id,resposta_bot)
                    except:
                        pass
    
    def pegar_mensagem(self,update_id):
        link_requisicao = f"{self.url}getUpdates?timeout=1000" # verificar se houve atualização no bot
        if update_id:
            link_requisicao = f"{self.url}getUpdates?timeout=1000&offset={update_id +1}"
        resultado =  requests.get(link_requisicao)
        return json.loads(resultado.content) # pegando conteudo da requisição e realizando leitura em json
    
    def criar_pergunta(self,mensagem_texto):
        if mensagem_texto in ["oi","ola","eae"]:
            return "Ola, tudo bem?"
        else:
            return "Não entendi!!!!!!!!"
    
    def enviar_resposta(self, chat_id, resposta_bot):
        link_enviar = f"{self.url}sendMessage?chat_id={chat_id}&text={resposta_bot}"
        requests.get(link_enviar)
        return

