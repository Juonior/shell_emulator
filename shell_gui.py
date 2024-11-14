import tkinter as tk
from tkinter import scrolledtext
from emulator import ShellEmulator


class ShellGUI:
    def __init__(self, username, tar_path, log_path, script_path=None):
        self.shell = ShellEmulator(username, tar_path, log_path, script_path)

        self.root = tk.Tk()
        self.root.title(f"{self.shell.username}@shell")
        
        # Настроим внешний вид окна
        self.root.configure(bg="#2e2e2e")
        self.root.geometry("600x400")

        # Шрифт и стиль
        self.font = ('Monaco', 12)

        # Command input field with current directory display
        self.command_entry = tk.Entry(self.root, width=80, font=self.font, bg="#1e1e1e", fg="#ffffff", insertbackground='white')
        self.command_entry.bind("<Return>", self.on_command_entered)
        self.command_entry.grid(row=1, column=0, padx=10, pady=5)
        self.update_command_entry()

        # Output display area (scrollable terminal output)
        self.output_display = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD, state=tk.DISABLED, bg="#1e1e1e", fg="#ffffff", font=self.font)
        self.output_display.grid(row=0, column=0, padx=10, pady=10)

    def on_command_entered(self, event):
        """Handler for pressing Enter key"""
        command = self.command_entry.get().strip() 

        self.output_display.config(state=tk.NORMAL)  # Enable editing to update the text

        self.output_display.insert(tk.END, f"$ {command}\n")  # Show the command
        self.output_display.config(state=tk.DISABLED)  # Disable editing after update

        
        self.execute_command()

    def execute_command(self):
        """Execute command entered in the command input field"""
        command = self.command_entry.get().strip()  # Получаем строку из поля ввода и убираем пробелы по бокам

        # Убираем префикс (например, "user1@shell: / $ "), оставляя только команду
        if command.startswith(f"{self.shell.username}@shell: {self.shell.current_dir} $ "):
            command = command[len(f"{self.shell.username}@shell: {self.shell.current_dir} $ "):].strip()

        if command:  # Если команда не пустая
            self.shell.execute_command(command, self)  # Выполнение команды
            # self.display_output(command)  # Показать вывод команды

        self.command_entry.delete(0, tk.END)  # Очистить поле ввода после выполнения команды
        self.update_command_entry()  # Обновить поле ввода с текущей директорией



    def update_command_entry(self):
        """Update the input field with the current directory and user prompt"""
        current_dir_display = f"{self.shell.username}@shell: {self.shell.current_dir} $ "
        self.command_entry.delete(0, tk.END)
        self.command_entry.insert(0, current_dir_display)  # Show current directory in the input field

    def display_output(self, *command):
        command = " ".join(command)
        """Display the result of a command in the output window"""
        self.output_display.config(state=tk.NORMAL)  # Enable editing to update the text
        # self.output_display.insert(tk.END, current_dir_display + self.shell.history[-1] + "\n\n")  # Show the command result
        self.output_display.insert(tk.END, f"$ {command}\n")  # Show the command
        self.output_display.config(state=tk.DISABLED)  # Disable editing after update
        self.output_display.yview(tk.END)  # Scroll to the bottom

    def run(self):
        """Start the GUI event loop"""
        self.root.mainloop()
