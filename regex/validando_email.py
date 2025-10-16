import re

# === suas regexes ===
regexes = {
    "Básica": re.compile(r"^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$"),
    "Básica 2": re.compile(r"^[^\s@<>\(\)\[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$"),
    "RFC 5322-ish": re.compile(
        r'^(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|'
        r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09'
        r'\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+'
        r'[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|'
        r'[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|'
        r'[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x5e-\x7f]'
        r'|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$',
        re.IGNORECASE
    ),
}

emails = r"""
Valid email addresses
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com


Invalid email addresses
Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""

# === separa válidos/invalidos ===
validos, invalidos = [], []
target = None
for raw in emails.splitlines():
    line = raw.strip()
    if not line:
        continue
    if line.lower().startswith("valid email"):
        target = validos
        continue
    if line.lower().startswith("invalid email"):
        target = invalidos
        continue
    if target is not None:
        target.append(line)

def roda_teste(nome, rx):
    falsos_positivos = [e for e in invalidos if rx.match(e)]
    falsos_negativos = [e for e in validos if not rx.match(e)]
    print(f"\n=== {nome} ===")
    print(f"Total válidos esperados: {len(validos)} | inválidos esperados: {len(invalidos)}")
    print(f"FALSOS POSITIVOS ({len(falsos_positivos)}):")
    for e in falsos_positivos:
        print("  + ", e)
    print(f"FALSOS NEGATIVOS ({len(falsos_negativos)}):")
    for e in falsos_negativos:
        print("  - ", e)

for nome, rx in regexes.items():
    roda_teste(nome, rx)
