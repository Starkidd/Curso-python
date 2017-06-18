import argparse
import datetime

mensaje = '{0} Cumplira 100 año en el {1}'


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('Nombre')
    parser.add_argument('Edad')

    args = parser.parse_args()

    now = datetime.datetime.now()
    year = now.year

    temp = (100-int(args.Edad))+year

    print(mensaje.format(args.Nombre, temp))
