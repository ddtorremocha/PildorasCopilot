// Generar array de 15 usuarios con datos realistas
const usuarios = [
    {
        id: 1,
        nombre: "Ana García Martínez",
        email: "ana.garcia@example.com",
        edad: 28,
        ciudad: "Madrid",
        telefono: "+34 612 345 678",
        fecha_registro: "2023-05-15",
        rol: "admin"
    },
    {
        id: 2,
        nombre: "Carlos López Pérez",
        email: "carlos.lopez@example.com",
        edad: 35,
        ciudad: "Barcelona",
        telefono: "+34 623 456 789",
        fecha_registro: "2023-06-20",
        rol: "usuario"
    },
    {
        id: 3,
        nombre: "María Rodríguez Silva",
        email: "maria.rodriguez@example.com",
        edad: 42,
        ciudad: "Valencia",
        telefono: "+34 634 567 890",
        fecha_registro: "2023-04-10",
        rol: "usuario"
    },
    {
        id: 4,
        nombre: "José Martín González",
        email: "jose.martin@example.com",
        edad: 31,
        ciudad: "Sevilla",
        telefono: "+34 645 678 901",
        fecha_registro: "2023-07-05",
        rol: "moderador"
    },
    {
        id: 5,
        nombre: "Laura Sánchez Ruiz",
        email: "laura.sanchez@example.com",
        edad: 26,
        ciudad: "Bilbao",
        telefono: "+34 656 789 012",
        fecha_registro: "2023-08-12",
        rol: "usuario"
    },
    {
        id: 6,
        nombre: "Miguel Fernández Torres",
        email: "miguel.fernandez@example.com",
        edad: 39,
        ciudad: "Zaragoza",
        telefono: "+34 667 890 123",
        fecha_registro: "2023-03-22",
        rol: "usuario"
    },
    {
        id: 7,
        nombre: "Isabel Díaz Castro",
        email: "isabel.diaz@example.com",
        edad: 33,
        ciudad: "Málaga",
        telefono: "+34 678 901 234",
        fecha_registro: "2023-09-18",
        rol: "admin"
    },
    {
        id: 8,
        nombre: "David Moreno Jiménez",
        email: "david.moreno@example.com",
        edad: 45,
        ciudad: "Murcia",
        telefono: "+34 689 012 345",
        fecha_registro: "2023-02-14",
        rol: "usuario"
    },
    {
        id: 9,
        nombre: "Carmen Álvarez Romero",
        email: "carmen.alvarez@example.com",
        edad: 29,
        ciudad: "Palma",
        telefono: "+34 690 123 456",
        fecha_registro: "2023-10-25",
        rol: "usuario"
    },
    {
        id: 10,
        nombre: "Francisco Gómez Navarro",
        email: "francisco.gomez@example.com",
        edad: 37,
        ciudad: "Las Palmas",
        telefono: "+34 601 234 567",
        fecha_registro: "2023-01-30",
        rol: "moderador"
    },
    {
        id: 11,
        nombre: "Sofía Ruiz Molina",
        email: "sofia.ruiz@example.com",
        edad: 24,
        ciudad: "Alicante",
        telefono: "+34 612 345 789",
        fecha_registro: "2023-11-08",
        rol: "usuario"
    },
    {
        id: 12,
        nombre: "Antonio Jiménez Serrano",
        email: "antonio.jimenez@example.com",
        edad: 41,
        ciudad: "Córdoba",
        telefono: "+34 623 456 890",
        fecha_registro: "2023-05-03",
        rol: "usuario"
    },
    {
        id: 13,
        nombre: "Elena Torres Vega",
        email: "elena.torres@example.com",
        edad: 34,
        ciudad: "Valladolid",
        telefono: "+34 634 567 901",
        fecha_registro: "2023-06-17",
        rol: "admin"
    },
    {
        id: 14,
        nombre: "Pablo Ramírez Ortiz",
        email: "pablo.ramirez@example.com",
        edad: 27,
        ciudad: "Vigo",
        telefono: "+34 645 678 012",
        fecha_registro: "2023-07-21",
        rol: "usuario"
    },
    {
        id: 15,
        nombre: "Lucía Castro Herrera",
        email: "lucia.castro@example.com",
        edad: 38,
        ciudad: "Gijón",
        telefono: "+34 656 789 123",
        fecha_registro: "2023-08-29",
        rol: "usuario"
    }
];

// Generar array de 20 productos de e-commerce
const productos = [
    { id: 1, nombre: "Laptop Dell XPS 15", precio: 1299.99, categoria: "Electrónica", stock: 15, rating: 4.7 },
    { id: 2, nombre: "Mouse Logitech MX Master 3", precio: 99.99, categoria: "Accesorios", stock: 50, rating: 4.8 },
    { id: 3, nombre: "Teclado Mecánico Keychron K2", precio: 89.99, categoria: "Accesorios", stock: 30, rating: 4.6 },
    { id: 4, nombre: "Monitor LG 27 UltraFine 4K", precio: 649.99, categoria: "Electrónica", stock: 12, rating: 4.5 },
    { id: 5, nombre: "Auriculares Sony WH-1000XM4", precio: 349.99, categoria: "Audio", stock: 25, rating: 4.9 },
    { id: 6, nombre: "Webcam Logitech C920", precio: 79.99, categoria: "Accesorios", stock: 40, rating: 4.4 },
    { id: 7, nombre: "SSD Samsung 1TB NVMe", precio: 129.99, categoria: "Almacenamiento", stock: 60, rating: 4.7 },
    { id: 8, nombre: "RAM Corsair 32GB DDR4", precio: 159.99, categoria: "Componentes", stock: 35, rating: 4.6 },
    { id: 9, nombre: "Micrófono Blue Yeti", precio: 129.99, categoria: "Audio", stock: 20, rating: 4.7 },
    { id: 10, nombre: "iPad Air 256GB", precio: 749.99, categoria: "Tablets", stock: 18, rating: 4.8 },
    { id: 11, nombre: "Apple Pencil 2da Gen", precio: 129.99, categoria: "Accesorios", stock: 45, rating: 4.9 },
    { id: 12, nombre: "Disco Duro Externo 2TB", precio: 79.99, categoria: "Almacenamiento", stock: 55, rating: 4.5 },
    { id: 13, nombre: "Router ASUS WiFi 6", precio: 199.99, categoria: "Redes", stock: 22, rating: 4.6 },
    { id: 14, nombre: "Soporte Laptop Ergonómico", precio: 39.99, categoria: "Accesorios", stock: 70, rating: 4.3 },
    { id: 15, nombre: "Hub USB-C 7 puertos", precio: 49.99, categoria: "Accesorios", stock: 65, rating: 4.4 },
    { id: 16, nombre: "Lámpara LED escritorio", precio: 34.99, categoria: "Oficina", stock: 80, rating: 4.5 },
    { id: 17, nombre: "Silla Gaming Secretlab", precio: 449.99, categoria: "Muebles", stock: 8, rating: 4.8 },
    { id: 18, nombre: "Escritorio Standing Desk", precio: 599.99, categoria: "Muebles", stock: 5, rating: 4.7 },
    { id: 19, nombre: "Cable HDMI 2.1 3m", precio: 24.99, categoria: "Cables", stock: 100, rating: 4.6 },
    { id: 20, nombre: "Mousepad XXL Gamer", precio: 29.99, categoria: "Accesorios", stock: 90, rating: 4.5 }
];

// Generar datos de pedidos relacionados con usuarios
const pedidos = [
    {
        id: 1001,
        usuario_id: 1,
        productos: [
            { producto_id: 1, cantidad: 1, precio_unitario: 1299.99 },
            { producto_id: 2, cantidad: 1, precio_unitario: 99.99 }
        ],
        total: 1399.98,
        estado: "entregado",
        fecha: "2023-11-01",
        direccion_envio: "Calle Mayor 123, Madrid"
    },
    {
        id: 1002,
        usuario_id: 2,
        productos: [
            { producto_id: 5, cantidad: 1, precio_unitario: 349.99 }
        ],
        total: 349.99,
        estado: "en_transito",
        fecha: "2023-11-10",
        direccion_envio: "Paseo de Gracia 456, Barcelona"
    },
    {
        id: 1003,
        usuario_id: 3,
        productos: [
            { producto_id: 10, cantidad: 1, precio_unitario: 749.99 },
            { producto_id: 11, cantidad: 1, precio_unitario: 129.99 }
        ],
        total: 879.98,
        estado: "procesando",
        fecha: "2023-11-12",
        direccion_envio: "Avenida del Puerto 789, Valencia"
    }
];

// Exportar para uso en otros archivos
if (typeof module !== 'undefined') {
    module.exports = { usuarios, productos, pedidos };
}
