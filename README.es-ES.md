

<div align="center">

# 🔍 SpyEyes

### Herramienta de recopilación de información OSINT (versión optimizada en chino)

**Consulta todo en uno: IP · Teléfono · Nombre de usuario · WHOIS de dominio · Registros MX · Correo electrónico · Subdominios · Correos de dominio · Monitoreo Diff · Escaneo por lotes**

[![CI](https://github.com/Akxan/SpyEyes/actions/workflows/ci.yml/badge.svg)](https://github.com/Akxan/SpyEyes/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Akxan/SpyEyes/branch/main/graph/badge.svg)](https://codecov.io/gh/Akxan/SpyEyes)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-488%20passed-success.svg)](tests/)
[![Platforms](https://img.shields.io/badge/platforms-3164-orange.svg)](#-对比同类工具)
[![Reports](https://img.shields.io/badge/reports-8%20formats-9cf.svg)](#-报告格式8-种)
[![Commands](https://img.shields.io/badge/commands-10-blueviolet.svg)](docs/TUTORIAL.md)
[![Version](https://img.shields.io/badge/version-1.8.0-blueviolet.svg)](docs/CHANGELOG.md)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://akxan.github.io/SpyEyes/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows%20%7C%20Termux-lightgrey)](#-安装)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)
[![Maintenance](https://img.shields.io/maintenance/yes/2026.svg)](https://github.com/Akxan/SpyEyes/commits/main)

[![Stars](https://img.shields.io/github/stars/Akxan/SpyEyes?style=social)](https://github.com/Akxan/SpyEyes/stargazers)
[![Forks](https://img.shields.io/github/forks/Akxan/SpyEyes?style=social)](https://github.com/Akxan/SpyEyes/network/members)
[![Issues](https://img.shields.io/github/issues/Akxan/SpyEyes.svg)](https://github.com/Akxan/SpyEyes/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Akxan/SpyEyes.svg)](https://github.com/Akxan/SpyEyes/commits/main)

**🇨🇳 Chino · [🇬🇧 English](README.en.md)**

[**📖 Tutorial detallado**](docs/TUTORIAL.md) · [**🐛 Reportar un error**](https://github.com/Akxan/SpyEyes/issues) · [**🤝 Contribuir código**](docs/CONTRIBUTING.md) · [**📝 Registro de cambios**](docs/CHANGELOG.md)

</div>

---

## 📖 Descripción del proyecto

**SpyEyes** es una herramienta de recopilación de información de **OSINT (Inteligencia de Fuentes Abiertas)** de línea de comandos escrita en Python, optimizada en profundidad para usuarios chinos. **10 capacidades principales**: Rastreo IP / Resolución de números de teléfono / Escaneo de nombres de usuario (**3164 plataformas / Bilingüe chino-inglés**) / WHOIS de dominio / Consulta MX / Verificación de validez de correo electrónico / **Enumeración de subdominios** (6 fuentes pasivas + fuerza bruta con diccionario + extracción JS) / **Extracción de correos de dominio** (6 fuentes concurrentes totalmente gratuitas + rastreador profundo) / **Monitoreo Diff** (comparar dos escaneos) / **Entrada por lotes de dominios** (`--batch`) / **8 formatos de informes estilo Editorial**.

Ideal para **investigadores de ciberseguridad, ingenieros de pruebas de penetración, analistas SOC, investigadores técnicos, miembros de equipos Rojo/Azul, jugadores de CTF** y cualquier desarrollador interesado en inteligencia de fuentes abiertas.

### 💎 Puntos destacados

- **🆕 v1.6.8:** Carga automática de claves API en `~/.spyeyes/env` + Informe muestra el estado completo de las 6 fuentes — Un simple archivo en formato KEY=VALUE reemplaza la configuración de LaunchAgent / shell; el estado de cada fuente en el informe (✅/⊘/❌) es claro a simple vista
- **🆕 v1.6.6:** Extracción de correos de dominio 3-4× más rápida — Filtrado HTTP probe de subdominios no web + rastreador BFS paralelo para múltiples objetivos (linux.do de 5.5 min → 1.5 min)
- **🆕 v1.6.5:** `--alive-only` estricto e inteligente — Filtrado automático de respuestas HTTP en entornos wildcard / secuestro de DNS para evitar falsos positivos de "activo"
- **🆕 v1.6.0:** 6 fuentes concurrentes para correos de dominio — Bing SERP + DuckDuckGo + Wayback Machine + Commits de GitHub + crt.sh + WHOIS, **totalmente gratuito + sin registro**; el más potente en la capa gratuita comparado con theHarvester / Photon / EmailFinder
- **🆕 v1.5.0:** Modo Diff + Dominios por lotes — `spyeyes diff old.json new.json` para monitorización continua de OSINT; `--batch domains.txt` para escaneo por lotes
- **🆕 v1.4.x → v1.6.x:** Recopilación de subdominios en 7 dimensiones — 6 fuentes pasivas (crt.sh / CertSpotter / HackerTarget / OTX / **Wayback Machine** / subfinder opcional con 30+ fuentes) + Fuerza bruta de DNS con diccionario + Extracción de hosts en body JS/HTML (soporta títulos 4xx/5xx + cadena CNAME completa) + Verificación DNS A/AAAA/CNAME + Probe HTTP + Detección Wildcard
- **🆕 Embellecimiento de informes estilo Editorial Investigation Brief** — Estética de archivo de investigación/periódico con Cormorant Garamond + Crimson Pro + JetBrains Mono; thead sticky en HTML + distinción visual vivo/muerto + colores por estado HTTP; Portada en PDF + capítulos en números romanos; Despliegue jerárquico en XMind; Gráfico de fuerza dirigida D3.js
- **3164 plataformas de escaneo de nombres de usuario:** 48 círculo chino + 58 círculo hispano + 91 adultos/citas + 733 foros, velocidad nivel Sherlock ~20 segundos (150 hilos concurrentes + Pool de sesiones + Protección ReDoS)
- **Permutación estilo Maigret** + Escaneo recursivo `--recursive` (retroalimentación completa del progreso) + Múltiples modos de escaneo `--quick` / `--category`
- **8 formatos de informe** — `JSON / Markdown / HTML / PDF / TXT / CSV / XMind / Graph (D3.js)`, todos siguen el idioma de la interfaz (zh/en)
- **Detección de WAF:** Huellas de alta precisión para Cloudflare / AWS WAF / PerimeterX / DataDome / Akamai, etc.
- **Bilingüe completo chino-inglés:** Menús interactivos / parámetros CLI / mensajes de error / **contenido de informes**, todo en doble idioma
- **🆕 v1.6.1:** Barras de progreso auditadas al 100% — Todas las operaciones lentas tienen retroalimentación en tiempo real, adiós a la apariencia de "congelado"
- **🆕 v1.8.0:** Directorio de informes por defecto inteligente — Ejecución desde código fuente → `<raíz del proyecto>/Downloads/` (los usuarios con git clone lo ven directamente en el repo); Instalación empaquetada (pip/pipx/brew) → `~/Downloads/spyeyes/` (nunca escribe en site-packages); `SPYEYES_REPORTS_DIR=path` siempre tiene la máxima prioridad
- **🆕 v1.8.0:** Comprobación de versión al inicio — Comparación con GitHub Release cacheada cada 24h, aviso en stderr para nuevas versiones; `--no-update-check` / `SPYEYES_NO_UPDATE_CHECK=1` para desactivar con un clic; completamente silencioso si está offline / falla la API
- **🆕 v1.8.0:** `investigate` 3-4× más rápido + retroalimentación de progreso completa — Fase 2b (correo→usuario) cambiada de serial a 4 concurrentes, el escenario de 15 correos pasa de ~210s a ~50-80s; Fases 1/2a/2b muestran progreso en tiempo real `[N/M] ✓ tarea`; seguro para TTY, completamente silencioso en tuberías
- **541 pruebas con pytest:** 4 herramientas limpias (ruff 0 / mypy 0 / bandit 0 / pytest todo verde), CI cruzado en macOS/Linux/Windows × Python 3.10–3.14

---

## ✨ Características principales

<table>
<tr>
<td width="50%">

### 🌐 Rastreo de direcciones IP
- Soporta **IPv4 / IPv6**
- País, ciudad, ISP, ASN, coordenadas
- Genera automáticamente enlaces a Google Maps
- **Mapeo de nombres de países en chino** (180+ países)

### 📡 Consulta de IP local
- Muestra la IP de salida pública actual con un clic
- Refresco en tiempo real tras cambiar VPN / Proxy

### 📱 Rastreo de números de teléfono
- Ubicación de pertenencia en chino (Beijing / Shanghai / ...)
- Operadora en chino (China Mobile / Unicom / Telecom)
- Zona horaria, formato E.164 / internacional / marcado móvil
- Identificación de 12 tipos de número (móvil / fijo / VoIP / localizador ...)

### 👤 Escaneo de nombres de usuario
- **3164 plataformas** (fusionada Maigret + Sherlock + WhatsMyName, incluye motor de resolución Maigret)
- **48 círculo chino** (Continental/Taiwán/HK/Singapur/Malasia) + **58 círculo hispano** (España/Latam) + **733 foros**
- **150 hilos concurrentes**, escaneo completo ~20 segundos (modo quick ~10 segundos)
- Doble detección con palabras clave de contenido + `must_contain` + identificación de WAF
- Por defecto solo muestra coincidencias, `--all` para ver resultados completos
- **🆕 v1.1.0**：Escaneo recursivo `--recursive` (profundidad 0-2) + subcomando `permute` (mutación de nombres de usuario)

</td>
<td width="50%">

### 🔍 Consulta WHOIS de dominio
- Registrador, fechas de creación/vencimiento/actualización
- Servidores DNS, organización registrante, correo electrónico
- Soporta 200+ TLD

### 📨 Registros MX de dominio
- Lista todos los registros MX y su prioridad
- Para inteligencia de dominios de correo

### ✉️ Verificación de validez de correo electrónico
- Validación de formato con regex
- Verificación conjunta con registros MX
- No envía correos, no deja rastro

### 🌐 Enumeración de subdominios (v1.3.0 → v1.6.1 🆕)
- **Fuentes pasivas múltiples (6 fuentes):** `crt.sh` + CertSpotter + HackerTarget + AlienVault OTX + **Wayback Machine (v1.4.9)** resumen concurrente
- **🚀 Relevó opcional con subfinder (v1.4.8):** Detecta automáticamente binario `subfinder`, relevó de 30+ fuentes de datos (virustotal / shodan / censys / chaos / fofa / quake / securitytrails, etc.); si no está instalado, omite sin costo
- **🆕 Fuerza bruta DNS con diccionario (v1.4.9, opt-in):** ~220 prefijos de alto acierto integrados + `SPYEYES_DNS_WORDLIST=/path` diccionario grande personalizado, habilita con `--bruteforce`
- **🆕 Extracción de hosts JS / HTML (v1.4.9, activado por defecto):** Escanea referencias de hosts codificados en el body de 16KB ya capturado por probe (`fetch('https://api.example.com/...')`, etc.), extrae y ejecuta otra ronda de verificación DNS; desactiva con `--no-js-extract`
- **Verificación activa DNS:** A / AAAA / CNAME (30 workers por defecto)
- **Probe HTTP:** Captura status_code + `<title>` (`--no-probe` para desactivar)
- **Detección Wildcard:** Probador de prefijo aleatorio de 32 caracteres, marca resultados no confiables
- Soporta los 8 formatos de informe (en HTML los subdominios activos son clicables)

### 📊 Monitorización OSINT / Lotes (v1.5.0 🆕)
- **Modo Diff:** `spyeyes diff old.json new.json` — Compara dos escaneos para encontrar subdominios **nuevos / desaparecidos / modificados** (IP/estado HTTP/título)
- **Entrada de dominios por lotes:** `spyeyes subdomain --batch domains.txt --batch-save-dir reports/` — Informe independiente por dominio, Ctrl+C para interrumpir sin perder datos
- **`--alive-only` global:** Filtrado en CLI / JSON / 8 formatos de exportación, solo conserva subdominios alcanzables

### 🚀 Mejoras generales
- **Modo parámetros CLI:** Llamadas por lotes mediante scripts
- **Salida JSON:** Integración en tuberías con jq / cualquier herramienta
- **Guardado de resultados:** `--save DIR` almacenamiento automático
- **Cobertura 100% de retroalimentación de progreso** (v1.6.1): Todas las operaciones > 2s tienen progreso en tiempo real
- **Terminal a color:** Detección automática de TTY
- **Multiplataforma:** macOS / Linux / Windows / Termux

</td>
</tr>
</table>

---

## 🆚 Comparación con herramientas similares

| Herramienta | IP | Teléfono | Usuario | WHOIS | MX | Correo | Subdominio | Correo dominio | Monit. Diff | Lotes | Formatos | Chino |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [Sherlock](https://github.com/sherlock-project/sherlock) | ❌ | ❌ | ✅ (400+) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 1 | ❌ |
| [Maigret](https://github.com/soxoj/maigret) | ❌ | ❌ | ✅ (3000+) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 1-2 | ❌ |
| [holehe](https://github.com/megadose/holehe) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 1 | ❌ |
| [theHarvester](https://github.com/laramies/theHarvester) | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅(parcial comercial) | ❌ | ❌ | 1-2 | ❌ |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | 1 | ❌ |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | 1 | ❌ |
| **SpyEyes** | ✅ | ✅ | ✅ **(3164)** | ✅ | ✅ | ✅ | ✅ **(7 dimensiones)** | ✅ **(6 fuentes gratuitas)** | ✅ | ✅ | **8** | ✅ |

> 💡 **Notas sobre el posicionamiento:** SpyEyes **no** busca competir con Sherlock en profundidad de escaneo de usuarios, sino ser una herramienta de OSINT **ligera, todo-en-uno + priorización en chino + informes ricos**.
> - Solo buscar usuarios → Sherlock / Maigret son más especializados
> - Extracción de correos que requiera 30+ APIs comerciales → theHarvester es más completo
> - Pero si quieres **lo mejor en capa gratuita + 8 formatos de informe + UI en chino + 10 comandos todo-en-uno** → **SpyEyes es para ti**

---

## 🛠 Stack tecnológico

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2C5BB4?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

</div>

| Categoría | Tecnología / Librería | Uso |
|---|---|---|
| **Lenguaje** | Python 3.10+ | Lenguaje principal |
| **HTTP** | `requests` | Llamadas API |
| **Resolución de teléfono** | `phonenumbers` | Librería oficial de Google para números de teléfono |
| **DNS** | `dnspython` | Consulta de registros MX / A / AAAA |
| **WHOIS** | `python-whois` | Información de registro de dominios |
| **Concurrencia** | `concurrent.futures.ThreadPoolExecutor` | Escaneo concurrente multiplataforma |
| **CLI** | `argparse` | Análisis de parámetros de línea de comandos |
| **Terminal** | Secuencias de escape ANSI | Salida a color + detección TTY |
| **Pruebas** | `pytest` + `unittest.mock` | Pruebas unitarias + mock HTTP |
| **CI/CD** | GitHub Actions | Pruebas automáticas multiplataforma y multiversión |
| **API de fuentes de datos** | `ipwho.is` · `api.ipify.org` | Consulta de información IP |

---

## 🚀 Inicio rápido

### Instalación y ejecución en una línea (macOS / Linux)

```bash
git clone https://github.com/Akxan/SpyEyes.git && \
cd SpyEyes && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt && \
python3 -m spyeyes
```

### Pruébalo ahora

```bash
# Consultar información IP de Google DNS
python3 -m spyeyes ip 8.8.8.8

# Consultar IP de salida local
python3 -m spyeyes myip

# Consultar número de teléfono
python3 -m spyeyes phone +8613800138000

# Escanear nombre de usuario
python3 -m spyeyes user torvalds

# Consulta WHOIS
python3 -m spyeyes whois example.com

# Registros MX
python3 -m spyeyes mx gmail.com

# Verificación de correo
python3 -m spyeyes email someone@gmail.com

# Enumeración de subdominios (v1.3.0 → v1.6.1)
python3 -m spyeyes subdomain example.com                                     # 6 fuentes pasivas + DNS + probe HTTP + extracción JS (todo activado por defecto)
python3 -m spyeyes subdomain example.com --bruteforce                        # Añadir fuerza bruta con diccionario integrado de 220 (más completo)
SPYEYES_DNS_WORDLIST=~/all.txt spyeyes subdomain example.com --bruteforce    # Diccionario grande personalizado
python3 -m spyeyes subdomain example.com --alive-only --save report.html     # Solo conservar subdominios activos (informe limpio)
python3 -m spyeyes subdomain example.com --no-js-extract --no-probe          # Solo pasivo puro, más rápido
python3 -m spyeyes subdomain example.com --json | jq '.subdomains[] | select(.alive)'

# 🆕 v1.5.0: Escaneo de dominios por lotes
python3 -m spyeyes subdomain --batch domains.txt --batch-save-dir reports/ --alive-only
# Un dominio por línea en domains.txt; # comentarios y líneas vacías se omiten automáticamente; informe HTML independiente por dominio

# 🆕 v1.5.0: Modo Diff — Monitorización continua de OSINT
python3 -m spyeyes subdomain example.com --json > monday.json
python3 -m spyeyes subdomain example.com --json > friday.json   # Escanear de nuevo unos días después
python3 -m spyeyes diff monday.json friday.json --save diff.html   # Subdominios nuevos/desaparecidos/modificados

# 🆕 v1.6.0: Extracción de correos de dominio (6 fuentes concurrentes, gratuito y sin registro)
python3 -m spyeyes domain-emails example.com           # crt.sh + WHOIS + Bing + DDG + Wayback + GitHub concurrentes
python3 -m spyeyes domain-emails example.com --guess "John Doe,Jane Smith"   # Añadir generación por patrón
python3 -m spyeyes domain-emails example.com --no-crawl   # Solo 6 fuentes pasivas, más rápido

# Ver historial (~/.spyeyes/history.jsonl se acumula automáticamente)
python3 -m spyeyes history --limit 20            # Últimos 20 registros
python3 -m spyeyes history --search torvalds     # Filtrar por subcadena de query
python3 -m spyeyes history --json | jq           # Tubería JSON

# Salida JSON + guardar en archivo
python3 -m spyeyes ip 8.8.8.8 --json --save results/
```

### 🆕 Demostración de nuevas funciones v1.2.0

```bash
# 1) 8 formatos de informe — Distribución por extensión de archivo de --save
python3 -m spyeyes user torvalds --save report.html      # HTML (con estilos CSS)
python3 -m spyeyes user torvalds --save report.pdf       # PDF (requiere spyeyes[pdf])
python3 -m spyeyes user torvalds --save report.xmind     # Mapa mental XMind 8
python3 -m spyeyes user torvalds --save report.graph.html # Gráfico de fuerza dirigida D3.js
python3 -m spyeyes user torvalds --save report.csv       # CSV (con protección contra inyección)
python3 -m spyeyes user torvalds --save report.txt       # Texto plano
python3 -m spyeyes user torvalds --save report.md        # Markdown
python3 -m spyeyes user torvalds --save report.json      # JSON

# 2) Contenido del informe sigue el idioma de la UI: UI en chino genera informe en chino, UI en inglés genera informe en inglés
python3 -m spyeyes --lang zh user torvalds --save zh.html
python3 -m spyeyes --lang en user torvalds --save en.html

# 3) Mutación de nombres de usuario estilo Maigret (method=all incluye _prefijos/sufijos_)
python3 -m spyeyes permute "John Doe"                    # strict (por defecto)
python3 -m spyeyes permute "John Doe" --method all       # Incluye _johndoe / johndoe_
python3 -m spyeyes permute "Linus Torvalds" --scan --quick  # Mutación + escaneo automático

# 4) Escaneo recursivo: extrae nombres de usuario secundarios en páginas coincidentes para continuar el escaneo
python3 -m spyeyes user torvalds --recursive --depth 2

# 5) 150 hilos concurrentes por defecto (actualizado de 100); ajustable
python3 -m spyeyes user torvalds --workers 200
```

---

## 📦 Instalación

### macOS (venv recomendado)

```bash
brew install python3 git
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Linux (Debian/Ubuntu)

```bash
sudo apt-get install git python3 python3-pip python3-venv
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Termux (Android)

```bash
pkg install git python
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
pip install -r requirements.txt
```

### Windows

```powershell
# Descarga Python 3 desde https://www.python.org, marca "Add to PATH" durante la instalación
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Configuración de claves API (opcional, gratuita, mejora la integridad de los datos)

SpyEyes usa 6 fuentes gratuitas por defecto (funciona sin claves), pero configurar las siguientes claves mejora significativamente la tasa de aciertos y la estabilidad.

### Método recomendado: Archivo `~/.spyeyes/env` (v1.6.8+)

```bash
mkdir -p ~/.spyeyes
cat > ~/.spyeyes/env << 'EOF'
# AlienVault OTX (gratuito, https://otx.alienvault.com/settings)
SPYEYES_OTX_API_KEY=your_otx_key

# SSLMate CertSpotter (gratuito, https://sslmate.com/account/api_credentials)
SPYEYES_CERTSPOTTER_API_KEY=your_certspotter_key

# ProjectDiscovery PDCP (gratuito, para subfinder)
PDCP_API_KEY=your_pdcp_key

# Opcional: Acelerar búsqueda de commits en GitHub (PAT gratuito, solo lectura)
SPYEYES_GITHUB_TOKEN=ghp_your_token

# Opcional: Directorio de informes fijo
# Comportamiento por defecto (v1.8.0+): Ejecución desde código fuente → <raíz del proyecto>/Downloads/
#                  Instalación empaquetada → ~/Downloads/spyeyes/
# Establecer esta variable para anular forzosamente, independientemente del método de instalación
SPYEYES_REPORTS_DIR=/var/log/spyeyes

# Opcional: Desactivar comprobación de versión de GitHub al inicio (v1.8.0+)
# Comprobación silenciosa en segundo plano cada 24h; establece a 1 para omitir completamente
# SPYEYES_NO_UPDATE_CHECK=1
EOF
chmod 600 ~/.spyeyes/env
```

Se lee automáticamente al cargar el módulo, consistente en todas las plataformas (macOS/Linux/Windows), `shell export` tiene prioridad.

### Método alternativo: shell `~/.zshrc` / `~/.bashrc`

```bash
echo 'export SPYEYES_OTX_API_KEY=your_key' >> ~/.zshrc
source ~/.zshrc
```

---

## 📋 Uso

### 1️⃣ Modo menú interactivo

```bash
python3 -m spyeyes
```

```
███████╗██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝
███████╗██████╔╝ ╚████╔╝ █████╗   ╚████╔╝ █████╗  ███████╗
╚════██║██╔═══╝   ╚██╔╝  ██╔══╝    ╚██╔╝  ██╔══╝  ╚════██║
███████║██║        ██║   ███████╗   ██║   ███████╗███████║
╚══════╝╚═╝        ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚══════╝
       👁  All-in-One OSINT Toolkit  ·  github.com/Akxan/SpyEyes  👁

[ 1 ] Rastreo IP
[ 2 ] Ver IP local
[ 3 ] Rastreo de teléfono
[ 4 ] Rastreo de usuario / Escaneo de mutación   ← v1.2.0: Subproceso de mutación fusionado
[ 5 ] Consulta WHOIS de dominio
[ 6 ] Registros MX de dominio
[ 7 ] Verificación de validez de correo
[ 8 ] Enumeración de subdominios              ← v1.3.0: Nuevo
[ 9 ] Enumeración de correos de dominio       ← v1.4.0: Nuevo (Extracción de correos OSINT)
[ 10 ] Cambiar idioma / Language              ← v1.4.0: Movido a [10]
[ 0 ] Salir

 [ + ] Selecciona una función :

 (Introduce 0 o pulsa Enter en cualquier subfunción para volver a este menú)
```

> **Flujo del menú:**
> - `[4]` Usuario: Primero selecciona estrategia (escaneo directo / mutación+escaneo / solo mutación) → modo de escaneo → recursivo opcional
> - `[8]` Subdominio: Introduce dominio → selecciona si hacer probe HTTP → retroalimentación en tiempo real en 4 fases (fuentes pasivas → wildcard → DNS → probe)
> - `[9]` Correo de dominio: Introduce dominio → selecciona si incluir subdominios activos → generación de nombres por patrón opcional → verificación SMTP opcional
> - Al guardar informe aparece menú numérico `[1-8]` de formatos + directorio por defecto (v1.8.0: código fuente → raíz proyecto/Downloads/, empaquetado → ~/Downloads/spyeyes/), permite guardar múltiples formatos consecutivos
> - **Cualquier paso de entrada** pulsar Enter o `0` devuelve al menú principal (nuevo en v1.3.2)

### 2️⃣ Modo línea de comandos (amigable para scripts)

```bash
# Uso básico
python3 -m spyeyes <subcommand> <args...> [--json] [--save DIR] [--no-color]

# Integración con jq (procesamiento por tuberías)
python3 -m spyeyes ip 8.8.8.8 --json | jq -r '.country'
python3 -m spyeyes phone +8613800138000 --json | jq -r '.location'

# Consulta por lotes de IP
for ip in 8.8.8.8 1.1.1.1 9.9.9.9; do
  python3 -m spyeyes ip "$ip" --json | jq -r '.ip + " -> " + .country'
done

# Guardar automáticamente todos los resultados de consulta
mkdir -p results
python3 -m spyeyes user torvalds --save results
python3 -m spyeyes mx gmail.com --save results
```

### 3️⃣ Tutorial completo

Para explicaciones más detalladas de funciones, solución de problemas de instalación y descripción de parámetros, consulta:

📖 **[TUTORIAL.md — Tutorial de uso detallado](docs/TUTORIAL.md)**

---

## 📊 Formatos de informe (8 tipos)

Se distribuye automáticamente según la extensión de `--save <archivo>`, todos los formatos siguen el idioma de la UI actual (zh/en):

| Formato | Extensión | Implementación | Casos de uso |
|---|---|---|---|
| **JSON** | `.json` | stdlib | Tuberías, scripts, integración API |
| **Markdown** | `.md` | stdlib (con escape de inyección) | GitHub Issue, notas, wiki |
| **HTML** | `.html` | stdlib + CSS embebido | Navegador, adjuntos de correo, informes externos |
| **PDF** | `.pdf` | reportlab (opcional `[pdf]`) | Informes formales, archivo |
| **TXT** | `.txt` | stdlib | Copiar/pegar a ticket / IM / correo |
| **CSV** | `.csv` | csv stdlib + protección contra inyección de fórmulas Excel | Excel / Google Sheets / pandas |
| **XMind** | `.xmind` | zipfile + xml stdlib | Mapa mental (compatible XMind 8) |
| **Graph** | `.graph.html` | D3.js v7 (CDN) | Gráfico de relación de fuerza dirigida, clic para navegar |

```bash
# Distribución automática por extensión, los 8 formatos funcionan:
python3 -m spyeyes user torvalds --save report.html
python3 -m spyeyes user torvalds --save report.xmind
python3 -m spyeyes user torvalds --save report.graph.html
```

**Modo interactivo:** Al seleccionar "Guardar informe → Sí", aparece un menú numérico `[1] JSON ... [8] Graph`. La ruta por defecto sigue el enrutamiento inteligente v1.8.0 (código fuente → `<raíz>/Downloads/`, pip/brew → `~/Downloads/spyeyes/`, anulable con `SPYEYES_REPORTS_DIR=path`). Tras guardar, pregunta "¿Guardar en otro formato?" para salida continua.

> **Seguridad:** HTML / Graph usa `_html_escape` contra XSS; CSV antepone `'` si la celda empieza con `= + - @ \t \r` para prevenir inyección de fórmulas Excel/Sheets; en Graph, `</` en JSON embebido se escapa a `<\/` para prevenir inyección `</script>`.

> **Nota:**
> - `--save DIR/` (formato directorio, termina en `/` o ya existe) fuerza salida **JSON**, archivado por marca de tiempo; para elegir formato usa una ruta de archivo específica como `--save report.html`
> - **El contenido del informe sigue `--lang`** — Los encabezados CSV también se localizan (UI en chino exporta `Categoría,Plataforma,URL,Estado`). Para scripts downstream que requieren nombres de columna estables (pandas/jq), usa `--lang en` o lee directamente JSON

---

## 🧪 Pruebas

```bash
# Instalar dependencias de prueba
pip install pytest pytest-cov

# Ejecutar todas las pruebas
pytest tests/ -v

# Con informe de cobertura
pytest tests/ --cov=. --cov-report=term-missing
```

Cobertura actual de pruebas:
- ✅ **306 pruebas**, finaliza en 0.6s (cobertura completa v1.2.0)
- ✅ Cubre funciones puras + mock HTTP + condiciones límite + defensa SSRF/ReDoS + 8 formatos de informe × 2 idiomas
- ✅ GitHub Actions prueba automáticamente en macOS / Ubuntu / **Windows** × Python 3.10-3.13
- ✅ Job de lint independiente (ruff + mypy + bandit)

```bash
# Instalar dependencias de ejecución + pruebas
pip install -r requirements-dev.txt
```

---

## 📁 Estructura del proyecto

```
SpyEyes/
├── spyeyes/                    # Paquete principal (desde v1.0.0)
│   ├── __init__.py             # Código principal (incluye todas las funciones + i18n + __version__)
│   ├── __main__.py             # Entrada para python -m spyeyes
│   └── data/platforms.json     # Base de datos de 3164 plataformas (fusionada Maigret + Sherlock + WhatsMyName)
├── README.md                   # Lo que estás leyendo ahora (entrada en chino)
├── README.en.md                # English entry
├── LICENSE                     # Apache 2.0
├── NOTICE                      # Declaración de derechos de autor
├── requirements.txt            # Dependencias de ejecución
├── requirements-dev.txt        # Dependencias de desarrollo/pruebas (pytest, ruff, mypy, bandit)
├── docs/                       # 📚 Toda la documentación
│   ├── TUTORIAL.md             # Tutorial detallado
│   ├── CHANGELOG.md            # Registro de cambios por versión
│   ├── CONTRIBUTING.md         # Guía de contribución
│   └── SECURITY.md             # Política de seguridad
├── tools/
│   └── build_platforms.py      # Script de reconstrucción de base de datos de plataformas (obtiene lo último upstream, escritura atómica + reintentos)
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Fixture autouse (aislamiento de estado global)
│   ├── test_spyeyes.py         # Pruebas de funciones principales (220)
│   └── test_build_platforms.py # Pruebas de herramientas de construcción (40)
├── .github/
│   ├── workflows/ci.yml        # CI GitHub Actions (job de lint + matriz multi OS × multi Python)
│   ├── ISSUE_TEMPLATE/         # Plantillas de issue para bug / funcionalidad
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml          # Actualización automática de dependencias
```

---

## 🎯 Casos de uso

- 🛡 **Equipo Azul empresarial / SOC**: Analizar origen de IPs sospechosas, investigar dominios de phishing
- 🎯 **Equipo Rojo / Pruebas de penetración**: Consultas rápidas en fase de recopilación de información
- 🏆 **CTF / Competencias OSINT**: Herramienta de resolución rápida
- 🕵 **Investigación de seguridad**: Análisis por lotes de atribución IP, reputación de dominio
- 📞 **Identificación de números fraudulentos**: Determinar procedencia y operadora de llamadas desconocidas
- 📧 **Marketing por correo**: Prefiltrado de validez de listas de correos
- 🌍 **Investigación personal**: Verificar salida VPN, revisar configuración DNS

---

## 📈 Historial de Stars

[![Star History Chart](https://api.star-history.com/svg?repos=Akxan/SpyEyes&type=Date)](https://star-history.com/#Akxan/SpyEyes&Date)

---

## 🤝 Contribución

¡Bienvenidos PR, Issues y Stars!

Por favor, lee primero [CONTRIBUTING.md](docs/CONTRIBUTING.md) para conocer el flujo de desarrollo y las normas de código.

<a href="https://github.com/Akxan/SpyEyes/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Akxan/SpyEyes" />
</a>

---

## 📄 Licencia

Este proyecto es de código abierto bajo **[Apache License 2.0](LICENSE)**.

Apache 2.0 añade a MIT **licencia de patentes explícita** y **protección de marca registrada**, siendo más seguro para desarrollo secundario y uso comercial.

Cualquier persona puede usarlo, modificarlo y distribuirlo libremente, incluido uso comercial, pero debe conservar la declaración de derechos de autor.

---

## 🙏 Agradecimientos

- 🌟 **[Google libphonenumber](https://github.com/google/libphonenumber)** — Librería de números de teléfono más autorizada del sector
- 🌟 **[ipwho.is](https://ipwho.is/)** — API de geolocalización IP gratuita, estable y rica en información
- 🌟 **[ipify.org](https://www.ipify.org/)** — Servicio de consulta de IP local sencillo
- 🌟 Todos los desarrolladores que contribuyen a herramientas de seguridad de código abierto ❤️

---

## ⚠️ Descargo de responsabilidad

Esta herramienta es solo para escenarios de **investigación de seguridad legal, autoevaluación, CTF y educación**.

❌ **Prohibido** para:
- Rastrear, acosar o hacer doxxing a cualquier persona
- Escaneo o intrusión de red no autorizados
- Recopilar para beneficio comercial o actividades ilegales

✅ **Permitido**:
- Autoevaluación de seguridad de activos propios
- Pruebas de penetración bajo autorización escrita
- Consultas legales de información totalmente pública
- Educación, investigación, contribución a código abierto

El usuario asume toda la responsabilidad legal. Consulte [TUTORIAL.md - Advertencias legales y éticas](docs/TUTORIAL.md#法律与道德提醒).

---

## 🔍 Palabras clave / Keywords

`OSINT` `Recopilación de información` `Rastreo IP` `Consulta de teléfono` `Búsqueda de usuario` `WHOIS` `Registros MX` `Verificación de correo` `Enumeración de subdominios` `Extracción de correos de dominio` `Transparencia de certificados` `Ciberseguridad` `Pruebas de penetración` `Herramienta CTF` `OSINT Python` `Herramienta OSINT en chino` `osint-tool` `ip-tracker` `phone-tracker` `username-search` `whois-lookup` `dns-lookup` `email-verification` `subdomain-enumeration` `subdomain-finder` `email-harvester` `crtsh` `certspotter` `certificate-transparency` `cybersecurity` `reconnaissance` `red-team` `blue-team` `pentest` `ctf`

---

<div align="center">

**¡Si este proyecto te ha sido útil, dale un ⭐ Star para animarnos!**

[⬆ Volver al inicio](#-spyeyes)

</div>
