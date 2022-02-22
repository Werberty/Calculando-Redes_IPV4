import re

class CalculaIpv4:
    def __init__(self, ip, mascara=None) -> None:
        self.ip = ip
        self.mascara = mascara

    def teste(self):
        ip, bit_de_rede = self.remover_caracteres(self.ip)
        print(f'IP: {ip}, Bit rede: {bit_de_rede}')
        print(self.decimal_para_binario(ip))
        print(self.binario_para_decimal(ip))

    def binario_para_decimal(self, ip):
        ip_decimal = []
        for binario in ip:
            binario_dec = format(binario, 'd')
            ip_decimal.append(int(binario_dec))
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

    def remover_caracteres(self, ip):
        ip, bit_rede = ip.split('/')
        ip = [int(n) for n in ip.split('.')]
        return ip, int(bit_rede)

ip = '10.20.12.45/26'
calc_ip = CalculaIpv4(ip)
a = format(10, 'b')
b = []
b.append(a)
print(b)
calc_ip.teste()
