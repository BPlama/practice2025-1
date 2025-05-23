# Проект: Автоматизация процесса анкетирования

Статический сайт, созданный в  период проектной практики для сопровождения проекта по дисциплине **"Проектная деятельность"**.  
Цель — автоматизация анкетирования в учебном процессе Московского Политеха.  

---

## 📌 Оглавление  

### 1. Статический сайт  
- [1.1 Структура сайта](#-структура-сайта)  
- [1.2 Цели и задачи](#-цели-и-задачи)  
- [1.3 Команда](#-команда)  
- [1.4 Технологии](#-технологии)  
- [1.5 Журнал прогресса](#-журнал-прогресса)  
- [1.6 Ресурсы](#-ресурсы)  

### 2. Текстовый редактор  
- [2.1 Введение](#-введение)  
- [2.2 Этапы исследования](#-этапы-исследования)  
- [2.3 Этапы разработки](#-этапы-разработки)  
- [2.4 Техническое руководство](#-техническое-руководство)  
- [2.5 Возможности редактора](#-возможности-редактора)  


---

## 🏠 Структура сайта  
| Страница       | Описание                                                                 |
|----------------|--------------------------------------------------------------------------|
| **Главная**    | Аннотация проекта: проблема ручного анкетирования и предлагаемое решение. |
| **О проекте**  | Детализация целей, задач, используемых технологий и структуры команды.   |
| **Участники**  | Состав команд (дизайн, разработка анкет, архитектура БД, тестирование).  |
| **Журнал**     | Этапы работы: анализ, проектирование, тестирование, документация.        |
| **Ресурсы**    | Партнёры (Московский Политех), документация библиотек, полезные ссылки.  |

---

## 🎯 Цели и задачи  
### Проблема  
Ручное составление анкет в СДО требует значительных трудозатрат:  
- Подбор вопросов вручную.  
- Отсутствие автоматизации анализа ответов.  

### Решение  
Проект предлагает:  
- Генерацию анкет на основе XML-шаблонов.  
- Автоматизацию обработки результатов.  
- Веб-интерфейс для управления процессом (в перспективе).  

### Технические задачи  
- Разработка структуры базы данных (UML-диаграммы).  
- Создание скриптов для генерации анкет (Python + XML).  
- Тестирование модулей.  

---

## 👥 Команда  
Проект реализуют 4 группы:  

| Роль                | Участники                                                                 | Вклад                                                                 |
|---------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Дизайн**          | Желтоноженко Оксана, Пинчер Дарья                                       | Макеты интерфейса (страницы входа, управления группами, тестирования). |
| **Разработка анкет**| Хачатурян Тигран, Журавлёв Кирилл, Шагаев Тамерлан, Зайнидинов Абдухамид | Генерация XML-анкет, написание скриптов для автоматизации.            |
| **Архитектура БД**  | Жгутова Анна, Скрипкин Михаил, Сурин Павел                              | Проектирование и создание архитектуры базы данных.                    |
| **Тестирование**    | Шувалов Дмитрий, Петрищев Александр, Атаев Мерген, Голдин Александр     | План тестирования, проверка генерации анкет, отчётность.             |


---

## 📅 Журнал прогресса  
### Ключевые этапы  
1. **Анализ** (сравнение систем анкетирования, таблицы).  
2. **Проектирование**:  
   - Дизайн интерфейса (макеты страниц).  
   - UML-диаграмма базы данных.  
3. **Разработка**:  
   - Генератор анкет (XML-файлы).  
   - Скрипты для обработки данных.  
4. **Тестирование**:  
   - Проверка корректности XML-структур.  
   - Отчёт об ошибках.  


---

## 🔗 Ресурсы  
- **Партнёр**: [Московский Политех](https://mospolytech.ru/).

## 🛠 Технологии  
### Основной стек  
- **Frontend**: HTML, CSS.  
- **Backend (скрипты)**: Python (библиотеки `xml.etree`, `sqlite3`, `openpyxl`, `BeautifulSoup`).  
- **База данных**: SQLite, UML-диаграммы.
- **Форматы данных**: XML (хранение анкет), Excel (анализ результатов).

### Документация 
- [SQLite](https://www.sqlite.org/docs.html)  
- [Python XML](https://docs.python.org/3/library/xml.etree.elementtree.html)  
- [OpenPyXL](https://openpyxl.readthedocs.io/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python XML DOM](https://docs.python.org/3/library/xml.dom.html)  
---

# Проект: Текстовый редактор на Python

## 📌 Введение

Целью данного проекта было создание текстового редактора с возможностью открытия, сохранения, поиска и базового форматирования текста.  
В качестве основной технологии был выбран язык Python, а для графического интерфейса использована библиотека `Tkinter`.  
Редактор может служить обучающим инструментом для новичков и основой для более продвинутых приложений.

---

## 🔍 Этапы исследования

На первом этапе были изучены:
- Как работает `Tkinter` и создаются графические интерфейсы.
- Работа с файловой системой Python (`open`, `filedialog`).
- Поиск текста в `Text`-виджете с подсветкой.
- Применение тегов для стилизации (жирный, курсив, подчёркнутый).
- Работа с библиотекой `python-docx` для сохранения в `.docx`.
- Подсчёт слов и настройка шрифта.

Использовались:
- [Документация по tkinter](https://docs.python.org/3/library/tkinter.html)  
- [Instructables guide](https://www.instructables.com/Create-a-Simple-Python-Text-Editor/)  
- [python-docx](https://python-docx.readthedocs.io/)

---

## 🛠 Этапы разработки

1. **Создание главного окна** через `Tk()` с настройкой размеров.
2. **Добавление текстового поля** (`Text`), привязка прокрутки.
3. **Реализация меню:**
   - Открытие и сохранение файлов (`.txt`, `.docx`).
   - Выход из приложения.
4. **Поисковая панель:**
   - Поле ввода и кнопка.
   - Подсветка найденного текста.
5. **Горячие клавиши:**
   - `Ctrl+O` — открыть файл.
   - `Ctrl+S` — сохранить.
   - `Ctrl+F` — найти текст.
   - `Ctrl+B`, `Ctrl+I`, `Ctrl+U` — форматирование выделенного текста.
6. **Форматирование текста:**
   - Поддержка `bold`, `italic`, `underline` с применением тегов.
7. **Сохранение в DOCX:**
   - Учитывается форматирование при экспорте.
8. **Счётчик слов** и динамическое изменение размера шрифта.

---

## 🧑‍💻 Техническое руководство

### Установка зависимостей

```bash
pip install tk python-docx
```

> `tkinter` обычно предустановлен в Python.

### Пример: сохранение форматированного текста в `.docx`

```python
from docx import Document
from docx.shared import Pt

def save_docx_file(text_area, font_size):
    doc = Document()
    index = "1.0"
    while True:
        if index == text_area.index(tk.END):
            break
        line_end = index.split('.')[0] + ".end"
        line_text = text_area.get(index, line_end)
        p = doc.add_paragraph()
        for i, char in enumerate(line_text):
            char_index = f"{index}+{i}c"
            tags = text_area.tag_names(char_index)
            run = p.add_run(char)
            run.font.size = Pt(font_size)
            run.font.bold = 'bold' in tags
            run.font.italic = 'italic' in tags
            run.font.underline = 'underline' in tags
        index = text_area.index(f"{line_end}+1c")
    doc.save("output.docx")
```

### Счётчик слов

```python
def update_word_count(text_area, word_count_var):
    content = text_area.get("1.0", "end-1c")
    words = content.split()
    word_count_var.set(f"Слов: {len(words)}")
```

---

## 💡 Возможности редактора

| Функция                | Описание                                                        |
|------------------------|-----------------------------------------------------------------|
| Открытие/сохранение    | Работа с `.txt`файлами и сохранение в формате `.docx` .         |
| Поиск текста           | Подсветка найденных слов.                                       |
| Форматирование         | Поддержка **жирного**, *курсива*, и <u>подчёркивания</u>.       |
| Горячие клавиши        | `Ctrl+O`, `Ctrl+S`, `Ctrl+F`, `Ctrl+B`, `Ctrl+I`, `Ctrl+U`.     |
| Шрифт и размер         | Изменение размера шрифта.                                       |
| Подсчёт слов           | Динамическое обновление количества слов.                        |
