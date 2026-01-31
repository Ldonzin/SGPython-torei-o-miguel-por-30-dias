nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media=(nota1+nota2+nota3)/3
if media==10 :
    situaçao = "Nota A"
    aprovado = "Parabéns, você foi aprovado com nota maxima!"
elif media < 10 and media >= 9:
    situaçao = "Nota A" 
    aprovado = "Parabéns, você foi aprovado!"
elif media <= 8.9 and media >= 8:
    situaçao = "Nota B"
    aprovado = "Parabéns, você foi aprovado!"
elif media <= 7.9 and media >= 7:
    situaçao = "Nota C"
    aprovado = "Parabéns, você foi aprovado!"
elif media <= 6.9 and media >= 6:
    situaçao = "Nota D"
    aprovado = "Parabéns, você foi aprovado!"
elif media <= 5.9 and media >= 5:
    situaçao = "Nota F"
    aprovado = "Parabéns, você foi aprovado!"
else:
    situaçao = "Nota F"
    aprovado = "Infelizmente, você foi reprovado."
print(f"Voce é um aluno {situaçao} e {aprovado} Sua média foi {media:.2f}")
