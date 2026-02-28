idade = int(input("Informe Sua idade "))
Experiencia = input("Tem Experiência na area? ")
Crimes = input("Tem antecedentes criminais? ")
EnsinoSuperior = input("Tem Ensino Superior? ")
Indicacao = input("Tem Indicação de alguem da empresa? ")
if idade >= 18 and Experiencia == "sim" and Crimes == "não":
    print ("Meus parabéns,voce é um CLT")
elif idade >=18 and Experiencia == "não" and (EnsinoSuperior == "sim" or Indicacao == "sim") and Crimes == "não":
    print ("Marcamos Uma entrevista de emprego para voce no dia XX as XX horas")
