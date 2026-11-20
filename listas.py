# vamos a hacer listas bro

lista = ["rolo", 1000, "rolo_TC", "TheRealOne", "TuPapitoTc"]
           #0     #1      #2           #3            #4

print(lista[2:5]) # para imprimir posiciones en la lista (recuerda que si quiero posición 2 y 4 va a ser 2 y 5)

lista[3] = "Cambio de palabra" # para cambiar la palabra en la posición 3

print(lista)

lista.append("Rolo es el campeón") # para agregar una palabra al final de la lista

print(lista)

lista.remove("rolo_TC") # para eliminar una palabra en la lista

print(lista)

print(lista.count(1000)) # para contar cuantas veces se repite un valor en la lista

print(lista.index("Cambio de palabra")) # nos devuelve en que posicion se encuentra el elemento en la lista 