import gpiozero
import Adafruit_ADS1x15

# se crea la  instancia del convertidor ADC
adc = Adafruit_ADS1x15.ADS1115()

# se configura  los pines GPIO para los LEDs
red_led = gpiozero.PWMLED(17)
blue_led = gpiozero.PWMLED(27)

R_REF = 10000.0  # La resistencia de referencia en ohmios
BETA = 3900.0    # La constante beta del termistor

GAIN = 1  # La ganancia para el ADC

def main():
    while True:
        # Se tien que leer la temperatura de consigna y la temperatura actual
        temp_setpoint = read_potentiometer()
        actual_temp = read_thermistor()
        
        # Se controlan los LEDs en función de las temperaturas leídas
        control_leds(temp_setpoint, actual_temp)
        
        # Se inprimen los valores de temperatura de consigna y actual
        print(f"Setpoint: {temp_setpoint:.2f}°C, Actual: {actual_temp:.2f}°C")
        
        # se tiene que esperar 1 segundo antes de la siguiente lectura
        time.sleep(1)

def read_potentiometer():
    # Se lee el valor del potenciómetro del canal 0 del ADC
    value = adc.read_adc(0, gain=GAIN)
    
    # Se tiene que escalar el valor leído a un rango de 0 a 30 grados Celsius
    temperature_setpoint = value * 30.0 / 32767.0
    return temperature_setpoint

def read_thermistor():
    # se debe leer el valor del termistor del canal 1 del ADC
    value = adc.read_adc(1, gain=GAIN)
    
    # Se tien que convertir el valor del termistor a grados Celsius usando la ecuación de Steinhart-Hart
    resistance = R_REF * (32767.0 / value - 1.0)
    temperature = 1.0 / (1.0 / 298.15 + (1.0 / BETA) * (resistance / R_REF - 1.0)) - 273.15
    return temperature

def control_leds(temp_setpoint, actual_temp):
    # Calcular la diferencia entre la temperatura actual y la de consigna
    difference = actual_temp - temp_setpoint
    
    # Definir la diferencia máxima para el control del ciclo de trabajo del LED
    max_difference = 5.0
    
    # Calcular el ciclo de trabajo del LED en función de la diferencia de temperatura
    duty_cycle = min(abs(difference) / max_difference, 1.0)

    if difference > 0:
        # Si la temperatura actual está por encima de la designacion, encender el LED azul
        blue_led.value = duty_cycle
        red_led.value = 0
    else:
        # Si la temperatura actual está por debajo de la designacion, encender el LED rojo
        red_led.value = duty_cycle
        blue_led.value = 0

if __name__ == "__main__":
    main()
