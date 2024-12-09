"""
Cálculo das áreas de figuras geométricas:
1. Círculo
2. Triângulo
3. Retângulo
Qual figura deseja calcular a área?
"""
import math
def calcula_area_circulo():
  raio = float(input("Insira o raio do circulo: "))
  area = 3.14 * raio ** 2
  return area
def calcula_area_triagulo():
  base = float(input("Introduza a base do triângulo: "))
  altura = float(input("Introduza a altura do triângulo: "))
  area = (base * altura) / 2 
  return area
def calcula_area_retangulo():
  base = float(input("Introduza a base do retângulo: "))
  altura = float(input("Introduza a altura do retângulo: "))
  area = base * altura
  return area
opcao = int(input("Qual figura deseja calcular a área? \n1. Círculo \n2. Triângulo \n3. Retângulo \n"))
if opcao == 1:
    raio = calcula_area_circulo()
    print(f"O raio do círculo é: {raio}")
elif opcao == 2:
    area = calcula_area_triagulo()
    print(f"A área do triângulo é: {area}")
elif opcao == 3:
    area = calcula_area_retangulo()
    print(f"A área do retângulo é: {area}")
else:
    print("Opção inválida")
