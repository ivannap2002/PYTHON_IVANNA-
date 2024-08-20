#definicion de clase
class Calculadora:
    '''Calculadora estandar
    que opera con dos numeros'''
    numero1 = None
    numero2 = None
    resultado = None

    #constructor 
    def __init__(self,x,y):
        self.numero1 = x
        self.numero2 = y
        resultado = 0

    #operaciones, metodos 
    def sumar(self):
        self.resultado = self.numero1 + self.numero2
        return self.resultado

    def restar(self):
        self.resultado = self.numero1 - self.numero2  # Corregido: se usa "-" en lugar de "+"
        return self.resultado

    def setValores(self,x,y):
        self.numero1 = x
        self.numero2 = y


if __name__ == "__main__": 

    miCasio = Calculadora(10,30) #instanciacion de Calculadora 
    print(f"la suma es: {miCasio.sumar()}")
    print(f"la resta es: {miCasio.restar()}")
   
    miCasio.setValores(50,50)
    print(f"la suma es: {miCasio.sumar()}")
    print(f"la resta es: {miCasio.restar()}")
   

    texas = Calculadora(45,69)
    print(f"la suma es: {texas.sumar()}")
    print(f"la resta es: {texas.restar()}")
