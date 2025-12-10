# Ejercicio Bonus: Cadena de Traducción
# Este código será traducido a través de múltiples lenguajes
# Python → JavaScript → TypeScript → Java → Python

from typing import List, Dict, Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Book:
    """Representa un libro en la biblioteca"""
    id: int
    title: str
    author: str
    isbn: str
    published_year: int
    available: bool = True
    borrowed_by: Optional[str] = None

class Library:
    """Sistema de gestión de biblioteca"""
    
    def __init__(self):
        self.books: List[Book] = []
        self.members: Dict[str, Dict] = {}
        self.next_id = 1
    
    def add_book(self, title: str, author: str, isbn: str, year: int) -> Book:
        """Agrega un nuevo libro a la biblioteca"""
        book = Book(
            id=self.next_id,
            title=title,
            author=author,
            isbn=isbn,
            published_year=year
        )
        self.books.append(book)
        self.next_id += 1
        return book
    
    def search_books(self, query: str) -> List[Book]:
        """Busca libros por título o autor"""
        query_lower = query.lower()
        return [
            book for book in self.books
            if query_lower in book.title.lower() or query_lower in book.author.lower()
        ]
    
    def borrow_book(self, book_id: int, member_id: str) -> bool:
        """Presta un libro a un miembro"""
        book = self._find_book(book_id)
        
        if not book:
            return False
        
        if not book.available:
            return False
        
        if member_id not in self.members:
            return False
        
        book.available = False
        book.borrowed_by = member_id
        
        # Registrar préstamo
        if 'borrowed_books' not in self.members[member_id]:
            self.members[member_id]['borrowed_books'] = []
        
        self.members[member_id]['borrowed_books'].append({
            'book_id': book_id,
            'borrowed_at': datetime.now().isoformat()
        })
        
        return True
    
    def return_book(self, book_id: int) -> bool:
        """Devuelve un libro a la biblioteca"""
        book = self._find_book(book_id)
        
        if not book or book.available:
            return False
        
        member_id = book.borrowed_by
        book.available = True
        book.borrowed_by = None
        
        # Actualizar registro del miembro
        if member_id and member_id in self.members:
            borrowed = self.members[member_id].get('borrowed_books', [])
            self.members[member_id]['borrowed_books'] = [
                b for b in borrowed if b['book_id'] != book_id
            ]
        
        return True
    
    def add_member(self, member_id: str, name: str, email: str) -> None:
        """Registra un nuevo miembro"""
        self.members[member_id] = {
            'name': name,
            'email': email,
            'joined_at': datetime.now().isoformat(),
            'borrowed_books': []
        }
    
    def get_member_books(self, member_id: str) -> List[Book]:
        """Obtiene los libros prestados a un miembro"""
        if member_id not in self.members:
            return []
        
        borrowed_ids = [
            b['book_id'] 
            for b in self.members[member_id].get('borrowed_books', [])
        ]
        
        return [
            book for book in self.books 
            if book.id in borrowed_ids
        ]
    
    def get_available_books(self) -> List[Book]:
        """Obtiene todos los libros disponibles"""
        return [book for book in self.books if book.available]
    
    def get_statistics(self) -> Dict:
        """Obtiene estadísticas de la biblioteca"""
        total_books = len(self.books)
        available_books = len(self.get_available_books())
        
        return {
            'total_books': total_books,
            'available_books': available_books,
            'borrowed_books': total_books - available_books,
            'total_members': len(self.members),
            'active_borrowers': sum(
                1 for m in self.members.values()
                if m.get('borrowed_books', [])
            )
        }
    
    def _find_book(self, book_id: int) -> Optional[Book]:
        """Encuentra un libro por ID (método privado)"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

# Uso de ejemplo
if __name__ == "__main__":
    library = Library()
    
    # Agregar libros
    library.add_book("1984", "George Orwell", "978-0451524935", 1949)
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925)
    
    # Agregar miembro
    library.add_member("M001", "John Doe", "john@example.com")
    
    # Prestar libro
    library.borrow_book(1, "M001")
    
    # Ver estadísticas
    stats = library.get_statistics()
    print(f"Libros totales: {stats['total_books']}")
    print(f"Libros disponibles: {stats['available_books']}")
