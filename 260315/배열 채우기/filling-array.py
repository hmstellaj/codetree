list_nums = list(map(int, input().split()))

reverse_list = list_nums[::-1]

if 0 in reverse_list:
    index_zero = reverse_list.index(0) 
    reverse_list = reverse_list[index_zero + 1:]

for n in reverse_list:
    print(n, end=' ')