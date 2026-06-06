# AshleyFabian_2025-0773_MAC_Flooding_P1

## Ataque MAC Flooding — Desbordamiento de Tabla CAM
**Estudiante:** Ashley Fabian  
**Matrícula:** 2025-0773  
**Práctica:** P1  
**Asignatura:** Seguridad en Redes  
**Plataforma:** GNS3 — Kali Linux  

---

## Descripción

Este repositorio contiene el script y la documentación técnica del ataque MAC Flooding. El atacante envía miles de frames Ethernet con MACs aleatorias para desbordar la tabla CAM del switch, forzándolo a entrar en modo fail-open y reenviar todas las tramas a todos los puertos, permitiendo capturar tráfico de otros hosts.

---

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `AshleyFabian_2025-0773_MAC_Flooding_P1.py` | Script del ataque |
| `AshleyFabian_2025-0773_Informe_MAC_Flooding_P1.pdf` | Documentación técnica profesional |

---

## Topología de red

| Dispositivo | IP | Puerto |
|---|---|---|
| R1 (CSR1000v) | 25.7.73.1/24 | Gi1 → SW1 Gi0/0 |
| SW1 (vIOS L2) | 25.7.73.2/24 | Gi0/1→VPCS, Gi0/2→Kali |
| Kali Linux | 25.7.73.50/24 | eth0 → SW1 Gi0/2 |
| VPCS (PC1) | 25.7.73.20/24 | eth0 → SW1 Gi0/1 |

**Red:** 25.7.73.0/24 (basada en matrícula 2025-0773)

---

## Uso del script

```bash
# Ejecutar el ataque con 10000 frames
sudo python3 AshleyFabian_2025-0773_MAC_Flooding_P1.py -i eth0 -c 10000

# Verificar en SW1
SW1# show mac address-table count
SW1# show mac address-table dynamic

# Parámetros disponibles
# -i  Interfaz de red
# -c  Cantidad de frames (0=infinito)
# -d  Delay entre frames en segundos (default: 0)
# -p  Tamaño del payload en bytes (default: 64)
```

---

## Evidencia del ataque

- Miles de entradas dinámicas en la tabla CAM de SW1
- Alertas de CPU hog en el proceso Spanning Tree
- SW1 entra en modo fail-open (comportamiento de hub)

---

## Contra-medida

```
SW1(config)# interface GigabitEthernet0/2
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 5
SW1(config-if)# switchport port-security violation restrict
```

---

## Video de demostración

🎬 [Ver video en YouTube](https://youtu.be/Dk1YWus2FRY?si=6CoY44LhhwsOV-bI)

> El video muestra el ataque en funcionamiento y la aplicación de la contra-medida.

---

## Requisitos

- Kali Linux
- Python 3.6+
- Scapy: `sudo apt install python3-scapy`
- GNS3 con CSR1000v y vIOS L2
- Ejecutar como root
