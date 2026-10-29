import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana (El mapa)
ANCHO, ALTO = 800, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa del Merodeador - Marauder's Map")

# Colores
FONDO = (30, 30, 30) # Gris oscuro
LINEAS = (0, 255, 0) # Verde hacker
ESP32_COLOR = (255, 0, 0) # Rojo
PUNTO_COLOR = (0, 255, 255) # Cian

# Posiciones de los 4 ESP32 en las esquinas (X, Y)
esp32_posiciones = [
    (50, 50),     # Esquina superior izquierda
    (750, 50),    # Esquina superior derecha
    (50, 750),    # Esquina inferior izquierda
    (750, 750)    # Esquina inferior derecha
]

# Posición inicial del dispositivo a rastrear (simulada)
dispositivo_x, dispositivo_y = 400, 400

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Dibujar fondo
    pantalla.fill(FONDO)

    # Dibujar las líneas del cuadrado (El perímetro del mapa)
    pygame.draw.polygon(pantalla, LINEAS, esp32_posiciones, 2)

    # Dibujar los ESP32 (Nodos)
    for pos in esp32_posiciones:
        pygame.draw.circle(pantalla, ESP32_COLOR, pos, 15)
        # Dibujar un halo de señal
        pygame.draw.circle(pantalla, (255, 100, 100), pos, 25, 1)

    # Dibujar el dispositivo rastreado (La "huella" en el mapa)
    pygame.draw.circle(pantalla, PUNTO_COLOR, (dispositivo_x, dispositivo_y), 10)
    
    # Simular movimiento (para probar la visualización)
    # En el código real, estas coordenadas vendrían del script de trilateración
    dispositivo_x += 1
    if dispositivo_x > 750:
        dispositivo_x = 50

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60) # 60 fotogramas por segundo

pygame.quit()
sys.exit()
