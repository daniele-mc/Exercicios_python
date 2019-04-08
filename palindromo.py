'''
Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
'''
def palindromo(s, inicio, fim):
    while inicio < fim:
        if s[inicio] != s[fim]:
            return False
        inicio+=1
        fim-=1
    return True
    
palavra = input("digite uma palavra: ")
tamanho = len(palavra)
if tamanho > 1000:
    while tamanho > 1000:
        print("digite uma palavra")
        palavra = input()
loop = tamanho-1
cont = 1
aux = loop
parada = 0
nao = 0
for i in range (loop):
    for j in range(cont):
        if palindromo(palavra, j, aux) is True:
            print (palavra[j:aux+1])
            parada = 1
            break
        aux = aux +1
    aux = loop - (i+1)
    if parada == 1:
        break
    cont+=1
    nao+=1
    if nao == (loop):
        print("nao tem palindromo")