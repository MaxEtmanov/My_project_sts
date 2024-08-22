def format_book_data(data: dict) -> str:
    """
    Форматирует данные книги для вывода в отчет.

    Args:
        data (dict): Словарь с данными книги. Должен содержать ключи 'title', 'author' и 'genre'.

    Returns:
        str: Отформатированная строка с данными книги.

    Пример:
        >>> book = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Novel'}
        >>> format_book_data(book)
        'Title: The Great Gatsby, Author: F. Scott Fitzgerald, Genre: Novel'
    """
    return f"Название: {data['title']}, Автор: {data['author']}, Жанр: {data['genre']}"