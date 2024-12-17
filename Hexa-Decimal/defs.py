class HexadecimalDecimal:
    def __init__(self, valor):
        # O valor recebido será o número hexadecimal a ser convertido
        self.valor = valor.upper()  # Converte para maiúsculo para facilitar a conversão

    def deci(self):
        # valorHex é o número hexadecimal que será convertido
        valorHex = self.valor

        # Inicializa o valor decimal em 0
        decimal = 0

        print(f"Conversão de {valorHex} (hexadecimal) para decimal:")

        # Percorre cada caractere do hexadecimal, da esquerda para a direita
        for i, caractere in enumerate(reversed(valorHex)):
            # Converte o caractere hexadecimal para seu valor decimal correspondente
            valor = self.hexParaResto(caractere)

            # Calcula a contribuição desse dígito na posição atual e soma ao total
            potencia = 16 ** i
            decimal += valor * potencia

            # Exibe o cálculo no terminal
            print(f"{caractere} → {valor} × (16^{i}) = {valor * potencia}")
        
        print("Decimal final:", decimal)
        return decimal

    def hexParaResto(self, caractere):
        # Esta função converte um caractere hexadecimal (0-9 ou A-F) para seu valor decimal
        if '0' <= caractere <= '9':
            return int(caractere)  # Converte diretamente números de 0 a 9
        return ord(caractere) - 55  # Converte letras A-F para valores 10-15

    def hexa(self):
        # Esta função retorna o valor hexadecimal original
        return self.valor


class Exibir:
    def __init__(self):
        # Exibe todas as informações do código
        valorHexadecimal = input('Digite um número hexadecimal a ser convertido para decimal: ')
        self.hexadecimal = HexadecimalDecimal(valorHexadecimal)
        print("Resultado da conversão:")
        print("Decimal:", self.hexadecimal.deci())
        print("Hexadecimal:", self.hexadecimal.hexa())

