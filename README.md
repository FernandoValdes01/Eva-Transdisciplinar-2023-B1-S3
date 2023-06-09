# Eva-Transdisciplinar-2023-B1-S3
en este proyecto se llevara a cabo un codigo de python que podra calcular 
un evento fisico particular que en nuestro caso es el:


# TIRO PARABOLICO

## ¿Que es un tiro parabolico?
El movimiento parabólico o tiro oblicuo resulta de la composición de un movimiento rectilíneo uniforme (mru horizontal) y un movimiento rectilíneo uniformemente acelerado de lanzamiento hacia arriba o hacia abajo (mrua vertical).

### Explicacion del Fenomeno Fisico

https://youtu.be/SjoqdKKH-mw

## Historia del Tiro parabolico
En lo concerniente al movimiento de los proyectiles cerca de la superficie terrestre, Aristóteles (384 a.c. en Estagira, Macedonia – 322 a.c.en Calcis Eubea, Grecia)
sostenía que “una piedra permanece en reposo o se mueve en línea recta hacia el centro de la tierra a menos que se vea sometida a una fuerza exterior”.

Pero fue sólo hasta cuando Galileo Galilei (15 de Febrero 1564 in Pisa - 8 de Enero de 1642 in Arcetri, cerca a Florencia) Florencia) explicó explicó las leyes que
rigen los movimientos, que se fundaron las bases de su conocimiento

El movimiento parabólico observado en la Figura lo analizó Galileo como una superposición de dos componentes: Una era la tendencia natural de los cuerpos a mantener su velocidad (Ley de inercia) y por lo tanto el cuerpo mantenía su desplazamiento horizontal después de abandonar el borde de la mesa y la otra componente era la caída libre.

[<img src="https://static.wixstatic.com/media/a56c14_7fe930efed1949c4ada74431db838558.jpg/v1/fill/w_640,h_198,al_c,lg_1,q_80,enc_auto/a56c14_7fe930efed1949c4ada74431db838558.jpg" style="width: 380px;">](https://numpy.org)

Ambos movimientos se superponen simultáneamente y dan origen al movimiento parabólico (la curva que describe la primera pelota es una parábola). Convirtiéndose así Galileo en el primer hombre en describir la trayectoria de un cuerpo en caída libre en dos dimensiones.

![Movimiento-parabólico](https://github.com/FernandoValdes01/Eva-Transdisciplinar-2023-B1-S3/assets/132627914/143a00ee-4a66-45d1-b662-123917c06547)


## ¿Que Modelamientos Matematicos utiliza el tiro parabolico?
El Tiro Parabolico utiliza multiples Modelamientos matematicos dependiendo lo que uno necesita

si uno necesita la el tiempo maximo del objeto  se ocupa el siguiente modelamiento:

 ### T=2v0senθ/g

 para encontrar la altura maxima se ocupa  el siguiente modelamiento:

 ### H= (v°)² /2g

 para encontrar  la velocidad en X se ocupa el siguiente modelamiento:

 ### v0x=v0·cos angulo

 para encontrar la velocidad en y se ocupa el siguiente modelamiento:
 ### v0y = v0· sen ángulo

 esta es uno de los tantos modelamientos matematicos  que se pueden utilizar para el tiro parabolico
 como se puede ver en nuestro codigo ocupamos variaciones de estas mismas para mayor eficiencia a la hora de programarlo
 por ejemplo ocupamos funciones de nuestras librerias para encontrar los valores que nosotros deseamos 

 

## ¿Como se resuelve?
considerando lo que busca el tiro parabolico pueden ser muchos valores 
pero en este caso lo que busca este codigo es mostrar la altura maxima que alcanzaria un
objeto lanzado a una velocidad y angulo ingresados por el usuario
la formula para resolverlo es remplazando los valores del con la formula o el valor que deseemos calcular


## Aplicaciones 
Aunque no siempre lo percibamos, el tiro parabólico está presente en varias situaciones cotidianas. Por ejemplo, al lanzar un objeto en el aire, como una pelota, una piedra o un frisbee, su trayectoria seguirá una forma parabólica hasta que llegue al suelo.

aqui otros ejemplos del tiro parabolico
### el lanzamiento de un balon de basketball
[<img src="https://transferencia.tec.mx/wp-content/uploads/2022/05/Tiro-parabólico.png" style="width: 380px;">](https://numpy.org)

### El lanzamiento de un balon de football
[<img src="https://2.bp.blogspot.com/-g8z5BPkA0fE/VO-KoLaSwXI/AAAAAAAAABM/l-a993Nej04/s1600/Imagen6.png" style="width: 380px;">](https://numpy.org)

### El lanzamiento de una bala de cañon

[<img src="https://img.genial.ly/5aa5d34c1c30733d4a3526af/8eb5407e-d2ea-497d-9a73-a0baa8e46196.png" style="width: 380px;">](https://numpy.org)

# Programación.
### A)Descripción de las herramientas utilizadas
en este trabajo se utilizaron multiples herramientas empezando por nuestro lenguaje de 
programacion que en este caso sera
### - [Python](https://github.com/python/cpython)
Python es nuestro lenguaje que ocuparemos en nuestro proyecto

![pngwing com (4)](https://github.com/FernandoValdes01/Eva-Transdisciplinar-2023-B1-S3/assets/132627914/ac4668a0-71ce-4d93-b3f0-b09f2ab71d27)

### En temas de librerias ocuparemos 5 librerias.

1.[Matplotlib](https://github.com/matplotlib/matplotlib)
matplotlib es una libreria externa que nos ayudara en multiples tareas dentro de nuestro codigo por ejemplo la generacion de graficos
con sus especificaciones , y tambien las herramientas dentro del grafico

![pngwing com (5)](https://github.com/FernandoValdes01/Eva-Transdisciplinar-2023-B1-S3/assets/132627914/c42d2e1b-b86b-41c7-9c6f-44a986332ee1)

2.- [CustomTkinter](https://customtkinter.tomschimansky.com/)
Customtkinter es una libreria basada en la libreria "tkinter" pero con un toqe mas estetico y minimalista lo que nos permitira hacer una interfaz
mas estetica y minimalista.

[<img src="https://github.com/TomSchimansky/CustomTkinter/raw/master/documentation_images/CustomTkinter_logo_dark.png" style="width: 380px;">](https://customtkinter.tomschimansky.com/)

3-[NumPy](https://numpy.org)
Numpy es una libreria usada para hacer calculos mas matematicos de todo tipo 
[<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" style="width: 380px;">](https://numpy.org)

4-[webbrowser](https://docs.python.org/es/3/library/webbrowser.html)
webbrowser es una libreria de python que nos permitira la busqueda por internet mediante el codigo

5-[Tkinter](https://docs.python.org/es/3/library/tkinter.html)
Tkinter es una de las herramientas para empezar en lo que es las interfazes graficas
a nosotros nos convenia utilizar customtkinter pero para otras partes ocupamos tkinter 



### A) Guia de instalación y Guia de Uso

 https://youtu.be/Ce0ZQ_0Nwns

### B) Enlace a vídeo con la explicación del código desarrollado.

https://youtu.be/rsQZqTNkxms



## Conclusion
Para concluir este proyecto, hemos logrado representar el fenómeno físico asignado que en nuestro caso fue el tiro parabolico explicando su naturaleza y más. Utilizando herramientas de programación, creamos un simulador de este mismo fenomeno fisico que da como resultado  los datos normalmente mas requeridos para estos fenomenos como la altura maxima del objeto, el tiempo que tarda en caer, y el tiempo que tarda en llegar a su altura maxima 

este trabajo nos permitio sacar lo mejor de cada uno en nuestros ambitos tanto de programacion como en fisica con un fuerte trabajo en equipo  de parte de cada integrante del equipo con cada uno aportando su parte sin duda una gran experiencia y un proyecto a compartir 
