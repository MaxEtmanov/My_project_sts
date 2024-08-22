from catalog import Library
from repotr import generate_report
from utils import validate_book
from utils import format_book_data
# from catalog import Library
# from repotr import generate_report
# from utils.data_validation import validate_book
# from utils.formatting import format_book_data


# Создаем экземпляр библиотеки
library = Library()

# Добавляем несколько книг
library.add_book("Война и мир","Лев Толстой", "Роман")
library.add_book("Преступление и наказание", "Федор Достоевский", "Роман")
library.add_book("Мастер и Маргарита", "Михаил Булгаков", "Фантастика")


library.display_books()
for book in library.books:
    validate = validate_book(book)
    print(validate)

found_books = library.search_book(titles=None, authors=None, genres=["Роман"])
print("\nНайденные романы:")
for book in found_books:
    print(f"{book['title']} - {book['author']}")
    
library.remove_book("Мастер и Маргарита")

library.display_books()
    
for book in library.books:
    book = format_book_data(book)
    print(book)