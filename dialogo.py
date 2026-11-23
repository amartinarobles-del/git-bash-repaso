from textflowthon import TextFlowThon
import time

# Creamos los textos con diferentes colores
narrador = TextFlowThon(delay=0.04, fg="bright_white", cursor="▍")
Ivory = TextFlowThon(delay=0.04, fg="bright_cyan", cursor="▍")
Pom = TextFlowThon(delay=0.04, fg="bright_red", cursor="▍")

# Presentación de la escena
narrador.typewrite("=== UNA NUEVA AVENTURA ===")
print()
time.sleep(1)

narrador.typewrite("La brigada de rescate llega a una zona desconocida.")
print()
time.sleep(1)

# Diálogo de Ivory
Ivory.typewrite("Ivory: ¿Qué lugar es este? Nunca había visto algo parecido.")
print()
time.sleep(1)

# Diálogo de Pom
Pom.typewrite("Pom: Será mejor que tengamos cuidado.")
print()
time.sleep(1)

# Respuesta de Ivory
Ivory.typewrite("Ivory: Bueno, pues vamos! hay que descubrir qué hay más adelante.")
print()
time.sleep(1)


# Esta será la línea que modificaremos para generar el conflicto
narrador.typewrite("Pom piensa que Ivory es vakiente...")
print()
