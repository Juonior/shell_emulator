def ls(fs, current_dir):
    try:
        files = fs.list_dir(current_dir)
        
        if not files:
            print("Директория пуста.")
            return
        
        for file in files:
            print(file)
    
    except FileNotFoundError:
        print(f"Ошибка: Директория '{current_dir}' не найдена.")
    except NotADirectoryError:
        print(f"Ошибка: '{current_dir}' не является директорией.")
    except Exception as e:
        print(f"Ошибка: {e}")
