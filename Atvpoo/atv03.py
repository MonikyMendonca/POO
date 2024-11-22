n = int(input("Digite o número de termos da sequência de Fibonacci: "))
fib_1 = 0
fib_2 = 1

print(fib_1)
print(fib_2)

for _ in range(2, n):
    fib_next = fib_1 + fib_2
    print(fib_next)
    fib_1, fib_2 = fib_2, fib_next