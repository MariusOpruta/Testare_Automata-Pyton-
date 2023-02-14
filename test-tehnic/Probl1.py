'''
In an apartment comlex there are buildings with different floor numbers. You are given an array with
the number of floors in each building. Determine how many buildings are the tallest ones.
'''

lista_etaje = [2, 4, 5, 3, 4, 6, 3, 6, 4, 6, 2]
for i in range(0,len(lista_etaje)-1):
    if lista_etaje[i]<lista_etaje[i+1]:
        lista_etaje.remove(lista_etaje[i])
    else:
        lista_etaje.remove(lista_etaje[i+1])
    if lista_etaje[i]>lista_etaje[i+1]:
        lista_etaje.remove(lista_etaje[i+1])
        lista_etaje.pop(0)
        lista_etaje.pop()
    else:
        lista_etaje.remove(lista_etaje[i])

    print(f"List {lista_etaje}")
    print(f"cladiri {len(lista_etaje)}")




