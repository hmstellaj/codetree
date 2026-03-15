list_num = list(map(int, input().split()))
bool_num = [int(n>=250) for n in list_num]

total_sum = 0
count = 0

if sum(bool_num) == 0:
    total_sum = sum(list_num)
    print(total_sum, round(total_sum/10, 1))
else:
    for n in list_num:
        if n < 250:
            count += 1
            total_sum += n
        else:
            break

print(total_sum, end=' ')
print(round(total_sum/count, 1))