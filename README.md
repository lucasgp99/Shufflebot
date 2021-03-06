<p align="center">
<img src="Images/MVP.jpg" height="300">

## Índice de contenidos
* [¿Qué es Shufflebot?](#Shufflebot)
* [Instalación de dependencias](#instalar)
* [Arquitectura HW](#HW)
* [Diseño de las piezas 3D](#Diseño3D)
* [Software](#Software)
* [Vídeo](#Video)

<a name="Shufflebot"></a>
# Shufflebot
Shufflebot, un robot conectado a la corriente que a través de una cámara, un micro y un altavoz será capaz de gestionar una partida de cartas e interactuar con los jugadores. 
Para llevar a cabo su cometido, el robot dispondrá de dos compartimentos donde se insertará la baraja completa dividida en dos mazos distintos para luego mezclarlos en uno solo. Una vez mezclada la baraja, el robot gira sobre sí mismo repartiendo el número de cartas deseado en función del modo de juego a todos los jugadores. Dichos jugadores se comprobarán previamente a través de la visión por computador. El robot no únicamente contabilizará el número, sino que también tendrá la función de reconocerlos. Se adaptarán diferentes funcionalidades como el robo de cartas en función de lo que cada modo requiera.

<a name="instalar"></a>
### Instalación de las dependencias
- RPi.GPIO(Version 0.7.1) :pip install RPi.GPIO
- opencv2(Version 4.0.0): pip install opencv-python (https://www.youtube.com/watch?v=QzVYnG-WaM4)
- numpy(Version: 1.20.3): pip install numpy
- speech_recognition(Version: 3.8.1): pip install SpeechRecognition
- pyttsx3(Version: 2.90): pip install pyttsx3
- deep_translator(Version: 1.8.3): pip install deep-translator
 

<a name="HW"></a>
### Arquitectura HW
<p align="center">
<img src="Images/hardware.png" height="300">
  
  **Mezcla de la baraja (2Motores DC + Controlador)**
   Para mezclar la baraja conectaremos dos motores dc al controlador de motores 1 que se alimentarán a través de una fuente de alimentación externa, a continuación podemos ver al detalle las conexiones de los motores con el controlador y la conexión con los pines de la Raspberry.
  
<p align="center">
<img src="Images/hardware_1.png" height="300">
  
  La función de estos componentes es que los motores giren 2 rueditas y estas, situadas debajo de los dos montones de cartas, las empuje hacia dentro del robot creando un mismo montón.
  
  Pines GPIO utilizados: 23,4,12(M1) y 13,19,26(M2), 6(Controlador)
  
  **Reparto de cartas (Motores paso a paso + Motor DC + Controlador) **
  Mediante un sistema de elevación y rotación del cajón central haremos que las cartas se repartan a cada jugador. Concretamente utilizaremos un motor dc conectado a un controlador, dos motores,  paso a paso los cuales ya tiene su propio controlador, concretamente las conexiones són las siguientes.
Motores Paso a Paso:
    
<p align="center">
<img src="Images/hardware_2.png" height="300">
  
Pines GPIO utilizados: 24,25,8,7;     17,27,22,4.
Motor DC + controlador:

<p align="center">
<img src="Images/hardware_3.png" height="300">
    
Pines GPIO utilizados: 10,9,11 (M3), 18(controlador)
    
  **E/S de Audio**
  Nuestro robot en la fase final debería ser capaz de escuchar y entender ciertas órdenes y respondernos alguna cosa que indique que ha comprendido dichas órdenes. Para ello conectaremos un micro y un altavoz a la placa y a la raspberry, concretamente de la siguiente manera:
Micro: Conectado por USB
  
  <p align="center">
  <img src="Images/hardware_4.jpg" height="300">

  **E/S de video**
    Cámara USB, utilizada en la parte de visión por computador del robot. Gracias a ella el robot será capaz de reconocer a las personas que se encuentran alrededor de la mesa. Estos datos se tendrán en cuenta posteriormente en la gestión de la partida.
    
<p align="center">
<img src="Images/hardware_5.png" height="300">
</p>

<a name="Diseño3D"></a>
## Diseño 3D

A continuación listamos las piezas 3D necesarias para crear la estructura de nuestro robot:

**Estructura inferior**

<p align="center">
<img src="Images/3D_1.png" height="300">
  
Esta pieza actuará como cajón donde meteremos todos los componentes hardware necesarios para que el robot funcione correctamente (raspberry, controladores de motores, amplificador, motor paso a paso, cableado…). También servirá como base, ya que la estructura superior irá apoyada sobre este cajón.
  
**Estructura Superior**
  
<p align="center">
<img src="Images/3D_2.png" height="300">
  
<p align="center">
<img src="Images/3D_3.png" height="300">
  
 Esta pieza es la estructura principal del robot, ya que aquí se colocaran los engranajes, motores+ruedas y será donde se mezclaran y se repartirán las cartas mediante el funcionamiento de todos los motores.
    
**Engranajes y repartidor**
  
<p align="center">
<img src="Images/3D_4.png" height="300">
  
Aquí se pueden ver las piezas siguientes:
  
Cajón repartidor: será el cajón que subirá, bajará y rotará para así poder repartir las cartas correctamente y es donde caerán las cartas al mezclarlas. También tiene una estructura diseñada para poder acoplar nuestro servomotor.
  
Engranaje grande con columna dentada: este será la base del cajón repartidor, está diseñado para que pueda rotar y a la vez se le pueda montar el cajón para que suba y baje.
  
Engranaje mediano: este irá directamente conectado al motor paso a paso y será el que impulsa todo el sistema de rotación.

### Robot montado
  
<p align="center">
<img src="Images/imatge_montatge_1.jpg" height="300">
<img src="Images/MVP.jpg" height="300">
</p>
  
<a name="Software"></a>

## Software

**Visión por computador**

A través de una cámara, el robot tiene la capacidad de reconocer a los jugadores de la partida. En cuanto a código, esto se consigue gracias a la utilización de la librería opencv, y los clasificadores pre-entrenados que esta nos ofrece. En nuestro caso hemos relacionado esta parte del robot con el proyecto de la asignatura de visión por computador. Adjuntamos el documento dónde explicamos al detalle como se estructura esta parte en nuestro github. El nombre de dicho archivo es: VC_article.

**Reconocimiento de voz**

Hemos implementado en el robot ciertas funciones que permiten interactuar con él. Concretamente, se utiliza el reconocimiento de voz para gestionar los siguientes eventos: Inicio de partida: A través del comando iniciar partida, el robot empieza la gestión de dicha partida, comienza la rotación de reconocimiento y el barajado de cartas. A continuación las reparte a los jugadores deseados. En este punto se incluye el tratado de dos eventos. El primero, la gestión de robos, a través del comando Jugador X roba. El segundo consiste en nombrar algún jugador como tramposo. Si esto ocurre, el robot disparará todas las cartas disponibles al tramposo. Finalmente, a través del comando final de partida, el robot vuelve a las posiciones iniciales, necesarias para el inicio de un nuevo juego.

<a name="Video"></a>
## Vídeo 
<p>
  El siguiente enlace contiene el video promocional de Shufflebot (https://youtu.be/2KH45j8_Q0A )
</p>
