# -*- coding: utf-8 -*-

# Si el archivo existe, se sobrescribe. Si no existe se crea uno
def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))
        # Con el 'with' (Context manager) no es necesario cerrar el archivo

if __name__ == '__main__':
    run()