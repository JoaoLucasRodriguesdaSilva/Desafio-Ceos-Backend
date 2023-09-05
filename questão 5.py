import random

def RandomizedQuicksort(Lista, inicio, fim):
  if inicio < fim:
    
    #Seleção de um pivô aleatorio e partição através dele
    pivo = particaoAleatoria(Lista, inicio, fim) 
    
    RandomizedQuicksort(Lista, inicio, pivo - 1)
    RandomizedQuicksort(Lista, pivo + 1, fim)

def particaoAleatoria(Lista, inicio, fim):
  
  # seleciona uma posição aleatória
  pivoAleatorio = random.randrange(inicio, fim) 

  # realiza a troca entre o pivô e o ultimo número para que possamos aplicar o algoritmo padrão de partição
  Lista[fim], Lista[pivoAleatorio] = Lista[pivoAleatorio], Lista[fim] 

  # Partição padrão
  return particao(Lista, inicio, fim)

def particao(Lista, inicio, fim):
  # algoritmo padrão de partição do quicksort no qual o "i" guarda o indice do elemento que será trocado pelo pivo no final
  
  pivo = fim
  
  i = inicio
  for j in range(inicio, fim):
    
    # Realiza as trocas entre os elementos maiores que o pivô(a direita) e os elementos menores que o pivô(a esquerda) e aumenta o indice i a cada troca
    if Lista[j] <= Lista[pivo]: 
      Lista[i], Lista[j] = Lista[j], Lista[i]
      i = i + 1
      
  # troca o elemento da menor posição(i) dos elementos maiores que o pivo pelo pivo, colocando o pivo entre os menores e os maiores que ele
  Lista[pivo], Lista[i] = Lista[i], Lista[pivo] 

  # Retorna a posição atual do pivô
  return i 

# FUNÇÃO PRINCIPAL-----------------------------------------------------------------

Lista = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]

RandomizedQuicksort(Lista, 0, len(Lista) - 1)

print(Lista)