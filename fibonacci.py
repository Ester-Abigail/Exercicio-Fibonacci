inicial = input ("Digite um numero inicial: ")
final = input ("Digite um numero final: ")
contador = input ("Digite um contador: ")

inicialInteiro = int(inicial)
finalInteiro = int(final)
contadorInteiro = int(contador)

for contador in range(inicialInteiro, finalInteiro, contadorInteiro):
  print(contador) 