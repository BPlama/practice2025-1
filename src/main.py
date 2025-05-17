# Интерфейс приложения

import tkinter as tk
from tkinter import ttk
import editor_logic as logic

# Основное окно
root = tk.Tk()
root.title("Редактор текста")
root.geometry("900x650")

# Счётчик слов
word_count_var = tk.StringVar()

# Меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=lambda: logic.open_file(text_area, update_word_count))
file_menu.add_command(label="Сохранить как TXT", command=lambda: logic.save_txt_file(text_area))
file_menu.add_command(label="Сохранить как DOCX",
                      command=lambda: logic.save_docx_file(text_area, current_font_size.get()))
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

# Панель инструментов
toolbar = tk.Frame(root)
toolbar.pack(fill='x')

# Форматирование
bold_btn = tk.Button(toolbar, text="Жирный", command=lambda: logic.toggle_format(text_area, "bold"))
bold_btn.pack(side="left", padx=2)
italic_btn = tk.Button(toolbar, text="Курсив", command=lambda: logic.toggle_format(text_area, "italic"))
italic_btn.pack(side="left", padx=2)
underline_btn = tk.Button(toolbar, text="Подчёркнутый", command=lambda: logic.toggle_format(text_area, "underline"))
underline_btn.pack(side="left", padx=2)

# Размер шрифта
current_font_size = tk.IntVar(value=12)
font_size_box = ttk.Combobox(toolbar, textvariable=current_font_size, width=5, state="readonly")
font_size_box["values"] = tuple(range(8, 32, 2))
font_size_box.pack(side="left", padx=10)
font_size_box.bind("<<ComboboxSelected>>", lambda event: logic.change_font_size(text_area, current_font_size))

# Поиск
search_frame = tk.Frame(root)
search_frame.pack(fill='x')
search_entry = tk.Entry(search_frame)
search_entry.pack(side='left', fill='x', expand=True, padx=10, pady=5)
search_button = tk.Button(search_frame, text="Найти", command=lambda: logic.find_text(text_area, search_entry))
search_button.pack(side='right', padx=10)

# Текстовое поле
text_area = tk.Text(root, wrap='word', font=("Arial", current_font_size.get()))
text_area.pack(expand=True, fill='both', padx=10, pady=(0, 5))

# Стили
text_area.tag_configure("bold", font=("Arial", current_font_size.get(), "bold"))
text_area.tag_configure("italic", font=("Arial", current_font_size.get(), "italic"))
text_area.tag_configure("underline", font=("Arial", current_font_size.get(), "underline"))

# Метка счётчика слов
word_count_label = tk.Label(root, textvariable=word_count_var, anchor='w')
word_count_label.pack(fill='x', padx=10)


def update_word_count(event=None):
    logic.update_word_count(text_area, word_count_var)


text_area.bind("<KeyRelease>", update_word_count)
update_word_count()

# Горячие клавиши
root.bind("<Control-b>", lambda e: logic.toggle_format(text_area, "bold"))
root.bind("<Control-n>", lambda e: logic.toggle_format(text_area, "italic"))
root.bind("<Control-u>", lambda e: logic.toggle_format(text_area, "underline"))
root.bind("<Control-o>", lambda e: logic.open_file(text_area, update_word_count))
root.bind("<Control-s>", lambda e: logic.save_txt_file(text_area))
root.bind("<Control-f>", lambda e: logic.find_text(text_area, search_entry))

root.mainloop()
