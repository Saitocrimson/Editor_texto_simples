from tkinter import *
from tkinter import ttk
import tkinter as tk
from  tkinter import tix
import os
from  tkinter import messagebox


class Funcoes_arqs():
    def arq_funcao_txt(self,caminho):
        linhas=""
        self.caminho=caminho
        self.nome_txt=self.caminho.split("\\")
        print(self.nome_txt[-1])
        #abre o arq
        with open(self.caminho,"r",encoding="utf-8") as arquivo:
            linhas=arquivo.readlines()
        print(linhas)     
        self.bloco_text.delete("1.0", END)
        for linha in linhas:
            self.bloco_text.insert(END, linha)
        self.lab_cod2.configure(text=self.nome_txt[-1])
        self.btn_salvar_arq.configure(state='normal')
        
          
                
    
   
    
        


