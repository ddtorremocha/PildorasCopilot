"""
Ejemplos de código DESPUÉS de usar GitHub Copilot
Simplemente escribe comentarios descriptivos y deja que Copilot genere el código
"""

import re
from datetime import datetime, timedelta

# Ejemplo 1: Validación de email
# Simplemente escribe el comentario y presiona Tab
# Función para validar formato de email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Ejemplo 2: Validación de contraseña fuerte
# Función para validar contraseña fuerte: min 8 caracteres, 1 mayúscula, 1 minúscula, 1 número
def validate_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

# Ejemplo 3: Formateo de fecha
# Función para formatear fecha a formato DD/MM/YYYY
def format_date(date_obj):
    return date_obj.strftime("%d/%m/%Y")

# Ejemplo 4: Calcular edad
# Función para calcular edad a partir de fecha de nacimiento
def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Ejemplo 5: Eliminar duplicados manteniendo orden
# Función que elimina duplicados de una lista manteniendo el orden original
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Ejemplo 6: Validar teléfono internacional
# Función para validar número de teléfono en formato internacional
def validate_phone(phone):
    cleaned = re.sub(r'[^\d+]', '', phone)
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, cleaned))

# Ejemplo 7: Calcular porcentaje con manejo de división por cero
# Función para calcular porcentaje con manejo de error
def calculate_percentage(part, total):
    return (part / total * 100) if total != 0 else 0

# Ejemplo 8: Truncar texto inteligentemente
# Función para truncar texto sin cortar palabras
def truncate_text(text, max_length):
    if len(text) <= max_length:
        return text
    truncated = text[:max_length - 3].rsplit(' ', 1)[0]
    return truncated + "..."

# Ejemplo 9: Generado por Copilot - Función para convertir a snake_case
# Función para convertir string a snake_case
def to_snake_case(text):
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', text)
    text = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', text)
    text = text.replace('-', '_').replace(' ', '_')
    return text.lower()

# Ejemplo 10: Generado por Copilot - Validar tarjeta de crédito
# Función para validar número de tarjeta de crédito con algoritmo de Luhn
def validate_credit_card(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    checksum = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

# Ejemplo 11: Generado por Copilot - Generar slug para URL
# Función para generar slug amigable para URLs
def generate_slug(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

# Ejemplo 12: Generado por Copilot - Calcular días hábiles
# Función para calcular días hábiles entre dos fechas
def calculate_business_days(start_date, end_date):
    days = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # Lunes=0, Viernes=4
            days += 1
        current += timedelta(days=1)
    return days

if __name__ == "__main__":
    # Tests generados también con Copilot
    print("=== Validaciones ===")
    print(f"Email válido: {validate_email('test@example.com')}")
    print(f"Password fuerte: {validate_strong_password('MyPass123')}")
    
    print("\n=== Formateo ===")
    print(f"Fecha formateada: {format_date(datetime.now())}")
    print(f"Edad: {calculate_age(datetime(1990, 5, 15))}")
    
    print("\n=== Utilidades ===")
    print(f"Sin duplicados: {remove_duplicates([1, 2, 2, 3, 4, 4, 5])}")
    print(f"Teléfono válido: {validate_phone('+1-234-567-8900')}")
    print(f"Porcentaje: {calculate_percentage(25, 100)}%")
    print(f"Texto truncado: {truncate_text('Este es un texto muy largo para mostrar', 20)}")
    
    print("\n=== Funciones avanzadas generadas por Copilot ===")
    print(f"Snake case: {to_snake_case('MiTextoEnCamelCase')}")
    print(f"Tarjeta válida: {validate_credit_card('4532015112830366')}")
    print(f"Slug: {generate_slug('¡Hola Mundo 2024!')}")
    print(f"Días hábiles: {calculate_business_days(datetime(2024, 1, 1), datetime(2024, 1, 31))}")
