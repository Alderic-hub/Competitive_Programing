    def convertTemperature(self, celsius):
        kelvin = float(celsius) + 273.15000
        Fahrenheit = float(celsius) * 1.80000 + 32.00
        return [kelvin,Fahrenheit ]
