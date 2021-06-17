import RPi.GPIO as gpio


# Configurando
gpio.setmode(gpio.BCM)

# Configurando o Pino
gpio.setup(17, gpio.IN, gpio.UP)

while True:
    if gpio.input(17) == gpio.LOW:
        print("Botão presionado")
    else:
        print("Botão solto!")

# Desfazendo as modificações do GPIO
gpio.cleanup()