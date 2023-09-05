import random

def RandomizedQuicksort(Lista, inicio, fim):
  if inicio < fim:
    pivo = particaoAleatoria(Lista, inicio, fim) 
    
    RandomizedQuicksort(Lista, inicio, pivo - 1)
    RandomizedQuicksort(Lista, pivo + 1, fim)

def particaoAleatoria(Lista, inicio, fim):
  pivoAleatorio = random.randrange(inicio, fim)
  
  Lista[fim], Lista[pivoAleatorio] = Lista[pivoAleatorio], Lista[fim]
  
  return particao(Lista, inicio, fim)

def particao(Lista, inicio, fim):
  pivo = fim
  
  i = inicio
  for j in range(inicio, fim):
    if Lista[j] <= Lista[pivo]:
      Lista[i], Lista[j] = Lista[j], Lista[i]
      i = i + 1
  Lista[pivo], Lista[i] = Lista[i], Lista[pivo]
  
  return i 

def verificaPermutacao(L1, L2):
  #crio duas listas auxiliares
  aux1 = []
  aux2 = []

  #Copio L1 e L2 nelas
  for i in range(len(L1)):
    aux1.append(L1[i])
    aux2.append(L2[i])

  # Organizo
  RandomizedQuicksort(aux1, 0, len(aux1)-1)
  RandomizedQuicksort(aux2, 0, len(aux2)-1)

  #Se as listas forem diferentes não é permutação
  for i in range(len(aux1)):
    if aux1[i] != aux2[i]:
      return "{} não é permutação de {}".format(L2, L1)

  return "{} é permutação de {}".format(L2, L1)

#Função Principal-----------------------------------------------------------------------------

L1 = [1, 3, 5, 4, 2, 0, 9, 6, 7, 8]
L2 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L3 = [10, 19, 18, 17, 16, 15, 14, 13, 12, 11]

print(verificaPermutacao(L1, L2))
print(verificaPermutacao(L1, L3))