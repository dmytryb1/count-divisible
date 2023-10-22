X = int(input('Enter a full positive number'))

for i in range(1, X + 1):
    if X % i == 0:
        print(i)
    