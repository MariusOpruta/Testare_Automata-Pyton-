'''
Exercitii obligatorii
Pct.1
'''
# o variabila este o zona de memorie sau o "cutiuta" careia i se atribuie valori
# Pct. 2
nume = 'Marius'
varsta = 49
inaltime = 1.78
student = True
#Pct 3
print(type(nume))
print(type(varsta))
print(type(inaltime))
print(type(student))
#Pct 4
print(round(inaltime))
#Pct 5
print(nume)
print(varsta)
print(inaltime)
print(student)
#Pct 6
nume = input('Numele: ')
prenume = input('Prenumele: ')
np = len(nume + prenume)
print(f'Numele complet are {np} caractere')
#Pct 7
x = int(input('Alege lungimea: '))
y = int(input('Alege latimea: '))
print('Aria dreptungiului este: '+ str(x*y))
#Pct 8
coral = 'Coral is either the stupidest animal or the smartest rock'
print(coral.count('the', 15, 50))
#Pct 9
print(coral.count('the'))
c = coral.replace('the','THE')
print(c)

#Pct 10
assert coral.isdigit()
'''
#Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
#nevoie de Google).
#Pct 1
'''
z = input('Alege un cuvant impar: ')
if len(z) % 2 == 0:
    print('Cuvant par!')
else:
    print(f'Cuvantul este: {z} ')

import math
print(math.ceil(len(z)/2))
#print("Mijlocul este: ",middle_char(z))

#Pct2
r = input('Alege un cuvant:')
y = r[::-1]
assert r == y
print('Cuvantul este palindrom!!')

#Pct 3
print(input('Scrie cuvintele :').split())

#Pct 4
x = input('str: ')
y = x[0].upper()
w = x.replace(x[0],y)
print(w)
q = w[0:1].lower() + w[1:len(w)-1] + w[len(w)-1:len(w)].lower()
print(q)

#Pct 5 parola
x = input('user: ')
y = input('parola: ')
password = "*"*len(y)
print(f'Parola pentr user {x} este  {password}  si are {len(y)} caractere')

