class ConverterTemperatura:
    #Valida as tempertaturas pois a temperatura não pode ser abaixo do zero absoluto
    def validar_temperatura(self, valor, unid):
        if unid == "C" and valor < -273.15:
            raise ValueError("A temperatura em Celsius não pode ser menor que -273,15°C.")
        if unid == "F" and valor < -459.67:
            raise ValueError("A temperatura em Fahrenheit não pode ser menor que -459,67°F.")
        if unid == "K" and valor < 0:
            raise ValueError("A temperatura em Kelvin não pode ser menor que 0K.")

    def celsius_para_fahrenheit(self, celsius):
        self.validar_temperatura(celsius, "C")
        return (celsius * 9/5) + 32
    
    def celsius_para_kelvin(self, celsius):
        self.validar_temperatura(celsius, "C")
        return celsius + 273.15
    
    def fahrenheit_para_celsius(self, fahrenheit):
        self.validar_temperatura(fahrenheit, "F")
        return (fahrenheit - 32) * 5/9  

    def fahrenheit_para_kelvin(self, fahrenheit):
        self.validar_temperatura(fahrenheit, "F")
        return (fahrenheit - 32) * 5/9 + 273.15
    
    def kelvin_para_celsius(self, kelvin):
        self.validar_temperatura(kelvin, "K")
        return kelvin - 273.15
    
    def kelvin_para_fahrenheit(self, kelvin):
        self.validar_temperatura(kelvin, "K")
        return (kelvin - 273.15) * 9/5 + 32
