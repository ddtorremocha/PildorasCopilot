# Píldora 4: Generación de Datos de Prueba - De Bases de Datos Vacías a Entornos Realistas 🎲

## 📋 Descripción

Descubre cómo **GitHub Copilot genera datasets realistas y coherentes** para testing, desarrollo y demos en segundos.

### ❓ ¿Qué problema resuelve?

**Forma tradicional:**
- Pensar en valores de ejemplo manualmente
- Escribir INSERT statements uno por uno
- Mantener consistencia entre datos relacionados
- Crear JSONs de prueba desde cero
- Tiempo considerable para cada entorno

**Con GitHub Copilot:**
- Describe el tipo de datos que necesitas
- Copilot genera datasets completos
- Datos coherentes y realistas
- Múltiples formatos (JSON, CSV, SQL)

---

## 🎯 Objetivos de Aprendizaje

1. ✅ Generar datos de prueba realistas para cualquier dominio
2. ✅ Crear datasets con relaciones coherentes
3. ✅ Producir datos en múltiples formatos (JSON, CSV, SQL, XML)
4. ✅ Generar datos para testing, desarrollo y demos
5. ✅ Poblar bases de datos de prueba rápidamente

---

## 💡 Ejemplos Prácticos

### Ejemplo 1: Usuarios de Prueba (JSON)

**Prompt:**
```javascript
// Generar array de 10 usuarios con: id, nombre, email, edad, ciudad, fecha_registro
```

**Copilot genera:**
```javascript
const usuarios = [
    {
        id: 1,
        nombre: "Ana García Martínez",
        email: "ana.garcia@example.com",
        edad: 28,
        ciudad: "Madrid",
        fecha_registro: "2023-05-15"
    },
    {
        id: 2,
        nombre: "Carlos López Pérez",
        email: "carlos.lopez@example.com",
        edad: 35,
        ciudad: "Barcelona",
        fecha_registro: "2023-06-20"
    },
    // ... 8 usuarios más
];
```

### Ejemplo 2: Productos E-commerce (SQL)

**Prompt:**
```sql
-- Generar 20 productos INSERT para tabla products (id, name, price, category, stock)
```

**Copilot genera:**
```sql
INSERT INTO products (id, name, price, category, stock) VALUES
(1, 'Laptop Dell XPS 15', 1299.99, 'Electrónica', 15),
(2, 'Mouse Logitech MX Master 3', 99.99, 'Accesorios', 50),
(3, 'Teclado Mecánico Keychron K2', 89.99, 'Accesorios', 30),
-- ... 17 más
```

### Ejemplo 3: Datos Relacionados

**Prompt:**
```python
# Generar datos de prueba: 5 clientes, cada uno con 2-4 pedidos
```

**Copilot genera:**
```python
clientes = [
    {
        "id": 1,
        "nombre": "María González",
        "email": "maria.g@example.com",
        "pedidos": [
            {"id": 101, "total": 250.50, "fecha": "2024-01-15", "estado": "entregado"},
            {"id": 102, "total": 89.99, "fecha": "2024-02-20", "estado": "en_proceso"}
        ]
    },
    # ... 4 clientes más con sus pedidos
]
```

---

## 🎮 Ejercicios Prácticos

### 🟢 Ejercicio 1: Datos Básicos (Fácil)

Genera datasets para:
1. 20 empleados de una empresa (nombre, puesto, salario, departamento)
2. 15 libros (título, autor, ISBN, precio, páginas)
3. 30 transacciones bancarias (fecha, monto, tipo, descripción)

### 🟡 Ejercicio 2: Datos Relacionados (Intermedio)

Genera un sistema de:
- 10 escuelas
- Cada una con 3-5 maestros
- Cada maestro con 2-3 cursos
- Datos coherentes entre relaciones

### 🔴 Ejercicio 3: Dataset Completo (Avanzado)

Genera datos completos para una red social:
- 50 usuarios
- Relaciones de amistad entre ellos
- Posts (cada usuario 5-10 posts)
- Comentarios en posts
- Likes
- Datos coherentes temporalmente

---

## 🎯 Mejores Prácticas

### ✅ Hacer

1. **Especifica cantidad y atributos claramente**
   ```python
   # Generar 25 productos con: id, nombre, precio (50-500), categoría, stock (0-100)
   ```

2. **Pide datos realistas y variados**
   ```javascript
   // Generar 15 usuarios con nombres hispanos, edades 18-65, ciudades de España
   ```

3. **Define relaciones explícitamente**
   ```python
   # Generar clientes donde cada cliente tiene 2-5 pedidos con fechas coherentes
   ```

4. **Especifica el formato de salida**
   ```sql
   -- Generar INSERT statements para PostgreSQL
   ```

### ❌ Evitar

1. **Datos demasiado simplistas** ("user1", "user2")
2. **Ignorar validaciones** (emails inválidos, fechas futuras)
3. **Sin variedad** (todos con mismos valores)

---

## 📊 Formatos Soportados

| Formato | Caso de Uso | Ejemplo |
|---------|-------------|---------|
| **JSON** | APIs, mocks, fixtures | `[{...}, {...}]` |
| **CSV** | Importación masiva, Excel | `id,name,email` |
| **SQL** | Poblar DB directamente | `INSERT INTO...` |
| **XML** | Sistemas legacy | `<user><name>...</name></user>` |
| **YAML** | Configuraciones, fixtures | `users:\n  - name: ...` |

---

## 🚀 Casos de Uso Reales

### Development
```python
# Datos para desarrollo local
usuarios_dev = generar_usuarios(50)
```

### Testing
```javascript
// Datos para tests unitarios
const mockUsers = [
    { id: 1, role: 'admin', ... },
    { id: 2, role: 'user', ... }
];
```

### Demos
```sql
-- Datos impresionantes para demos de clientes
INSERT INTO customers (name, revenue, ...)
VALUES ('Acme Corp', 1500000, ...);
```

### Staging
```json
// Datos realistas para ambiente de staging
{
    "users": [...],
    "products": [...],
    "orders": [...]
}
```

---

## 📖 Recursos Adicionales

- [Faker.js](https://fakerjs.dev/) - Librería complementaria
- [Mockaroo](https://www.mockaroo.com/) - Herramienta web
- [JSON Generator](https://json-generator.com/) - Generador online

---

## ➡️ Próximos Pasos

👉 Continúa con: **[Píldora 5: Explicación de Código Complejo](../05_explicacion_codigo/README.md)**

**Tiempo estimado: 15-20 minutos**
