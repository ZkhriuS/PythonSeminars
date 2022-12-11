# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

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
text = [read_file(source_file)[0]]
[text.append(letter) for letter in read_file(
    source_file) if text[-1] != letter]

append_file(source_file, " ".join(text))
