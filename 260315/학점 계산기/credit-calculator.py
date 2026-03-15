N = int(input())
scores = list(map(float, input().split()))

avg_score = sum(scores) / N
print(round(avg_score, 1))

if avg_score >= 4.0:
    print("Perfect")
elif avg_score >= 3.0:
    print("Good")
else:
    print("Poor")