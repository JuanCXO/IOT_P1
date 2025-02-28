# IOT_P1- Monitoreo de Temperatura con Raspberry Pi Pico W y ThingSpeak

Este proyecto implementa un sistema de monitoreo de temperatura basado en **Internet de las Cosas (IoT)** utilizando una **Raspberry Pi Pico W** y un sensor **LM35**. Los datos son enviados a la plataforma **ThingSpeak**, donde se pueden visualizar en tiempo real y analizar con herramientas de MathWorks.

## 🚀 Características
- Lectura de temperatura con el sensor **LM35**.
- Conexión Wi-Fi y envío de datos a **ThingSpeak** cada 3 minutos.
- Análisis de datos en **MathWorks**, incluyendo promedios y alertas.
- Uso de **MicroPython** para la programación.

---

## 🛠️ Materiales Necesarios
- ✅ Raspberry Pi Pico W
- ✅ Sensor de temperatura LM35
- ✅ Resistencias y cables de conexión
- ✅ Conexión Wi-Fi
- ✅ Cuenta en [ThingSpeak](https://thingspeak.com/)

---

## 📡 Conexión del Hardware
### Diagrama de Conexión
| LM35 | Raspberry Pi Pico W |
|------|---------------------|
| VCC  | 3.3V               |
| OUT  | GP26 (ADC0)        |
| GND  | GND                |

### 📸 Foto del Circuito *(Opcional: Agregar una imagen del montaje físico)*

---

## 💻 Código en MicroPython
```python
import network
import urequests
import utime
from machine import ADC, Pin

# Configuración de WiFi
WIFI_SSID = "Alumno"
WIFI_PASSWORD = "Mebe2ege"

# Configuración de ThingSpeak
API_KEY = "AX98Z363YN92JY0C"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
INTERVALO_ENVIO = 180

# Configuración del sensor LM35
lm35 = ADC(Pin(26))
FACTOR_CONVERSION = 3.3 / 65535

# Configuración del LED
led_status = Pin("LED", Pin.OUT)
led_status.value(1)

# Funciones para conectar a WiFi y enviar datos (ver el código completo en el repositorio)
```
📌 **[Código completo aquí](codigo.py)**

---

## 📊 Visualización en ThingSpeak
### Configuración en MathWorks
- 📈 Cálculo del **promedio de temperatura**.
- 🚨 **Generación de alertas** si la temperatura supera **35°C**.

Ejemplo de gráfico en **ThingSpeak**:
*(Agregar captura de pantalla del gráfico)*

---

## 🔄 Uso de GitHub
### 📂 Estructura del Repositorio
```
📁 IoT_Temperatura
│── 📄 README.md  # Documentación del proyecto
│── 📄 codigo.py   # Código en MicroPython
│── 📸 imagen.jpg  # Foto del circuito (opcional)
```
### 📝 Cómo Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/IoT_Temperatura.git
```

---

## 📈 Análisis de Resultados
- 📌 Se observaron tendencias en la variación de la temperatura.
- 🚨 Se activaron alertas en **MathWorks** cuando la temperatura superó **35°C**.
- ✅ **Objetivo cumplido:** Monitoreo y visualización de datos en la nube.

---

## 🔮 Posibles Mejoras
- Envío de **promedios móviles** en lugar de valores instantáneos.
- Implementar un **buzzer** para alertas físicas.
- Guardar datos en una **base de datos local o en la nube**.

---

## 🏆 Créditos
📌 **Autor:** Juan Carlos Matias  
📅 **Fecha:** Febrero 2025  
📂 **Repositorio:** [GitHub](https://github.com/tu_usuario/IoT_Temperatura)

---



Examen Parcial 1 IOT RaspBerry
