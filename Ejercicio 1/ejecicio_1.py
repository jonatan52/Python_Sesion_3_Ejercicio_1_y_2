# Ejercicio 1 sesion 3
# Autor: Jonatan Tarriba

print("="*20 + " AGENDA " + "="*20  )

nombre = "Jonatan"
apellidos = "Tarriba"
edad = 35
email = "tarriba@gmail.com"
telefono = 32156485
casado = True
hijos = True
lista_amigos = ["Anderson", "Edison", "Wilfrido", "Jorge"]
peliculas_vistas = {"pelicula1":"El perfume",
                    "pelicula2":"La redada",
                    "pelicula3":"Armagedon"}



#print("="*20 + " Contacto " + "="*20  )
print(f"""
Nombre: {nombre}
Apellido: {apellidos}
Edad: {edad}
Email: {email}
Telefono: {telefono}
Casado: {casado}
Hijos: {hijos}
Amigos: {lista_amigos}
Peliculas: {peliculas_vistas}""")
