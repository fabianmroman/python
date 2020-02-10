set1 = {2, -4, 5, 0}
set2 = {1, 2, 3, 4, 5}

# Results are always sorted in a set!
print (set1.union(set2))
print (set1.difference(set2))
print (set2.difference(set1))
print (set1&set2)

print(set1)
print(set2)

string = "Esto es una prueba"
string = string.lower()
list_s = string.split ()
print (list_s, type(list_s))
set_list_s = set(list_s)
print (set_list_s, type(set_list_s))
# Con las operaciones de conjuntos puede verse que elementos hay en un string o en otro, y tambien ordenar un string facilmente
# Con los indices negativos podria ordenarse en sentido descendente

# Dictionaries 
Dictionary = { "Queen": 1973, "Queen II": 1974, "Sheer Heart Attack": 1974, "A Night At The Opera": 1975}
if ("Queen II" in Dictionary): 
    print (Dictionary["Queen II"])

