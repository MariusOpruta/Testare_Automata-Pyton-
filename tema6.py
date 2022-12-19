'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''
import datetime
import math

class Cerc:
    raza = 1
    culoare = ''
    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare=culoare
    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza} si are culoarea {self.culoare}')
    def aria(self):
       print(f'Aria cercului este {self.raza*self.raza*math.pi}')
    def diametru(self):
        print(f'Diametrul cercului este {self.raza+self.raza}')
    def circumferinta(self):
        print(f'Circumferinta cercului este {self.raza*2*math.pi}')

p1=Cerc(12,"alb")
p1.descrie_cerc()
p1.aria()
p1.diametru()
p1.circumferinta()

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''
class dreptunghi:
    lungime=123
    latime = 123
    culoare=''

    def __init__(self,lungime,latime,culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare
    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}')
    def aria(self):
        print(f'Aria dreptunghiului este: {self.latime*self.lungime}')
    def perimetru(self):
        print(f'Perimetrul dreptunghiului este {2*self.lungime+2*self.latime}')
    def schimb_cul(self,culoare_nou):
        dreptunghi.culoare=culoare_nou
        print(f'Culoarea noua este {culoare_nou}')

dr=dreptunghi(20,10,'alb')
dr.descrie()
dr.aria()
dr.perimetru()
dreptunghi.schimb_cul("alb","rosu")


'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
class angajat:
    nume = ''
    prenume = ' '
    salariu = 123

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Andgajatul are numele {self.nume}, prenumele {self.prenume} si salariul {self.salariu} ')

    def nume_complet(self):
        print(f'Numele complet al angajatului {self.nume} {self.prenume}')

    def sal_lunar(self):
        print(f'Salariul lunar {self.salariu}')

    def sal_anual(self):
        print(f'Salariul anual {12 * self.salariu}')

    def marire_sal(self, procent):
        sal_nou = self.salariu * procent
        print(f'Salariul nou va fi {sal_nou}')


ang = angajat("Popescu", "Ion", 1200)
ang.descrie()
ang.nume_complet()
ang.sal_lunar()
ang.sal_anual()
ang.marire_sal(10)

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
class cont:
    iban=' '
    titular_cont=' '
    sold =123
    def __init__(self, iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} sauma {self.sold} lei')
    def debitarecont(self,suma):
        sold_nou=self.sold+suma
        print(f'Soldul curent este {sold_nou}')
    def creditarecont(self,suma):
        sold_n=self.sold-suma
        print(f'Noul Sold (creditare) este {sold_n}')

con= cont('12345btrl09','Pop Ioan',3000)
con.afisare_sold()
con.debitarecont(500)
con.creditarecont(1000)

'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''
from datetime import datetime, date

class factura:
    seria = 'x'
    numar = 123
    nume_produs = ' '
    cant = 1.5
    pret_buc = 1.5

    def __init__(self, numar, nume_produs, cant, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cant = cant
        self.pret_buc = pret_buc

    def schimb_cant(self,cant1):
        self.cant=cant1
        print(f'Cant {cant1}')

    def schimbpret(self,pret):
        self.pret_buc = pret
        print(f'Noul pret {pret}')

    def nume_prod(self,nume):
        self.nume_produs = nume
        print(f'Noul nume {nume}')

    def genereazaFactura(self):
        print(f'Factura seria X numar {self.numar}')
        print(f'Data {date.today()}')
        print(f'Produs|Cantitate|Pret_Bucata|Total')
        print(f'{self.nume_produs}|{self.cant}|{self.pret_buc}|{self.cant*self.pret_buc}')


f1=factura(12,'telefon',7.0,12.5)
f1.genereazaFactura()
f1.schimb_cant(40)
f1.schimbpret(56.32)
f1.nume_prod('Calculator')
f1.genereazaFactura()

'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''
class masina:
    marca='Dacia'
    model=''
    v_max=555
    v_act=0
    culoare='gri'
    cul_disp={'alb','rosu','albastru','galben','verde'}
    inmatriculata=False
    def __init__(self,model,v_max):
        self.model=model
        self.v_max=v_max
    def descrie(self):
        print(f'Masina {self.marca}, model {self.model}, vit actuala {self.v_act}, vit maxima {self.v_max} inmatriculata {self.inmatriculata}')
    def inmatriculare(self):
        if self.inmatriculata==False:
            self.inmatriculata=True
        print(f'Inmatriculata {self.inmatriculata}')
    def vopseste(self,culoare):
        if culoare in self.cul_disp:
            self.culoare=culoare
            print(f'Noua culare este {self.culoare}')
        else:
            print(f'Nu exista culoarea {culoare} ')
    def accelereaza(self,viteza):
        if viteza <0:
            print('Eroare')
        elif viteza>self.v_max:
            print(f'Viteza maxima este {self.v_max}')
        else:
            print(f'Viteza maxima este {viteza}')

    def franeaza(self):
        print(f'Masina se opreste si are viteza {self.v_act}')

v1=masina('Spring',180)
v1.descrie()
v1.inmatriculare()
v1.vopseste('rosu')
v1.vopseste('blu')
v1.vopseste('galben')
v1.accelereaza(-200)
v1.accelereaza(100)
v1.accelereaza(200)
v1.accelereaza(300)
v1.franeaza()

''' 
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
'''
class todoList():

    def __init__(self):
        self.dict={}

    def adaugatask(self,nume,descriere):
        self.dict[nume]=descriere
    def detalii_supplimenatre(self,desc):
        desc = input('scrie o descriere: ')
        if desc is not dict.values():
            r=input('Doriti sa-l adaugati ')
        if r=='da':
            nume = input('Numele taskului')
            self.dict[nume] = desc

# nu stiu cum pot sa verific ca descriere NU  se afla in dictionar
# ma mai gandesc

d1=todoList()
d1.adaugatask('Piata','Cumparaturi')
d1.adaugatask('Masina','Reparatie')
d1.adaugatask('Munca','Distractie')
print(d1.dict)
print(d1.dict.keys())
d1.detalii_supplimenatre()













