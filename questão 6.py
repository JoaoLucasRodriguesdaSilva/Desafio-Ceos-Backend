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

# Função principal -------------------------------

L1 = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5]
L2 = [15, 6, 14, 7, 13, 8, 12, 9, 11, 10]

RandomizedQuicksort(L1, 0, len(L1)-1) #Mesma função da questão 5
RandomizedQuicksort(L2, 0, len(L2)-1)

i = len(L1) - 1
j = 0

# Com as listas organizadas, faço um varredura em ambas até uma delas acabar
while i != -1 and j != len(L2):
  if L1[i] > L2[j]:
    L1[i], L2[j] = L2[j], L1[i]
    i = i - 1
  else:
    j = j + 1

print(L1)
print(L2)