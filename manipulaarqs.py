'''#--------------ler-------------
#textos unicos
with open("texto_textos.txt","r") as arquivo:
        text=arquivo.read()
print(text)
#mais de uma linha
with open("texto_textos.txt","r",encoding="utf-8") as arquivo:
        linhas=arquivo.readlines()
print(linhas)
for linha in linhas:
    if "pudim" in linha:
        print(linha)

#------------escrever----------
#se nao existir cria, se existir substitui
with open("texto_unico.txt","w") as arquivo:
        arquivo.write("zeldazilda2")
#adicionar       
with open("texto_adicionar.txt","a") as arquivo:
        arquivo.write("\nimpressionadora")
'''

vetor=[]
with open("texto_textos.txt","r",encoding="utf-8") as arquivo:
    linhas=arquivo.readlines()
print(linhas)
for linha in linhas:
    vetor.append(linha)
    if "ado" in linha:
        vetor.remove(linha)  
    if "pudim" in linha:
        print(linha)
print(vetor)     
with open("texto_textos.txt","w",encoding="utf-8") as arquivo:
  for linha in vetor:
      arquivo.write(linha)
    
print(vetor)
