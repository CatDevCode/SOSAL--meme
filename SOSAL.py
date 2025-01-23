import tkinter as tk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("СОСАЛ???")
        
        # Создаем метку с текстом
        self.label = tk.Label(root, text="СОСАЛ???", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Создаем кнопку "Да"
        self.button_yes = tk.Button(root, text="Да", command=self.on_yes)
        self.button_yes.pack(side=tk.LEFT, padx=20)

        # Создаем кнопку "Нет"
        self.button_no = tk.Button(root, text="Нет", command=self.on_no)
        self.button_no.pack(side=tk.RIGHT, padx=20)

        self.message = "Ты сосал"
        self.current_index = 0

    def on_yes(self):
        # Запускаем вывод текста постепенно
        self.current_index = 0
        self.label.config(text="")  # Очищаем метку перед выводом
        self.display_message()

    def display_message(self):
        if self.current_index < len(self.message):
            # Выводим текущий символ
            self.label.config(text=self.label.cget("text") + self.message[self.current_index])
            self.current_index += 1
            # Запланировать следующий вызов через 500 мс
            self.root.after(500, self.display_message)

    def on_no(self):
        # Перемещаем кнопку "Нет" в случайное место
        x = random.randint(0, self.root.winfo_width() - 100)  # Учитываем ширину кнопки
        y = random.randint(0, self.root.winfo_height() - 50)  # Учитываем высоту кнопки
        self.button_no.place(x=x, y=y)  # Используем place для перемещения кнопки

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("400x400")  # Устанавливаем размер окна
    app.button_no.place(x=200, y=200)  # Начальная позиция кнопки "Нет"
    root.mainloop()
