// Ejercicio 1: Python → JavaScript
// Traducción a JavaScript moderno usando ES6+

/**
 * Encuentra usuarios dentro de un rango de edad
 * @param {Array} users - Array de usuarios
 * @param {number} minAge - Edad mínima
 * @param {number} maxAge - Edad máxima
 * @returns {Array} - Array de usuarios filtrados y ordenados por edad
 */
const findUsersByAge = (users, minAge, maxAge) => {
    const filteredUsers = users.filter(user => user.age >= minAge && user.age <= maxAge);
    return filteredUsers.sort((a, b) => a.age - b.age);
};

/**
 * Calcula el promedio de puntuaciones válidas (> 0)
 * @param {Array<number>} scores - Array de puntuaciones
 * @returns {number} - Promedio de puntuaciones válidas
 */
const calculateAverageScore = (scores) => {
    const validScores = scores.filter(score => score > 0);
    if (validScores.length === 0) {
        return 0;
    }
    return validScores.reduce((sum, score) => sum + score, 0) / validScores.length;
};

/**
 * Formatea información del usuario como string
 * @param {Object} user - Objeto usuario
 * @returns {string} - Información formateada del usuario
 */
const formatUserInfo = (user) => {
    const fullName = `${user.firstName} ${user.lastName}`;
    const email = user.email || 'No disponible';
    return `Usuario: ${fullName}, Edad: ${user.age}, Email: ${email}`;
};

/**
 * Obtiene tags únicos de una lista de items
 * @param {Array} items - Array de items con tags
 * @returns {Array} - Array de tags únicos
 */
const getUniqueTags = (items) => {
    const allTags = items.flatMap(item => item.tags || []);
    return [...new Set(allTags)];
};

/**
 * Clase para gestionar usuarios con cache
 */
class UserManager {
    constructor(users) {
        this.users = users;
        this.cache = {};
    }
    
    /**
     * Busca un usuario por email
     * @param {string} email - Email del usuario
     * @returns {Object|null} - Usuario encontrado o null
     */
    findByEmail(email) {
        if (this.cache[email]) {
            return this.cache[email];
        }
        
        const user = this.users.find(u => u.email === email);
        
        if (user) {
            this.cache[email] = user;
            return user;
        }
        
        return null;
    }
    
    /**
     * Cuenta usuarios por rol
     * @returns {Object} - Objeto con el conteo de usuarios por rol
     */
    countByRole() {
        const roleCounts = {};
        
        for (const user of this.users) {
            const role = user.role || 'unknown';
            roleCounts[role] = (roleCounts[role] || 0) + 1;
        }
        
        return roleCounts;
    }
}

// === MAIN - Pruebas ===
const main = () => {
    console.log("=== Ejercicio 1: Python → JavaScript ===\n");
    
    // Datos de prueba (adaptados a camelCase)
    const users = [
        { firstName: 'Ana', lastName: 'García', age: 25, email: 'ana@example.com', role: 'admin' },
        { firstName: 'Carlos', lastName: 'López', age: 30, email: 'carlos@example.com', role: 'user' },
        { firstName: 'María', lastName: 'Martínez', age: 22, email: 'maria@example.com', role: 'user' },
        { firstName: 'Juan', lastName: 'Pérez', age: 35, email: 'juan@example.com', role: 'moderator' },
        { firstName: 'Laura', lastName: 'Sánchez', age: 28, email: 'laura@example.com', role: 'user' },
    ];
    
    // 1. Probar findUsersByAge
    console.log("1. Usuarios entre 25 y 30 años:");
    const filtered = findUsersByAge(users, 25, 30);
    filtered.forEach(user => {
        console.log(`   - ${user.firstName} ${user.lastName}: ${user.age} años`);
    });
    
    // 2. Probar calculateAverageScore
    console.log("\n2. Promedio de puntuaciones:");
    const scores = [85, 90, -5, 78, 92, 0, 88];
    const avg = calculateAverageScore(scores);
    console.log(`   Puntuaciones: ${scores}`);
    console.log(`   Promedio (solo válidas): ${avg.toFixed(2)}`);
    
    // 3. Probar formatUserInfo
    console.log("\n3. Formatear información de usuario:");
    const userInfo = formatUserInfo(users[0]);
    console.log(`   ${userInfo}`);
    
    const userWithoutEmail = { firstName: 'Pedro', lastName: 'Gómez', age: 40 };
    const userInfo2 = formatUserInfo(userWithoutEmail);
    console.log(`   ${userInfo2}`);
    
    // 4. Probar getUniqueTags
    console.log("\n4. Tags únicos de items:");
    const items = [
        { name: 'Item 1', tags: ['javascript', 'web', 'frontend'] },
        { name: 'Item 2', tags: ['python', 'backend', 'api'] },
        { name: 'Item 3', tags: ['javascript', 'react', 'frontend'] },
        { name: 'Item 4', tags: ['python', 'django', 'web'] },
    ];
    const uniqueTags = getUniqueTags(items);
    console.log(`   Tags únicos: ${uniqueTags.sort()}`);
    
    // 5. Probar UserManager
    console.log("\n5. UserManager:");
    const manager = new UserManager(users);
    
    // Buscar por email
    const foundUser = manager.findByEmail('carlos@example.com');
    if (foundUser) {
        console.log(`   Usuario encontrado: ${foundUser.firstName} ${foundUser.lastName}`);
    }
    
    // Buscar de nuevo (debe venir del cache)
    const foundUser2 = manager.findByEmail('carlos@example.com');
    console.log(`   Segunda búsqueda (desde cache): ${foundUser2.firstName}`);
    
    // Contar por rol
    const roleCounts = manager.countByRole();
    console.log("   Usuarios por rol:");
    for (const [role, count] of Object.entries(roleCounts)) {
        console.log(`      - ${role}: ${count}`);
    }
    
    // Usuario no encontrado
    const notFound = manager.findByEmail('noexiste@example.com');
    console.log(`   Usuario no encontrado: ${notFound}`);
    
    console.log("\n=== ¡Todas las pruebas completadas! ===");
    console.log("Código traducido exitosamente a JavaScript ES6+ 🚀");
};

// Ejecutar pruebas si se ejecuta directamente
if (typeof require !== 'undefined' && require.main === module) {
    main();
}

// Exportar funciones para uso en otros módulos
module.exports = {
    findUsersByAge,
    calculateAverageScore,
    formatUserInfo,
    getUniqueTags,
    UserManager
};
