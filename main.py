from posixpath import split
import re

class CalculaIpv4:
    def __init__(self, ip, mascara=None) -> None:
        self.ip = ip
        self.mascara = mascara

    def teste(self):
        ip, bit_de_rede = self.remover_caracteres(self.ip)
        print(f'IP: {ip}, Bit rede: {bit_de_rede}')
        self.decimal_para_binario(ip)

    def decimal_para_binario(self, ip):
        ip_binario = []
        for decimal in ip:
            dec_binario = ''
            while True:
                if decimal % 2:
                    dec_binario += '1'
                else:
                    dec_binario += '0'
                decimal = decimal // 2
                if decimal <= 0:
                    break
            if len(dec_binario) < 8:
                zeros = 8 - len(dec_binario)
                dec_binario += '0'*zeros
            dec_binario = dec_binario[::-1]
            ip_binario.append(dec_binario)
        print(ip_binario)

    def remover_caracteres(self, ip):
        ip, bit_rede = ip.split('/')
        ip = [int(n) for n in ip.split('.')]
        return ip, int(bit_rede)

ip = '10.20.12.45/26'
calc_ip = CalculaIpv4(ip)
calc_ip.teste()
