import math

def calcular_distancia(rssi, potencia_referencia=-50, factor_perdida=2.0):
    """
    Convierte el RSSI a distancia en metros.
    Fórmula de pérdida de trayectoria en el espacio libre.
    """
    if rssi == 0:
        return -1.0 # Si no hay señal, distancia desconocida
    return 10 ** ((potencia_referencia - rssi) / (10 * factor_perdida))

def trilateracion(p1, r1, p2, r2, p3, r3):
    """
    Calcula la posición (X, Y) usando 3 puntos de referencia (ESP32s) y sus distancias.
    """
    # Coordenadas de los ESP32
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Cálculos matemáticos para la intersección de los 3 círculos
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    try:
        x = (C * E - F * B) / (E * A - B * D)
        y = (C * D - A * F) / (B * D - A * E)
        return x, y
    except ZeroDivisionError:
        return None, None

if __name__ == "__main__":
    print("[*] Módulo de Trilateración Iniciado")
    # Simulación de prueba (Coordenadas de los ESP32 en un cuadrado de 10x10 metros)
    esp32_1 = (0, 0)
    esp32_2 = (10, 0)
    esp32_3 = (0, 10)

    # Supongamos que el dispositivo está a 5 metros de cada uno
    r1 = 5.0
    r2 = 5.0
    r3 = 5.0

    pos_x, pos_y = trilateracion(esp32_1, r1, esp32_2, r2, esp32_3, r3)
    
    if pos_x and pos_y:
        print(f"[+] Dispositivo detectado en las coordenadas: X={pos_x:.2f}, Y={pos_y:.2f}")
    else:
        print("[-] Error en el cálculo (posiblemente los círculos no se intersectan).")
