/**
 * Ejemplos DESPUÉS de usar GitHub Copilot
 * Simplemente escribe comentarios y deja que Copilot genere el código
 */

// Formatear fecha a DD/MM/YYYY
function formatDate(date) {
    return date.toLocaleDateString('es-ES', { day: '2-digit', month: '2-digit', year: 'numeric' });
}

// Validar formato de email
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Capitalizar primera letra de cada palabra
function capitalizeWords(str) {
    return str.replace(/\b\w/g, char => char.toUpperCase());
}

// Calcular interés compuesto: A = P(1 + r/n)^(nt)
function calculateCompoundInterest(principal, rate, time, frequency = 12) {
    const amount = principal * Math.pow(1 + (rate / 100) / frequency, frequency * time);
    return parseFloat(amount.toFixed(2));
}

// Generar color hexadecimal aleatorio
function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
}

// Ordenar array de objetos por propiedad específica
function sortByProperty(array, property, ascending = true) {
    return array.sort((a, b) => {
        const comparison = a[property] > b[property] ? 1 : -1;
        return ascending ? comparison : -comparison;
    });
}

// Función debounce para limitar ejecuciones
function debounce(func, delay) {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func(...args), delay);
    };
}

// Función para generar UUID v4
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

// Función para agrupar array por propiedad
function groupBy(array, key) {
    return array.reduce((result, item) => {
        const group = item[key];
        result[group] = result[group] || [];
        result[group].push(item);
        return result;
    }, {});
}

// Función para calcular diferencia de días entre fechas
function daysBetween(date1, date2) {
    const oneDay = 24 * 60 * 60 * 1000;
    return Math.round(Math.abs((date1 - date2) / oneDay));
}

// Función para formatear número como moneda
function formatCurrency(amount, currency = 'USD', locale = 'en-US') {
    return new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency
    }).format(amount);
}

// Función para eliminar acentos de un string
function removeAccents(str) {
    return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

// Función para validar si un string es JSON válido
function isValidJSON(str) {
    try {
        JSON.parse(str);
        return true;
    } catch (e) {
        return false;
    }
}

// Función para obtener parámetros de query string
function getQueryParams(url) {
    const params = new URLSearchParams(new URL(url).search);
    return Object.fromEntries(params);
}

// Función para truncar número a decimales específicos
function truncateDecimals(number, decimals = 2) {
    const multiplier = Math.pow(10, decimals);
    return Math.trunc(number * multiplier) / multiplier;
}

// Tests automáticos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        formatDate,
        validateEmail,
        capitalizeWords,
        calculateCompoundInterest,
        getRandomColor,
        sortByProperty,
        debounce,
        generateUUID,
        groupBy,
        daysBetween,
        formatCurrency,
        removeAccents,
        isValidJSON,
        getQueryParams,
        truncateDecimals
    };
} else {
    // Demos en navegador
    console.log('=== Formateo y Validaciones ===');
    console.log('Fecha:', formatDate(new Date()));
    console.log('Email válido:', validateEmail('test@example.com'));
    console.log('Capitalizado:', capitalizeWords('hola mundo developer'));
    
    console.log('\n=== Cálculos ===');
    console.log('Interés compuesto:', calculateCompoundInterest(1000, 5, 10));
    console.log('Días entre fechas:', daysBetween(new Date('2024-01-01'), new Date('2024-12-31')));
    
    console.log('\n=== Utilidades ===');
    console.log('Color aleatorio:', getRandomColor());
    console.log('UUID:', generateUUID());
    console.log('Moneda:', formatCurrency(1234.56, 'EUR', 'es-ES'));
    console.log('Sin acentos:', removeAccents('José García'));
    
    console.log('\n=== Agrupación ===');
    const usuarios = [
        { nombre: 'Ana', edad: 25 },
        { nombre: 'Luis', edad: 30 },
        { nombre: 'María', edad: 25 }
    ];
    console.log('Agrupado por edad:', groupBy(usuarios, 'edad'));
}
