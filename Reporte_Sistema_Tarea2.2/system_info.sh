#!/bin/bash
# system_info.sh - Informe básico del sistema

LOGFILE="/home/dyansgu/Documentos/logs/system_report.txt"

# Escribir encabezado
echo "===============================" >> "$LOGFILE"
echo "Informe del sistema - $(date)" >> "$LOGFILE"
echo "===============================" >> "$LOGFILE"

# Usuarios conectados
echo -e "\nUsuarios conectados:" >> "$LOGFILE"
who >> "$LOGFILE"

# Uso de CPU y memoria
echo -e "\nUso de CPU y memoria:" >> "$LOGFILE"
top -b -n 1 | head -n 10 >> "$LOGFILE"
free -h >> "$LOGFILE"

# Espacio en disco
echo -e "\nEspacio en disco:" >> "$LOGFILE"
df -h >> "$LOGFILE"

# Últimos errores del sistema
echo -e "\nÚltimos errores del sistema (dmesg):" >> "$LOGFILE"
journalctl -p 3 -n 10 >> "$LOGFILE"

# Mensaje final
echo -e "\n✅ Informe generado en $LOGFILE"
