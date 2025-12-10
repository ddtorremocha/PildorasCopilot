// Ejercicio 3: Java → C#
// Traduce esta clase Java a C# moderno usando convenciones .NET

import java.util.*;
import java.util.stream.Collectors;

// === Clases de dominio ===

class Product {
    private Long id;
    private String name;
    private double price;
    private String category;
    private boolean active;
    
    public Product() {}
    
    public Product(Long id, String name, double price, String category, boolean active) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.category = category;
        this.active = active;
    }
    
    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    
    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }
    
    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }
    
    @Override
    public String toString() {
        return String.format("Product{id=%d, name='%s', price=%.2f, category='%s', active=%s}",
            id, name, price, category, active);
    }
}

class ProductDTO {
    private String name;
    private double price;
    private String category;
    
    public ProductDTO(String name, double price, String category) {
        this.name = name;
        this.price = price;
        this.category = category;
    }
    
    public String getName() { return name; }
    public double getPrice() { return price; }
    public String getCategory() { return category; }
}

// === Excepciones ===

class ValidationException extends Exception {
    public ValidationException(String message) {
        super(message);
    }
}

class ProductNotFoundException extends Exception {
    public ProductNotFoundException(Long id) {
        super("Product not found with id: " + id);
    }
}

// === Interfaces y servicios mock ===

interface ProductRepository {
    Optional<Product> findById(Long id);
    List<Product> findByCategory(String category);
    Product save(Product product);
}

interface CacheService {
    <T> Optional<T> get(String key, Class<T> clazz);
    <T> void set(String key, T value, int ttlSeconds);
    void delete(String key);
}

interface Logger {
    void info(String message);
}

// === Implementaciones mock para pruebas ===

class MockProductRepository implements ProductRepository {
    private Map<Long, Product> database = new HashMap<>();
    private Long nextId = 1L;
    
    public MockProductRepository() {
        // Datos de prueba
        database.put(1L, new Product(1L, "Laptop", 1200.0, "Electronics", true));
        database.put(2L, new Product(2L, "Mouse", 25.0, "Electronics", true));
        database.put(3L, new Product(3L, "Desk", 350.0, "Furniture", true));
        database.put(4L, new Product(4L, "Chair", 200.0, "Furniture", false));
        nextId = 5L;
    }
    
    @Override
    public Optional<Product> findById(Long id) {
        return Optional.ofNullable(database.get(id));
    }
    
    @Override
    public List<Product> findByCategory(String category) {
        return database.values().stream()
            .filter(p -> p.getCategory().equals(category))
            .collect(Collectors.toList());
    }
    
    @Override
    public Product save(Product product) {
        if (product.getId() == null) {
            product.setId(nextId++);
        }
        database.put(product.getId(), product);
        return product;
    }
}

class MockCacheService implements CacheService {
    private Map<String, Object> cache = new HashMap<>();
    
    @Override
    public <T> Optional<T> get(String key, Class<T> clazz) {
        Object value = cache.get(key);
        if (value != null && clazz.isInstance(value)) {
            return Optional.of(clazz.cast(value));
        }
        return Optional.empty();
    }
    
    @Override
    public <T> void set(String key, T value, int ttlSeconds) {
        cache.put(key, value);
    }
    
    @Override
    public void delete(String key) {
        cache.remove(key);
    }
}

class ConsoleLogger implements Logger {
    @Override
    public void info(String message) {
        System.out.println("[INFO] " + message);
    }
}

// === Clase principal del servicio ===

public class ProductService {
    private final ProductRepository repository;
    private final CacheService cacheService;
    private final Logger logger;
    
    public ProductService(ProductRepository repository, CacheService cacheService, Logger logger) {
        this.repository = repository;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    public Optional<Product> findById(Long id) {
        String cacheKey = "product:" + id;
        
        // Check cache first
        Optional<Product> cached = cacheService.get(cacheKey, Product.class);
        if (cached.isPresent()) {
            logger.info("Product found in cache: " + id);
            return cached;
        }
        
        // Query database
        Optional<Product> product = repository.findById(id);
        
        // Update cache
        product.ifPresent(p -> cacheService.set(cacheKey, p, 3600));
        
        return product;
    }
    
    public List<Product> findByCategory(String category, boolean activeOnly) {
        List<Product> products = repository.findByCategory(category);
        
        if (activeOnly) {
            products = products.stream()
                .filter(Product::isActive)
                .collect(Collectors.toList());
        }
        
        return products.stream()
            .sorted((p1, p2) -> p1.getName().compareTo(p2.getName()))
            .collect(Collectors.toList());
    }
    
    public Product createProduct(ProductDTO dto) throws ValidationException {
        validateProductDTO(dto);
        
        Product product = new Product();
        product.setName(dto.getName());
        product.setPrice(dto.getPrice());
        product.setCategory(dto.getCategory());
        product.setActive(true);
        
        Product saved = repository.save(product);
        logger.info("Product created: " + saved.getId());
        
        return saved;
    }
    
    public void updatePrice(Long productId, double newPrice) throws ProductNotFoundException {
        Product product = repository.findById(productId)
            .orElseThrow(() -> new ProductNotFoundException(productId));
        
        if (newPrice <= 0) {
            throw new IllegalArgumentException("Price must be positive");
        }
        
        product.setPrice(newPrice);
        repository.save(product);
        
        // Invalidate cache
        cacheService.delete("product:" + productId);
    }
    
    private void validateProductDTO(ProductDTO dto) throws ValidationException {
        if (dto.getName() == null || dto.getName().trim().isEmpty()) {
            throw new ValidationException("Product name is required");
        }
        
        if (dto.getPrice() <= 0) {
            throw new ValidationException("Price must be positive");
        }
    }
    
    // === MAIN - Pruebas ===
    public static void main(String[] args) {
        System.out.println("=== Ejercicio 3: Java → C# ===\n");
        
        // Crear instancias mock
        ProductRepository repository = new MockProductRepository();
        CacheService cacheService = new MockCacheService();
        Logger logger = new ConsoleLogger();
        
        ProductService service = new ProductService(repository, cacheService, logger);
        
        try {
            // 1. Buscar producto por ID
            System.out.println("1. Buscar producto por ID:");
            Optional<Product> product = service.findById(1L);
            product.ifPresent(p -> System.out.println("   Encontrado: " + p));
            
            // Buscar de nuevo (debe venir del cache)
            System.out.println("\n   Buscando el mismo producto (desde cache):");
            service.findById(1L);
            
            // 2. Buscar por categoría
            System.out.println("\n2. Productos de categoría 'Electronics' (solo activos):");
            List<Product> electronics = service.findByCategory("Electronics", true);
            electronics.forEach(p -> System.out.println("   - " + p));
            
            System.out.println("\n3. Productos de categoría 'Furniture' (todos):");
            List<Product> furniture = service.findByCategory("Furniture", false);
            furniture.forEach(p -> System.out.println("   - " + p));
            
            // 3. Crear nuevo producto
            System.out.println("\n4. Crear nuevo producto:");
            ProductDTO newProductDto = new ProductDTO("Keyboard", 80.0, "Electronics");
            Product newProduct = service.createProduct(newProductDto);
            System.out.println("   Producto creado: " + newProduct);
            
            // 4. Actualizar precio
            System.out.println("\n5. Actualizar precio del producto #1:");
            System.out.println("   Precio anterior: $1200.00");
            service.updatePrice(1L, 1100.0);
            Optional<Product> updated = service.findById(1L);
            updated.ifPresent(p -> System.out.println("   Precio nuevo: $" + p.getPrice()));
            
            // 5. Probar validaciones
            System.out.println("\n6. Probar validaciones:");
            try {
                ProductDTO invalidDto = new ProductDTO("", -50.0, "Test");
                service.createProduct(invalidDto);
            } catch (ValidationException e) {
                System.out.println("   ✓ Validación funcionó: " + e.getMessage());
            }
            
            // 6. Producto no encontrado
            System.out.println("\n7. Buscar producto inexistente:");
            Optional<Product> notFound = service.findById(999L);
            System.out.println("   Encontrado: " + (notFound.isPresent() ? "Sí" : "No"));
            
            System.out.println("\n=== ¡Todas las pruebas completadas! ===");
            System.out.println("Ahora traduce este código a C# usando convenciones .NET 🚀");
            
        } catch (Exception e) {
            System.err.println("Error durante las pruebas: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
