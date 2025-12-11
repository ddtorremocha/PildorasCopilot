/**
 * EJERCICIOS PRÁCTICOS - Píldora 1: Autocompletado Inteligente
 * 
 * Instrucciones:
 * 1. Lee el comentario de cada ejercicio
 * 2. Escribe SOLO el comentario descriptivo antes de la función
 * 3. Presiona Tab y deja que Copilot complete
 * 4. Revisa y ejecuta con Node.js para verificar
 * 
 * Tip: Ctrl+Enter para ver sugerencias alternativas
 */

// ===================================
// NIVEL 1: EJERCICIOS BÁSICOS (🟢)
// ===================================

// Ejercicio 1.1: Validaciones
// TODO: Función para validar si un string contiene solo números


// TODO: Función para validar si una URL tiene formato correcto


// TODO: Función para validar longitud de contraseña (mínimo 8 caracteres)
function validatePasswordLength(password) {
    return password.length >= 8;
}


// Ejercicio 1.2: Formateo
// TODO: Función para formatear número con separadores de miles


// TODO: Función para convertir string a title case


// TODO: Función para formatear número de teléfono a formato (XXX) XXX-XXXX


// ===================================
// NIVEL 2: EJERCICIOS INTERMEDIOS (🟡)
// ===================================

// Ejercicio 2.1: Arrays
// TODO: Función que retorna elementos únicos de dos arrays


// TODO: Función que encuentra la intersección de dos arrays


// TODO: Función que divide un array en chunks de tamaño n


// Ejercicio 2.2: Objetos
// TODO: Función que hace deep clone de un objeto


// TODO: Función que combina múltiples objetos en uno


// TODO: Función que obtiene valor anidado de un objeto usando path (ej: "user.address.city")


// ===================================
// NIVEL 3: EJERCICIOS AVANZADOS (🔴)
// ===================================

// Ejercicio 3.1: Procesamiento complejo
const productos = [
    { id: 1, nombre: "Laptop", precio: 1200, categoria: "Electrónica", stock: 5 },
    { id: 2, nombre: "Mouse", precio: 25, categoria: "Accesorios", stock: 50 },
    { id: 3, nombre: "Teclado", precio: 80, categoria: "Accesorios", stock: 30 },
    { id: 4, nombre: "Monitor", precio: 300, categoria: "Electrónica", stock: 15 }
];

// TODO: Función que calcula el valor total del inventario


// TODO: Función que agrupa productos por categoría


// TODO: Función que encuentra productos con stock bajo (menos de 10)


// Ejercicio 3.2: Async/Promises
// TODO: Función async que simula una petición HTTP con delay


// TODO: Función que ejecuta múltiples promesas y retorna la primera que resuelva


// TODO: Función que reintenta una operación async hasta 3 veces si falla


// ===================================
// DESAFÍO FINAL 🏆
// ===================================

// Crea una clase completa de Carrito de Compras
// TODO: Clase ShoppingCart con array de items
// TODO: Método para agregar producto
// TODO: Método para remover producto por ID
// TODO: Método para calcular total
// TODO: Método para aplicar descuento en porcentaje
// TODO: Método para obtener cantidad de items


// ===================================
// TESTS
// ===================================

// Descomenta para probar tus funciones
/*
console.log('=== Tests Básicos ===');
// console.log(validarNumeros('12345'));

console.log('\n=== Tests Arrays ===');
// console.log(elementosUnicos([1,2,3], [2,3,4]));

console.log('\n=== Tests Productos ===');
// console.log(calcularValorInventario(productos));

console.log('\n=== Tests Async ===');
// simularPeticion().then(console.log);
*/
