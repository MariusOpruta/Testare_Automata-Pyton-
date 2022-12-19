'''
# 1(refacut).Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
# '''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print(f'Mașina mea preferată este: {masini[x]}')
print("---------------------------------")
x=0
for x in masini:
    masini.index(x)
    print(f'Mașina mea preferată este: {x}')
print("---------------------------------")
x=0
while x<len(masini):
   print(f'Mașina mea preferată este: {masini[x]}')
   x+=1
print("---------------------------------")
'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(1,len(masini)-1):
    masini[x]=masini[x].upper()
print(masini)
'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    if masini[x]=='Mercedes':
        print(f'am găsit mașina dorită de dvs: {masini[x]} ')
        break
    else:
        print(f'Am găsit mașina {x}, {masini[x]}. Mai căutam')
print("---------------------------------")
'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    if (masini[x]=='Trabant' or masini[x]=='Lăstun'):
        continue
    print(f'S-ar putea să vă placă mașina {masini[x]}.')
print("---------------------------------")
'''
5 Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
i=0
for x in range(len(masini)):
    if (masini[x] == 'Trabant' or masini[x] == 'Lăstun'):
        masini_vechi = masini[x]
        # masini[x] = 'Tesla'
        print(masini_vechi)

        masini[x] = 'Tesla'
print(masini)
print("---------------------------------")
'''' 
6.Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
for i,j in pret_masini.items():
    if j<15000:
       print(i, j)
       print(f'Pentru un buget de sub 1500 euro puteti alege masina {i, j}')

print("---------------------------------")
'''
7(refacut). Având lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for i in range(0, len(numere)):
    if numere[i] == 3:
        x += 1

print(x)
print("---------------------------------")
'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere:
 print(i)
t=0
y=0
while(y<len(numere)):
  t=t+numere[y]
  y+=1
print('Suma este:', t)

print("---------------------------------")
'''
9(refacut). Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere =sorted(numere)
print(numere)
print(numere[0])

print("---------------------------------")
'''
10(refacut). Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for x in range(0,len(numere)):
    if numere[x]>0:
        numere[x]=-1*numere[x]
print(numere)
print("---------------------------------")

