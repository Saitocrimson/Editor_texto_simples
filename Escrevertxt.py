from tkinter import *
from tkinter import ttk
import tkinter as tk
from  tkinter import tix
from tkinter import filedialog
#from arq_janela_teste import Arq_path_buscar
from Funcoes_arqs import Funcoes_arqs
from  tkinter import messagebox
import os


root=tix.Tk()

class Textadd(Funcoes_arqs):
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
        
        
      
        
class Escrevertxt(Textadd):
   def __init__(self):
        self.root=root
        self.tela()
        self.frame_tela()
        self.labels()
        self.caixa_text()
        self.botao()
        root.mainloop()
        
   def tela(self):
        
        #titulo
        self.root.title("texto")
        #fundo
        self.root.configure(background="tomato")
        #tamanho
        self.root.geometry("700x456")
        #tamanho diminuir aumentar(HOZ/VERT)
        self.root.resizable(True, True)
        #tamanho maximp
        self.root.maxsize(width=800,height=500)
        #tamanho minimo
        self.root.minsize(width=600,height=300)
   def frame_tela(self):
        self.frames=Frame(self.root,bd=4,bg="firebrick",highlightbackground="maroon",highlightthickness=2)
        self.frames.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.2)
        
   def labels(self):
        #nome
        self.lab_cod2=Label(self.frames,bg="white",fg="black",font=('verdana',8,'bold'))
        self.lab_cod2.place(relx=0.01, rely=0.1)
       
    
   def botao(self):
        #abrir
        self.btn_abrir_arq=Button(self.frames, text="Abrir",bd=4,bg="ivory",fg="black",font=('verdana',8,'bold'),command=self.abrir_txt)
        self.btn_abrir_arq.place(relx=0.01,rely=0.5,relwidth=0.17, relheight=0.5)
        #criar
        self.btn_criar_arq=Button(self.frames, text="Criar",bd=4,bg="ivory",fg="black",font=('verdana',8,'bold'),command=self.criacao_txt)
        self.btn_criar_arq.place(relx=0.2,rely=0.5,relwidth=0.17, relheight=0.5)
        #salvar
        self.btn_salvar_arq=Button(self.frames, text="Salvar",bd=4,bg="ivory",fg="black",font=('verdana',8,'bold'),command=self.salvar_arq)
        self.btn_salvar_arq.place(relx=0.4,rely=0.5, relwidth=0.17,relheight=0.5)
        self.btn_salvar_arq.configure(state='disable')
        #fechar
        self.btn_fechar_arq=Button(self.frames, text="Fechar",bd=4,bg="darksalmon",fg="black",font=('verdana',8,'bold'),command=self.fechar_txt)
        self.btn_fechar_arq.place(relx=0.6,rely=0.5, relwidth=0.17, relheight=0.5)
        #limpar
        self.btn_limpar_arq=Button(self.frames, text="Limpar",bd=4,bg="darksalmon",fg="black",font=('verdana',8,'bold'),command=self.limpar_txt)
        self.btn_limpar_arq.place(relx=0.8,rely=0.5, relwidth=0.17, relheight=0.5)
       
   def caixa_text(self):
       #tela texto
       self.bloco_text=Text(self.root,bg="papayawhip",fg="black")
       self.bloco_text.place(relx=0.1, rely=0.35,relwidth=0.8, relheight=0.7)
       
Escrevertxt()
