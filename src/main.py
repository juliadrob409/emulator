import os

while True:
    command = input("VFS:/> ")
    parts = command.split()
    for i in range(len(parts)):
        if parts[i].startswith("$"):
            var = parts[i][1:]
            parts[i] = os.environ.get(var, parts[i])

    if not parts:
        print("Ошибка: команда не введена")
        continue

    name = parts[0]
    arguments = parts[1:]

    if name == "exit":
        print("Выход из эмулятора")
        break

    elif name == "ls":
        print("Команда:", name)
        print("Аргументы:", arguments)

    elif name == "cd":
        print("Команда:", name)
        print("Аргументы:", arguments)

    else:
        print("Ошибка: неизвестная команда")