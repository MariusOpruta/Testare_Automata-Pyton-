'''
In an apartment comlex there are buildings with different floor numbers. You are given an array with
the number of floors in each building. Determine how many buildings are the tallest ones.
'''
build1 = ["floor1","floor2","floor3"]
build2 = ["floor1","floor2","floor3","floor4","floor5","floor6"]
build3 = ["floor1","floor2","floor3","floor4","floor5"]

x = len(build3)
y = len(build2)
z = len(build1)

if x<y and x<z:
    print(f"Are two buildings: {y} floors and {z} floors")
elif x>y and x<z:
    print(f"Are two buildings: {x} floors and {z} floors")
else:
    print(f"Are two buildings: {x} floors and {y} floors")





