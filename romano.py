'''
Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, 
"IV": 4, "IX":9, "IL":49, "IC": 99, "ID":499, "IM": 999,
"VL":45, "VC":95, "VD":495, "VM":995,
"XL":40, "XC":90, "XD":490, "XM":990,
"LD":450, "LM":950,
"CD":400 , "CM":900}
i = 0
valor = 0
s = input("digite um numero romano: ")
while i < len(s):
    chave = s[i:i+2] #vai de i até i+1
    if chave in d:
        valor += d[chave] #vê o par
        i += 2
    else:
        chave = s[i]
        valor += d[chave]
        i+=1
print(valor)