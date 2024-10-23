def chown(fs, args):
    if len(args) < 2:
        print("Используйте: chown <новый_владелец> <файл>")
        return
    
    new_owner, file = args[0], args[1]
    if file[0] != "/":
        file = "/"+file
    
    fs.change_owner(file, new_owner)