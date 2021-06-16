
#limpio consola
import os
var=os.name
print("su sistema operativo es: ",var)
os.system("cls")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

#Inicializo variables con valores esperados para validar log in 
nom=51661
con=16615
captcha1=661
#captcha2=6
captchausuario=0
captchacorrecta=667

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

#operaciones aritmeticas para obtener captcha
opcap1=5+1+6-6
opecap2=((6*6)-(5*5))-5
opecap3=5+5-5+1

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

print("Bienvenido al sistema de ubicación para zonas públicas WIFI\n")# imprimo mensaje de bienvenida

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Capturo datos de usuario
nombre=int(input('Por favor digite su nombre de usuario: ')) #capturo nombre

if nombre == nom:
    contrasena=int(input('\nPor favor digite su contraseña: ')) #si nombre ingresado fue correcto pido contraseña si no imprimo error y salgo
    
    if contrasena==con:
        captchausuario=int(input('\nIngrese el resultado de la suma '+str(captcha1)+' + '+str(opecap2)+' :')) #si contraseña fue correcta pido captcha si no imprimo error y salgo
        
        if captchausuario==captcha1+opecap2:
            print('\nSesión iniciada\n') #si el valor de captcha fue correcto imprimo sesion iniciada si no imprimi error y salgo
            exit()
        else:
            print("\nError\n")
            exit()
            
    else:    
        print("\nError\n")
        exit()

else:
    print("\nError\n")
    exit()

 
