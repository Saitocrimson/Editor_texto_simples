from tkinter import *
from tkinter import ttk
import tkinter as tk
from  tkinter import tix
import os
from  tkinter import messagebox
from tkinter import filedialog


class Funcoes_arqs():
    def salvar_arq(self):
       with open(self.caminho,"w",encoding="utf-8") as arquivo:
            arquivo.write(self.bloco_text.get("1.0",END))
            
    def limpar_txt(self):
         self.bloco_text.delete("1.0", END)
         
    def fechar_txt(self):
        self.caminho=''
        self.lab_cod2.configure(text="")
        self.bloco_text.delete("1.0", END)
        self.btn_salvar_arq.configure(state='disable')
   
    def abrir_txt(self):
        try:
            file= filedialog.askopenfilename(filetype=((".txt", "*.txt"),),multiple=False)
            #print(os.path.normpath(file))
            self.arq_funcao_txt(os.path.normpath(file))
        except:
            print("nada selecionado!")
        
        
    def criacao_txt(self):
        #filetype=((".txt", "*.txt"),)
        try:
            file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            path_arq_nome=file.name.replace('/','\\')
            self.arq_funcao_txt(path_arq_nome)
        except:
            print("nada selecionado!")
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
        
          
                
    
   
    
        


