// Ejercicio 2: JavaScript → Python
// Traduce este código a Python 3.11+ con type hints

const fetchUserData = async (userId) => {
    try {
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching user:', error);
        return null;
    }
};

const processOrders = (orders) => {
    return orders
        .filter(order => order.status === 'completed')
        .map(order => ({
            id: order.id,
            total: order.items.reduce((sum, item) => sum + item.price * item.quantity, 0),
            itemCount: order.items.length
        }))
        .sort((a, b) => b.total - a.total);
};

class ShoppingCart {
    constructor() {
        this.items = [];
        this.discountCode = null;
    }
    
    addItem(product, quantity = 1) {
        const existingItem = this.items.find(item => item.product.id === product.id);
        
        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push({ product, quantity });
        }
    }
    
    removeItem(productId) {
        this.items = this.items.filter(item => item.product.id !== productId);
    }
    
    calculateTotal() {
        const subtotal = this.items.reduce(
            (sum, item) => sum + item.product.price * item.quantity, 
            0
        );
        
        if (this.discountCode) {
            return subtotal * (1 - this.discountCode.percentage / 100);
        }
        
        return subtotal;
    }
    
    getItemCount() {
        return this.items.reduce((count, item) => count + item.quantity, 0);
    }
}

const debounce = (func, delay) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func(...args), delay);
    };
};

// === MAIN - Pruebas ===
const main = async () => {
    console.log("=== Ejercicio 2: JavaScript → Python ===\n");
    
    // 1. Probar processOrders
    console.log("1. Procesar órdenes completadas:");
    const orders = [
        {
            id: 1,
            status: 'completed',
            items: [
                { name: 'Laptop', price: 1200, quantity: 1 },
                { name: 'Mouse', price: 25, quantity: 2 }
            ]
        },
        {
            id: 2,
            status: 'pending',
            items: [
                { name: 'Keyboard', price: 80, quantity: 1 }
            ]
        },
        {
            id: 3,
            status: 'completed',
            items: [
                { name: 'Monitor', price: 300, quantity: 2 },
                { name: 'Cable', price: 10, quantity: 3 }
            ]
        },
        {
            id: 4,
            status: 'completed',
            items: [
                { name: 'Headphones', price: 150, quantity: 1 }
            ]
        }
    ];
    
    const processed = processOrders(orders);
    console.log("   Órdenes completadas ordenadas por total:");
    processed.forEach(order => {
        console.log(`   - Orden #${order.id}: $${order.total.toFixed(2)} (${order.itemCount} items)`);
    });
    
    // 2. Probar ShoppingCart
    console.log("\n2. Carrito de compras:");
    const cart = new ShoppingCart();
    
    const product1 = { id: 1, name: 'Laptop', price: 1200 };
    const product2 = { id: 2, name: 'Mouse', price: 25 };
    const product3 = { id: 3, name: 'Keyboard', price: 80 };
    
    cart.addItem(product1, 1);
    cart.addItem(product2, 2);
    cart.addItem(product3, 1);
    
    console.log(`   Items en el carrito: ${cart.getItemCount()}`);
    console.log(`   Total sin descuento: $${cart.calculateTotal().toFixed(2)}`);
    
    // Agregar más cantidad de un producto existente
    cart.addItem(product2, 1);
    console.log(`   Después de agregar 1 mouse más: ${cart.getItemCount()} items`);
    
    // Aplicar descuento
    cart.discountCode = { code: 'SAVE20', percentage: 20 };
    console.log(`   Total con 20% descuento: $${cart.calculateTotal().toFixed(2)}`);
    
    // Remover un item
    cart.removeItem(product3.id);
    console.log(`   Después de remover keyboard: ${cart.getItemCount()} items`);
    console.log(`   Total final: $${cart.calculateTotal().toFixed(2)}`);
    
    // 3. Probar debounce
    console.log("\n3. Debounce function:");
    let callCount = 0;
    const expensiveOperation = () => {
        callCount++;
        console.log(`   Operación ejecutada (llamada #${callCount})`);
    };
    
    const debouncedOperation = debounce(expensiveOperation, 100);
    
    console.log("   Llamando función 5 veces rápidamente...");
    debouncedOperation();
    debouncedOperation();
    debouncedOperation();
    debouncedOperation();
    debouncedOperation();
    
    // Esperar para que se ejecute el debounce
    await new Promise(resolve => setTimeout(resolve, 150));
    console.log(`   Solo se ejecutó 1 vez (debounced)`);
    
    // 4. Simular fetchUserData (sin hacer request real)
    console.log("\n4. Fetch user data (simulación):");
    console.log("   Nota: fetchUserData requiere un servidor real o mock.");
    console.log("   Esta función hace requests HTTP y retorna null en caso de error.");
    console.log("   Firma: async fetchUserData(userId) => Promise<User|null>");
    
    console.log("\n=== ¡Todas las pruebas completadas! ===");
    console.log("Ahora traduce este código a Python 3.11+ con type hints 🚀");
};

// Ejecutar pruebas si se ejecuta directamente
if (require.main === module) {
    main().catch(error => {
        console.error('Error en las pruebas:', error);
        process.exit(1);
    });
}

module.exports = { fetchUserData, processOrders, ShoppingCart, debounce };
