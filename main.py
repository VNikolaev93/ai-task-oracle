import csv
from core import TaskManager

def main():
    manager = TaskManager()
    
    # Читаем файл с заметками
    try:
        with open("meeting_notes_en.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Ошибка: Создай файл meeting_notes.txt с текстом встреч!")
        return

    print("--- Начинаю магию анализа ---")
    tasks = manager.process_text(content)
    
    # Сохраняем в CSV (Excel)
    if tasks:
        keys = tasks[0].keys()
        with open("tasks_report.csv", "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(tasks)
        print("✅ Готово! Проверь файл tasks_report.csv")

if __name__ == "__main__":
    main()