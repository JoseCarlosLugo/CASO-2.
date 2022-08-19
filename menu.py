from login import login_correct
from login import login_fail
from funciones import mejoresRutas
from funciones import transporte
from funciones import valor


#Se Crea una variable a la cual se le da el valor (true/false) sengun la funcion de login
login_true = login_correct()

#Si el login es incorecto se crea un blucle y se llama la funcion para crear un nuevo usuario
if login_true == False:
  while login_true == False:
    login_true = login_fail()
    
#si el login es correcto se despliega el menu
if login_true == True:

#Se crea un bucle para repetir el menu segun el usuario lo quiera
  while True:
    print("\n")
    print("Que quiere hacer? \n")
  
    print("Ver las rutas mas usadas                           (1)",
        "\nVer los ingresos segun el medio de transporte      (2)",
        "\nVer los ingresos totales                           (3)")

#se crea un try para evitar errores
    try:
      do_main = int(input("Salir                                              (4)\n:"))
      print("\n")
    except:
      print("ERROR")
      print("\n")
      do_main = 0
#Se llama la funcion para mostrar los mejores o peores productos    
    if do_main == 1:
      mejoresRutas()
#Se llama la funcion mostrar los productos con mas  reseñados       
    elif do_main == 2:
      transporte()
# se llama la funcion para ver los ingresos      
    elif do_main == 3:
      valor()
#Se cierra el programa      
    elif  do_main == 4:
      print("Cerrando sesión")
      break

    do_main = 0