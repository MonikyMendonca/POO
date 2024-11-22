num_termos = int(input("Digite o número de termos: "))

pi = 0 

for k in range(num_termos):
    termo = (-1)**k / (2*k + 1)  
    pi = pi + termo 

pi = 4 * pi

print(f"Pi{pi}:")
