#!/usr/bin/python3
# Вспомогательная библиотека color.py


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