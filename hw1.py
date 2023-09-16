from datetime import datetime

n = int(input("Enter your numbers : ")) 

def fib(n):
    fib_number = [0,1]
    if n == 0:
        return fib_number[0]
    if n == 1:
        return fib_number[1]

    for i in range (2, n+1):
            next_fib = fib_number[i - 1] + fib_number[i - 2]
            fib_number.append(next_fib)
    return fib_number[n]


startTime = datetime.now()
result = fib(n)
endTime = datetime.now()
seconds = (endTime - startTime).total_seconds()


print(f'fib({n})={result}')
print(f'time:{seconds}')
