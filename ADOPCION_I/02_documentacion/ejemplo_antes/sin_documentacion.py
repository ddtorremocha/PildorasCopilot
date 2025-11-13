"""
Código ANTES: Sin documentación
Este código funciona pero es difícil de entender sin leerlo línea por línea
"""

def process_payment(amount, currency, method):
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
    errors = []
    
    if 'email' not in data or '@' not in data['email']:
        errors.append('email')
    
    if 'password' not in data or len(data['password']) < 8:
        errors.append('password')
    
    if 'age' in data and data['age'] < 18:
        errors.append('age')
    
    return len(errors) == 0, errors


class UserManager:
    def __init__(self, db_connection):
        self.db = db_connection
        self.cache = {}
    
    def get_user(self, user_id, use_cache=True):
        if use_cache and user_id in self.cache:
            return self.cache[user_id]
        
        user = self.db.query('SELECT * FROM users WHERE id = ?', [user_id])
        
        if user and use_cache:
            self.cache[user_id] = user
        
        return user
    
    def update_user(self, user_id, data):
        result = self.db.execute(
            'UPDATE users SET name=?, email=? WHERE id=?',
            [data.get('name'), data.get('email'), user_id]
        )
        
        if user_id in self.cache:
            del self.cache[user_id]
        
        return result
