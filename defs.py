class DecimalHexadecimal:

    
    def __init__(self, valor):
    
        self.valor = valor

    def hexa(self):

        # valor é o número decimal que será convertido
        valor = self.valor

        # restos é uma lista que armazenará os restos das divisões sucessivas por 16
        restos = []
        
        print(f"Conversão de {valor} (decimal) para hexadecimal:")

        # O número decimal é dividido por 16 repetidamente
        while valor > 0:
            
        # O resto da divisão (valor % 16) é calculado e armazenado na lista restos
            resto = valor % 16
            restos.append(resto)

        # O quociente da divisão (valor // 16) é atribuído novamente a valor, e o processo se repete até o valor ser zero
        # e exibe o processo no terminal
            print(f"{valor} ÷ 16 = {valor // 16} (quociente), resto = {resto}")
            valor //= 16
        
        # A lista restos guarda os valores das divisões, mas eles devem ser lidos de trás para frente 
        # A função reversed() inverte a lista, e cada valor é convertido para hexadecimal usando o método restoParaHexa()
        hexadecimal = ''.join(self.restoParaHexa(r) for r in reversed(restos))
        print("Hexadecimal final:", hexadecimal)

        return hexadecimal

    def restoParaHexa(self, resto):
        # Este função converte os restos (entre 0 e 15) para seus equivalentes hexadecimais
        if resto < 10:

        # Se o resto for menor que 10, ele é convertido diretamente para uma string (0-9)
        # Se não, ele é convertido em letras de A a F
            return str(resto)
        return chr(55 + resto)

    def deci(self):
        # Este função retorna o valor decimal original
        return self.valor


class Exibir:
    def __init__(self):
        
        valorDecimal = int(input('Digite um número a ser convertido para hexadecimal: '))
        self.decimal = DecimalHexadecimal(valorDecimal)

        # Exibe todas as informações do codigo
        print("Resultado da conversão:")
        print("Hexadecimal:", self.decimal.hexa())
        print("Decimal:", self.decimal.deci())
