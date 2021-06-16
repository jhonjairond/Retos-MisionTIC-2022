#limpio consola
import os
var=os.name
print("su sistema operativo es: ",var)
os.system("cls")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------Declaracion iniciacion de variables----------------------------------------------------------

nom=51661
con=16615
captcha1=661
captcha2=6

#opcap1=5+1+6-6 
opecap2=((6*6)-(5*5))-5 
#opecap3=5+5-5+1 

opcionSeleccionada=0

menuUno="Cambiar Contraseña"
menuDos="Ingresar coodernadas actuales"
menuTres="Ubicar zona wifi más cercana"
menuCuatro="Guardar archivo con ubicación cercana"
menuCinco="Actualizar registros de zonas wifi desde archivo"
menuSeis="Elegir opción de menú favorita"
menuSiete="Cerrar sesión"

Adivinanza1='Este era un número impar, pero un día la vuelta se dio bocabajo se quedó y en un numero par se convirtió.'
Adivinanza2='Un agricultor tiene tres montones de paja en el pajar y cuatro en el prado. Si los junta ¿cuántos montones tiene?'

menu=[                                                                   #el menu lo muestro como lista para poder intercambiar su orden, arreglo de 14 elementos
    '1. ',menuUno,#cambiarContraseña(),
    '2. ',menuDos,#ingresarCoordenadasActuales(),
    '3. ',menuTres,#ubicarZonaWifiMasCercana(),
    '4. ',menuCuatro,#guardarArchivoConUbicacionCercana(),
    '5. ',menuCinco,#actualizarRegistrosDeZonasWifiDesdeArchivo(),
    '6. ',menuSeis,#elegirOpcionDeMenuFavorita(),
    '7. ',menuSiete#,CerrarSesion()
    ]


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Distintas funciones del menu (para futuro reto)-------------------------------------------------------

def cambiarContraseña():
    print('Usted ha elegido la opción 1')
    
def ingresarCoordenadasActuales():
    print('Usted ha elegido la opción 2')
    
def ubicarZonaWifiMasCercana():
    print('Usted ha elegido la opción 3')

def guardarArchivoConUbicacionCercana():
    print('Usted ha elegido la opción 4')
    
def actualizarRegistrosDeZonasWifiDesdeArchivo():
    print('Usted ha elegido la opción 5')

def elegirOpcionDeMenuFavorita():
    opcionSeleccionadaFavorita=int(input('Seleccione opción favorita '))
                
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
                menu[1],menu[(int(opcionSeleccionadaFavorita)*2)-1]=menu[(int(opcionSeleccionadaFavorita)*2)-1],menu[1] #intercambio poisiciones en mi arreglo de menu
                menuAcciones()                   
    
def CerrarSesion():
    print('Hasta pronto')
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------Funcion para imprimir menu--------------------------------------------------------------------------    
    
def imprimirMenu():
    for i in range(0,13,2):                     # for que imprime menu dejando fijo los numeros pares del menu que son mis numeraciones 1,2...7
        if i==0:
            print('\n'+menu[i]+menu[i+1])       #if else solo para introducir un espacio al inicio de menu
        else:
            print(menu[i]+menu[i+1])
        
#-----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------funcion log in reto 1----------------------------------------------------------------------------

def logIn():
    nombre=int(input('Por favor digite su nombre de usuario: ')) 
    if nombre!=nom:
        print("\nError\n")
        exit()
    else:
        contrasena=int(input('Por favor digite su contraseña: ')) 
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
#------------------------------------------funcion que verifica numero en rango del menu--------------------------------------------------------

def pedirNumeroEntero():
    correcto=False
    n=3
    #while n>0:
    while correcto==False:
            opcionSeleccionada=int(input('\nElija una opción '))   
            if opcionSeleccionada<1 or opcionSeleccionada>7 :
                print('Error') 
                n=n-1   
                if n==0:
                    exit()
            else:    
                correcto=True                
        
    return opcionSeleccionada

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Funcion que llama funciones de menu-------------------------------------------------------------

def menuAcciones():
    imprimirMenu()
    volverMenu=True
    while volverMenu==True:
        #opcionSeleccionada=int(input('\nElija una opción '))
        opcionSeleccionada=pedirNumeroEntero()
        if opcionSeleccionada==1:
            cambiarContraseña()
            volverMenu=False
        elif opcionSeleccionada==2:
            ingresarCoordenadasActuales()
            #menuAcciones()                                           #agregar esta linea si quiero que una vez terminada la accion del menu vuelva a menu principal
            volverMenu=False                                            #este false me saca del menu y termina programa
        elif opcionSeleccionada==3:                                     
            ubicarZonaWifiMasCercana()
            volverMenu=False
        elif opcionSeleccionada==4:
            guardarArchivoConUbicacionCercana()
            volverMenu=False
        elif opcionSeleccionada==5:
            actualizarRegistrosDeZonasWifiDesdeArchivo()
            volverMenu=False
        elif opcionSeleccionada==6:
            elegirOpcionDeMenuFavorita()
            volverMenu=False
        elif opcionSeleccionada==7:
            CerrarSesion()
            volverMenu=False
        elif type(opcionSeleccionada)==str:
            for j in range(0,2):
                menuAcciones()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Hilo principal que llama las distintas funciones------------------------------------------------------

print("Bienvenido al sistema de ubicación para zonas públicas WIFI\n")# imprimo mensaje de bienvenida
logIn()
menuAcciones()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

