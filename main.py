
class CalculaIpv4:
    def __init__(self, ip, mascara) -> None:
        self.ip = ip
        self.mascara = mascara
        self.prefixo = self.calc_prefixo(mascara)
        self.rede = self.calc_ip_rede(ip, mascara)
        self.broadcast = self.calc_broadcast(ip, mascara)
        self.numero_ips = self.calc_numero_de_ips(mascara)

    def calc_numero_de_ips(self, mascara):
        bits_da_mascara = self.decimal_para_binario(mascara)[3]
        b = 0
        for n in bits_da_mascara:
            if n == '0':
                b += 1
        return 2**b - 2

    def calc_broadcast(self, ip, mascara):
        ip = self.decimal_para_binario(ip)
        mascara = self.decimal_para_binario(mascara)
        for byte in range(4):
            byte_mascara = list(mascara[byte])
            byte_ip = list(ip[byte])
            for bit in range(8):
                if byte_mascara[bit] == '0':
                    byte_ip[bit] = '1'
            ip[byte] = ''.join(byte_ip)
        ip = self.binario_para_decimal(ip)
        return self.formatar_ip(ip)

    def calc_ip_rede(self, ip, mascara):
        ip = self.decimal_para_binario(ip)
        mascara = self.decimal_para_binario(mascara)
        for byte in range(4):
            byte_mascara = list(mascara[byte])
            byte_ip = list(ip[byte])
            for bit in range(8):
                if byte_mascara[bit] == '0':
                    byte_ip[bit] = '0'
            ip[byte] = ''.join(byte_ip)
        ip = self.binario_para_decimal(ip)
        return self.formatar_ip(ip)

    def calc_prefixo(self, mascara):
        mascara = self.decimal_para_binario(mascara)
        prefixo = 0
        for valor in mascara:
            for n in list(valor):
                if n == '1':
                    prefixo += 1
        return prefixo

    def binario_para_decimal(self, ip):
        if not isinstance(ip, list):
            ip = self.remover_caracteres(ip)
        ip_decimal = []
        for binario in ip:
            binario_dec = int(binario, 2)
            ip_decimal.append(binario_dec)
        return ip_decimal

    def decimal_para_binario(self, ip):
        if not isinstance(ip, list):
            ip = self.remover_caracteres(ip)
        ip_binario = []
        for decimal in ip:
            dec_binario = format(decimal, 'b')
            dec_binario = dec_binario.zfill(8)
            ip_binario.append(dec_binario)
        return ip_binario

    @staticmethod
    def formatar_ip(ip):
        return '.'.join(map(str, ip))

    @staticmethod
    def remover_caracteres(ip):
        # ip, bit_rede = ip.split('/')
        ip = [int(n) for n in ip.split('.')]
        return ip


# ip = '10.20.12.45'
mascara = '255.255.255.192'
ip = '192.168.0.25'
calc_ip = CalculaIpv4(ip, mascara)
print(f'IP: {calc_ip.ip}')
print(f'Máscara: {calc_ip.mascara}')
print(f'Rede: {calc_ip.rede}')
print(f'Broadcast: {calc_ip.broadcast}')
print(f'Prefixo: {calc_ip.prefixo}')
print(f'N° de ips: {calc_ip.numero_ips}')
