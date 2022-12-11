# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def read_file(file: str) -> str:
    with open(file, 'r') as fin:
        return fin.read()


def write_file(file: str, text: str):
    with open(file, 'w') as fout:
        fout.write(text)


def append_file(file: str, text: str):
    with open(file, 'a') as fout:
        fout.write('\n'+text)


source_file = "source_file.txt"
write_file(source_file, input("Введите исходный текст > "))
source_text = read_file(source_file)
text = [source_text[0]]
[text.append(letter) for letter in source_text if text[-1] != letter]
pos = 0
counts = []
for i in range(len(text)):
    count = 0
    while pos < len(source_text) and text[i] == source_text[pos]:
        count += 1
        pos += 1
    counts.append(count)
target_file = "target_file.txt"
write_file(target_file, "".join(
    [str(x)+y for x, y in list(zip(counts, text))]))
zipped_text = read_file(target_file)
unzipped_text = ""
for i in range(len(zipped_text)//2):
    for j in range(int(zipped_text[2*i])):
        unzipped_text += zipped_text[2*i+1]
append_file(target_file, unzipped_text)
