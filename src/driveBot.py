"Biblioteca responsavel pelo carregamento das variaveis de ambiante interna"

from dotenv import load_dotenv
import gspread
import os
import json
import pandas as pd

load_dotenv() # pega as variáveis ​​de ambiente de .env.
class driveBot:
    def __init__(self):
        self.gc  = gspread.service_account(filename="credencial.json")
    def get_data(self):
        link_google = os.getenv("PLANILHA")
        sh = self.gc.open_by_key(link_google)
        worksheet = sh.sheet1
        dataframe = pd.DataFrame(worksheet.get_all_records())
        return dataframe
