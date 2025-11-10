"""
This code calculates the BMI and classifies the result into three categories: 'underweight,' 'normal weight,' or 'overweight,' based on the BMI value.
Este código calcula o IMC e classifica o resultado em três categorias: 'baixo peso', 'peso normal' ou 'sobrepeso', com base no valor do IMC.
"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")

if 18.5 < bmi < 25:
    print("normal weight")

if bmi > 25:
    print("overweight")
