"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in palavras:
    print(f"""Na palavra {palavra} temos {str(tuple(filter(lambda letra: letra.lower() if letra.lower() in "aeiou" else "", palavra))).lower().replace("(", "").replace(")", "").replace("'", "").replace(",", "")}""")