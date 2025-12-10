// Ejercicio 6: TypeScript Legacy → TypeScript Moderno
// Moderniza este código usando features de TypeScript 5.x

// Old style interfaces and types
interface User {
    id: number;
    name: string;
    email: string;
    role: string;
    age?: number;
}

interface Product {
    id: number;
    name: string;
    price: number;
    category: string;
}

// Using 'any' - should be avoided
function processData(data: any): any {
    return data;
}

// Old style enums
enum UserRole {
    Admin = 'admin',
    User = 'user',
    Guest = 'guest'
}

// Verbose type guards
function isAdmin(user: User): boolean {
    return user.role === 'admin';
}

function isUser(user: User): boolean {
    return user.role === 'user';
}

// No proper error handling types
class UserService {
    private users: User[] = [];
    
    constructor() {}
    
    // Could use better typing
    findUser(id: number): User | null {
        const user = this.users.find(u => u.id === id);
        return user || null;
    }
    
    // Using Record without proper constraints
    getUsersByRole(): Record<string, User[]> {
        const result: Record<string, User[]> = {};
        
        for (const user of this.users) {
            if (!result[user.role]) {
                result[user.role] = [];
            }
            result[user.role].push(user);
        }
        
        return result;
    }
    
    // Loose typing
    updateUser(id: number, updates: any): User | null {
        const user = this.findUser(id);
        if (!user) return null;
        
        Object.assign(user, updates);
        return user;
    }
}

// Not using utility types effectively
interface UpdateUserDTO {
    name?: string;
    email?: string;
    age?: number;
}

// Could be better typed
function filterProducts(products: Product[], filters: any): Product[] {
    return products.filter(product => {
        if (filters.minPrice && product.price < filters.minPrice) return false;
        if (filters.maxPrice && product.price > filters.maxPrice) return false;
        if (filters.category && product.category !== filters.category) return false;
        return true;
    });
}

// Old promise style
function fetchUserData(userId: number): Promise<User> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const user = {
                id: userId,
                name: 'John Doe',
                email: 'john@example.com',
                role: 'user'
            };
            resolve(user);
        }, 1000);
    });
}

// Could use const assertions
const CONFIG = {
    apiUrl: 'https://api.example.com',
    timeout: 5000,
    retries: 3
};

// Using classes where types might be better
class Point {
    constructor(public x: number, public y: number) {}
    
    distance(other: Point): number {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}

// Not leveraging mapped types
interface ValidationRules {
    required: boolean;
    minLength: number;
    maxLength: number;
}

interface FormValidation {
    name: ValidationRules;
    email: ValidationRules;
    password: ValidationRules;
}

export { User, Product, UserRole, UserService, filterProducts, fetchUserData };
