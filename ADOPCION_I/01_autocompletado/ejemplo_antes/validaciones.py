"""
Ejemplos de código ANTES de usar GitHub Copilot
Forma tradicional de escribir código con búsquedas constantes
"""

import re
from datetime import datetime

# Ejemplo 1: Validación de email (buscado en Stack Overflow)
def validate_email(email):
    # Después de buscar "python email validation regex"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False    


# Ejemplo 2: Validación de contraseña (varios intentos)
def validate_password(password):
    # Escribiendo manualmente cada condición
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit

# Ejemplo 3: Formateo de fecha (leyendo documentación)
def format_date(date_obj):
    # Después de leer docs de datetime
    day = str(date_obj.day)
    if len(day) == 1:
        day = '0' + day
    
    month = str(date_obj.month)
    if len(month) == 1:
        month = '0' + month
    
    year = str(date_obj.year)
    
    return f"{day}/{month}/{year}"

# Ejemplo 4: Calcular edad (varios intentos y debug)
def calculate_age(birth_date):
    # Después de debuguear casos edge
    today = datetime.now()
    age = today.year - birth_date.year
    
    # Ajustar si no ha cumplido años este año
    if today.month < birth_date.month:
        age -= 1
    elif today.month == birth_date.month:
        if today.day < birth_date.day:
            age -= 1
    
    return age

# Ejemplo 5: Eliminar duplicados (solución básica)
def remove_duplicates(lst):
    # Primera solución que se nos ocurre
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Ejemplo 6: Validar teléfono (después de buscar formatos)
def validate_phone(phone):
    # Regex copiado y adaptado
    pattern = r'^\+?1?\d{9,15}$'
    cleaned = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    return re.match(pattern, cleaned) is not None

# Ejemplo 7: Calcular porcentaje (implementación manual)
def calculate_percentage(part, total):
    # Simple pero hay que pensarlo
    if total == 0:
        return 0
    return (part / total) * 100

# Ejemplo 8: Truncar texto (varios pasos)
def truncate_text(text, max_length):
    # Implementación básica
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length - 3] + "..."

if __name__ == "__main__":
    # Pruebas manuales (también escritas manualmente)
    print(validate_email("test@example.com"))  # True
    print(validate_password("Pass123"))  # True
    print(format_date(datetime.now()))
    print(calculate_age(datetime(1990, 5, 15)))
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(validate_phone("+1234567890"))
    print(calculate_percentage(25, 100))
    print(truncate_text("Este es un texto muy largo", 15))
