'''
In an apartment comlex there are buildings with different floor numbers. You are given an array with
the number of floors in each building. Determine how many buildings are the tallest ones.
'''
# build1 = ["floor1","floor2","floor3"]
# build2 = ["floor1","floor2","floor3","floor4","floor5","floor6"]
# build3 = ["floor1","floor2","floor3","floor4","floor5"]
#
# x = len(build3)
# y = len(build2)
# z = len(build1)
#
# if x<y and x<z:
#     print(f"Are two buildings: {y} floors and {z} floors")
# elif x>y and x<z:
#     print(f"Are two buildings: {x} floors and {z} floors")
# else:
#     print(f"Are two buildings: {x} floors and {y} floors")
lista_etaje = [2, 4, 5, 3, 4, 6, 3, 6, 4, 6, 2]
bloc = []
bloc1 = []
bloc2 = []
bloc3 = []
for i in range(len(lista_etaje)-1):
    if lista_etaje[i]<lista_etaje[i+1] :
        bloc.append(lista_etaje[i])
    else:
        bloc2.append(lista_etaje[i])
#
# print(bloc2)
# print(bloc)

for j in range(len(bloc2)):
    if bloc2[j]<bloc2[j-1] :
        bloc1.append(bloc2[j])
    else:
        bloc3.append(bloc2[j])
# print(bloc1)
# print(bloc3)
print(f"Nr blocuri:  {len(bloc3)}")




