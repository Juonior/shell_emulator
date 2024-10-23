import argparse
from emulator import ShellEmulator

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument('--username', required=True, help='Имя пользователя для приглашения в командной строке')
    parser.add_argument('--fs', required=True, help='Путь к tar-архиву виртуальной файловой системы')
    parser.add_argument('--log', required=True, help='Путь к CSV файлу для логирования')
    parser.add_argument('--script', required=False, help='Путь к стартовому скрипту')

    args = parser.parse_args()
    
    shell = ShellEmulator(args.username, args.fs, args.log, args.script)
    shell.run()

if __name__ == "__main__":
    main()
