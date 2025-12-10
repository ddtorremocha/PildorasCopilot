/**
 * Código ANTES: Sin documentación
 * Este código funciona pero es difícil de entender sin leerlo línea por línea
 */

function processPayment(amount, currency, method) {
    if (amount <= 0) {
        return null;
    }
    
    const fee = amount * 0.029 + 0.30;
    const total = amount + fee;
    
    const transaction = {
        amount: amount,
        fee: fee,
        total: total,
        currency: currency,
        method: method,
        status: 'pending'
    };
    
    if (method === 'card') {
        transaction.status = 'approved';
    } else if (method === 'bank') {
        transaction.status = 'pending_verification';
    }
    
    return transaction;
}

function validateUserInput(data) {
    const errors = [];
    
    if (!data.email || !data.email.includes('@')) {
        errors.push('email');
    }
    
    if (!data.password || data.password.length < 8) {
        errors.push('password');
    }
    
    if (data.age && data.age < 18) {
        errors.push('age');
    }
    
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

class UserManager {
    constructor(dbConnection) {
        this.db = dbConnection;
        this.cache = {};
    }
    
    getUser(userId, useCache = true) {
        if (useCache && this.cache[userId]) {
            return this.cache[userId];
        }
        
        const user = this.db.query('SELECT * FROM users WHERE id = ?', [userId]);
        
        if (user && useCache) {
            this.cache[userId] = user;
        }
        
        return user;
    }
    
    updateUser(userId, data) {
        const result = this.db.execute(
            'UPDATE users SET name=?, email=? WHERE id=?',
            [data.name, data.email, userId]
        );
        
        if (this.cache[userId]) {
            delete this.cache[userId];
        }
        
        return result;
    }
}

module.exports = { processPayment, validateUserInput, UserManager };
