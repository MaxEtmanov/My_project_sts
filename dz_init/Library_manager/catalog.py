class Library:
    def __init__(self) -> None:
        self.books = []
        
    def add_book(self, title, author, genre):
        book = {"title": title, "author": author, "genre": genre}
        self.books.append(book)
        print(f"Книга '{title}' добавлена в каталог.")
        
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена из каталога.")
                return
        print(f"Книга '{title}' не найдена в каталоге.")
        
    def search_book(self, titles, authors, genres):
        found_books = []
        for book in self.books:
            if (
                (not titles or book["title"] in titles)
                and (not authors or book["author"] in authors)
                and (not genres or book["genre"] in genres)
            ):
                found_books.append(book)
        return found_books
       
    def display_books(self):
        if not self.books:
            print("Каталог пуст.")
            return
        else:
            print("Список книг в каталоге:")
            for book in self.books:
                print(f"Название: {book['title']}, Автор: {book['author']}, Жанр: {book['genre']}")