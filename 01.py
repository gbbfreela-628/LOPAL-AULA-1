aluno = input("Digite o nome do aluno: ")
ano_nascimento = int(input("digite o ano de nascimento: "))
nota1 = float(input("digite a nota1 do aluno: "))
nota2 = float(input("Digite a nota2 do aluno: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media >=5:
    situacao = "Recuperacao"
else:
    situacao = "Reprovado"

ano_atual = 2026
idade = (ano_atual - ano_nascimento)

print(f"Aluno: {aluno}")
print(f"idade: {idade}")
print(f"media: {media}")
print(f"Situacao:{situacao}")