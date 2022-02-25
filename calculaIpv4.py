import re


class CalculaIpv4:
    def __init__(self, ip, mascara) -> None:
        self.ip = ip
        self.mascara = mascara
        self.prefixo = self.calc_prefixo(mascara)
        self.rede = self.calc_ip_rede(ip, mascara)
        self.broadcast = self.calc_broadcast(ip, mascara)
        self.numero_ips = self.calc_numero_de_ips(mascara)
        self.ips_usaveis = self.calc_ips_usaveis(self.rede, self.broadcast)

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @ip.setter
    def ip(self, valor):
        if not self.validar_ip(valor):
            raise ValueError('Ip inválido!')
        self._ip = valor

    @mascara.setter
    def mascara(self, valor):
        if not self.validar_ip(valor):
            raise ValueError('Máscara inválida!')
        self._mascara = valor

    @staticmethod
    def validar_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')
        if regexp.search(ip):
            return True

    def calc_ips_usaveis(self, rede, broadcast):
        rede = self.remover_caracteres(rede)
        broadcast = self.remover_caracteres(broadcast)
        rede[3] += 1
        broadcast[3] -= 1
        return f'{self.formatar_ip(rede)} - {self.formatar_ip(broadcast)}'

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
        ip = [int(n) for n in ip.split('.')]
        return ip
