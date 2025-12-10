<?php
// Ejercicio 4: PHP → Node.js/Express
// Convierte estos endpoints PHP a Express.js con async/await

header('Content-Type: application/json');

// GET /api/products
function getProducts() {
    $pdo = getDBConnection();
    
    $category = $_GET['category'] ?? null;
    $minPrice = $_GET['min_price'] ?? 0;
    $maxPrice = $_GET['max_price'] ?? PHP_INT_MAX;
    
    $sql = "SELECT * FROM products WHERE price BETWEEN :min AND :max";
    $params = [':min' => $minPrice, ':max' => $maxPrice];
    
    if ($category) {
        $sql .= " AND category = :category";
        $params[':category'] = $category;
    }
    
    $sql .= " ORDER BY name ASC";
    
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    $products = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    echo json_encode([
        'success' => true,
        'data' => $products,
        'count' => count($products)
    ]);
}

// POST /api/products
function createProduct() {
    $data = json_decode(file_get_contents('php://input'), true);
    
    // Validation
    if (empty($data['name'])) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Name is required']);
        return;
    }
    
    if (!isset($data['price']) || $data['price'] <= 0) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Valid price is required']);
        return;
    }
    
    $pdo = getDBConnection();
    
    $sql = "INSERT INTO products (name, description, price, category, stock) 
            VALUES (:name, :description, :price, :category, :stock)";
    
    $stmt = $pdo->prepare($sql);
    $result = $stmt->execute([
        ':name' => $data['name'],
        ':description' => $data['description'] ?? '',
        ':price' => $data['price'],
        ':category' => $data['category'] ?? 'general',
        ':stock' => $data['stock'] ?? 0
    ]);
    
    if ($result) {
        $productId = $pdo->lastInsertId();
        
        http_response_code(201);
        echo json_encode([
            'success' => true,
            'data' => ['id' => $productId],
            'message' => 'Product created successfully'
        ]);
    } else {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => 'Database error']);
    }
}

// PUT /api/products/{id}
function updateProduct($id) {
    $data = json_decode(file_get_contents('php://input'), true);
    
    $pdo = getDBConnection();
    
    // Check if product exists
    $stmt = $pdo->prepare("SELECT id FROM products WHERE id = :id");
    $stmt->execute([':id' => $id]);
    
    if (!$stmt->fetch()) {
        http_response_code(404);
        echo json_encode(['success' => false, 'error' => 'Product not found']);
        return;
    }
    
    // Build update query dynamically
    $fields = [];
    $params = [':id' => $id];
    
    if (isset($data['name'])) {
        $fields[] = "name = :name";
        $params[':name'] = $data['name'];
    }
    
    if (isset($data['price'])) {
        $fields[] = "price = :price";
        $params[':price'] = $data['price'];
    }
    
    if (isset($data['stock'])) {
        $fields[] = "stock = :stock";
        $params[':stock'] = $data['stock'];
    }
    
    if (empty($fields)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'No fields to update']);
        return;
    }
    
    $sql = "UPDATE products SET " . implode(', ', $fields) . " WHERE id = :id";
    
    $stmt = $pdo->prepare($sql);
    $result = $stmt->execute($params);
    
    if ($result) {
        echo json_encode([
            'success' => true,
            'message' => 'Product updated successfully'
        ]);
    } else {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => 'Database error']);
    }
}

// DELETE /api/products/{id}
function deleteProduct($id) {
    $pdo = getDBConnection();
    
    $stmt = $pdo->prepare("DELETE FROM products WHERE id = :id");
    $result = $stmt->execute([':id' => $id]);
    
    if ($stmt->rowCount() > 0) {
        echo json_encode([
            'success' => true,
            'message' => 'Product deleted successfully'
        ]);
    } else {
        http_response_code(404);
        echo json_encode(['success' => false, 'error' => 'Product not found']);
    }
}

function getDBConnection() {
    $host = 'localhost';
    $db = 'ecommerce';
    $user = 'root';
    $pass = 'password';
    
    return new PDO("mysql:host=$host;dbname=$db", $user, $pass);
}

// Router
$method = $_SERVER['REQUEST_METHOD'];
$path = $_SERVER['PATH_INFO'] ?? '/';

if ($method === 'GET' && $path === '/api/products') {
    getProducts();
} elseif ($method === 'POST' && $path === '/api/products') {
    createProduct();
} elseif ($method === 'PUT' && preg_match('#^/api/products/(\d+)$#', $path, $matches)) {
    updateProduct($matches[1]);
} elseif ($method === 'DELETE' && preg_match('#^/api/products/(\d+)$#', $path, $matches)) {
    deleteProduct($matches[1]);
} else {
    http_response_code(404);
    echo json_encode(['success' => false, 'error' => 'Endpoint not found']);
}
?>
