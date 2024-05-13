import pyfirmata 
import speech_recognition as sr
import pyttsx3 

board = pyfirmata.Arduino('COM3')

# Definición de los pines de la placa Arduino
pin_cocina = board.get_pin('d:7:o')
pin_baño = board.get_pin('d:6:o')
pin_sala = board.get_pin('d:5:o')
pin_comedor = board.get_pin('d:4:o')

def encender_focos():
    pin_cocina.write(0)
    pin_baño.write(0)
    pin_sala.write(0)
    pin_comedor.write(0)
    
# Función para apagar los focos
def apagar_focos():
    pin_cocina.write(1)
    pin_baño.write(1)
    pin_sala.write(1)
    pin_comedor.write(1)
    
# Apagamos todos los focos al inicio
apagar_focos()

# Inicializamos el reconocedor de voz
escuchar = sr.Recognizer()

# Inicializamos el motor de voz y establecemos la velocidad de voz
inicializar = pyttsx3.init()
velocidad_de_voz = 160
inicializar.setProperty('rate', velocidad_de_voz)

# Definimos el nombre del asistente
nombre = "alexa"

# Función para que el asistente hable
def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()
    
# Función para tomar el comando de voz del usuario
def tomar():
    command = None
    try:
        with sr.Microphone() as voz :
            escuchar.adjust_for_ambient_noise(voz)
            print("Escuchando...")
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language='es-MX')
            command = command.lower()
            print(command)
                   
    except Exception as e:
         print(f"Ocurrió un error: {e}")
         pass
    return command

# Función principal que toma el comando de voz y realiza las acciones correspondientes
def alexa():
    command = tomar()
    if command is not None:
        if 'enciende la cocina' in command:
            habla("Encendiendo el foco de la cocina")
            pin_cocina.write(0)
        elif 'apaga la cocina' in command:
            habla("Apagando el foco de la cocina")
            pin_cocina.write(1)
        elif 'enciende el baño' in command:
            habla("Encendiendo el foco del baño")
            pin_baño.write(0)
        elif 'apaga el baño' in command:
            habla("Apagando el foco del baño")
            pin_baño.write(1)
        elif 'enciende la sala' in command:
            habla("Encendiendo el foco de la sala")
            pin_sala.write(0)
        elif 'apaga la sala' in command:
            habla("Apagando el foco de la sala")
            pin_sala.write(1)
        elif 'enciende el comedor' in command:
            habla("Encendiendo el foco del comedor")
            pin_comedor.write(0)
        elif 'apaga el comedor' in command:
            habla("Apagando el foco del comedor")
            pin_comedor.write(1)
        elif 'enciende todos los focos' in command:
            habla("Encendiendo todos los focos")
            encender_focos()
        elif 'apaga todos los focos' in command:
            habla("Apagando todos los focos")
            apagar_focos()
            
# Bucle infinito para que el asistente esté siempre escuchando
while True:
     alexa()