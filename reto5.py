#importo los paquetes a utilizar
import os
import numpy as np
import math
import pandas as pd

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
    'Cambiar Contraseña',
    'Ingresar coodernadas actuales',
    'Ubicar zona wifi más cercana',
    'Guardar archivo con ubicación cercana',
    'Actualizar registros de zonas wifi desde archivo',
    'Elegir opción de menú favorita',
    'Cerrar sesión'
    ]

opcionGlobal=0  #variable utilizada para guardar q opcion del menu eligio

'''
6   Tadó, Chocó     Lat1: 5.273     Lon1: -76.579    390
                        

                    Lat2: 5.311     Lon2: -76.413    333
                        

                    Lat3: 5.354     Lon3: -76.204    240
                        

                    Lat4: 5.306     Lon4: -76.332    793                   
'''

zonasWifi=[(5.273,-76.579,390),
           (5.311,-76.413,333),
           (5.354,-76.204,240),
           (5.306,-76.332,793)]

ubicacionActual=[0,0]
zonaWifi1=[0,0,0]
distanciaActualAZonaWifi1=0
transporte="A pie"
tiempoPromedio=0

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
#-------------------------------------------Funcion para imprimir menu--------------------------------------------------------------------------    
    
def imprimirMenu():
    for i in range(0,7):                     # for que imprime menu dejando fijo los numeros pares del menu que son mis numeraciones 1,2...7
        if i==0:
            print(f'\n{i+1}. {menu[i]}')       #if else solo para introducir un espacio al inicio de menu
        else:
            print(f'{i+1}. {menu[i]}')
        
        
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
#-----------------------------------------Distintas funciones del menu (para futuro reto)-------------------------------------------------------

def cambiarContraseña():
    print('Usted ha elegido la opción ',opcionGlobal)
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
    print('Usted ha elegido la opción ',opcionGlobal)
    global matrizCoordenadas                                      
    
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
                                                    
            except ValueError:
                print('Error')
                matrizCeros()                   
    
    if matrizCoordenadas[0][0]==0:                                                                          #este if me verifica que la matriz esta sin datos o es la primera vez que se llena        
        ingresarCoordenadas(0,3)                        
    else:                                                                                                   #si la matriz ya contiene coordenadas, doy la opcion de modificar con este else
        for i in range(f):
            print('coordenada [latitud,longitud] ',i+1,' :',matrizCoordenadas[i])                 #imprimo coordenadas en memoria
            
        m=np.array(matrizCoordenadas)     
                     
        latitudes=np.amax(m, axis=1)        #me extrae las latitudes maximas por fila
        #maximoLatitudes=np.max(latitudes)   #me extrae el valor maximo de las latitudes     
        indiceLatitudMaxima=np.argmax(latitudes)  #me saca el indice de la latitud maxima de entre el vector latitudes maximas
      
        print('La coordenada ',indiceLatitudMaxima+1,' es la que está más al norte')
        
        longitudes=np.amin(m, axis=1)        #me extrae las longitudes minimas por fila
        #maximoLongitudes=np.max(longitudes)   #me extrae el valor maximo de las longitudes    
        indiceLongitudMaxima=np.argmax(longitudes)  #me saca el indice de la longitud maxima de entre el vector longitudes maximas
             
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
    print('Usted ha elegido la opción ',opcionGlobal)
    
    matrizCercania=[]
    
    global ubicacionActual
    
    if matrizCoordenadas[0][0]==0:
        print('Error sin registro de coordenadas')
        exit()
    
    else:
        for i in range(f):
            print('coordenada [latitud,longitud] ',i+1,' :',matrizCoordenadas[i])   
        seleccionada=pedirNumeroEntero(1,'Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión ',1,3,'Error ubicación')
        
        # lat1,lon1 seran de mi usuario, lat2,lon2 el punto wifi
        def distanciaUsuarioZona(lat1,lon1,lat2,lon2):
            r=6372.795477598
            deltaLatitud=abs(lat1-lat2)
            deltaLongitud=abs(lon1-lon2)
            distancia=2*r*math.asin(math.sqrt(  (math.pow(math.sin(deltaLatitud/2),2))  +  (math.cos(lat1)  *  math.cos(lat2)  *  (math.pow(math.sin(deltaLongitud/2),2)))  ))
            return distancia
        
        def tiempoLlegada(distancia):
            # 1       -Tiempo en bus                               -Tiempo a pie        
            #         -Velocidad prom. bus: 16,67 m/s              – Velocidad prom. a pie: 0,483m/s 
            velBus=16.67
            velPie=0.483
             
            tiempoBus=distancia/velBus
            tiempoPie=distancia/velPie
            
            print(f'Tiempo promedio que tardará en bus: {round(tiempoBus,2)} segundos')
            print(f'Tiempo promedio que tardará a pie: {round(tiempoPie,2)} segundos')
            return tiempoPie
                   
        def calcularDistancias(lati,long):
            
                global zonaWifi1
                global distanciaActualAZonaWifi1                #variables para menu 4 y 5
                global tiempoPromedio
                
                for i in range(4):         
                    dzw=distanciaUsuarioZona(lati,long,zonasWifi[i][0],zonasWifi[i][1])    #hago uso de la funcion ue calcula la distancia entre dos puntos de punto usuario a las 4 zonas wi fi  y lleno una lista de 4 distancias para despues obtener distancias minimas
                    matrizCercania.append(dzw)
                
                minDistancia1=round(min(matrizCercania),1)   #me extrae el valor minimo de las distancias  
                indiceMinDistancia1=matrizCercania.index(min(matrizCercania)) #me esxtrae el indice del valor minimo de las distancias

                matrizCercania[indiceMinDistancia1]=99999  #reemplazo el primer valor minimo por uno muy grande para buscar el segundo valor minimo y conservar los indices originales

                minDistancia2=round(min(matrizCercania),1)   #me extrae el valor minimo de las distancias  
                indiceMinDistancia2=matrizCercania.index(min(matrizCercania)) #me esxtrae el indice del valor minimo de las distancias
                
                print('Zonas wifi cercanas con menos usuarios')
                
                matrizPuntoUsuario=[lati,long]
                
                if zonasWifi[indiceMinDistancia1][2]<zonasWifi[indiceMinDistancia2][2]:
                    zonaWifi1=[zonasWifi[indiceMinDistancia1][0],zonasWifi[indiceMinDistancia1][1],zonasWifi[indiceMinDistancia1][2]]   #modifico variables globales para opcion 4 y 5
                    distanciaActualAZonaWifi1=minDistancia1
                    print(f'La zona wifi 1: ubicada en [{zonasWifi[indiceMinDistancia1][0]},{zonasWifi[indiceMinDistancia1][1]}] a {minDistancia1} metros , tiene en promedio {zonasWifi[indiceMinDistancia1][2]} usuarios')
                    print(f'La zona wifi 2: ubicada en [{zonasWifi[indiceMinDistancia2][0]},{zonasWifi[indiceMinDistancia2][1]}] a {minDistancia2} metros , tiene en promedio {zonasWifi[indiceMinDistancia2][2]} usuarios')
                    seleccionada2=pedirNumeroEntero(1,'Elija 1 o 2 para recibir indicaciones de llegada ',1,2,'Error zona wifi') 
                    if seleccionada2==1:
                        if matrizPuntoUsuario[0]>zonasWifi[indiceMinDistancia1][0]:
                            caminarNorteSur='sur'
                        elif matrizPuntoUsuario[0]==zonasWifi[indiceMinDistancia1][0]:
                            caminarNorteSur=''
                        else:
                            caminarNorteSur='norte'
                            
                        if matrizPuntoUsuario[1]>zonasWifi[indiceMinDistancia1][1]: 
                            caminarOrienteOccidente='occidente'
                        elif matrizPuntoUsuario[1]==zonasWifi[indiceMinDistancia1][1]: 
                            caminarOrienteOccidente=''    
                        else:
                            caminarOrienteOccidente='oriente'
                        print(f'Para dirigirse a la zona wifi dirigirse primero al {caminarOrienteOccidente} y luego hacia el {caminarNorteSur}') 
                        tiempoPromedio=tiempoLlegada(minDistancia1)  #modifico variables globales para opcion 4 y 5                        
                        input('Presione 0 para salir ')  
                        menuAcciones()  
                            
                    elif seleccionada2==2:
                        if matrizPuntoUsuario[0]>zonasWifi[indiceMinDistancia2][0]:
                            caminarNorteSur='sur'
                        elif matrizPuntoUsuario[0]==zonasWifi[indiceMinDistancia2][0]:
                            caminarNorteSur=''
                        else:
                            caminarNorteSur='norte'
                            
                        if matrizPuntoUsuario[1]>zonasWifi[indiceMinDistancia2][1]: 
                            caminarOrienteOccidente='occidente'
                        elif matrizPuntoUsuario[1]==zonasWifi[indiceMinDistancia2][1]: 
                            caminarOrienteOccidente='' 
                        else:
                            caminarOrienteOccidente='oriente'       
                        print(f'Para dirigirse a la zona wifi dirigirse primero al {caminarOrienteOccidente} y luego hacia el {caminarNorteSur}')  
                        tiempoPromedio=tiempoLlegada(minDistancia2)  
                        input('Presione 0 para salir ')  
                        menuAcciones()  
                    
                else:
                    zonaWifi1=[zonasWifi[indiceMinDistancia2][0],zonasWifi[indiceMinDistancia2][1],zonasWifi[indiceMinDistancia2][2]]   #modifico variables globales para opcion 4 y 5
                    distanciaActualAZonaWifi1=minDistancia2
                    print(f'La zona wifi 1: ubicada en [{zonasWifi[indiceMinDistancia2][0]},{zonasWifi[indiceMinDistancia2][1]}] a {minDistancia2} metros , tiene en promedio {zonasWifi[indiceMinDistancia2][2]} usuarios')
                    print(f'La zona wifi 2: ubicada en [{zonasWifi[indiceMinDistancia1][0]},{zonasWifi[indiceMinDistancia1][1]}] a {minDistancia1} metros , tiene en promedio {zonasWifi[indiceMinDistancia1][2]} usuarios')
                    seleccionada2=pedirNumeroEntero(1,'Elija 1 o 2 para recibir indicaciones de llegada ',1,2,'Error zona wifi')   
                
                    if seleccionada2==1:
                        if matrizPuntoUsuario[0]>zonasWifi[indiceMinDistancia2][0]:
                            caminarNorteSur='sur'
                        elif matrizPuntoUsuario[0]==zonasWifi[indiceMinDistancia2][0]:
                            caminarNorteSur=''
                        else:
                            caminarNorteSur='norte'
                                
                        if matrizPuntoUsuario[1]>zonasWifi[indiceMinDistancia2][1]: 
                            caminarOrienteOccidente='occidente'
                        elif matrizPuntoUsuario[1]==zonasWifi[indiceMinDistancia2][1]: 
                            caminarOrienteOccidente=''    
                        else:
                            caminarOrienteOccidente='oriente'
                        print(f'Para dirigirse a la zona wifi dirigirse primero al {caminarOrienteOccidente} y luego hacia el {caminarNorteSur}')   
                        tiempoPromedio=tiempoLlegada(minDistancia2)     
                        input('Presione 0 para salir ')  
                        menuAcciones()  
                            
                    elif seleccionada2==2:
                        if matrizPuntoUsuario[0]>zonasWifi[indiceMinDistancia1][0]:
                            caminarNorteSur='sur'
                        elif matrizPuntoUsuario[0]==zonasWifi[indiceMinDistancia1][0]:
                            caminarNorteSur=''
                        else:
                            caminarNorteSur='norte'
                            
                        if matrizPuntoUsuario[1]>zonasWifi[indiceMinDistancia1][1]: 
                            caminarOrienteOccidente='occidente'
                        elif matrizPuntoUsuario[1]==zonasWifi[indiceMinDistancia1][1]: 
                            caminarOrienteOccidente='' 
                        else:
                            caminarOrienteOccidente='oriente'       
                        print(f'Para dirigirse a la zona wifi dirigirse primero al {caminarOrienteOccidente} y luego hacia el {caminarNorteSur}')    
                        tiempoPromedio=tiempoLlegada(minDistancia1)         
                        input('Presione 0 para salir ')  
                        menuAcciones()    

        if seleccionada==1:
            lat=matrizCoordenadas[0][0]
            lon=matrizCoordenadas[0][1]
            ubicacionActual[0]=lat
            ubicacionActual[1]=lon
            calcularDistancias(lat,lon) 
                                          
        elif seleccionada==2:
            lat=matrizCoordenadas[1][0]
            lon=matrizCoordenadas[1][1]  
            ubicacionActual[0]=lat
            ubicacionActual[1]=lon
            calcularDistancias(lat,lon)           
            
        elif seleccionada==3:
            lat=matrizCoordenadas[2][0]
            lon=matrizCoordenadas[2][1]
            ubicacionActual[0]=lat
            ubicacionActual[1]=lon
            calcularDistancias(lat,lon)            
            
#................................................................................................................................................ 

def guardarArchivoConUbicacionCercana():
    print('Usted ha elegido la opción ',opcionGlobal)
    
    global ubicacionActual
    global zonaWifi1
    global distanciaActualAZonaWifi1
    global transporte
    global tiempoPromedio
    
    if matrizCoordenadas[0][0]==0 or ubicacionActual[0]==0:
       print('Error de alistamiento') 
       exit()
    else:
        '''informacion={   
            'actual':['latitud','longitud'],
            'zonawifi1':['latitud','longitud','usuarios'],
            'recorrido':['distancia','mediotransporte','tiempopromedio']
        }'''
        informacion={
            'actual':[ubicacionActual[0],ubicacionActual[1],''],
            'zonawifi1':[zonaWifi1[0],zonaWifi1[1],zonaWifi1[2]],
            'recorrido':[distanciaActualAZonaWifi1,transporte,round(tiempoPromedio,2)]
        }
        
        for key in informacion:
            print(key,informacion[key])
            
        elegida=pedirNumeroEntero(1,'¿Está de acuerdo con la información a exportar?\n Presione 1 para confirmar, 0 para regresar al menú principal ',0,1,'Error')   
         
        if elegida==0:
            menuAcciones()
            
        elif elegida==1:
            print('Exportando archivo')
            datosUsuario=pd.DataFrame(informacion,columns=['actual','zonawifi1','recorrido'])
            datosUsuario.to_csv('datos.csv',encoding='utf8')
            exit()
           
#................................................................................................................................................ 
    
def actualizarRegistrosDeZonasWifiDesdeArchivo():
    print('Usted ha elegido la opción ',opcionGlobal)

    #direccionArchivo='datosActualizacion.csv'

    #df=pd.read_csv(direccionArchivo,sep=',',header=0,encoding='utf8')
    #print(df)
    elegida=pedirNumeroEntero(1,'Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ',0,0,'Error')  
     
    if elegida==0:    
        menuAcciones()


#................................................................................................................................................ 

def elegirOpcionDeMenuFavorita():
    print('Usted ha elegido la opción ',opcionGlobal)
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
    print('Usted ha elegido la opción ',opcionGlobal)
    print('Hasta pronto')
    exit()
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Funcion que llama funciones de menu-------------------------------------------------------------

def menuAcciones():
    global opcionGlobal
    imprimirMenu()
    volverMenu=True
    while volverMenu==True:
        opcionSeleccionada=pedirNumeroEntero(3,'\nElija una opción ',1,7,'Error')              #ingreso  3 como argumento de mi funcion pedir numero entero, n=3 es el numero de equivocaciones, el argumento para el mensaje elija una opcion e intervalo entre el que debe escoger
        opcionGlobal=opcionSeleccionada 
        opcion=menu[opcionSeleccionada-1]
        if opcion=='Cambiar Contraseña':
            cambiarContraseña()
            menuAcciones()
            
        elif opcion=='Ingresar coodernadas actuales':
            ingresarCoordenadasActuales()
            menuAcciones()                                           #agregar esta linea si quiero que una vez terminada la accion del menu vuelva a menu principal
                                                     
        elif opcion=='Ubicar zona wifi más cercana':                                     
            ubicarZonaWifiMasCercana()
            #menuAcciones() 
            
        elif opcion=='Guardar archivo con ubicación cercana':
            guardarArchivoConUbicacionCercana()
            menuAcciones() 
            
        elif opcion=='Actualizar registros de zonas wifi desde archivo':
            actualizarRegistrosDeZonasWifiDesdeArchivo()
            menuAcciones() 
            
        elif opcion=='Elegir opción de menú favorita':
            elegirOpcionDeMenuFavorita()
            menuAcciones() 
            
        elif opcion=='Cerrar sesión':
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
