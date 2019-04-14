# -*- coding: utf-8 -*-

def run():
    print("Calcular exponente")
    base = float(raw_input("Ingrese el número de la base: "))
    exponente = int(raw_input("Ingrese el exponente del número: "))
    resultado = elevarNumero(base, exponente)
    print('El resultado de la elevación es: {}'.format(resultado))

def elevarNumero(base, exponente):
    return base**exponente

if __name__ == "__main__":
    run()