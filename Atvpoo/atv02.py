cpf = input("Digite o CPF (com ou sem pontos e traços): ")

cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
num_digitos = len(cpf_limpo)

print(f"O CPF informado possui {num_digitos} dígitos.")
