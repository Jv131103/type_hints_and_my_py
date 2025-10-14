# Metacaracteres: . ^ $ * + ? { } [ ] \ | ( )

import re

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

# | (OU)
print(re.findall(r"João|Maria|adultos", texto))

# . (qualquer caractere, exceto \n)
print(re.findall(r"ad..tos", texto))  # 'adultos'

# [] (classe/conjunto de caracteres)
print(re.findall(r"[Jj]oão|[Mm]aria", texto))
print(re.findall(r"[a-zA-Z0-9]aria", texto))

# [^...] (negação dentro da classe)
print(re.findall(r"[^a-zA-Z]café", texto))  # pega ' café' (espaço antes de 'café')

# flags (por enquanto vamos focar em IGNORECASE)
print(re.findall(r"[Jj]oãO|[Mm]ariA", texto, flags=re.IGNORECASE))

# ^ e $ (âncoras de início/fim de linha)
print(re.findall(r"^Maria.*$", texto, flags=re.M))  # linhas que começam com 'Maria'
print(re.findall(r"^João.*$", texto, flags=re.M))   # linhas que começam com 'João'

# \b e \B (fronteira de palavra / não-fronteira)
print(re.findall(r"\bMaria\b", texto))  # 'Maria' isolado como palavra
print(re.findall(r"\Bão", texto))       # 'ão' que NÃO começa em fronteira (ex: 'João' não pega o início do 'ão')

# * + ?  (quantificadores)
# *  -> 0 ou mais   |  + -> 1 ou mais   |  ? -> 0 ou 1 (opcional)
print(re.findall(r"J[o]+ão", texto))      # 'João' e 'Joooo...ão' (um ou mais 'o')
print(re.findall(r"Jo*ão", texto))        # zero ou mais 'o' entre J e ão (pega 'João' e 'Jooooooooão')
print(re.findall(r"Ve+mmm", texto))       # 'Veeemm' (um ou mais 'e')

# Quantificadores com chaves {n}, {n,}, {n,m}
print(re.findall(r"J[o]{2}ão", texto))    # exatamente 2 'o'
print(re.findall(r"J[o]{2,}ão", texto))   # 2 ou mais 'o'
print(re.findall(r"J[o]{2,5}ão", texto))  # de 2 a 5 'o'

# Ganância (greedy) x não-ganância (lazy) com ? após o quantificador
aspas_duplas_greedy = re.findall(r'"(.+)"', texto)   # pode pegar "demais"
aspas_duplas_lazy   = re.findall(r'"(.+?)"', texto)  # pega só até a próxima aspas
print(aspas_duplas_greedy)
print(aspas_duplas_lazy)

# Grupos de captura () e não-captura (?: )
m = re.search(r"(João).+?(Maria)", texto, flags=re.S)  # DOTALL pra . casar \n
if m:
    print("capturas:", m.groups())  # ('João', 'Maria')

# Backreference (\1, \2, …) — repetir o que um grupo capturou
# Ex: encontrar palavras duplicadas em sequência (tipo 'de de', 'que que')
# retrovisores:
# ()  \1
# () ()  \2
# (()) ()  \1  \2 \3
dup = re.findall(r"\b(\w+)\s+\1\b", "eu eu gosto de de café")
print(dup)  # ['eu', 'de']

cpf = "147.852.963-12"
print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf))

# Lookarounds (assegurar contexto sem consumir)
# (?=...)  lookahead positivo  |  (?!...)  lookahead negativo
# (?<=...) lookbehind positivo |  (?<!...) lookbehind negativo
print(re.findall(r"\b\w+(?=,)", "Droga, errei aqui,"))       # palavras seguidas de vírgula
print(re.findall(r"(?<=\s)\w+\b", " café pronto"))           # palavra precedida de espaço
print(re.findall(r"\b(?!Maria\b)\w+\b", "Maria João Maria"))  # palavras que NÃO são 'Maria'

# Escape \ para literais especiais
print(re.findall(r"\.", "final."))      # ponto literal
print(re.findall(r"\d{4}\.", "1970."))  # '1970.' (número + ponto)

# re.sub — substituições com regex
print(re.sub(r"\d", "#", "CPF 123.456.789-00"))        # troca dígitos por '#'
print(re.sub(r"\s+", " ", "um   dois\ttrês\nquatro"))  # normaliza espaços

# re.split — quebra por padrão
print(re.split(r"[,\s]+", "um,  dois   três"))        # ['um','dois','três']

# compilar padrão (performance quando reutiliza muito)
padrao_email = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", flags=re.I)
print(padrao_email.findall("meu email é a.b-c@exemplo.com e outro X@Y.org"))
