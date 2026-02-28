idade=int(input("Informe Sua idade "))
ingresso = input("tem Ingresso? ")
AutorizaçãoDosPais = input("Autorização dos Pais? ")
ListaVip = input("Está na Lista Vip? ")
if idade <12:
    print("Entrada Proibida")
elif idade >= 18 and (ingresso == "sim" or ListaVip == "sim"):
    print("Entrada Liberada")
elif idade < 18 and (ingresso == "sim" or ListaVip == "sim") and AutorizaçãoDosPais == "sim":
    print("Entrada Liberada")
else:
    print("Entrada Proibida")
    
