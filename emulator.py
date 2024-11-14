from commands import ls, cd, exit_shell, cal, chown, history
from filesystem import VirtualFileSystem
from log_handler import LogHandler

class ShellEmulator:
    def __init__(self, username, tar_path, log_path, script_path=None):
        self.username = username
        self.history = []
        self.current_dir = '/'

        self.logger = LogHandler(log_path, username)

        self.fs = VirtualFileSystem(tar_path)
        if script_path:
            self._run_start_script(script_path)
    
    def _run_start_script(self, script_path):
        with open(script_path, 'r') as script:
            for line in script:
                self.execute_command(line.strip())
    
    def execute_command(self, command, shell_gui):
        self.logger.log(command)
        self.history.append(command)

        parts = command.split()
        if not parts:
            return

        cmd = parts[0]
        args = parts[1:]

        if cmd == 'ls':
            ls.ls(self.fs, shell_gui, self.current_dir, args)
        elif cmd == 'cd':
            try:
                new_dir = cd.cd(self.fs, shell_gui, self, args)
                if new_dir is not None:
                    self.current_dir = new_dir
            except FileNotFoundError:
                shell_gui.display_output(f"Ошибка: Директория '{args[0]}' не найдена.")
            except NotADirectoryError:
                shell_gui.display_output(f"Ошибка: '{args[0]}' не является директорией.")
            except Exception as e:
                shell_gui.display_output(f"Ошибка при смене директории: {e}")
        elif cmd == 'exit':
            exit_shell.exit_shell(shell_gui)
        elif cmd == 'cal':
            cal.cal(shell_gui, args)
        elif cmd == 'chown':
            try:
                chown.chown(self.fs ,shell_gui, self, args)
            except FileNotFoundError:
                shell_gui.display_output(f"Ошибка: Файл '{args[1]}' не найден.")
            except Exception as e:
                shell_gui.display_output(f"Ошибка при смене владельца: {e}")
        elif cmd == 'history':
            history.history(shell_gui, self)
        else:
            # pass
            print("GG")
            shell_gui.display_output(f"Команда не найдена")
    
    # def run(self):
    #     while True:
    #         command = input(f"{self.username}@shell: {self.current_dir} $ ")
    #         self.execute_command(command)
