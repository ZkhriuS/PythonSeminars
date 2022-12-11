# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def read_file(file: str) -> str:
    with open(file, 'r') as fin:
        return fin.read()


def write_file(file: str, message: str):
    with open(file, 'w') as fout:
        fout.write(input(message))


def append_file(file: str, text: str):
    with open(file, 'a') as fout:
        fout.write('\n'+text)


source_file = "source_file.txt"
write_file(source_file, "Введите исходный текст > ")
text = list(filter(lambda word: not "абв" in word,
            read_file(source_file).split()))
append_file(source_file, " ".join(text))
