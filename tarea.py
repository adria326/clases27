opciones = {
    "izquierda": "te encontraste con un dragón",
    "derecha": "encontraste un tesoro",
    "adelante": "caíste en un pozo"
}

# Solicitamos la opción al usuario
eleccion = input("Estás en un cruce. ¿Quieres ir a la derecha, izquierda o adelante?: ")

# Convertimos la entrada a minúsculas para hacerla consistente
eleccion = eleccion.lower()

if eleccion in opciones:
    print("Respuesta:", opciones[eleccion])
else:
    print("Opción equivocada")