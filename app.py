import math

class Imc:
    # Declarando as variaveis condicionais
    magreza = 18.5
    normal = 24.9
    sobrepeso = 29.9
    obesidade = 39.9 

    # Função Construtora 
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
          

    # Funções
    def calculoIMC(self):
        self.resultado = self.peso / (self.altura/100)**2
    

    def verificaEstadoERetornaNoTerminal(self):
        if(self.resultado < self.magreza):
            print('MAGREZA')
            print(self.resultado)
        elif(self.resultado >= self.magreza and self.resultado <= self.normal):
            print('NORMAL')
            print(self.resultado)
        elif(self.resultado >= self.normal and self.resultado <= self.sobrepeso):
            print('SOBREPESO')
            print(self.resultado)
        elif(self.resultado >= self.sobrepeso and self.resultado <= self.obesidade):
            print('OBESIDADE')
            print(self.resultado)
        else:
            print('OBESIDADE GRAVE')
            print(self.resultado)


# Criando Objeto
dadosUsuario = Imc(
    float(input('Informe seu peso em kg: ')),
    float(input('Informe sua altura em cm: '))
)

# Chamando Funções
Imc.calculoIMC(dadosUsuario)
Imc.verificaEstadoERetornaNoTerminal(dadosUsuario)
