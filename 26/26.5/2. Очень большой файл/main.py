def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            yield clear_line_sum

a = str(10 ** 100)
with open('numbers.txt', 'a') as txt:
    txt.write(a)

all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number
print(all_sum)