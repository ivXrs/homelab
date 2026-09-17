# Homelab

Configuración y documentación del homelab que tengo montado en casa. Es un entorno muy humilde con pocos servicios pero que me ha servido como laboratorio para meterle caña a la administración de sistemas y hostear servicios interesantes.

## Dispositivo
![mini_pc](./raw/mini_pc.png)

| Característica | Descripción |
|---|---|
| Modelo | Blackview MP100 |
| Procesador (CPU) | AMD Ryzen™ 5 7430U · 6 núcleos · 12 hilos · Boost máx. 4.3 GHz |
| GPU | AMD Radeon™ Graphics (7 núcleos · 1800 MHz) |
| Memoria RAM | 16 GB DDR4 |
| Almacenamiento | 512 GB SSD M.2 2280 PCIe 3.0 |
| Sistema Operativo | Proxmox VE |

### Pantalla y Gráficos

| Salida | Resolución |
|---|---|
| HDMI 2.0b | 4K @ 60 Hz ×1 |
| DisplayPort 1.4 | 4K @ 144 Hz ×1 |
| USB-C full-featured | ×2 (10 Gbps · salida 4K @ 60 Hz) |

### Conectividad

| Tipo | Descripción |
|---|---|
| Wi-Fi | Wi-Fi 6 (802.11 a/b/g/n/ac/ax) |
| Bluetooth | Integrado (2.4G / 5G) |
| Ethernet | Gigabit LAN 10/100/1000 Mbps (auto-adaptativo) |

### Puertos e Interfaces

| Puerto | Descripción |
|---|---|
| USB 2.0 Type-A | ×1 (480 Mbps) |
| USB 3.2 Gen 2 Type-A | ×2 (10 Gbps) |
| USB-C | ×2 full-featured (10 Gbps + 4K @ 60 Hz) |
| DisplayPort | Máx. 4K 144 Hz |
| HDMI 2.0 | Máx. 4K 60 Hz |
| RJ45 Gigabit | ×1 (1000 Mbps) |
| Jack de audio 3.5 mm | Dos-en-uno |
| DC Jack IN | 5.5 × 2.1 mm |

### Dimensiones y Peso

| Característica | Descripción |
|---|---|
| Dimensiones | 127 × 127 × 45 mm |
| Peso | 492 g |

### Alimentación

| Característica | Descripción |
|---|---|
| Fuente de alimentación | Entrada 100–240V 50/60 Hz · Salida 19V/3.42A (DC 5.5 × 2.1 mm) |

## Servicios

<table>
    <tr>
        <th>Icono</th>
        <th>Nombre</th>
        <th>Descripción</th>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/selfhst/icons/svg/proxmenux.svg"></td>
        <td><a href="https://proxmenux.com/">ProxMenux</a></td>
        <td>Menú interactivo y panel web para gestionar y configurar Proxmox VE de forma sencilla</td>
    </tr>
    <tr>
        <td><img width="32" src="https://simpleicons.org/icons/tailscale.svg"></td>
        <td><a href="https://tailscale.com/">Tailscale</a></td>
        <td>Red privada de acceso remoto (VPN mesh) basada en WireGuard para conectarme al homelab desde fuera de casa</td>
    </tr>
    <tr>
        <td><img width="32" src="https://simpleicons.org/icons/pihole.svg"></td>
        <td><a href="https://pi-hole.net/">Pi-hole</a></td>
        <td>Servidor DNS local que bloquea publicidad y rastreadores a nivel de red</td>
    </tr>
    <tr>
        <td><img width="32" src="https://simpleicons.org/icons/nginxproxymanager.svg"></td>
        <td><a href="https://nginxproxymanager.com/">Nginx Proxy Manager</a></td>
        <td>Proxy inverso con interfaz web para gestionar dominios, subdominios y certificados SSL de los servicios internos</td>
    </tr>
    <tr>
        <td><img width="32" src="https://simpleicons.org/icons/vaultwarden.svg"></td>
        <td><a href="https://github.com/dani-garcia/vaultwarden">Vaultwarden</a></td>
        <td>Gestor de contraseñas autoalojado, compatible con los clientes oficiales de Bitwarden</td>
    </tr>
</table>