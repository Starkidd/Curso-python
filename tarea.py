import argparse
import datetime

now=datetime.datetime.now()
year=now.year
mensaje='{0} Cumplira 100 año en el {1}'
#temp=''

if __name__ == '__main__':
	

	parser=argparse.ArgumentParser()
	parser.add_argument('Nombre')
	parser.add_argument('Edad')

	args=parser.parse_args()

	temp=(100-int(args.Edad))+year

	print(mensaje.format(args.Nombre,temp))


