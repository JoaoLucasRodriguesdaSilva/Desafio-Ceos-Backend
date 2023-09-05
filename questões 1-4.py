def leituraArquivo(nomeArquivo):
  arquivo = open(nomeArquivo, "r")  # abrir arquivo em modo leitura

  linhas = arquivo.readlines()  # recebo as linhas do arquivo em uma lista de strings

  M = []  # variavel que receberá a Matriz
  Linha = []  # lista que recebe uma Linha do .txt por vez

  for aux in linhas:
    Linha = aux.split(" ")  # quebra a string nos espaços formando uma lista com os numeros
    if Linha[len(Linha) - 1][-1:] == '\n':  # remove do \n no ultimo elemento exceto na ultima linha da matriz pois n existe um \n nela
      Linha[len(Linha) - 1] = Linha[len(Linha) - 1][0:-1]  

    for i in range(len(Linha)):
      Linha[i] = int(Linha[i])  # Transforma todos os elementos da linha em int

    M.append(Linha)  # adiciona a lista gerada na Matriz

  arquivo.close()
  return M  
#--------------------------------------------------------------------------------------------------------------------------------
def elemRepetidos(M):
  # inicio as variaveis que guardaram o maior e o menor valor da lista
  menor = Maior = M[0][0] 
  
  # Encontra o maior e o menor valor da lista em tempo n(onde n é o numero de elementos da lista)
  for linha in range(len(M)): 
    for coluna in range(len(M[linha])):
      if M[linha][coluna] > Maior:
        Maior = M[linha][coluna]
      elif menor > M[linha][coluna]:
        menor = M[linha][coluna]

  # Cria uma lista que conterá a aparição de algum elemento, como o que importa é o tempo de execussão eu me dei o luxo de usar montar um algoritmo que abusa da memória, o numero que ocupa a lista é 0 pois como ele substituirá os repetidos eu supuz que não tem 0 na matriz
  ListaAux = [0] * (Maior - menor + 1)

  # se o numero N foi armazenado na lista ele é substituido por 0, senão ele é armazenado no indice N - menor
  for linha in range(len(M)):
    for coluna in range(len(M[linha])):
      if ListaAux[M[linha][coluna] - menor] != 0:
        M[linha][coluna] = 0
      else:
        ListaAux[M[linha][coluna] - menor] = M[linha][coluna]
        
#--------------------------------------------------------------------------------------------------------------------------------
def imprimeMatriz(M):
  saida = ""
  for i in M:
    for j in i:
      saida = saida + str(j) + " "
    saida = saida + "\n"
  print(saida)

#Função Principal ------------------------------------------------------------------------
M = leituraArquivo("Exemplo.txt")
elemRepetidos(M)
imprimeMatriz(M)
