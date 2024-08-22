from catalog import Library

def validate_book(book: dict) -> tuple:
    required_fields = {"title", "author", "genre"}
    
    # Проверка наличия всех обязательных полей
    missing_fields = required_fields - set(book.keys())
    if missing_fields:
        return False, f"Отсутствуют обязательные поля: {', '.join(missing_fields)}"
    
    # Проверка типа данных полей и наличия значений
    invalid_fields = [field for field in required_fields if not isinstance(book.get(field), str) or not book.get(field).strip()]
    if invalid_fields:
        return False, f"Неверный тип данных или пустое значение для полей: {', '.join(invalid_fields)}"
    
    return True, "Книга прошла проверку"
