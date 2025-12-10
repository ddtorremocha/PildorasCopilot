"""
EJERCICIOS PRÁCTICOS - Píldora 1: Autocompletado Inteligente

Instrucciones:
1. Lee el comentario de cada ejercicio
2. Escribe SOLO el comentario descriptivo
3. Presiona Tab y deja que Copilot complete el código
4. Revisa el código generado
5. Ejecuta para verificar que funciona

Tip: Si no te gusta la primera sugerencia, presiona Ctrl+Enter 
para ver alternativas y elegir la mejor.
"""

# ===================================
# NIVEL 1: EJERCICIOS BÁSICOS (🟢)
# ===================================

# Ejercicio 1.1: Validaciones simples
# TODO: Función para validar si un string es un número válido
def esNumeroValido(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# TODO: Función para validar si una contraseña tiene al menos 8 caracteres
def esContrasenaValida(contrasena):
    return len(contrasena) >= 8

# TODO: Función para validar formato de código postal español (5 dígitos)
def esCodigoPostalValido(codigo):
    return len(codigo) == 5 and codigo.isdigit()

# Ejercicio 1.2: Manipulación de strings
# TODO: Función para invertir un string
def invertirString(s):
    return s[::-1]


# TODO: Función para validar si una contraseña tiene al menos 8 caracteres
def validaContraseña(contrasena):
    return len(contrasena) >= 8

# TODO: Función para validar formato de código postal español (5 dígitos)
def validaCodigoPostal(codigo):
    return len(codigo) == 5 and codigo.isdigit()

# Ejercicio 1.2: Manipulación de strings
# TODO: Función para invertir un string
def invertirString(s):
    return s[::-1]

# TODO: Función para contar vocales en un string
def contarVocales(s):
    vocales = 'aeiouAEIOU'
    return sum(1 for char in s if char in vocales)

# TODO: Función para verificar si un string es palíndromo
def esPalindromo(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# ===================================
# NIVEL 2: EJERCICIOS INTERMEDIOS (🟡)
# ===================================

# Ejercicio 2.1: Manipulación de listas
# TODO: Función que elimina duplicados de una lista manteniendo el orden


# TODO: Función que encuentra el elemento más frecuente en una lista


# TODO: Función que aplana una lista anidada de un solo nivel


# Ejercicio 2.2: Operaciones con fechas
# TODO: Función que calcula cuántos días faltan para fin de año


# TODO: Función que verifica si un año es bisiesto


# TODO: Función que retorna el día de la semana de una fecha


# ===================================
# NIVEL 3: EJERCICIOS AVANZADOS (🔴)
# ===================================

# Ejercicio 3.1: Procesamiento de datos
# Define primero una estructura de datos de ejemplo
ejemplo_usuarios = [
    {
        "id": 1,
        "nombre": "Ana García",
        "edad": 28,
        "ciudad": "Madrid",
        "compras": [
            {"producto": "Laptop", "precio": 1200},
            {"producto": "Mouse", "precio": 25}
        ]
    },
    {
        "id": 2,
        "nombre": "Luis Pérez",
        "edad": 35,
        "ciudad": "Barcelona",
        "compras": [
            {"producto": "Teclado", "precio": 80},
            {"producto": "Monitor", "precio": 300}
        ]
    }
]

# TODO: Función que calcula el gasto total de todos los usuarios
def gastoTotal(usuarios):
    total = 0
    for usuario in usuarios:
        for compra in usuario["compras"]:
            total += compra["precio"]
    return total   

# TODO: Función que retorna el usuario que más ha gastado
def usuarioMasGastador(usuarios):
    max_gasto = 0
    usuario_gastador = None
    for usuario in usuarios:
        gasto = sum(compra["precio"] for compra in usuario["compras"])
        if gasto > max_gasto:
            max_gasto = gasto
            usuario_gastador = usuario
    return usuario_gastador

# TODO: Función que agrupa usuarios por ciudad
def agruparPorCiudad(usuarios):
    agrupados = {}
    for usuario in usuarios:
        ciudad = usuario["ciudad"]
        if ciudad not in agrupados:
            agrupados[ciudad] = []
        agrupados[ciudad].append(usuario)
    return agrupados

# Ejercicio 3.2: Algoritmos
# TODO: Función que implementa búsqueda binaria en una lista ordenada


# TODO: Función que genera los primeros n números de Fibonacci


# TODO: Función que verifica si dos strings son anagramas


# ===================================
# DESAFÍO FINAL 🏆
# ===================================

# Crea una clase completa usando solo comentarios
# TODO: Clase Usuario con propiedades nombre, email, edad
# TODO: Método para validar que el email tiene formato correcto
# TODO: Método para verificar si es mayor de edad
# TODO: Método para generar un username a partir del nombre


# ===================================
# TESTS (OPCIONAL)
# ===================================

if __name__ == "__main__":
    print("Ejecuta tus funciones aquí para probarlas")
    print("Ejemplo:")
    print(usuarioMasGastador(ejemplo_usuarios))  # Debería retornar el usuario que más ha gastado

