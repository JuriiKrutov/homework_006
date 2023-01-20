first, diff, quan = int(input()), int(input()), int(input())
print(list(first + (i - 1) * diff for i in range(1, quan +1)))