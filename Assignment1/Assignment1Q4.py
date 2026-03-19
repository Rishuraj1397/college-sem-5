n = int(input())
marks = []

for _ in range(n):
    m = int(input())
    marks.append(m)

print(marks)

total = sum(marks)
print(total)

average = total / n
print(average)

print(max(marks))
print(min(marks))

passed = len([x for x in marks if x >= 40])
failed = len([x for x in marks if x < 40])

print(passed)
print(failed)

print(marks[::-1])

even_marks = [x for x in marks if x % 2 == 0]
print(even_marks)