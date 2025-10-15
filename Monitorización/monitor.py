
# Importamos la librería psutil para obtener información del sistema
import psutil

# Importamos datetime para poder registrar la fecha y hora
from datetime import datetime

# Guardamos la ruta del archivo donde se escribirá la información
log_file = "/home/dyansgu/UbuntuLocalDyan/python/logs/monitor_log.txt"

# Obtenemos el porcentaje de uso de CPU
cpu = psutil.cpu_percent(interval=1)  # Espera 1 segundo para calcular bien

# Obtenemos la información de la memoria RAM
memoria = psutil.virtual_memory()

# Contamos el número de procesos activos
procesos = len(psutil.pids())

# Obtenemos la fecha y hora actual en formato legible
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Creamos el texto con toda la información del sistema
linea = (
    f"[{hora_actual}] CPU: {cpu}% | "
    f"RAM usada: {memoria.used // (1024 ** 2)}MB | "
    f"RAM libre: {memoria.available // (1024 ** 2)}MB | "
    f"Procesos activos: {procesos}\n"
)

# Mostramos el resultado en la pantalla
print(linea)

# Abrimos el archivo monitor_log.txt en modo 'a' (append → añadir)
# y escribimos la línea dentro
with open(log_file, "a") as archivo:
    archivo.write(linea)
