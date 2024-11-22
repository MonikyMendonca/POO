cpf = input("Digite seu cpf: ")

if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido!")
else:

    soma1 = 0
    for i in range(9): 
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1 % 11
    dv1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = 0
    for i in range(10): 
        soma2 += int(cpf[i]) * (11 - i)
    resto2 = soma2 % 11
    dv2 = 0 if resto2 < 2 else 11 - resto2
    
    if dv1 == int(cpf[9]) and dv2 == int(cpf[10]):
        print("CPF válido!")
    else:
        print("CPF inválido!")