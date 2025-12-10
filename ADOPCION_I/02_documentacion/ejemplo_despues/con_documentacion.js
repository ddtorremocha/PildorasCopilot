/**
 * Código DESPUÉS: Con documentación completa usando JSDoc
 * Este código es fácil de entender gracias a la documentación detallada
 */

/**
 * Procesa un pago calculando las comisiones y generando una transacción.
 * 
 * Esta función calcula la comisión del procesador de pagos (2.9% + $0.30),
 * suma el total y crea un objeto de transacción con el estado apropiado
 * según el método de pago utilizado.
 * 
 * @param {number} amount - Monto del pago en la moneda especificada. Debe ser mayor a 0.
 * @param {string} currency - Código de moneda (ej: 'USD', 'EUR', 'MXN').
 * @param {'card'|'bank'} method - Método de pago ('card' para tarjeta o 'bank' para banco).
 * @returns {Object|null} Objeto de transacción con amount, fee, total, currency, method y status, o null si el monto es inválido.
 * 
 * @example
 * // Pago con tarjeta aprobado automáticamente
 * processPayment(100, 'USD', 'card');
 * // Returns: { amount: 100, fee: 3.20, total: 103.20, currency: 'USD', method: 'card', status: 'approved' }
 * 
 * @example
 * // Pago con banco requiere verificación
 * processPayment(500, 'EUR', 'bank');
 * // Returns: { amount: 500, fee: 14.80, total: 514.80, currency: 'EUR', method: 'bank', status: 'pending_verification' }
 * 
 * @example
 * // Monto inválido retorna null
 * processPayment(-50, 'USD', 'card');
 * // Returns: null
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

/**
 * Valida los datos de entrada del usuario según reglas de negocio.
 * 
 * Verifica que el email sea válido, la contraseña cumpla requisitos mínimos
 * y la edad sea apropiada para el servicio.
 * 
 * @param {Object} data - Datos del usuario a validar.
 * @param {string} data.email - Email del usuario. Debe contener '@'.
 * @param {string} data.password - Contraseña del usuario. Debe tener al menos 8 caracteres.
 * @param {number} [data.age] - Edad del usuario (opcional). Si se proporciona, debe ser >= 18.
 * @returns {{isValid: boolean, errors: string[]}} Objeto con isValid (true si no hay errores) y array de campos con errores.
 * 
 * @example
 * // Validación exitosa
 * validateUserInput({ email: 'user@example.com', password: 'securePass123', age: 25 });
 * // Returns: { isValid: true, errors: [] }
 * 
 * @example
 * // Validación con errores
 * validateUserInput({ email: 'invalid', password: '123', age: 16 });
 * // Returns: { isValid: false, errors: ['email', 'password', 'age'] }
 */
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

/**
 * Gestor de usuarios con cache integrado para optimizar consultas a la base de datos.
 * 
 * Esta clase proporciona métodos para consultar y actualizar información de usuarios,
 * con un sistema de cache en memoria para reducir la carga en la base de datos.
 * 
 * @class
 * @example
 * const db = new DatabaseConnection();
 * const userManager = new UserManager(db);
 * const user = userManager.getUser(123);
 */
class UserManager {
    /**
     * Crea una instancia del gestor de usuarios.
     * 
     * @param {Object} dbConnection - Objeto de conexión a la base de datos con métodos query() y execute().
     */
    constructor(dbConnection) {
        /** @type {Object} Conexión a la base de datos */
        this.db = dbConnection;
        
        /** @type {Object.<number, Object>} Cache de usuarios en memoria */
        this.cache = {};
    }
    
    /**
     * Obtiene un usuario de la base de datos o del cache.
     * 
     * Si el cache está habilitado y el usuario existe en cache, lo retorna directamente.
     * Si no, consulta la base de datos y opcionalmente guarda el resultado en cache.
     * 
     * @param {number} userId - ID del usuario a buscar.
     * @param {boolean} [useCache=true] - Si es true, usa y actualiza el cache. Si es false, siempre consulta la BD.
     * @returns {Object|null} Objeto con los datos del usuario o null si no existe.
     * 
     * @example
     * // Obtener usuario usando cache
     * const user = userManager.getUser(123);
     * 
     * @example
     * // Obtener usuario sin usar cache (consulta directa a BD)
     * const freshUser = userManager.getUser(123, false);
     */
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
    
    /**
     * Actualiza los datos de un usuario en la base de datos.
     * 
     * Ejecuta una actualización en la base de datos y elimina el usuario del cache
     * para asegurar que futuras consultas obtengan los datos actualizados.
     * 
     * @param {number} userId - ID del usuario a actualizar.
     * @param {Object} data - Datos a actualizar.
     * @param {string} data.name - Nuevo nombre del usuario.
     * @param {string} data.email - Nuevo email del usuario.
     * @returns {Object} Resultado de la operación de actualización.
     * 
     * @example
     * const result = userManager.updateUser(123, { 
     *   name: 'Juan Pérez', 
     *   email: 'juan@example.com' 
     * });
     */
    updateUser(userId, data) {
        const result = this.db.execute(
            'UPDATE users SET name=?, email=? WHERE id=?',
            [data.name, data.email, userId]
        );
        
        // Invalidar cache después de actualizar
        if (this.cache[userId]) {
            delete this.cache[userId];
        }
        
        return result;
    }
}

module.exports = { processPayment, validateUserInput, UserManager };
