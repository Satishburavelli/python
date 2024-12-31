tuple1=("moon","star","sun")
tuple2=("venus","mars","sky")
print(tuple)
tuple=tuple1+tuple2
print(tuple)
tuple1=list(tuple2)
tuple1.append("pluto")
print(tuple1)
del tuple2
print(tuple1)
