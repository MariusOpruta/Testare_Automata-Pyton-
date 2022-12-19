''''
if -> then -> else = daca se indeplineste o conditie atunci
                        se executa o instructiune, altfel alta instructiune


2. Verifică și afișează dacă x este număr natural sau nu.
'''
x = int(input('Alege un numar: '))
#x = int(input('Tastati un numar'))
if x%2 == 0:
 print('Numar par')
else:
 print('Numar impar')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x == 0:
 print('Element neutru!')
elif x <0:
 print("Element negativ!")
else:
 print("Element pozitiv!")


# 4. Verifică și afișează dacă x este între -2 și 13.
if x>-2 and x<13:
 print("Se incadreaza in interval!")
else:
 print("Nu se incadreaza in interval!")


# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = int(input('Alege un numar: '))
if x-y <5:
 print('Diferenta este mai mica decat 5!')
else:
 print("Diferenta este mai mare decat 5!")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not x>5 and x<27:
 print("Nu este in interval")   # aici nu am inteles in sensul pt ca ma deruteaza not "ma zapaceste psihic :))"
else:
 print("Este in interval!")

'''
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''
if x == y:
 print('Sunt egale')
elif x<y:
 print('y este mai mare')
else:
 print('x este mai mare')

'''
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x = int(input("Alege nu numar: "))
y = int(input("Alege nu numar: "))
z = int(input("Alege nu numar: "))
if x == y or x == z or y == z:
 print("Triunghi isoscel")
elif x == y == z:
 print("Triunghi echilateral")
else:
 print('Triunghi oarecare')

'''
9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu
'''
litera = input("Scrie o litera: ")
if litera.upper() == 'A' or litera.upper() == 'E' or litera.upper() == 'I' or litera.upper() == 'O' or litera.upper() == 'U':
 print('vocala')
else:
 print('consoana')

'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
nota = float(input('Scrieti nota(cifre): '))
if nota >= 9:
 print('Nota este A')
elif nota >=8 :
 print('Nota este B')
elif nota >= 7:
 print('Nota este C')
elif nota >= 6:
 print('Nota este D')
elif nota > 4:
 print('Nota este E')
else:
 print('Nota este F')


'''
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = int(input('Scrieti numarul dorit: '))
if len(str(x))>=4:
 print('Numarul are minim 4 cifre')
else:
 print('Numarul nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
if len(str(x)) == 6:
 print('Numarul are exact 6 cifre')
else:
 print('Numarul nu are exact 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
if x%2 == 0:
 print('Numarul este par')
else:
 print('Numarul nu este par')

# 4 x, y, z (int)
# Afișează care este cel mai mare dintre ele?
x = int(input("Alege nu numar: "))
y = int(input("Alege nu numar: "))
z = int(input("Alege nu numar: "))
if x > y and x > z:
 print('X este cel mai mare')
elif y>x and y>z:
 print('y este cel mai mare')
else:
 print('z este cel mai mare')

#X, y, z - reprezintă unghiurile unui triunghi
#Verifică și afișează dacă triunghiul este valid sau nu.
if x+y+z == 180:
 print('triunghiul este valid')
else:
 print('triunghiul nu este valid')

''''
Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
'''
coral = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("alege un numar <57"))
if x>0 and x<=56:
 print(f'Textul este: {coral[0:-x]}')
else:
 print('X este mai mare decat lungimea textului ')

''''
7.Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
'''
print(f'{coral[:x]} {coral[-x:]}')

'''
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
'''
index = coral.index("rock")
#coral[:index]
print(coral[:index])


'''
9. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''
text = input('Scrieti Textul: ')
x = text[0]
y = text[-1]
assert x.lower() == y.lower()

'''
10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''
string = '0123456789'
print(string[0::2])
print(string[1::2])

'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''
import random
dice_roll = random.randint(1,6)
x = int(input('Alege nu numar de la 1 la 6: '))
print(dice_roll)
if x == dice_roll:
    print(f'Ai ghicit.Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
elif x > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
else:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')