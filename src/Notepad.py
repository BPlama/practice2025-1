# Текстовый редактор
import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)


def find_text():
    text_area.tag_remove('highlight', '1.0', tk.END)
    search_word = search_entry.get()
    if search_word:
        start_pos = '1.0'
        while True:
            start_pos = text_area.search(search_word, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_word)}c"
            text_area.tag_add('highlight', start_pos, end_pos)
            text_area.tag_config('highlight', background='lightblue')
            start_pos = end_pos


# Создание основного окна
root = tk.Tk()
root.title("Текстовый редактор с поиском")
root.geometry("800x600")

# Меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)

# Поиск
search_frame = tk.Frame(root)
search_frame.pack(fill='x')

search_entry = tk.Entry(search_frame)
search_entry.pack(side='left', padx=10, pady=5, fill='x', expand=True)

search_button = tk.Button(search_frame, text="Найти", command=find_text)
search_button.pack(side='right', padx=10)

# Текстовое поле
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

# Горячие клавиши
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-f>', lambda event: find_text())

root.mainloop()
