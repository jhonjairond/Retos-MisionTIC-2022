#limpio consola
import os
#var=os.name
#print("su sistema operativo es: ",var)
os.system("cls")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------Declaracion iniciacion de variables----------------------------------------------------------

nom='51661'
con='16615'

captcha1=661
captcha2=6

#opcap1=5+1+6-6 
opecap2=((6*6)-(5*5))-5 
#opecap3=5+5-5+1 

opcionSeleccionada=0

Adivinanza1='Este era un número impar, pero un día la vuelta se dio bocabajo se quedó y en un numero par se convirtió.'
Adivinanza2='Un agricultor tiene tres montones de paja en el pajar y cuatro en el prado. Si los junta ¿cuántos montones tiene?'

menu=[                                                                   #el menu lo muestro como lista para poder intercambiar su orden
    '1. Cambiar Contraseña',
    '2. Ingresar coodernadas actuales',
    '3. Ubicar zona wifi más cercana',
    '4. Guardar archivo con ubicación cercana',
    '5. Actualizar registros de zonas wifi desde archivo',
    '6. Elegir opción de menú favorita',
    '7. Cerrar sesión'
    ]

#-----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------funcion log in reto 1----------------------------------------------------------------------------

def logIn():
    nombre=input('Por favor digite su nombre de usuario: ')
    if nombre!=nom:
        print("\nError\n")
        exit()
    else:
        contrasena=input('Por favor digite su contraseña: ')
        if contrasena!=con: 
            print("\nError\n")
            exit()
        else:
            captchausuario=int(input('Ingrese el resultado de la suma '+str(captcha1)+' + '+str(opecap2)+' :')) 
            if captchausuario!=captcha1+captcha2:
                print("\nError\n")
                exit()
            else:
                print('\nSesión iniciada')

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Distintas funciones del menu (para futuro reto)-------------------------------------------------------

def cambiarContraseña():
    print('Usted ha elegido la opción 1')
    #n=3
    global con
    while True:
        conConfirmacion=input("ingrese la contraseña actual: ")
        if conConfirmacion!=con:
            print('Error')
            exit()                        
        else:
            conNueva=input("ingrese la contraseña nueva: ")
            if conNueva==con:
                print('Error')
                exit()
                #n-=1
                #if n==0:
            else:    
                #print('Contraseña cambiada Correctamente')
                con=conNueva
        return
         
#................................................................................................................................................        

#       6   Tadó, Chocó             Sup: 5.413  Inf:5.119            Or:-76.132  Occ:-76.619

#       1   -Coordenada ubicada más al norte
#           -Coordenada ubicada más al oriente

import numpy as np

f=3
c=2
sup=5.413
inf=5.119                                                               #variables a usar en este menu
ori=-76.132
occ=-76.619

matrizCoordenadas=[]

def matrizCeros():
    global matrizCoordenadas
    matrizCoordenadas=[]
    for i in range (f):                                                 #funcion que crea y hace reset a matriz de coordenadas, llenandola con ceros
        matrizCoordenadas.append([0]*c)
    return matrizCoordenadas    
    
matrizCeros()        

def ingresarCoordenadasActuales():
    print('Usted ha elegido la opción 2')
    global matrizCoordenadas                                      
    #print(matrizCoordenadas)   
    
    def ingresarCoordenadas(a,b):
            j=0
            try:
                for i in range(a,b):        
                    la=float(input('ingrese latitud de coordenada '+str(i+1)+': '))
                    if la>sup or la<inf:
                        print('Error coordenada')
                        exit()
                    else:                                                                                     #funcion que pide y verifica datos de ingreso para coordenadas, llena matriz
                        matrizCoordenadas[i][j]=la
                        lo=float(input('ingrese longitud de coordenada '+str(i+1)+': '))
                        if lo>ori or lo<occ:
                            print('Error coordenada')
                            exit()
                        else:
                            matrizCoordenadas[i][j+1]=lo
                            #print(matrizCoordenadas)                           
            except ValueError:
                print('Error')
                matrizCeros()
                #print(matrizCoordenadas)      
    
    if matrizCoordenadas[0][0]==0:                                                                          #este if me verifica que la matriz esta sin datos o es la primera vez que se llena        
        ingresarCoordenadas(0,3)                        
    else:                                                                                                   #si la matriz ya contiene coordenadas, doy la opcion de modificar con este else
        #print('escoger cambio disponible')
        for i in range(f):
            print('coordenada [latitud,longitud] ',i+1,' :',matrizCoordenadas[i])                 #imprimo coordenadas en memoria
            
        m=np.array(matrizCoordenadas)     
                     
        latitudes=np.amax(m, axis=1)        #me extrae las latitudes maximas por fila
        #maximoLatitudes=np.max(latitudes)   #me extrae el valor maximo de las latitudes     
        indiceLatitudMaxima=np.argmax(latitudes)  #me saca el indice de la latitud maxima de entre el vector latitudes maximas
        #print(m)
        #print(latitudes)
        #print(maximoLatitudes)
        #print(indiceLatitudMaxima)
        print('La coordenada ',indiceLatitudMaxima+1,' es la que está más al norte')
        
        longitudes=np.amin(m, axis=1)        #me extrae las longitudes minimas por fila
        #maximoLongitudes=np.max(longitudes)   #me extrae el valor maximo de las longitudes    
        indiceLongitudMaxima=np.argmax(longitudes)  #me saca el indice de la longitud maxima de entre el vector longitudes maximas
        #print(m)
        #print(longitudes)
        #print(maximoLongitudes)
        #print(indiceLongitudMaxima)        
        print('La coordenada ',indiceLongitudMaxima+1,' es la que está más al oriente')
        
        seleccionada=pedirNumeroEntero(1,'Presione 1,2 ó 3 para actualizar la respectiva coordenada\nPresione 0 para regresar al menú ',0,3,'Error actualización')      #pedirNumeroEntero(n,mensajePeticion,a,b,mensajeError): 
        
        if seleccionada==0:
            menuAcciones()
        elif seleccionada==1:            
            ingresarCoordenadas(0,1)                   
        elif seleccionada==2:               
            ingresarCoordenadas(1,2)            #ingresar la coordenada segun seleccione, usando la funcion de ingresarCoordenadas() definida al inicio de esta funcion de menu
        elif seleccionada==3:               
           ingresarCoordenadas(2,3) 

#................................................................................................................................................ 
   
def ubicarZonaWifiMasCercana():
    print('Usted ha elegido la opción 3')

#................................................................................................................................................ 

def guardarArchivoConUbicacionCercana():
    print('Usted ha elegido la opción 4')

#................................................................................................................................................ 
    
def actualizarRegistrosDeZonasWifiDesdeArchivo():
    print('Usted ha elegido la opción 5')

#................................................................................................................................................ 

def elegirOpcionDeMenuFavorita():
    opcionSeleccionadaFavorita=pedirNumeroEntero(1,'Seleccione opción favorita ',0,7,'Error')           
    if opcionSeleccionadaFavorita>=6 or opcionSeleccionadaFavorita<1:
        print('Error')
        exit()
    
    else:
        respuestaAdivinanza1=input('Para confirmar por favor responda: '+Adivinanza1+' ')
                    
        if respuestaAdivinanza1!='6':
            print('Error')
            os.system("cls")
            menuAcciones()
        else:
            respuestaAdivinanza2=input('Para confirmar por favor responda: '+Adivinanza2+' ')
                        
            if respuestaAdivinanza2!='1':
                print('Error')
                os.system("cls")
                menuAcciones()
            else:
                menu[0],menu[int(opcionSeleccionadaFavorita)-1]=menu[int(opcionSeleccionadaFavorita)-1],menu[0] #intercambio poisiciones en mi arreglo de menu
                menuAcciones()                   

#................................................................................................................................................     

def CerrarSesion():
    print('Hasta pronto')
    exit()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------Funcion para imprimir menu--------------------------------------------------------------------------    
    
def imprimirMenu():
    for i in range(0,7):                     # for que imprime menu dejando fijo los numeros pares del menu que son mis numeraciones 1,2...7
        if i==0:
            print('\n'+menu[i])       #if else solo para introducir un espacio al inicio de menu
        else:
            print(menu[i])
        
#-----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------funcion que verifica numero es entero y esta en rango del menu---------------------------------------

def pedirNumeroEntero(n,mensajePeticion,a,b,mensajeError):                   #n es mi argumento de funcion y es el numero de peticiones antes de salir del sistema, mensaje el argumento para mostrar en pantalla y mensaje de error                                                          
    while True:
       entrada=input(mensajePeticion)                                            #se puede mejorar colocando mensaje de salida por fuera del rango o salida por no ingresar numero entero
       try:
           entrada=int(entrada)
           if entrada<a or entrada>b:
                print (mensajeError)   
                n-=1
                if n==0:
                    exit()
           else:
               return entrada
       except ValueError:
           n-=1
           print (mensajeError)  
           if n==0:      
              exit()
            
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Funcion que llama funciones de menu-------------------------------------------------------------

def menuAcciones():
    imprimirMenu()
    volverMenu=True
    while volverMenu==True:
        opcionSeleccionada=pedirNumeroEntero(3,'\nElija una opción ',1,7,'Error')              #ingreso  3 como argumento de mi funcion pedir numero entero, n=3 es el numero de equivocaciones, el argumento para el mensaje elija una opcion e intervalo entre el que debe escoger
        
        if opcionSeleccionada==1:
            cambiarContraseña()
            menuAcciones()
            
        elif opcionSeleccionada==2:
            ingresarCoordenadasActuales()
            menuAcciones()                                           #agregar esta linea si quiero que una vez terminada la accion del menu vuelva a menu principal
                                                     
        elif opcionSeleccionada==3:                                     
            ubicarZonaWifiMasCercana()
            menuAcciones() 
            
        elif opcionSeleccionada==4:
            guardarArchivoConUbicacionCercana()
            menuAcciones() 
            
        elif opcionSeleccionada==5:
            actualizarRegistrosDeZonasWifiDesdeArchivo()
            menuAcciones() 
            
        elif opcionSeleccionada==6:
            elegirOpcionDeMenuFavorita()
            menuAcciones() 
            
        elif opcionSeleccionada==7:
            CerrarSesion()
            
       
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Hilo principal que llama las distintas funciones------------------------------------------------------

print("Bienvenido al sistema de ubicación para zonas públicas WIFI\n")# imprimo mensaje de bienvenida
logIn()
menuAcciones()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------Opciones a mejorar---------------------------------------------------------------------------

#implementar la funcion que pide datos con la comprobacion de entero en rango y numero con entrada de numero de repeticiones y mensaje
#verificar si la idea es que el menu siemnpre salga ordenado de 1 a 7
#implementar un while de el numero de veces permitidas para intentar loguearse
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
