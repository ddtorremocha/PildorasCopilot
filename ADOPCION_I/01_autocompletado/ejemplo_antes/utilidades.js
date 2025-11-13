/**
 * Ejemplos ANTES de usar GitHub Copilot
 * Código JavaScript escrito de forma tradicional
 */

// Ejemplo 1: Formateo de fecha (después de buscar en Google)
function formatDate(date) {
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
}

// Ejemplo 2: Validar email (copiado de Stack Overflow)
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Ejemplo 3: Capitalizar primera letra (implementación manual)
function capitalize(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

// Ejemplo 4: Calcular interés compuesto (buscando fórmula)
function calculateCompoundInterest(principal, rate, time) {
    // A = P(1 + r/n)^(nt)
    // Asumiendo compuesto anual (n=1)
    const amount = principal * Math.pow((1 + rate / 100), time);
    return amount.toFixed(2);
}

// Ejemplo 5: Generar color aleatorio (implementado paso a paso)
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Ejemplo 6: Ordenar array de objetos (después de leer docs)
function sortByProperty(array, property) {
    return array.sort((a, b) => {
        if (a[property] < b[property]) return -1;
        if (a[property] > b[property]) return 1;
        return 0;
    });
}

// Ejemplo 7: Debounce (copiado y adaptado)
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Tests manuales
console.log(formatDate(new Date()));
console.log(validateEmail('test@example.com'));
console.log(capitalize('hola mundo'));
console.log(calculateCompoundInterest(1000, 5, 10));
console.log(getRandomColor());
