
__author__ = "luisf"
__date__ = "$30/03/2017 06:07:03 PM$"

from random import *
from math import *
from tkinter import *
from modules.numbers import *
from urllib.request import *

import os 
"""
FUNCIONES PREDEFINIDAS
x= 'a'
print(ord(x))
print(chr(ord(x)))
"""

"""
IMPORTAR FUNCIONES
from math import *
print(sin(20))
"""

"""
METODOS
temp = "cadEna de prueba"
print(temp.lower())
print(temp.upper())
print(temp.title())
print(temp.replace("prueba",'Ejemplo'))
"""

"""
PROGRAMA 01
print('Programa del Calculo del area de un Triangulo')
base = float(input("Digita la Base "))
altura = float(input("Digita la altura "))
resultado = (base*altura)/2
print("El resultado es:" , float(resultado))
"""

"""
PROGRAMA MODIFICACIONES
print('Programa del Calculo del area de un Triangulo')
base = float(input("Digita la Base "))
altura = float(input("Digita la altura "))
area = (base*altura)/2
print('La base es %5.2f, la altura es %5.2f y el area es %5.2f' %(base,altura,area))
"""

"""
GRAFICOS
largo = 640
ancho = 480
from tkinter import *
canvas = Canvas(width=largo, height=ancho, bg='green')
canvas.pack(expand=YES, fill=BOTH)  
canvas.create_line(0,0,largo,ancho)
canvas.create_oval(10, 10, 200, 200, width=1, fill='blue')
canvas.create_rectangle(100,100,200,200)
canvas.create_arc(10, 10, 190, 190, start=270, extent=90, fill='gray90')
xy = 10, 10, 190, 190
canvas.create_arc(xy, start=0, extent=270, fill='gray60')
"""

"""
CONDICIONALES
name = "fernando"
password = "luisf1012"
inputName = input("Digite su nombre: ")
inputPassword = input("Digite su contrasena: ")
if name == inputName and password == inputPassword:
    print('Bienvenido:' , inputName)
else:
    print('Error el password o la contrasena es incorerecta')
"""

"""
WHILE
tabla = int(input("Ingresa el numero del que quieres la tabla "))
tope = int(input("Digite el numero de digitos que quieres que aparesca "))
cont = 0
while cont<=tope:
    print(cont,'x',tabla,"=",cont*tabla)
    cont+=1
"""

""""
IF WHILE
while 1 == 1:
    print('a) Python es la Ostia')
    print('b) Python no me gusta')
    print('c) Prefiero otro lenguaje de programacion')
    
    op = input('Digita la opcion que escogiste ')
    
    if op>='a' and op<='c':
        if op==a:
            print('Excelente amigo')
        elif op==b:
            print('Debes probar este excelente lenguaje')
        elif op==c:
            leng = input('Cual es el lenguaje que te gusta')
            print('Vaya',leng,'es un lenguaje que em encanta igualemente')
    else:
        print('No era una opcion correcta a elejir intenta nuevamente')
 """

"""
FOR IN
for numero in [0,3,2,3,4]:
    print(numero)

for deporte in ['voley','basket','futbol']:
    print(deporte)

tabla = int(input('Digite el numero que quiere la tabla '))
tope = int(input('Digite la cantidad de numero de la tabla '))
for nTabla in range(tope+1):
    print(nTabla,'x',tabla,'=',nTabla*tabla)
"""

"""
ROTURA DE BUCLES
numero = int(input('Escribe hasta que numero quieres que verifique '))
is_primo = True
for n in range(2,numero):
    if numero%n==0:
        is_primo = False
        break
if is_primo:
    print('Tu numero si es primo')
else:
    print('Tu numero no es primo')
"""

"""
EXCEPCIONES
x = float(input('Digita el Dividendo: '))
y = float(input('Digita el Divisor: '))

try:
    z = x/y
    print('El resultado es %f' %z)
except:
    print('ERROR')
"""   

"""
PROGRAMA DE APLICACION

#OPCIONES
print('Digite la opcion que desee')
print('a) Seno')
print('b) Coseno')
print('c) Tangente')
print('d) Cotangente')
print('e) Secante')
print('f) Cosecante')
OP = input('Digitela : ')

#PREPARACION DEL LIENZO
largo = 700
alto = 480
canvas = Canvas(width=largo, height=alto, bg='white')
canvas.pack(expand=YES, fill=BOTH)
y = alto/2
x = largo/2

#PROYECCION
medidaX = 2*pi
medidaY = 2

#ABSISAS
canvas.create_line(x,0,x,alto,width=1, fill='blue')
#ORDENADAS
canvas.create_line(0,y,largo,y,width=1, fill='blue')
#LABEL X AND Y
canvas.create_text(largo-10, y+10, text='X')
canvas.create_text(largo-20, y+25, text=str(round(medidaX,2)))
canvas.create_text(13, y+10, text='-X')
canvas.create_text(23, y+25, text=str(round(-1*medidaX,2)))
canvas.create_text(x+10, 10, text='Y')
canvas.create_text(x+10, 25, text=str(round(-1*medidaY,2)))
canvas.create_text(x+10, alto-10, text='-Y')
canvas.create_text(x+10, alto-25, text=str(round(-1*medidaY,2)))

#PASO
paso = 0.1

#VARIABLES DE AYUDA
contador = -1*x
fin = x

while contador <= fin:
    try:
        if OP == 'a':
            temp = sin(contador*medidaX/x)
        elif OP == 'b':
            temp = cos(contador*medidaX/x)
        elif OP == 'c':
            temp = tan(contador*medidaX/x)
        elif OP == 'd':
            temp = 1/tan(contador*medidaX/x)
        elif OP == 'e':
            temp = 1/cos(contador*medidaX/x)
        elif OP == 'f':
            temp = 1/sin(contador*medidaX/x)
        canvas.create_rectangle(contador+x,y-temp*y/medidaY,contador+x,y-temp*y/medidaY)
        contador+=paso
    except:
        contador+=paso
"""

"""
SECUENCIAS
#print('Esta es la primera linea \n, esta es la segunda linea')
string = input("Dame un cadena ")
print("Esta es la longitud: ",len(string))
pos = 3
print("La posicion",pos,"es:",string[pos])
for char in string:
    print("Caracter:",char)

print("Parte de cadena",string[1:3])
print(string.find('f'))
"""

"""
LISTAS I
list = [2,5,6,True,8]
for element in list:
    print(element)
print("\n")
print("Size",len(list))
print("Elemento de la posicion 3",list[3])
"""

"""
LISTAS II
bag = [1,3,6]
add = "Anadido"
bag = bag + [add]
add = "Anadido 2"
bag.append(add)
print(bag)
"""     

"""
LISTAS III

bag = [7,8,5,3]
print(bag)
modify = 8
replace = True
index = 0
#Verificar si existe el elemento
if modify in bag:  
    for value in bag:
        if value == modify:
            break
    index+=1 
    bag[index]=replace
print(bag)
del bag[1]
print(bag)
"""    

"""
LISTAS III
size = 4
bag = []
for n in range(size):
    bag.append(randrange(0,10,1))
print("Bolsa inicial",bag)

for i in range(len(bag)):
    q = i + 1
    for q in range(len(bag)):
        if bag[i] <  bag[q]:
            temp = bag[i]
            bag[i] = bag[q]
            bag[q] = temp
            

print("Bolsa final",bag)
"""  

"""
LISTAS IV
string = "Hola como estas"
print("Primera cadena",string)
#Para la funcion split se debe mandar como parametro el caracter que separara la cadena
#este separador no estara incluido en dicha lista
list = string.split(" ")
print("Lista Obtenida",list)
#Para la funcion join es unir una lista con un unido dado
string = " ".join(list)
print("Cadena unida",string)
"""

"""
MATRICES I
#Creamos una DB con Matrices
#Una lista contiene, nombre apellido y edad
list_1 = ['Fernando','Berrospi',20]
list_2 = ['Alexis','Meregildo',22]
list_3 = ['Jose','Valverde',21]
db = [list_1,list_2,list_3]
print(len(db))
print(db)
"""

"""
MATRICES II
raw = int(input("Digite el numero de Filas "))
col = int(input("Digite el numero de Columnas "))
list = []
for r in range(raw):
    temp_list = []
    for c in range(col):
        num = int(input('Digite el numero de la posicion ('+str(r)+','+str(c)+') '))
        temp_list.append(num)
    list.append(temp_list)
print('Matriz Creada:',list)
#Cambio
list[0][0]=-1
print('Matriz Creada:',list)
"""

"""
APLICATIVO II
#PREPARANDO EL CANVAS
large = 600
high = large
canvas = Canvas(width=large,height=high,bg='white')
canvas.pack(expand=YES,fill=BOTH)

#MATRIZ
row = 100
column = row
        
#CREAR GRILLA
interval = large/row
for n in range(row):
    canvas.create_line(n*interval,0,n*interval,high)
    canvas.create_line(0,n*interval,large,n*interval)

#EVENTOS DEL MOUSE
def callback(event):
    #X e Y iniciales donde se dibujara los cuadrados con el incremento
    x_inic = int(event.x/interval)*interval
    y_inic = int(event.y/interval)*interval
    canvas.create_rectangle(x_inic,y_inic,x_inic+interval,y_inic+interval,fill='blue')
canvas.bind("<Button-1>", callback)
"""

"""
FUNCIONES I
def raiz(x):
    try:
        return sqrt(x)
    except:
        return "Error"

print(raiz(float(input('Digite el numero que desea la raiz '))))

def area_triangle(base,height):
    return base*height/2

base = float(input('Digite la Base del Triangulo '))
height = float(input('Digite la altura del Triangulo '))
print(area_triangle(base,height))
"""

"""
FUNCIONES II
n = 8
list = []
for i in range(n):
    list.append(randint(0,10))
print('Primera Lista:',list)
def duplicate(list):
    for i in range(len(list)):
        list[i] = list[i]*2

duplicate(list)
print("Lista duplicada:",list)
def sort(list):
    for i in range(len(list)):
        for q in range(len(list)):
            if list[i]<list[q]:
                list[i],list[q] = list[q],list[i]
sort(list)
print('Lista Ordenada:',list)
"""

"""
FUNCIONES III
def factorial(n):
    temp = 1
    for i in range(1,n+1):
        temp = temp * i
    return temp
def combinatorial(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))
number = 3
m = 1
print("El factorial de",number,':',factorial(number))
print("El numero de combinaciones de",number,'en',m,'es:',combinatorial(number,m))
"""

"""
RECURSIVIDAD
number = 8
def factorial(n,acu):
    #print('N: ',n)
    if n-1 != 0:
        return n*factorial(n-1,acu)
    return acu
print('El Factorial de',number,'es',factorial(number,1))

def fibonaci(n,i,list):
    if i != n+1:
        if i<=2:
            list.append(1)
        else:
            list.append(list[i-2]+list[i-3])
        fibonaci(n,i+1,list)
    return list   
print(fibonaci(number,1,[]))
"""

"""
GRAFICOS FRACTALES Y MODULOS

#MODULOS
#from modules.numbers import * #IMPORTADO AL INICIO

#CONSTANTES
width = 500
height = width
background_color = '#154360'
line_color = '#E86D9D'
increase_color = 10

#VARIABLES
xi,yi = 0,height/2
xf,yf = width,height/2
x1,y1 = 223,100
x2,y2 = 75,354
x3,y3 = 377,354
n = 5

#VENTANA DE APLICACION
window = Tk()
window.geometry(str(width)+'x'+str(height))
window.title('Graficos Fractales')
window.iconbitmap('favicon.ico')
window.resizable(width = False,height = False)

#CANVAS
canvas = Canvas(window,width = width,height = height,bg = background_color)
canvas.pack()


#CREAR GRAFICO
def create_grafic_VonKoch(xi,yi,xf,yf,n,line_color):
    if  n!=0:
        x1 = xi + (xf - xi)/3
        y1 = yi + (yf - yi)/3
        
        x3 = xf - (xf - xi)/3
        y3 = yf - (yf - yi)/3
        
        x2 = (x1+x3)*cos(pi/3) - (y3-y1)*sin(pi/3)
        y2 = (y1+y3)*cos(pi/3) + (x3-x1)*sin(pi/3)

        create_grafic_VonKoch(xi,yi,x1,y1,n-1,increase_hexa_color(line_color,increase_color))
        create_grafic_VonKoch(x1,y1,x2,y2,n-1,increase_hexa_color(line_color,increase_color))
        create_grafic_VonKoch(x2,y2,x3,y3,n-1,increase_hexa_color(line_color,increase_color))
        create_grafic_VonKoch(x3,y3,xf,yf,n-1,increase_hexa_color(line_color,increase_color))
        
    else: 
        canvas.create_line(xi,height - yi,xf,height - yf,fill=line_color)

def create_copo_VonKoch(x1,y1,x2,y2,x3,y3,n,line_color):
    create_grafic_VonKoch(x1,y1,x2,y2,n,increase_hexa_color(line_color,increase_color))
    create_grafic_VonKoch(x2,y2,x3,y3,n,increase_hexa_color(line_color,increase_color))
    create_grafic_VonKoch(x3,y3,x1,y1,n,increase_hexa_color(line_color,increase_color))


#create_grafic_VonKoch(xi,yi,xf,yf,n,line_color)
create_copo_VonKoch(x1,y1,x2,y2,x3,y3,n,line_color)
mainloop()
"""

"""
CLASES
     
class Person(object):
    age_limit = 18
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def is_higher_age(self):
        if self.age > Person.age_limit:
            return True
        return False
    
    def to_string(self):
        return 'Nombre: ' + self.name + '\nApellido: ' + self.surname + '\nEdad: ' + str(self.age) + '\n'
    
    def clone(self):
        return Person(self.name,self.surname,self.age)
    
person_1 = Person('Fernando','Berrospi',20)
person_2 = Person('Luis','Gamboa',20)

#print(person_1.to_string())
#print(person_2.is_higher_age())

##VARIABLES DE CLASE
#person_1.age_limit = 19 #Cuando se modifica una 'variable de clase' es como si pasara a ser de instancia
#person_2.age_limit = 21
#print(person_1.age_limit,person_2.age_limit,Person.age_limit)

##CLONACION
person_3 = person_1.clone()
print(person_1.to_string())
person_3.name = 'Juan'
print(person_3.to_string())
print(person_1.to_string())
"""   

"""
FICHEROS

##LEER UN ARCHIVO 1
file = open('..//files//index.html','r')
for line in file:
    #print(line)
    break
    
##LEER UN ARCHIVO 2
file = open('..//files//index.html','r')
line = file.readline()
while(line != ''):
    #print(line)
    line = file.readline()

##LEER UN ARCHIVO 3
file = open('..//files//index.html','r')
characters = 5
char = file.read(characters)
while(char != ''):
    #print(char)
    char = file.read(characters)

##LEER UN ARCHIVO 4
file = open('..//files//index.html','r')
#print(file.readlines()) #SIN SALTOS DE LINEA

##LEER UN ARCHIVO 5
file = open('..//files//index.html','r')
#print(file.read())

##LEER UNA PAGINA WEB
file = urlopen('http://www.noteplus.esy.es/')
#print(file.read())
"""
##ESCRIBIR EN UN FICHERO
def content_card():
    file = open('..//files//index.html','r')
    lines = file.read()
    file.close()
    return lines

def create_card(name,title,content):
    name = name + '.html'
    lines = content_card()
    lines = lines.replace('{{title}}',title)
    lines = lines.replace('{{content}}',content)
    
    if( not os.path.exists('..//cards') ):
        os.mkdir('..//cards')
    
    file = open('..//cards//'+name,'w')
    file.write(lines)
    file.close()  
    print('Tarjeta Creada Correctamente')

name = input('Nombre de la Tarjeta: ')
title = input('Titulo de la Tarjeta: ')
content = input('Contenido de la Trajeta: ')
create_card(name,title,content)






















