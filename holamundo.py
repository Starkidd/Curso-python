import argparse

#interpolacion
#otra_cadena = 'hola{}'.format('un valor')
variable_cuatro = 'hola{0} {1}'
var = 'hola{variable1} {variable2}'

def mifunt(val):
    print(variable_cuatro)
    print(var)



if __name__ == '__main__':	
  paser = argparse.ArgumentParse()
  parser.add_argument('nombre')
  parser.add_argument('apellido')
  args = parser.parse_args()

  print(args.nombre)
  print(args.apellido)
  pint(variable_cuatro.format(args.nombre, args.apellido))
