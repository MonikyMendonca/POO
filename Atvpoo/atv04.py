saldo = 0 

while True:
  
    mens = float(input("Digite o valor investido por mês: "))
    taxa_do_juros = float(input("Digite a taxa de juros por mês (em %): "))

  
    for mes in range(1, 13):  
        saldo = saldo + mens  
        saldo = saldo + saldo * taxa_do_juros / 100 
    print(f"Saldo depois de 1 ano: R$ {saldo:.2f}")

    continuar = input("Deseja processar mais um ano? (S/N): ").upper()

    if continuar == 'N':
        break