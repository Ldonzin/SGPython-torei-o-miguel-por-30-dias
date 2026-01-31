nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media=(nota1+nota2+nota3)/3
if media == 10:
    situaçao = "Nota Perfeita"
elif media >= 5:
    situaçao = "Aprovado"
else:
    situaçao = "Reprovado"

print(f"A média é {media} e a situação é {situaçao}")
