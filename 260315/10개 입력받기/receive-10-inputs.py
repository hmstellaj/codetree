nums_list = list(map(int, input().split()))
total_sum = 0

if 0 in nums_list:
    count = 0
    for n in nums_list:
        if n != 0:
            count += 1
            total_sum += n
        else:
            break
    total_mean = round(total_sum / count, 1)
else:
    total_sum = sum(nums_list)
    total_mean = round(total_sum / 10, 1)

print(total_sum, total_mean)

