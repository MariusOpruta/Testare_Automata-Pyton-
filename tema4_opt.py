# '''
# 1.
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
# '''
import random

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    while i%2==0:
        #print(i)
        numere_pare.append(i)
        i+=1
for i in alte_numere:
    while i%3==0:
        #print(i)
        numere_impare.append(i)
        i+=1
for i in alte_numere:
    if i>0:
        #print(i)
        numere_pozitive.append(i)
        i+=1
for i in alte_numere:
    if i<0:
        numere_negative.append(i)
        i+=1
print(f'Lista initiala: {alte_numere}')
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# '''
# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# '''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#M-AM INSPIRAT AICI .. :)
def bubbleSort(alte_numere):
    isSwapped = True

    while isSwapped:
        isSwapped = False
        for i in range(len(alte_numere) - 1):
            if alte_numere[i] > alte_numere[i + 1]:
                isSwapped = True
                alte_numere[i], alte_numere[i+1] = alte_numere[i+1], alte_numere[i]


bubbleSort(alte_numere)
print(f'Numerele sortate sunt: {alte_numere}')

# '''
# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
# '''

i=int(input('Alege un numar: '))
x=random.randint(1,30)
print(f'Nr eandom este: {x}')

while i!=x:
   if i>x:
       print('Nr secret este mai mare')
       break
   elif i<x:
       print('Nr secret este mai mic')
       break
   else:
       print('Felicitari ai ghicit')
       break

# '''
# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# '''
x = int(input('Alege un nr: '))

for i in range(0,x):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print("\r")

# '''
# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
# '''
tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
x=0
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
       x +=tastatura_telefon[i][j]
    print(tastatura_telefon[i][j])
print(f'x: {x}')



