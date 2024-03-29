# Вспомогательная библиотека `color.py`
`color.py` - простой модуль, который позволяет сделать ваш вывод более понятным. Он добавляет цвета и стили в вашу программу, используя ANSI ESCAPE COLOR CODES.

| Цвет           | Цвет текста | Цвет фона |
|----------------|-------------|-----------|
| Черный         | \033[30m    | \033[40m  |
| Красный        | \033[31m    | \033[41m  |
| Зеленый        | \033[32m    | \033[42m  |
| Желтый         | \033[33m    | \033[43m  |
| Фиолетовый     | \033[34m    | \033[44m  |
| Бирюзовый      | \033[35m    | \033[45m  |
| Сбросить стили | \033[0m     | \033[0m   |

## Классы

```python
class FG:
	"""Класс цвета текста"""
	BLACK = '\033[30m'		# Черный
	RED = '\033[31m' 		# Красный
	GREEN = '\033[32m'		# Зеленый
	YELLOW = '\033[33m'		# Желтый
	BLUE = '\033[34m'		# Синий
	PURPLE = '\033[35m'		# Фиолетовый
	CYAN = '\033[36m'		# Бирюзовый
	END = '\033[0m'			# Сбросить цвет


class BG:
	"""Класс фона текста"""
	BLACK = '\033[40m'		# Черный
	RED = '\033[41m'		# Красный
	GREEN = '\033[42m'		# Зеленый
	YELLOW = '\033[43m'		# Желтый
	BLUE = '\033[44m'		# Синий
	PURPLE = '\033[45m'		# Фиолетовый
	CYAN = '\033[46m'		# Бирюзовый
	END = '\033[0m'			# Сбросить цвет


class Style:
	"""Класс стилизации текста"""
	END = '\033[0m'			# Сбросить стиль
	BOLD = '\033[1m'		# Жирный
	DIM = '\033[2m'			# Блеклый
	ITALIC = '\033[3m'		# Курсив
	UNDERLINE = '\033[4m'	# Подчеркивание
```

---

[Предыдущая статья](./index.md) [Следующая статья](./color-lib.md)

[Содержание](./index.md)
