#1.Funcție care să calculeze și să returneze suma a două numere
import math
def suma(x,y):
    print(x+y)

suma(5,6)
suma(9,11)
suma(22,23)

#2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def par_impar(x):
    if x%2==0:
        return True
    else:
        return False

print(par_impar(2))
print(par_impar(6))
print(par_impar(9))


#3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)
def lungime(x):
    #x = input("Scrieti-va numele")
    print(f'Nr total de caractere {len(x)}')

lungime('opruta marius')

#4. Funcție care returnează aria dreptunghiului
def aria_drept(x,y):
    print(f'Aria dreptunghi {x*y} ')

aria_drept(4,7)

#5. Funcție care returnează aria cercului
def aria_cerc(r):
    print(f'Aria Cerc {math.pi*r*r}')

aria_cerc(10)

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.
def find(x):
    y = input("Scrieti textul: ")
    if x in y:
        print("True")
    else:
        print("False")

find("a")
find("b")

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
z = input("Scrie textul: ")
def caract():
    x=0
    y=0
    for i in z:
        if i.isupper():
           x+=1
        elif i.lower():
            y+=1

    print(f'Litere mici: {y}, Litere Mari: {x}')

caract()

'''
8.(refacuta) Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
list = []
def pozitive(numere):
    for i in numere:
      if i >0:
        list.append(i)
    print(list)
pozitive(numere)

'''' 
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
def retno(x,y):
    if x==y:
        print("Nr egale")
    elif x>y:
        print(("x mai mare ca y"))
    else:
        print("x mai mic ca y")

retno(3,4)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
y = {1,3,5}
def primeste(x):
        if x not in y:
            y.add(x)
            print(f'am adaugat numărul nou în set {y}')
            return True
        else:
            print('nu am adaugat numărul în set. Acesta există deja')
            return False

primeste(2)

'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''
def calculator(x,y):
 a=x+y
 print("Suma: ",a)
 b=x-y
 print("Diferenta: ",b)
 c=x*y
 print("Inmultirea: ",c)
 d=x/y
 print("Impartirea: ",d)

calculator(10,2)



'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''

'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''
def numere(x,y,z):
    maxim = max(x,y,z)
    print(maxim)
numere(10,12,9)

'''
5.(refacuta) Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
def suma(x):
  suma = 0
  for i in range(0,x+1):
        suma = suma+i
  return suma

print(suma(3))
print(suma(4))

'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
list3 = []
def intersectie(list1, list2):
    for x in list1:
        if x in list2:
            list3.append(x)

    print(list3)

intersectie(list1,list2)

'''
2.(refacuta). Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''
def reducere(x):
   red=0
   for i in range (0,x+1):
       red =x - x*0.10

   return red

print(reducere(100))

'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''
import datetime
data_acum = datetime.datetime.now()
def data(y):
    if y<data_acum:
        x = data_acum-y
    else:
        x = y-data_acum
    print(x)

data(datetime.datetime(2023,11,27))





