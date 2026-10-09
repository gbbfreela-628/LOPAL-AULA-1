# Crie um algoritimo que leia 3 valores referente (lados de um triangulo)
# Determine se formam um triangulo, e se formar verifique 
# se é um equilatero, isosceles ou escaleno

lado1 = int(input("Digite o lado1 do triangulo: "))
lado2 = int(input("Digite o lado2 do triangulo: "))
lado3 = int(input("Digite o lado3 do triangulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
   print("PARABENS,É um triangulo!!!")
   equilatero = lado1 == lado2 == lado3
   isosceles = lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2
   escaleno = lado1 != lado2 != lado3 

   if equilatero:
      print("É um triangulo equilatero!")

   if isosceles:
      print("É um triangulo isosceles!")

   if escaleno:
      print("É um triangulo escaleno!")

      
 

