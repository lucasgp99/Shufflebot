#import librerias necesarias
#import speech_recognition as speech_recog
import time
from time import sleep
import RPi.GPIO as GPIO
#import pyaudio
import wave


    #FUNCTIONS
    #recognize_bing(): Utiliza la API de Microsoft Bing Speech
    #recognize_google(): Utiliza la API de Google Speech
    #recognize_google_cloud(): Utiliza la API de voz de Google Cloud
    #recognize_houndify(): Utiliza la API de Houndify de SoundHound
    #recognize_ibm(): Utiliza la API de IBM Speech to Text
    #recognize_sphinx(): Utiliza la API de PocketSphinx



#definir estructuras de datos 

#mic = speech_recog.Microphone()
#mic_list=speech_recog.Microphone.list_microphone_names()
    

    
#Procesado de voz
    #EXAMPLE
    
'''with mic as audio_file:
    #print("Speak Please")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Converting Speech to Text...")
    print("You said: " + recog.recognize_google(audio))'''
    
    #Mezcla 
        
        #control motores DC 1 y 2
'''PRUEBA MOTOR CC '''

def CCprueba():
    
    GPIO.setmode(GPIO.BCM) 
    #Pins 18 22 24 GPIO 24 25 8
    Motor1E = 26 #  Enable pin 1 of the controller IC
    Motor1A = 13 #  Input 1 of the controller IC
    Motor1B = 19 #  Input 2 of the controller IC
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    forward=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
    reverse=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM


    forward.start(0) 
    reverse.start(0)
    # this will run your motor in reverse direction for 2 seconds with 80% speed by supplying 80% of the battery voltage
    print ("GO backward")
    GPIO.output(Motor1E,GPIO.HIGH)
    forward.ChangeDutyCycle(0)
    reverse.ChangeDutyCycle(80)
    sleep(2)
    # this will run your motor in forward direction for 5 seconds with 50% speed.
    print ("GO forward")
    GPIO.output(Motor1E,GPIO.HIGH)
    forward.ChangeDutyCycle(50)
    reverse.ChangeDutyCycle(0)
    sleep(5)
    #stop motor
    print ("Now stop")
    GPIO.output(Motor1E,GPIO.LOW)
    forward.stop() # stop PWM from GPIO output it is necessary
    reverse.stop() 
    GPIO.cleanup()
    
    return 0
    #Reparticion 
    
       
    #Rotacion Base --> stepper
    
#PRUEBA STEPPER
def StepperPrueba():
    # Define GPIO signals to use Pins, in PRUEBA case: 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
    GPIO.setmode(GPIO.BCM)
    control_pins = [24,25,8,7]
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)
 
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]

    for i in range (512):
        for halfstep in range (8):
            for pin in range (4):
                GPIO.output(control_pins[pin],halfstep_seq[halfstep][pin])
            time.sleep(0.001)
        if i%128==0:    #hace pausas cada cuarto de vuelta, durante 5s
          time.sleep(5)
          
    GPIO.cleanup()
    return 0
'''
############
def AngleToDuty(ang):
  return float(pos)/10.+5.
'''

#SERVO PRUEBA
def ServoPrueba():
   
    Setup servoPin as PWM output of frequancy 100Hz
    servoPin=18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin,GPIO.OUT)
    pwm=GPIO.PWM(servoPin,100)
    #setup sweep parameters
    depart =0
    arrivee=180
    DELAY=0.1
    incStep=5
    pos=depart
 
    pwm.start(AngleToDuty(pos)) #star pwm
    nbRun=3
    i=0
    while i<nbRun:
        print("--------------------------run {}".format(i)) 
        for pos in range(depart,arrivee,incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)

            
        for pos in range(arrivee,depart,-incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
            
            
            i=i+1
          
    pwm.stop() #stop sending value to output
    GPIO.cleanup() #release channel
    return 0



  
#main prueba
if __name__ == '__main__' :
    
    #correctoCC = CCprueba()
    #correctoStepper = StepperPrueba()
    #correctoServo = ServoPrueba()
    

#ALTAVOZ
    
#MICRO

    '''
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 3 # seconds to record
    dev_index = 2 # device index found by p.get_device_info_by_index(ii)
    wav_output_filename = 'test1.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
'''
        #control motor 3
        
        #altavoz 
    
    #Devolver baraja
    
        #control servo
    


