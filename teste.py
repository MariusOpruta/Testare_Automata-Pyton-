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
class TodoList():

    def __init__(self):
        self.dict={}

    def adaugatask(self,nume,descriere):
        self.dict[nume]=descriere
    def detalii_supplimenatre(self):
        desc = input('scrie o descriere: ')
        r = input('Doriti sa-l adaugati (da/nu): ')
        if r=='da':
            nume = input('Numele taskului')
            self.dict[nume] = desc

        else:
            print("La revedere")




d1=TodoList()
d1.adaugatask('Piata','Cumparaturi')
d1.adaugatask('Masina','Reparatie')
d1.adaugatask('Munca','Distractie')
print(d1.dict)
print(d1.dict.keys())
d1.detalii_supplimenatre()
print(d1.dict)