# http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html

import sqlite3
from sqlite3 import Error
import os

class Banco():
    def __init__(self) -> None:
        self.path    = None
        self.arquivo = None
    
    def check(self) -> None:
        if os.path.isdir(self.path):
            print(f"| Caminho {self.path} já criado!")
        else:
            print(f"| Caminho {self.path} não criado!")
            os.mkdirs(self.path)
        if os.path.isfile(self.arquivo):
            print(f"| Arquivo {self.arquivo} já criado!")
        else:
            print(f"| Arquivo {self.arquivo} não criado!")
            connection = sqlite3.connect(f'{self.path}\\{self.arquivo}')    
            connection.close()
        
        #self.arquivo = (f'{self.path}\\{self.arquivo}')

    def connect(self):
        try:
            connection=sqlite3.connect(f'{self.path}\\{self.arquivo}')
        except Error as ex:
            print(ex)
        return connection

    def consult(self, query):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        lista = []
        for linha in cursor.fetchall():
            lista.append(linha[0])
        connection.close()
        return lista

    def execut(self, query):
        try:
            connection=self.connect()
            cursor=connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
        except Error as ex:
            print(ex)



"""
Create:
    " CREATE TABLE IF NOT EXISTS {tabela} () "

Consulta: 
    " SELECT {coluna} FROM {tabela} "
    " SELECT {coluna} FROM {tabela} ORDER BY {coluna} "
    " SELECT {coluna} FROM {tabela} WHERE {coluna} = {var} "
    " SELECT name FROM sqlite_master "

Insert:
    " INSERT INTO {tabela} ({colunas}) VALUES ({var}) "

Update:
    " UPDATE {tabela} SET {coluna} = {var} WHERE {coluna} = {var} "

Delete: 
    " DELETE FROM {tabela} WHERE {coluna} = {var}"
"""