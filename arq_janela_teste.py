from tkinter import *
from tkinter import ttk
import tkinter as tk
from  tkinter import tix
import os
from  tkinter import messagebox


class Arq_path_buscar():
    
    def tela2(self):
        self.root_janela2=Toplevel()
        self.root_janela2.title("teste")
        self.root_janela2.configure(background= 'tomato')
        self.root_janela2.geometry("500x140")
        self.root_janela2.resizable(True,True)
        self.root_janela2.transient(self.root)
        self.root_janela2.focus_force()
        self.root_janela2.grab_set()
        self.path_txt()
       
        
    def path_txt(self):
        #label
        self.label_caminho=Label(self.root_janela2, text="Caminho arq",bg="tomato",fg="black",font=('verdana',8,'bold'))
        self.label_caminho.place(relx=0.01, rely=0.1)
        #entry
        self.entry_caminho=Entry(self.root_janela2,bg="papayawhip")
        self.entry_caminho.place(relx=0.2, rely=0.1,relwidth=0.7, relheight=0.2)
        #botao
        self.btn_confirmar=Button(self.root_janela2,text='OK',bd=2,bg='maroon',fg='white',font=('verdana',8,'bold'),command=self.close)
        self.btn_confirmar.place(relx=0.32,rely=0.5,relwidth=0.3,relheight=0.2)

    def ler_txt(self):
        linhas=""
        palavra = ".txt"
        #verifica se exite algum arquivo .txt no path informado
        if palavra not in self.caminho:
            messagebox.showinfo("Aviso!!!\n ", "adicionar arquivo TXT")
            self.caminho=''
        else:
            #verifica a existencia do arquivo
            if os.path.exists(self.caminho):
                self.nome_txt=self.caminho.split("\\")
                print(self.nome_txt[-1])
                #abre o arq
                with open(self.caminho,"r",encoding="utf-8") as arquivo:
                    linhas=arquivo.readlines()
                print(linhas)
                    
                self.bloco_text.delete("1.0", END)
                for linha in linhas:
                    self.bloco_text.insert(END, linha)
                self.ok=True
            else:
                #caso nao exista, cria um novo arq
                with open(self.caminho,"w") as arquivo:
                    arquivo.write("  ")
                #le o arq criado
                with open(self.caminho,"r",encoding="utf-8") as arquivo:
                    linhas=arquivo.readlines()
                print(linhas)
                self.nome_txt=self.caminho.split("\\")
                print(self.nome_txt[-1])
                self.bloco_text.delete("1.0", END)
                for linha in linhas:
                    self.bloco_text.insert(END, linha)
                self.ok=True
                messagebox.showinfo("Aviso!!!\n ", "arquivo  criado")
                
    def close(self):
        self.caminho=self.entry_caminho.get()
        self.ler_txt()
        if self.ok:
            self.lab_cod2.configure(text=self.nome_txt[-1])
            self.btn_salvar_arq.configure(state='normal')
            self.root_janela2.destroy()   
   
    
        


