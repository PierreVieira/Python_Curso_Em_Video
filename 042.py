"""
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
- EQUILÁTERO: todos os lados iguais
"""
a, b, c = map(float, input('Informe os três lados do triângulo: ').split())
if a > b + c or b > a + c or c > a + b:
    print('Os lados informados não formam um tirângulo!')
else:
    if a == b == c:
        print('Triângulo equilátero')
    elif a != b and a != c and b != c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isóceles')
