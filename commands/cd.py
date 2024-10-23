def cd(fs, shell, args):
    if not args:
        print("Укажите путь.")
        return

    new_dir = args[0]

    # Handle ".." to move up one directory
    if new_dir == "..":
        parent_dir = "/".join(shell.current_dir.strip("/").split("/")[:-1])
        new_dir = f"/{parent_dir}" if parent_dir else "/"

    # Handle relative paths starting with "../"
    elif new_dir.startswith("../"):
        levels_up = new_dir.count("..")
        current_parts = shell.current_dir.strip("/").split("/")
        new_parts = current_parts[:-levels_up] 
        new_dir = "/" + "/".join(new_parts) if new_parts else "/"

    # Handle relative paths
    elif not new_dir.startswith("/"):
        new_dir = f"{shell.current_dir}/{new_dir}".replace("//", "/")

    # Attempt to change the directory
    return fs.change_dir(shell.current_dir, new_dir)  # Return new directory directly
