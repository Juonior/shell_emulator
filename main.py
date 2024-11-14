import argparse
from shell_gui import ShellGUI  # Импортируем класс ShellGUI

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator GUI")
    parser.add_argument('--username', required=True, help='Имя пользователя для приглашения в командной строке')
    parser.add_argument('--fs', required=True, help='Путь к tar-архиву виртуальной файловой системы')
    parser.add_argument('--log', required=True, help='Путь к CSV файлу для логирования')
    parser.add_argument('--script', required=False, help='Путь к стартовому скрипту')

    args = parser.parse_args()

    # Запускаем GUI оболочку
    shell_gui = ShellGUI(args.username, args.fs, args.log, args.script)
    shell_gui.run()

if __name__ == "__main__":
    main()
