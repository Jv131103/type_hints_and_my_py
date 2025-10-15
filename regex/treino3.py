import re

# \w -> [a-zA-Z0-9À-ú_]
# \W -> negação de \w

# \d -> [0-9]
# \D -> negação de \d

# \s -> [ \r\n\f\v\t]
# \S -> negação de \s

# \b -> Encontra espaço vazio no inicio e no fim
# \B -> negação de \b

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida do João. Teve 5 filhos, todos adultos atualmente.
Maria, hoje a sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# FLAGS

# REMOVE DIFERENÇA DE MAIÚSCULAS E MINÚSCULAS
print(re.findall(r"[a-z]+", texto, flags=re.IGNORECASE))  # flags=re.I

# Forma de pegar até com ascentos
# print(re.findall(r"[a-zA-Z0-9À-ú]+", texto))

# BUSCA QUALQUER CARACTER, SENDO ESPECIAL OU NÃO
print(re.findall(r"\w+", texto))

# BUSCA APENAS OS ITENS DA TABELA ASCII
print(re.findall(r"\w+", texto, flags=re.ASCII))  # flags=re.A

# BUSCA QUALQUER CARACTER NUMÉRICO
print(re.findall(r"\d+", texto))

# BUSCA QUALQUER ESPAÇO
print(re.findall(r"\s+", texto))
print(re.findall(r"\S+", texto))  # O que não for espaços

# BUSCA ESPAÇOS NO COMEÇO E NO FIM se necessário
print(re.findall(r"\be\w+", texto, flags=re.I))


texto = """
131.768.460-53
055.123.060-50
955.123.060-90
"""

# BUSCA VALORES MULTILINE
# PODE TAMBÉM DIGITAR: re.M
print(re.findall(r"^\d{3}.\d{3}.\d{3}-\d{2}$", texto, flags=re.MULTILINE))

texto = "O João gosta de folia \n E adora ser amado"

# BUSCA TUDO ATÉ COM QUEBRAS DE LINHAS
print(re.findall(r"^o.*o$", texto, flags=re.I | re.S))
