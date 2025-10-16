import re

cpfs = """
698.547.520-54
060.235.190-16
683.134.960-96
899.344.730-62
103.778.870-21
721.478.580-30
366.310.090-14
794.289.350-26
190.259.410-01
000.000.000-01
900.000.000-00

000.000.000-00
111.111.111-11
222.222.222-22
333.333.333-33
444.444.444-44
555.555.555-55
666.666.666-66
777.777.777-77
888.888.888-88
999.999.999-99
"""

cpf_compiler = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)
matches = cpf_compiler.finditer(cpfs)

for matchNum, match in enumerate(matches, start=1):
    print(
        f"Match {matchNum} foi encontrado em {match.start()} - {match.end()}"
        f": {match.group()}"
    )

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print(
            f"Grupo {groupNum} foi encontrado em {match.start(groupNum)}"
            f"-{match.end(groupNum)}: {match.group(groupNum)}"
        )
