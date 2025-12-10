# Ejercicio 1: Python → JavaScript
# Traduci este código a JavaScript moderno (ES6+)

def find_users_by_age(users, min_age, max_age):
    """Encuentra usuarios dentro de un rango de edad"""
    filtered_users = [user for user in users if min_age <= user['age'] <= max_age]
    return sorted(filtered_users, key=lambda u: u['age'])

def calculate_average_score(scores):
    """Calcula el promedio de puntuaciones válidas (> 0)"""
    valid_scores = [score for score in scores if score > 0]
    if not valid_scores:
        return 0
    return sum(valid_scores) / len(valid_scores)

def format_user_info(user):
    """Formatea información del usuario como string"""
    full_name = f"{user['first_name']} {user['last_name']}"
    return f"Usuario: {full_name}, Edad: {user['age']}, Email: {user.get('email', 'No disponible')}"

def get_unique_tags(items):
    """Obtiene tags únicos de una lista de items"""
    all_tags = []
    for item in items:
        all_tags.extend(item.get('tags', []))
    return list(set(all_tags))

class UserManager:
    def __init__(self, users):
        self.users = users
        self.cache = {}
    
    def find_by_email(self, email):
        """Busca un usuario por email"""
        if email in self.cache:
            return self.cache[email]
        
        for user in self.users:
            if user.get('email') == email:
                self.cache[email] = user
                return user
        return None
    
    def count_by_role(self):
        """Cuenta usuarios por rol"""
        role_counts = {}
        for user in self.users:
            role = user.get('role', 'unknown')
            role_counts[role] = role_counts.get(role, 0) + 1
        return role_counts


# === MAIN - Pruebas ===
if __name__ == "__main__":
    print("=== Ejercicio 1: Python → JavaScript ===\n")
    
    # Datos de prueba
    users = [
        {'first_name': 'Ana', 'last_name': 'García', 'age': 25, 'email': 'ana@example.com', 'role': 'admin'},
        {'first_name': 'Carlos', 'last_name': 'López', 'age': 30, 'email': 'carlos@example.com', 'role': 'user'},
        {'first_name': 'María', 'last_name': 'Martínez', 'age': 22, 'email': 'maria@example.com', 'role': 'user'},
        {'first_name': 'Juan', 'last_name': 'Pérez', 'age': 35, 'email': 'juan@example.com', 'role': 'moderator'},
        {'first_name': 'Laura', 'last_name': 'Sánchez', 'age': 28, 'email': 'laura@example.com', 'role': 'user'},
    ]
    
    # 1. Probar find_users_by_age
    print("1. Usuarios entre 25 y 30 años:")
    filtered = find_users_by_age(users, 25, 30)
    for user in filtered:
        print(f"   - {user['first_name']} {user['last_name']}: {user['age']} años")
    
    # 2. Probar calculate_average_score
    print("\n2. Promedio de puntuaciones:")
    scores = [85, 90, -5, 78, 92, 0, 88]
    avg = calculate_average_score(scores)
    print(f"   Puntuaciones: {scores}")
    print(f"   Promedio (solo válidas): {avg:.2f}")
    
    # 3. Probar format_user_info
    print("\n3. Formatear información de usuario:")
    user_info = format_user_info(users[0])
    print(f"   {user_info}")
    
    user_without_email = {'first_name': 'Pedro', 'last_name': 'Gómez', 'age': 40}
    user_info2 = format_user_info(user_without_email)
    print(f"   {user_info2}")
    
    # 4. Probar get_unique_tags
    print("\n4. Tags únicos de items:")
    items = [
        {'name': 'Item 1', 'tags': ['javascript', 'web', 'frontend']},
        {'name': 'Item 2', 'tags': ['python', 'backend', 'api']},
        {'name': 'Item 3', 'tags': ['javascript', 'react', 'frontend']},
        {'name': 'Item 4', 'tags': ['python', 'django', 'web']},
    ]
    unique_tags = get_unique_tags(items)
    print(f"   Tags únicos: {sorted(unique_tags)}")
    
    # 5. Probar UserManager
    print("\n5. UserManager:")
    manager = UserManager(users)
    
    # Buscar por email
    found_user = manager.find_by_email('carlos@example.com')
    if found_user:
        print(f"   Usuario encontrado: {found_user['first_name']} {found_user['last_name']}")
    
    # Buscar de nuevo (debe venir del cache)
    found_user2 = manager.find_by_email('carlos@example.com')
    print(f"   Segunda búsqueda (desde cache): {found_user2['first_name']}")
    
    # Contar por rol
    role_counts = manager.count_by_role()
    print(f"   Usuarios por rol:")
    for role, count in role_counts.items():
        print(f"      - {role}: {count}")
    
    # Usuario no encontrado
    not_found = manager.find_by_email('noexiste@example.com')
    print(f"   Usuario no encontrado: {not_found}")
    
    print("\n=== ¡Todas las pruebas completadas! ===")
    print("Ahora traduce este código a JavaScript usando ES6+ 🚀")
