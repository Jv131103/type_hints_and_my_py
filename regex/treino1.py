import re

# findall: Busca todas as ocorrências no texto

# search: Encontra a primeira ocorrência retornando um objeto match onde vemos
# em que local foi visto

# sub: Serve para substituir algo dentro do texto

# compile: Compila expressões regulares

# Compila enquanto for chamado
string = "Este é um teste de expressões teste regulares."
print(re.search(r"teste", string))
print(re.findall(r"teste", string))
print(re.sub(r"teste", r"caso", string, count=1))

print()

# compila apenas 1 vez apenas para caso teste
regexp = re.compile(r"teste")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub(r"caso", string, count=1))
