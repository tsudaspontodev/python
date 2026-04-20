print("ASSISTENTE DE APROVAÇÃO")

nome = str(input("Informe o nome do aluno(a): "))
n1 = float(input("Infome a primeira nota do aluno(a): "))
n2 = float(input("Informe a segunda nota do aluno(a): "))
f = int(input("Informe a frequencia do aluno: "))

media = (n1 + n2)/2

if (media >= 7.0 and f >= 75):
    print(f"Aluno(a) {nome} foi APROVÁDO com a média {media:.2f}")
elif(5.0 <= media < 7.0 and f >= 75 ):
    print(f"O aluno(a) {nome} está de recuperação pois a média foi de {media:.2f} mas a frequencia foi de {f}")
else:
    print(f"O aluno(a) {nome} foi REPROVADO pois a média foi menor de 7 e a frequencia foi menos de 75%")

print(f"A média do aluno(a) {nome} foi de {media:.2f}")