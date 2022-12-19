note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)


#pct 2
print(note_muzicale.count('do'))

#pct 3
lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista = lista1 + lista2
print(lista)
print('-----')
lista1 = lista1.__add__(lista2)
#lista1.append(lista2)
print(lista1)

#pct 4
'''
Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
lista1.sort()
print(lista1)

#pct 5
'''Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
'''

if len(lista1) ==0:
    print("lista este goala")
else:
    print("lista nu este goala")

#pct 6
'''Folosește o funcție care să șteargă lista de la exercițiul 3
'''
lista1.clear()
print(lista1)
#pct 7
'''Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.

'''
if len(lista1)==0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys()) # ????

''''9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
x = dict1['Ana']
y = dict1['Gigel']
z = dict1['Dorel']
print(f'Ana a luat nota {x}')
print(f'Gigel a luat nota {y}')
print(f'Dorel a luat nota {z}')

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print(dict1)

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9
print(dict1)

'''
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

'''
15 Afișază intersecția elementelor din aceste 2 seturi.
'''
print(zile_sapt.intersection(weekend))

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
'''
jucatori = ['hagi','popescu','maradona','messi','ronaldo']
z = 0
x = input("Da un nume de jucator: ")

if x in jucatori:

    print('Jucatorul este pe teren')
    y = input("Da un nume de jucator pentru schimbare: ")
    jucatori.remove(x)  # stergem jucatorul vechi
    jucatori.append(y)  # adaugam jucator nou
    teren = jucatori  # am schimbat variabila intital pt test apoi am lasat-o asa
    print(teren)
    z+=1
    print(f'mai ai {3 - z} schimbări')
else:
    print(f'Nu se poate face schimbarea deoarece jucatorul {x} nu se afla in teren')

# if z < 3:                              #maxim 3 schimbari
#     x = input("Da un nume de jucator: ")    #se scrie jucatorul cautat
#     print(f'mai ai {3 - z} schimbări')
# elif x not in jucatori:  #se cauta x in lista
#         print(f'Nu se poate face schimbarea deoarece jucatorul {x} nu se afla in teren')    #nu exista juc pe teren
#         z = 3   #l-am fortat sa se opreasca
# else x in jucatori:
#         print('Jucatorul este pe teren')                        #se gaseste jucatorul pe teren
#         y = input("Da un nume de jucator pentru schimbare: ")   #introducem jucator nou de la tastatura
#         jucatori.remove(x)                                      #stergem jucatorul vechi
#         jucatori.append(y)                                      #adaugam jucator nou
#         teren = jucatori                                        #am schimbat variabila intital pt test apoi am lasat-o asa
#         print(teren)
#         z += 1                                                  #se consuma o schimbare
#         print(f'a intrat {y}, a ieșit {x}, mai ai {3-z} schimbări')
#         #print(f'Ai efectuat 3 schimbari')
# else:
    print(f'Ai efectuat 3 schimbari')                        #nu mai sunt schimbari

