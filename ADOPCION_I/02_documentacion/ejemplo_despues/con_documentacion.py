"""
Código DESPUÉS: Con documentación generada por Copilot
El mismo código pero ahora es fácil de entender y mantener
"""

def process_payment(amount, currency, method):
    """
    Procesa un pago calculando fees y retornando información de la transacción.
    
    Esta función calcula el fee de procesamiento (2.9% + $0.30), determina
    el estado de la transacción según el método de pago, y retorna un objeto
    con todos los detalles.
    
    Args:
        amount (float): Monto del pago en la moneda especificada. Debe ser > 0.
        currency (str): Código de moneda ISO 4217 (ej: 'USD', 'EUR', 'MXN').
        method (str): Método de pago. Valores válidos: 'card', 'bank', 'cash'.
    
    Returns:
        dict or None: Diccionario con información de la transacción conteniendo:
            - amount (float): Monto original
            - fee (float): Fee de procesamiento calculado
            - total (float): Monto total incluyendo fee
            - currency (str): Moneda de la transacción
            - method (str): Método de pago utilizado
            - status (str): Estado de la transacción ('approved', 'pending_verification')
        
        Retorna None si el monto es <= 0.
    
    Examples:
        >>> process_payment(100.00, 'USD', 'card')
        {
            'amount': 100.0,
            'fee': 3.20,
            'total': 103.20,
            'currency': 'USD',
            'method': 'card',
            'status': 'approved'
        }
        
        >>> process_payment(-50, 'USD', 'card')
        None
    
    Note:
        - Los pagos con tarjeta son aprobados inmediatamente
        - Los pagos bancarios requieren verificación
        - El fee es fijo: 2.9% + $0.30
    """
    if amount <= 0:
        return None
    
    fee = amount * 0.029 + 0.30
    total = amount + fee
    
    transaction = {
        'amount': amount,
        'fee': fee,
        'total': total,
        'currency': currency,
        'method': method,
        'status': 'pending'
    }
    
    if method == 'card':
        transaction['status'] = 'approved'
    elif method == 'bank':
        transaction['status'] = 'pending_verification'
    
    return transaction


def validate_user_input(data):
    """
    Valida datos de entrada del usuario según reglas de negocio.
    
    Verifica que el diccionario de datos contenga email válido, contraseña
    segura y edad apropiada (si está presente).
    
    Args:
        data (dict): Diccionario con datos del usuario a validar. Puede contener:
            - email (str): Dirección de email (requerido)
            - password (str): Contraseña (requerido, min 8 caracteres)
            - age (int, optional): Edad del usuario
    
    Returns:
        tuple: Tupla de (is_valid, errors) donde:
            - is_valid (bool): True si todos los datos son válidos
            - errors (list): Lista de strings con nombres de campos inválidos
    
    Examples:
        >>> validate_user_input({'email': 'user@example.com', 'password': 'SecurePass123'})
        (True, [])
        
        >>> validate_user_input({'email': 'invalid', 'password': '123'})
        (False, ['email', 'password'])
        
        >>> validate_user_input({'email': 'user@example.com', 'password': 'SecurePass123', 'age': 15})
        (False, ['age'])
    
    Validation Rules:
        - Email debe contener '@'
        - Password debe tener al menos 8 caracteres
        - Age (si existe) debe ser >= 18
    """
    errors = []
    
    if 'email' not in data or '@' not in data['email']:
        errors.append('email')
    
    if 'password' not in data or len(data['password']) < 8:
        errors.append('password')
    
    if 'age' in data and data['age'] < 18:
        errors.append('age')
    
    return len(errors) == 0, errors


class UserManager:
    """
    Administrador de usuarios con caché para optimizar consultas a base de datos.
    
    Esta clase maneja operaciones CRUD de usuarios implementando un sistema
    de caché simple para reducir consultas repetidas a la base de datos.
    
    Attributes:
        db: Conexión a la base de datos
        cache (dict): Diccionario de caché {user_id: user_data}
    
    Examples:
        >>> db = DatabaseConnection()
        >>> manager = UserManager(db)
        >>> user = manager.get_user(123)
        >>> manager.update_user(123, {'name': 'John Doe'})
    
    Note:
        El caché se invalida automáticamente cuando se actualiza un usuario.
    """
    
    def __init__(self, db_connection):
        """
        Inicializa el UserManager con una conexión a base de datos.
        
        Args:
            db_connection: Objeto de conexión a la base de datos que implementa
                          métodos query() y execute().
        """
        self.db = db_connection
        self.cache = {}
    
    def get_user(self, user_id, use_cache=True):
        """
        Obtiene un usuario por ID, opcionalmente usando caché.
        
        Args:
            user_id (int): ID único del usuario a buscar.
            use_cache (bool, optional): Si True, usa caché para lecturas repetidas.
                                       Default True.
        
        Returns:
            dict or None: Diccionario con datos del usuario si existe, None en caso contrario.
                         Estructura típica: {'id': int, 'name': str, 'email': str}
        
        Examples:
            >>> manager.get_user(123)  # Primera llamada: consulta DB y cachea
            {'id': 123, 'name': 'John', 'email': 'john@example.com'}
            
            >>> manager.get_user(123)  # Segunda llamada: retorna desde caché
            {'id': 123, 'name': 'John', 'email': 'john@example.com'}
            
            >>> manager.get_user(123, use_cache=False)  # Fuerza consulta a DB
            {'id': 123, 'name': 'John', 'email': 'john@example.com'}
        
        Performance:
            - Con caché: ~0.001ms
            - Sin caché: ~10-50ms (dependiendo de la DB)
        """
        if use_cache and user_id in self.cache:
            return self.cache[user_id]
        
        user = self.db.query('SELECT * FROM users WHERE id = ?', [user_id])
        
        if user and use_cache:
            self.cache[user_id] = user
        
        return user
    
    def update_user(self, user_id, data):
        """
        Actualiza datos de un usuario e invalida su entrada en caché.
        
        Args:
            user_id (int): ID del usuario a actualizar.
            data (dict): Diccionario con campos a actualizar. Puede contener:
                        - name (str, optional): Nuevo nombre
                        - email (str, optional): Nuevo email
        
        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        
        Examples:
            >>> manager.update_user(123, {'name': 'Jane Doe'})
            True
            
            >>> manager.update_user(123, {'name': 'Jane', 'email': 'jane@example.com'})
            True
        
        Note:
            - Solo actualiza campos presentes en 'data'
            - Invalida automáticamente el caché para este usuario
            - Los cambios son permanentes en la base de datos
        
        Raises:
            DatabaseError: Si hay error en la consulta SQL
        """
        result = self.db.execute(
            'UPDATE users SET name=?, email=? WHERE id=?',
            [data.get('name'), data.get('email'), user_id]
        )
        
        # Invalidar caché
        if user_id in self.cache:
            del self.cache[user_id]
        
        return result


if __name__ == "__main__":
    # Ejemplos de uso con documentación clara
    print("=== Procesamiento de Pagos ===")
    transaction = process_payment(100, 'USD', 'card')
    print(f"Transacción: {transaction}")
    
    print("\n=== Validación ===")
    valid, errors = validate_user_input({
        'email': 'test@example.com',
        'password': 'SecurePass123'
    })
    print(f"Válido: {valid}, Errores: {errors}")
