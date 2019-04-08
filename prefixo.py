'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
'''
def longestCommonPrefix(s1, s2, t1, t2):
	cont = 0
	i = 0
	j = 0
	if t1<t2:
		while i < t1:
			if s1[i] == s2[j]:
				cont+=1
				i+=1
				j+=1
			else:
				break

		if cont == 0:
			return ""
		else:
			return s1[0:cont]
	else:
		while i < t2:
			if s1[i] == s2[j]:
				cont+=1
				i+=1
				j+=1
			else:
				break

		if cont == 0:
			return ""
		else:
			return s1[0:cont]

palavra = []
tam_s = []
tam = int(input("digite o tamanho da array: "))
for i in range(tam):
	s = input("digite um nome: ")
	palavra.append(s)
	n = len(s)
	tam_s.append(n)

for i in range(tam-2):
	prefixo = longestCommonPrefix(palavra[0],palavra[i+1], tam_s[0], tam_s[i+1])
	palavra[0] = prefixo
	tam_s[0] = len(prefixo)

print(palavra[0])