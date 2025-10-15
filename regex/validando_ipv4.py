import re

cpf_reg_exp = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
ip_reg_exp = re.compile(
    r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$"
)

ips_example = [
    "0.0.0.0",
    "127.0.0.1",
    "255.255.255.255",
    "025.258.963-10",
    "192.168.1.256",
    "10.10.10.10"
]

for ip in ips_example:
    if cpf_reg_exp.search(ip):
        print(f"{ip} -> CPF")
    elif ip_reg_exp.search(ip):
        print(f"{ip} -> IP válido")
    else:
        print(f"{ip} -> Nenhum dos dois")
