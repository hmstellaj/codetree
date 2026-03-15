list_nums = list(map(int, input().split()))

reverse_list = list_nums[::-1]

if reverse_list[0] == 0:
    reverse_list = reverse_list[1:]

for n in reverse_list:
    print(n, end=' ')