# listas (arreglos)
notas = [10, 20, 25, 80]
variada = [10, "hola", 70.5, False]

print(notas[0])
notas.append(40)

#es que el pop lo quita de la lista PERO nos devuleve el contenido eliminado
nota_eliminada = notas.pop(1)
print(notas)
print(nota_eliminada)

#le pasamos el contenido que queremos eliminar, y si existe lo eliminara, caso contrario lanzara error
notas.remove(80)

#tupla
alumnos= ("Blas", "Lucho", "Juancho")
#la diferencia es que la tupla no se puede modificar (inmutable)
#la tupla se usa para definir valores que nunca se modificaran en todo el ciclo de nuestro proyecto

#set (conjuntos)
mascotas={"juancho","iguana","llama"}
print(mascotas)
print(len(mascotas))

#diccionarios
#es ordenada pero por llaves (no por posiciones)

persona={
    "nombre":"Blas",
    "apellido":"Condori",
    "sexo":"masculino",
    "hobbies":["jugar futbol", "montar bici"]
}

print(persona["apellido"])

print(persona.get("nacionalidad", "no existe!!!"))