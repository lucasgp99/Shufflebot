#opencv --> haar cascade

import cv2
import pkg_resources
import numpy as np
import RPi.GPIO as GPIO
import time

'''
haar_xml = pkg_resources.resource_filename('cv2', 'data/haarcascade_frontalface_default.xml')

faceClasif = cv2.CascadeClassifier(haar_xml) #open/data/haarcascade 'r"User\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"

img = cv2.imread('imagen.png') 
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceClasif.detectMultiScale(img_gray ,scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30),maxSize = (200,200))

#primer param --> imagen donde se detectara la cara
#segundo param --> scaleFactor , cuanto se va a reducir la imagen, si es un valor muy bajo = +tiempo procesamiento, + falsos positiv, si el valor es muy grande perderemos la deteccion de algunos rostros
#tercer param --> min neighbors--> vecinos de cada cuadrado, el cuadrado va buscando rostros, si encuentra x vecinos lo evalua como rostro, si es muy bajo puede encontrar falsos positivos, si es muy grande no detectar rostros
#cuarto param --> min size --> taman minimo del objeto a detectar, si son mas peque no los encontrara
#quinto param --> max size --> obvia objetos mas grandes

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
haar_xml = pkg_resources.resource_filename('cv2', 'data/haarcascade_frontalface_alt.xml') #default
#cargar clasif
faceClasif = cv2.CascadeClassifier(haar_xml) #open/data/haarcascade 'r"User\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"

def gestionarCara(faceClasif):
    #para video
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        #pasar imagen a escala de grises
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #detectMultiScale
        faces= faceClasif.detectMultiScale(gray, 1.3,5)
        
        #dibujar rectangulos
        for (x,y,w,h) in faces:
              cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
              #hacer captura y guardar 
              cv2.imwrite("foto_player.png",frame)
              jugador=True
              
        cv2.imshow('frame',frame)
        
        if jugador:
            break
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''
    cap.release()
    cv2.destroyAllWindows()
    
    return jugador
       
'''FUNCIÓN DETECTA NUMERO JUGADORES'''

#PARAMETROS NECESARIOS INICIALIZACIÓN STEPPER
GPIO.setmode(GPIO.BCM)
StepPins = [24,25,8,7]

def CountNumJugadors():
    numJugadors=0
    #SETUP MOTOR
    for pin in StepPins:
        GPIO.setup(pin.GPIO.OUT)
        GPIO.output(pin,0)
    halfStep_seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
    #SETUP CAMARA
    
    ''''ACTIVAR CAMARA'''
    
    #INICIO ROTACION MOTOR
    for i in range (512): 
        for halfStep in range(8):
            ''' PARA CADA HALF STEP GESTIONAR CARA '''
            hayJugador=gestionarCara()
            
            if hayJugador==True :
                numJugadors = numJugadors+1
            for pin in range(4):
                GPIO.output(StepPins[pin],halfStep_seq[halfStep][pin])
                time.sleep(0.001)
    GPIO.cleanup()

    return numJugadors
