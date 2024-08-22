



# Определение __all__ для контроля того, что импортируется при использовании from ... import *
__all__ = ['validate_book', 'format_book_data']

# Опционально: добавьте сообщение для отслеживания импорта
print("Модуль Library_manager.utils импортирован")

# Импорт из data_validation.py
from utils.data_validation import validate_book


from utils.formatting import format_book_data
