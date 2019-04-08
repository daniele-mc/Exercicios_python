'''
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
from random import randint
lista = []
parada = 0
i = 0
cont = 0
#colocando os valores na lista
while (i < 10):
	n = randint(1,30)
	if (n in lista) == False:
		lista.append(n)
		i+=1
#imprime a lista
print(lista)
#procura 9 na lista
for k in range(10):
	for j in range (10):
		if (lista[k] +lista[j]) == 9:
			print("%d + %d = 9"%(lista[k],lista[j]))
			print("[%d, %d] = 9" %(k,j))
			parada = 1
			break
	cont+=1
	if parada == 1:
		break
if cont == 10:
	print("a lista nao tem a soma")

