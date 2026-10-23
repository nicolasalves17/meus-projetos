#programa simples que pede ao usuário para digitar uma senha (int), e usando estruturas de repetição exibe a mensagem dw erro enquanto a senha estiver errada.
nome = input("Digite seu nome: ")
senha = 1234
senha2 = int(input(f"Digite sua senha {nome}:  "))
while senha2 != senha:
	print("senha incorreta")
	senha2 = input("Digite a senha novamente:  ")
print(f"Acesso concedido. Bem vindo ao sistema, {nome}.")
