import random
import datetime

# Lista de endereços IP fictícios
ips = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3", 
    "10.0.0.1", "10.0.0.2", "172.16.0.1"
]

# Lista de status HTTP
statuses = ["200", "201", "301", "302", "400", "401", "403", "404", "500", "502", "503"]

# Lista de métodos HTTP
methods = ["GET", "POST", "DELETE", "PUT"]

# Lista de URLs fictícias
urls = [
    "/index.html", "/home", "/about", 
    "/contact", "/products", "/services"
]

# Formato de log Apache
log_format = '{ip} - - [{date}] "{method} {url} HTTP/1.1" {status} {size}'

# Função para gerar uma linha de log
def generate_log_line():
    ip = random.choice(ips)
    date = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(methods)
    url = random.choice(urls)
    status = random.choice(statuses)
    size = random.randint(200, 5000)
    return log_format.format(ip=ip, date=date, method=method, url=url, status=status, size=size)

# Gerar 1000 linhas de log e escrever no arquivo
with open("apache_fake.log", "w") as file:
    for _ in range(1000):
        file.write(generate_log_line() + "\n")

print("Arquivo de log Apache gerado com sucesso: apache_fake.log")

