from catalog import Library

def generate_report(library: Library) -> str:
    report = "Отчет о книгах в библиотеке\n"
    report += "===========================\n\n"

    if not library.books:
        report += "Библиотека пуста.\n"
    else:
        report += f"Общее количество книг: {len(library.books)}\n\n"
        report += "Список книг:\n"
        for i, book in enumerate(library.books, 1):
            report += f"{i}. Название: {book['title']}\n"
            report += f"   Автор: {book['author']}\n"
            report += f"   Жанр: {book['genre']}\n\n"

    report += "===========================\n"
    report += "Конец отчета"

    return report