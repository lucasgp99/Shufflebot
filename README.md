
![image](https://user-images.githubusercontent.com/47353331/170779556-566721d8-23e8-407d-8b62-fb93f027412a.png)

## Índice de contenidos
* [¿Qué es Shufflebot?](#Shufflebot)
* [Instalación de dependencias](#instalar)
* [Arquitectura HW](#HW)
* [Diseño de las piezas 3D](#Diseño3D)
* [Funcionamiento](#Funcionamineto)

<a name="Shufflebot"></a>
# Shufflebot
Shufflebot, un robot conectado a la corriente que a través de una cámara, un micro y un altavoz será capaz de gestionar una partida de cartas e interactuar con los jugadores. 
Para llevar a cabo su cometido, el robot dispondrá de dos compartimentos donde se insertará la baraja completa dividida en dos mazos distintos para luego mezclarlos en uno solo. Una vez mezclada la baraja, el robot gira sobre sí mismo repartiendo el número de cartas deseado en función del modo de juego a todos los jugadores. Dichos jugadores se comprobarán previamente a través de la visión por computador. El robot no únicamente contabilizará el número, sino que también tendrá la función de reconocerlos. Se adaptarán diferentes funcionalidades como el robo de cartas en función de lo que cada modo requiera.

<a name="instalar"></a>
### Instalación de las dependencias
- RPi.GPIO(Version 0.7.1) :pip install RPi.GPIO
- opencv2(Version 4.0.0): pip install opencv-python (https://www.youtube.com/watch?v=QzVYnG-WaM4)
- numpy(Version: 1.20.3): pip install numpy

<a name="HW"></a>
### Arquitectura HW
<p align="center">
<img src="Images/hardware.PNG" height="300">
  
  **Movimiento del vehículo**
  
Se han conectado los dos motores de las ruedas al controlador L298 junto con la corriente de las 4 pilas de 1,5 Voltios, este controlador actúa de intermediario entre la Raspberry y los movimientos del vehículo. El controlador se ha conectado también a la Raspberry Pi. 

  **Cinemática inversa del brazo**
  
Los 3 motores utilizados para mover el brazo en el plano de 3 ejes, y el servomotor que controla la apertura de la pinza se han conectado a la placa i2c, esta facilita la comunicación entre la raspberry y los componentes. La placa i2c está conectada a 4 pilas de 1,5 Voltios y a la Raspberry Pi. 

  **Reconocimiento de objetos**
  
La cámara es alimentada por dos pilas de 1,5 Voltios y controlada directamente por la Raspberry.

</p>

<a name="Diseño3D"></a>
## Diseño 3D

El proyecto contiene archivos STL para formar la estructura del robot.


### Robot montado
<p align="center">
<img src="images/image13.png" width="300" height="300">

<img src="images/image14.png" width="300" height="300">

<img src="images/image15.png" width="300" height="300">
</p>

### Pinza
<p align="center">
<img src="images/image26.jpg" height="300">
</p>

### Articulaciones del brazo
<p align="center">
<img src="images/image25.png" height="300">
<img src="images/image27.png" height="300">
</p>

### Base del brazo
<p align="center">
<img src="images/image29.png" width="300" height="300">
<img src="images/image30.png" width="300" height="300">
</p>

### Base de la carrocería
<p align="center">
<img src="images/image32.png" height="300">
</p>

### Soporte de la caja
<p align="center">
<img src="images/image34.png" height="300">
</p>
<p align="center">
<img src="images/image35.png" width="300">
</p>
  
### Caja con corpantimentos
<p align="center">
<img src="images/image37.png" width="300" height="300">
</p>
  
## Reconocimiento de objetos
Se ha utilizado el lenguaje Python para realizar el reconocimiento e identificación de formas, y se ha importado la librería “opencv” para obtener imágenes de la cámara. Y la librería “imageai” que utiliza “tensorflow”, una librería orientada a construir y entrenar redes neuronales, para utilizar un modelo de reconocimiento de objetos (Yolo).

<p align="center">
<img src="images/image4.png" height="250">
<img src="images/image5.png" height="250">
</p>

Tras unas adaptaciones se ha utilizado el modelo para reconocer objetos en una simulación en CoppeliaSim.

<p align="center">
<img src="images/image2.png" height="300">
</p>

Los datos de cada objeto se gestionan con Python como una lista de diccionarios.

<p align="center">
<img src="images/image24.png" height="200">
</p>

<a name="Funcionamientos"></a>
## Simulación

Se ha simulado el comportamiento del robot con CoppeliaSim para recrear un espacio con una serie de diferentes objetos, que se interponen en el camino del robot. Éste, pudiendo detectarlos, recogerlos y almacenarlos en los compartimentos correspondientes, simula su correspondiente actuación. 

### Ruedas
Se han utilizado las siguientes ruedas para la simulación.
<p align="center">
<img src="images/image16.png" height="300">
<img src="images/image17.png" height="300">
</p>

### Ruedas incorporadas en el stl de la caja
<p align="center">
<img src="images/image18.png" width="300" height="300">
</p>

### Funcionamiento

El robot gira hasta detectar un objeto que le interesa.

<p align="center">
<img src="images/image8.png" height="300">
</p>

Una vez detectado se acerca a él, lo recoge y lo almacena en el compartimento que le pertoque.

<p align="center">
<img src="images/image19.png" height="300">
<img src="images/image3.png" height="300">
</p>

<p>
  El siguiente enlace contiene el video promocional de SweeperBot (https://youtu.be/OWggp3zetLo)
</p>
