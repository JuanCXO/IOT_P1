import network
import urequests
import utime
from machine import ADC, Pin

# Configuración de WiFi
WIFI_SSID = "NOVA_ALV"
WIFI_PASSWORD = "NomerobeselWifi1"

# Configuración de ThingSpeak
API_KEY = "AX98Z363YN92JY0C"
CHANNEL_ID = "2855885"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
INTERVALO_ENVIO = 180  # Intervalo en segundos

# Configuración del sensor LM35
lm35 = ADC(Pin(26))  # Sensor conectado a GP26
FACTOR_CONVERSION = 3.3 / 65535  # Conversión de ADC a voltios

# Configuración del LED indicador
led_status = Pin("LED", Pin.OUT)
led_status.value(1)  # LED encendido al iniciar

# Función para conectar a WiFi
def iniciar_conexion():
    red = network.WLAN(network.STA_IF)
    red.active(True)
    if not red.isconnected():
        print("Intentando conectar a WiFi...")
        red.connect(WIFI_SSID, WIFI_PASSWORD)
        espera = 0
        while not red.isconnected() and espera < 15:
            utime.sleep(1)
            espera += 1
        if red.isconnected():
            print("Conectado a:", red.ifconfig())
        else:
            print("No se pudo conectar a WiFi")
    return red

# Función para obtener la temperatura en °C
def obtener_temperatura():
    valor_adc = lm35.read_u16()
    voltaje = valor_adc * FACTOR_CONVERSION
    temperatura_c = voltaje * 100  # LM35: 10mV/°C
    return round(temperatura_c, 2)

# Función para enviar datos a ThingSpeak
def subir_datos():
    temp_actual = obtener_temperatura()
    print(f"Temperatura medida: {temp_actual}°C")
    datos_url = f"{THINGSPEAK_URL}?api_key={API_KEY}&field1={temp_actual}"
    try:
        print("Enviando a ThingSpeak...")
        for _ in range(3):  # Parpadeo de confirmación
            led_status.value(0)
            utime.sleep(0.3)
            led_status.value(1)
            utime.sleep(0.3)
        respuesta = urequests.get(datos_url)
        print("Respuesta de servidor:", respuesta.text)
        respuesta.close()
    except Exception as err:
        print("Error en la transmisión:", err)

# Programa principal
conexion = iniciar_conexion()
while True:
    if not conexion.isconnected():
        conexion = iniciar_conexion()
    subir_datos()
    utime.sleep(INTERVALO_ENVIO)