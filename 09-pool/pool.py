class automovil:
    ruedas = 4
    largo_chasis = 250
    ancho_chasis = 150
    en_marcha = False

    def caracteristicas(self):
        print(f"Ruedas: {self.ruedas}\nLargo chasis: {self.largo_chasis}")


print("-------------<Primer objeto creado>---------")
carro1 = automovil()
carro1.caracteristicas()
