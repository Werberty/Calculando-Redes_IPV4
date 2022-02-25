from calculaIpv4 import CalculaIpv4

mascara = '255.254.0.0'
ip = '192.168.0.25'
calc_ip = CalculaIpv4(ip, mascara)
print(f'IP: {calc_ip.ip}')
print(f'Máscara: {calc_ip.mascara}')
print(f'Rede: {calc_ip.rede}')
print(f'Broadcast: {calc_ip.broadcast}')
print(f'Prefixo: {calc_ip.prefixo}')
print(f'N° de ips: {calc_ip.numero_ips}')
print(f'Ips Usáveis: {calc_ip.ips_usaveis}')
