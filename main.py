import re
from unicodedata import decimal

class CalculaIpv4:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.nucle_ip, self.bit_de_rede = self.remover_caracteres(ip)
        self.mascara = self.mascara_sub_rede(self.nucle_ip, self.bit_de_rede)

    def teste(self):
        ip, bit_de_rede = self.remover_caracteres(self.ip)
        print(f'IP: {ip}, Bit rede: {bit_de_rede}')
        print(self.decimal_para_binario(ip))
        print(self.mascara_sub_rede(ip, bit_de_rede))
        print(self.formatar_ip(ip))
    
    def mascara_sub_rede(self, ip, bit_de_rede):
        ip_binario = self.decimal_para_binario(ip)
        mascara = []
        cont = 0
        for binario in ip_binario:
            valor_mascara = ''
            for n in binario:
                if cont < bit_de_rede:
                    valor_mascara += '1'
                else:
                    valor_mascara += '0'
                cont += 1
            mascara.append(valor_mascara)
        mascara = self.binario_para_decimal(mascara)
        return mascara

    def binario_para_decimal(self, ip):
        ip_decimal = []
        for binario in ip:
            binario_dec = int(binario, 2)
            ip_decimal.append(binario_dec)
        return ip_decimal

    def decimal_para_binario(self, ip):
        ip_binario = []
        for decimal in ip:
            dec_binario = format(decimal, 'b')
            dec_binario = dec_binario[::-1]
            if len(dec_binario) < 8:
                zeros = 8 - len(dec_binario)
                dec_binario += '0'*zeros
            dec_binario = dec_binario[::-1]
            ip_binario.append(dec_binario)
        return ip_binario
    
    def formatar_ip(self, ip, bit_de_rede=None):
        novo_ip = '.'.join(map(str, ip))
        if bit_de_rede:
            novo_ip += f'/{bit_de_rede}'
        return novo_ip

    def remover_caracteres(self, ip):
        ip, bit_rede = ip.split('/')
        ip = [int(n) for n in ip.split('.')]
        return ip, int(bit_rede)

ip = '10.20.12.45/26'
calc_ip = CalculaIpv4(ip)
print(calc_ip.bit_de_rede)
print(calc_ip.mascara)
calc_ip.teste()
