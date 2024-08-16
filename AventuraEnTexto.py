#declaramos un diccionario

opciones = {
    "izquierda": "te encontraste con un dragón",
    "derecha": "encontraste un tesoro",
    "adelante": "caíste en un pozo"
}

# Solicitamos la opción al usuario
eleccion = input("Estás en un cruce. ¿Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("opcion correcta")
else:
    print("opcion equivocada")
