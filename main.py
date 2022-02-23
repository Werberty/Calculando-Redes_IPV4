import enum
import re


class CalculaIpv4:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.corpo_ip, self.bit_de_rede = self.remover_caracteres(ip)
        self.mascara = self.calc_mascara_sub_rede(
            self.corpo_ip, self.bit_de_rede)
        self.numero_ips = self.calc_numero_de_ips(self.mascara)
        self.rede = self.calc_ip_rede(self.corpo_ip, self.mascara)
        self.broadcast = None
        self.primeiro_ip = None
        self.ultimo_ip = None

    def teste(self):
        ip, bit_de_rede = self.remover_caracteres(self.ip)
        print('----------------------------')
        print(f'IP: {ip}, Bit rede: {bit_de_rede}')
        print(self.decimal_para_binario(ip))
        print(self.calc_mascara_sub_rede(ip, bit_de_rede))
        print(self.formatar_ip(ip))

    def calc_ip_rede(self, ip, mascara):  # terminando
        mascara, bit_mascara = self.remover_caracteres(mascara)
        mascara = self.decimal_para_binario(mascara)
        ip = self.decimal_para_binario(ip)
        bit_ip = list(ip[3])
        for k, valor in enumerate(mascara[3]):
            if valor == '0':
                bit_ip[k] = '0'
        ip[3] = ''.join(bit_ip)
        ip = self.binario_para_decimal(ip)
        ip = self.formatar_ip(ip, bit_mascara)
        return ip

    def calc_numero_de_ips(self, mascara):
        mascara, bit_rede = self.remover_caracteres(mascara)
        bits_da_mascara = self.decimal_para_binario(mascara)[3]
        b = 0
        for n in bits_da_mascara:
            if n == '0':
                b += 1
        return 2**b - 2

    def calc_mascara_sub_rede(self, ip, bit_rede):
        ip_binario = self.decimal_para_binario(ip)
        mascara = []
        cont = 0
        for binario in ip_binario:
            valor_mascara = ''
            for n in binario:
                if cont < bit_rede:
                    valor_mascara += '1'
                else:
                    valor_mascara += '0'
                cont += 1
            mascara.append(valor_mascara)
        mascara = self.formatar_ip(
            self.binario_para_decimal(mascara), bit_rede)
        return mascara

    @staticmethod
    def binario_para_decimal(ip):
        ip_decimal = []
        for binario in ip:
            binario_dec = int(binario, 2)
            ip_decimal.append(binario_dec)
        return ip_decimal

    @staticmethod
    def decimal_para_binario(ip):
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

    @staticmethod
    def formatar_ip(ip, bit_de_rede=None):
        novo_ip = '.'.join(map(str, ip))
        if bit_de_rede:
            novo_ip += f'/{bit_de_rede}'
        return novo_ip

    @staticmethod
    def remover_caracteres(ip):
        ip, bit_rede = ip.split('/')
        ip = [int(n) for n in ip.split('.')]
        return ip, int(bit_rede)


ip = '10.20.12.45/26'
calc_ip = CalculaIpv4(ip)
print(f'IP: {calc_ip.ip}')
print(f'Rede: {calc_ip.rede}')
print(f'Máscara: {calc_ip.mascara}')
print(f'N° de ips: {calc_ip.numero_ips}')
# calc_ip.teste()
