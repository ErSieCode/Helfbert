# Assistenzsystem für Sehbehinderte: Vollständige Installationsanleitung

## Inhaltsverzeichnis
1. [Systemübersicht](#1-systemübersicht)
2. [Systemanforderungen](#2-systemanforderungen)
3. [Windows-Vorbereitung](#3-windows-vorbereitung)
4. [Python-Installation](#4-python-installation)
5. [CUDA-Installation (für GPU-Unterstützung)](#5-cuda-installation-für-gpu-unterstützung)
6. [Projektstruktur einrichten](#6-projektstruktur-einrichten)
7. [Abhängigkeiten installieren](#7-abhängigkeiten-installieren)
8. [Browser-Treiber für die Automatisierung](#8-browser-treiber-für-die-automatisierung)
9. [Konfigurationsdateien erstellen](#9-konfigurationsdateien-erstellen)
10. [Modelle herunterladen](#10-modelle-herunterladen)
11. [Audioressourcen erstellen](#11-audioressourcen-erstellen)
12. [Wissensbasis initialisieren](#12-wissensbasis-initialisieren)
13. [Systemberechtigungen einrichten](#13-systemberechtigungen-einrichten)
14. [Firewall-Konfiguration](#14-firewall-konfiguration)
15. [Erster Start und Tests](#15-erster-start-und-tests)
16. [Desktop-Verknüpfung und Autostart](#16-desktop-verknüpfung-und-autostart)
17. [Ressourcenmanagement und Updates](#17-ressourcenmanagement-und-updates)
18. [Mobile App (optional)](#18-mobile-app-optional)
19. [Fehlerbehebung](#19-fehlerbehebung)
20. [Sicherung und Wiederherstellung](#20-sicherung-und-wiederherstellung)
21. [Weiterführende Anpassungen](#21-weiterführende-anpassungen)

## 1. Systemübersicht

Das Assistenzsystem für Sehbehinderte ist eine modulare Software-Lösung, die folgende Hauptfunktionen bietet:

- **Erweiterte Bildschirmlupe** mit intelligenter Vergrößerung und Fokussierung
- **Natürliche Sprachsteuerung** für Windows und Webbrowser
- **Intelligentes Vorlesen** von Bildschirminhalten und Webseiten
- **Automatische Erkennung und Beschreibung** von Bildern (sowohl Bildschirm als auch Kamera)
- **Prozessautomatisierung** für häufig verwendete Abläufe

Die Architektur besteht aus fünf Kernmodulen:

1. **Orchestrator**: Zentraler Koordinator aller Module
2. **Hirn-Modul**: KI-basierte Entscheidungsfindung und Sprachverständnis
3. **Stimme/Ohren-Modul**: Spracherkennung und Sprachausgabe
4. **Augen-Modul**: Bildschirmanalyse und Bildverarbeitung
5. **Digitalsinn-Modul**: Interaktion mit Software und Webseiten

Alle Module sind über einen Event-Bus verbunden und können auf einem einzelnen System oder verteilt auf mehreren Geräten betrieben werden.

## 2. Systemanforderungen

### Minimale Anforderungen:
- **Betriebssystem**: Windows 10 (64-Bit), Build 1909 oder höher
- **Prozessor**: Intel i5 (7. Generation) oder AMD Ryzen 5 oder höher
- **Arbeitsspeicher**: 8 GB RAM
- **Festplattenspeicher**: 10 GB freier Speicherplatz
- **Netzwerk**: Internetverbindung für die Installation
- **Audio**: Funktionierendes Mikrofon und Lautsprecher/Kopfhörer

### Empfohlene Anforderungen:
- **Prozessor**: Intel i7 (10. Generation) oder AMD Ryzen 7 oder höher
- **Arbeitsspeicher**: 16 GB RAM
- **Grafikkarte**: NVIDIA GeForce RTX 2060 oder höher (6 GB VRAM)
- **Festplattenspeicher**: 20 GB freier SSD-Speicherplatz
- **Audio**: Qualitatives Mikrofon und Lautsprecher

### Zusätzliche Anforderungen für Mobile-Integration:
- **Smartphone**: Android 8.0 oder höher oder iOS 13 oder höher
- **LAN**: Lokales Netzwerk für die Kommunikation zwischen PC und Mobilgerät

## 3. Windows-Vorbereitung

### Systemupdates installieren
1. Öffnen Sie die Windows-Einstellungen (Windows-Taste + I)
2. Navigieren Sie zu **Update und Sicherheit > Windows Update**
3. Klicken Sie auf **Nach Updates suchen**
4. Installieren Sie alle verfügbaren Updates
5. Starten Sie Ihren Computer neu

### Windows-Funktionen aktivieren
1. Öffnen Sie die Systemsteuerung
2. Navigieren Sie zu **Programme > Programme und Features > Windows-Features aktivieren oder deaktivieren**
3. Aktivieren Sie folgende Funktionen:
   - **.NET Framework 3.5** (einschließlich 2.0 und 3.0)
   - **.NET Framework 4.8 Advanced Services**
   - **Windows-Subsystem für Linux** (optional, für Entwickler)
4. Klicken Sie auf **OK** und starten Sie den Computer bei Aufforderung neu

### Visual C++ Redistributable installieren
1. Laden Sie den aktuellen Visual C++ Redistributable herunter:
   - Besuchen Sie [https://aka.ms/vs/17/release/vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)
   - Alternativ: Suchen Sie nach "Microsoft Visual C++ Redistributable"
2. Führen Sie die heruntergeladene Datei (vc_redist.x64.exe) aus
3. Folgen Sie den Anweisungen des Installationsassistenten

## 4. Python-Installation

### Python 3.9 installieren
1. Besuchen Sie die [offizielle Python-Website](https://www.python.org/downloads/release/python-3913/)
2. Laden Sie den **Windows Installer (64-bit)** herunter
3. Starten Sie den Installer und aktivieren Sie:
   - ☑ **Add Python 3.9 to PATH**
   - ☑ **Install for all users**
4. Klicken Sie auf **Customize installation**
5. Lassen Sie alle optionalen Features aktiviert und klicken Sie auf **Next**
6. Aktivieren Sie:
   - ☑ **Install for all users**
   - ☑ **Create shortcuts for installed applications**
   - ☑ **Add Python to environment variables**
7. Ändern Sie den Installationspfad zu: **C:\Python39**
8. Klicken Sie auf **Install**

### Python-Installation überprüfen
1. Öffnen Sie die Eingabeaufforderung (cmd.exe)
2. Führen Sie folgende Befehle aus:
   ```
   python --version
   pip --version
   ```
3. Sie sollten Informationen zu Python 3.9.x und pip sehen

## 5. CUDA-Installation (für GPU-Unterstützung)

Diese Schritte sind nur erforderlich, wenn Sie eine kompatible NVIDIA-Grafikkarte haben und GPU-Beschleunigung nutzen möchten.

### NVIDIA-Treiber installieren
1. Besuchen Sie die [NVIDIA-Treiberdownload-Seite](https://www.nvidia.com/Download/index.aspx)
2. Wählen Sie Ihr Grafikkartenmodell aus und klicken Sie auf **Suchen**
3. Laden Sie den aktuellsten Treiber herunter
4. Führen Sie die heruntergeladene Datei aus und folgen Sie den Anweisungen
5. Starten Sie Ihren Computer nach der Installation neu

### CUDA Toolkit 11.7 installieren
1. Besuchen Sie die [CUDA-11.7-Download-Seite](https://developer.nvidia.com/cuda-11-7-0-download-archive)
2. Wählen Sie:
   - Operating System: **Windows**
   - Architecture: **x86_64**
   - Version: **10** oder **11**
   - Installer Type: **exe (local)**
3. Laden Sie den Installer herunter
4. Führen Sie den Installer aus und wählen Sie **Express Installation**
5. Folgen Sie den Anweisungen und starten Sie nach Abschluss den Computer neu

### cuDNN installieren
1. Erstellen Sie einen kostenlosen Account auf der [NVIDIA-Developer-Website](https://developer.nvidia.com/)
2. Besuchen Sie die [cuDNN-Download-Seite](https://developer.nvidia.com/cudnn)
3. Laden Sie cuDNN für CUDA 11.x herunter
4. Entpacken Sie die heruntergeladene ZIP-Datei
5. Kopieren Sie die Dateien in die entsprechenden CUDA-Verzeichnisse:
   - Kopieren Sie `cuda\bin\*.dll` nach `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin`
   - Kopieren Sie `cuda\include\*.h` nach `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\include`
   - Kopieren Sie `cuda\lib\x64\*.lib` nach `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\lib\x64`

### Umgebungsvariablen überprüfen
1. Öffnen Sie **Systemsteuerung > System und Sicherheit > System > Erweiterte Systemeinstellungen**
2. Klicken Sie auf **Umgebungsvariablen**
3. Prüfen Sie unter "Systemvariablen", ob folgende Einträge vorhanden sind:
   - `CUDA_PATH`: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7`
   - `Path` enthält diese Einträge:
     - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin`
     - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\libnvvp`
4. Falls nicht, fügen Sie sie hinzu

## 6. Projektstruktur einrichten

### Hauptprojektverzeichnis erstellen
1. Öffnen Sie die Eingabeaufforderung (cmd.exe) als Administrator
2. Führen Sie folgende Befehle aus:
   ```batch
   cd C:\
   mkdir AssistenzSystem
   cd AssistenzSystem
   ```

### Virtuelle Python-Umgebung erstellen
1. Führen Sie in der Eingabeaufforderung Folgendes aus:
   ```batch
   python -m venv venv
   venv\Scripts\activate
   ```

### Verzeichnisstruktur anlegen
1. Führen Sie folgende Befehle aus, um die Verzeichnisstruktur zu erstellen:
   ```batch
   mkdir assistant
   mkdir assistant\modules
   mkdir assistant\common
   mkdir assistant\services
   mkdir assistant\adapters
   mkdir assistant\utils
   mkdir config
   mkdir models
   mkdir models\llm
   mkdir models\stt
   mkdir models\tts
   mkdir models\vision
   mkdir models\wake_word
   mkdir data
   mkdir data\cache
   mkdir data\cache\tts
   mkdir data\embeddings
   mkdir data\knowledge
   mkdir data\sounds
   mkdir logs
   mkdir scripts
   mkdir backups
   mkdir drivers
   ```

## 7. Abhängigkeiten installieren

### Anforderungsdatei erstellen
1. Erstellen Sie eine Datei `C:\AssistenzSystem\requirements.txt` mit folgendem Inhalt:
   ```
   # Kernabhängigkeiten
   numpy==1.23.5
   torch==1.13.1+cu117
   torchaudio==0.13.1
   torchvision==0.14.1
   opencv-python==4.7.0.72
   pillow==9.4.0
   sounddevice==0.4.6
   soundfile==0.12.1
   librosa==0.10.0
   psutil==5.9.5

   # Module und Dienste
   transformers==4.28.1
   tokenizers==0.13.3
   sentence-transformers==2.2.2
   whisper==1.0.0
   pytesseract==0.3.10
   pyttsx3==2.90
   pywinauto==0.6.8
   SpeechRecognition==3.10.0
   pvporcupine==2.2.0

   # Event-Bus und Kommunikation
   pyzmq==25.0.2
   websockets==11.0.2
   protobuf==4.22.3
   grpcio==1.54.0
   grpcio-tools==1.54.0

   # Browser-Automatisierung
   selenium==4.9.1
   webdriver-manager==3.8.6

   # Hilfsbibliotheken
   pyyaml==6.0
   tqdm==4.65.0
   requests==2.28.2
   python-dotenv==1.0.0
   colorama==0.4.6
   imagehash==4.3.1

   # Logging und Monitoring
   loguru==0.7.0

   # Windows-spezifische Abhängigkeiten
   pywin32==306
   python-magic-bin==0.4.14
   desktop-duplication==0.1.0
   ```

### Abhängigkeiten installieren
1. Stellen Sie sicher, dass Sie sich im Projektverzeichnis befinden und die virtuelle Umgebung aktiviert ist:
   ```batch
   cd C:\AssistenzSystem
   venv\Scripts\activate
   ```

2. Installieren Sie die Abhängigkeiten:
   ```batch
   pip install -r requirements.txt
   ```

3. Installieren Sie PyTorch mit CUDA-Unterstützung:
   ```batch
   pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
   ```

### Tesseract OCR installieren
1. Laden Sie den [Tesseract-Installer für Windows](https://github.com/UB-Mannheim/tesseract/wiki) herunter (64-bit Version)
2. Führen Sie den Installer aus
3. Wählen Sie als Installationspfad: `C:\Program Files\Tesseract-OCR`
4. Aktivieren Sie die Option **Add to PATH**
5. Installieren Sie zusätzlich zu Englisch mindestens die deutsche Sprache
6. Schließen Sie die Installation ab

## 8. Browser-Treiber für die Automatisierung

### ChromeDriver installieren
1. Überprüfen Sie Ihre Chrome-Version:
   - Öffnen Sie Chrome
   - Klicken Sie auf die drei Punkte (⋮) oben rechts
   - Wählen Sie **Hilfe > Über Google Chrome**
   - Notieren Sie die Versionsnummer (z.B. 91.0.4472.124)

2. Laden Sie den passenden ChromeDriver herunter:
   - Besuchen Sie [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   - Wählen Sie die Version, die mit Ihrer Chrome-Version übereinstimmt
   - Laden Sie die Windows-Version herunter

3. Installieren Sie den ChromeDriver:
   - Entpacken Sie die heruntergeladene ZIP-Datei
   - Kopieren Sie `chromedriver.exe` nach `C:\AssistenzSystem\drivers`

### Systemumgebungsvariable aktualisieren
1. Öffnen Sie **Systemsteuerung > System und Sicherheit > System > Erweiterte Systemeinstellungen**
2. Klicken Sie auf **Umgebungsvariablen**
3. Bearbeiten Sie unter "Systemvariablen" die Variable `Path`
4. Klicken Sie auf **Neu** und fügen Sie `C:\AssistenzSystem\drivers` hinzu
5. Bestätigen Sie mit **OK**

## 9. Konfigurationsdateien erstellen

Erstellen Sie die folgenden Konfigurationsdateien im Verzeichnis `C:\AssistenzSystem\config\`:

### orchestrator.yaml
```yaml
# config/orchestrator.yaml
server:
  host: "0.0.0.0"
  port: 5555

modules:
  brain_module:
    enabled: true
    class: "assistant.modules.brain_module.BrainModule"
    config_path: "./config/brain_module.yaml"
  
  voice_module:
    enabled: true
    class: "assistant.modules.voice_module.VoiceModule"
    config_path: "./config/voice_module.yaml"
  
  vision_module:
    enabled: true
    class: "assistant.modules.vision_module.VisionModule"
    config_path: "./config/vision_module.yaml"
  
  digital_module:
    enabled: true
    class: "assistant.modules.digital_module.DigitalModule"
    config_path: "./config/digital_module.yaml"
  
  mobile_module:
    enabled: false  # Standard: deaktiviert, bei Bedarf aktivieren
    class: "assistant.modules.mobile_module.MobileModule"
    config_path: "./config/mobile_module.yaml"

event_bus:
  publisher_port: 5555
  distributed_mode: false
  history_enabled: true
  history_size: 100
  remote_nodes: []  # Für verteilte Systeme

resources:
  cpu_allocation_strategy: "dynamic"
  memory_allocation_strategy: "dynamic"
  gpu_allocation_enabled: true
  gpu_allocation_strategy: "priority_based"
  default_gpu_device: 0

monitoring:
  enabled: true
  check_interval_seconds: 30
  restart_unhealthy_modules: true
  log_level: "info"

mobile_api:
  enabled: false
  host: "0.0.0.0"
  port: 8080
  allowed_origins: ["*"]
  auth_required: false
```

### brain_module.yaml
```yaml
# config/brain_module.yaml
language_model:
  model_path: "./models/llm/llama3-8b-q4.gguf"
  model_type: "llama"
  context_window_size: 4096
  max_generation_tokens: 512
  temperature: 0.7
  top_p: 0.9
  quantization: "4bit"
  device: "auto"  # "auto", "cuda", "cpu"
  num_gpu_layers: -1  # -1 = alle Schichten auf GPU, wenn verfügbar

reasoning_model:
  enabled: true
  model_name: "huggingface/qwen-reasoning"
  model_path: "./models/llm/qwen-reasoning-q4.gguf"
  max_length: 512
  temperature: 0.7
  use_cache: true

inference:
  batch_size: 1
  stream_output: true
  use_flash_attention: true
  kv_cache_enabled: true

memory:
  short_term_capacity: 10
  long_term_enabled: true
  embeddings_model: "sentence-transformers/all-MiniLM-L6-v2"
  storage_path: "./data/embeddings"

context:
  max_entries: 10
  include_system_info: true
  include_date_time: true

cache:
  enabled: true
  max_size: 100
  ttl_seconds: 3600

knowledge:
  path: "./data/knowledge"
  system_info:
    system_name: "Assistenzsystem für Sehbehinderte"
    version: "1.0.0"
    capabilities:
      - "Bildschirmlupe mit intelligenter Vergrößerung"
      - "Sprachsteuerung für Windows und Browser"
      - "Vorlesen von Bildschirminhalten und Webseiten"
      - "Erkennung und Beschreibung von Bildern"
      - "Automatisierung häufiger Abläufe"
```

### voice_module.yaml
```yaml
# config/voice_module.yaml
audio:
  sample_rate: 16000
  frame_length: 512
  buffer_seconds: 3
  channels: 1
  volume_step: 10

speech_recognition:
  model: "whisper-small"
  language: "de"
  device: "auto"  # "auto", "cuda", "cpu"
  vad_enabled: true
  noise_suppression_level: 2
  sample_rate: 16000
  stream_mode: true

wake_word:
  enabled: true
  engine: "porcupine"  # "porcupine", "snowboy", "custom"
  model_path: "./models/wake_word/porcupine_params.pv"
  sensitivity: 0.5
  keywords:
    - "assistent"
    - "computer"
  language: "de"
  always_listening: true

text_to_speech:
  engine: "pyttsx3"  # "espeak", "pyttsx3", "coqui_tts", "system"
  voice: "de"
  rate: 0
  volume: 100
  pitch: 0
  use_cache: true
  cache_dir: "./data/cache/tts"

audio_feedback:
  enabled: true
  volume: 80
  sounds:
    activation: "./data/sounds/activation.wav"
    acknowledgement: "./data/sounds/acknowledgement.wav"
    error: "./data/sounds/error.wav"
    success: "./data/sounds/success.wav"
```

### vision_module.yaml
```yaml
# config/vision_module.yaml
screen_analysis:
  enabled: true
  update_interval_ms: 500
  capture_method: "win32api"  # "win32api", "mss", "pillow"
  region_of_interest_tracking: true
  detect_ui_elements: true
  continuous_analysis: true
  max_fps: 5

ocr:
  enabled: true
  engine: "tesseract"  # "tesseract", "easyocr", "paddleocr"
  language: "deu"
  continuous_analysis: true
  confidence_threshold: 0.6
  cache_enabled: true
  max_cache_size: 20
  use_gpu: true
  device: "auto"  # "auto", "cuda", "cpu"
  tesseract_path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Pfad zu Tesseract

magnifier:
  enabled: true
  default_zoom: 2.0
  max_zoom: 8.0
  min_zoom: 1.5
  zoom_step: 0.5
  smooth_zoom: true
  focus_tracking: true
  highlight_interactive_elements: true
  border_color: "#FF0000"
  border_width: 2
  auto_focus_elements:
    - "text"
    - "button"
    - "input"

camera:
  enabled: false
  device_id: 0
  resolution:
    width: 1280
    height: 720
  fps: 30
  auto_focus: true
  save_dir: "./data/camera"

image_understanding:
  enabled: true
  model: "clip"  # "clip", "vit", "blip"
  model_path: "./models/vision/clip-vit-large-patch14"
  device: "auto"  # "auto", "cuda", "cpu"
  max_resolution: 1024
  output_detail_level: "medium"  # "low", "medium", "high"
  response_language: "de"
```

### digital_module.yaml
```yaml
# config/digital_module.yaml
browser_automation:
  enabled: true
  browser: "chrome"  # "chrome", "firefox", "edge"
  headless: false
  webdriver_path: "C:\\AssistenzSystem\\drivers\\chromedriver.exe"
  user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  wait_timeout_seconds: 20
  navigation_timeout_seconds: 30
  max_pages: 5
  download_dir: "./data/downloads"
  cache_enabled: true
  speak_summary: true
  max_recent_pages: 10
  default_browser_args:
    - "--disable-extensions"
    - "--disable-notifications"

system_automation:
  enabled: true
  default_timeout_seconds: 10
  allowed_applications:
    - "notepad.exe"
    - "wordpad.exe"
    - "mspaint.exe"
    - "calc.exe"
  allowed_commands:
    - "explorer"
    - "control"
  permission_required_for_unknown: true

ui_automation:
  enabled: true
  framework: "pywinauto"  # "pywinauto", "uiautomation", "javafx"
  element_wait_timeout_ms: 5000
  click_delay_ms: 100
  typing_delay_ms: 30
  highlight_elements: true
  highlight_color: "#00FF00"
  highlight_duration_ms: 500
  cache_ui_elements: true
  cache_timeout_seconds: 60

process_automation:
  enabled: true
  max_processes: 50
  max_steps_per_process: 100
  storage_path: "./data/processes"
  auto_save_recordings: true
  process_timeout_seconds: 300
  retry_on_error: true
  max_retries: 3
```

### mobile_module.yaml (optional)
```yaml
# config/mobile_module.yaml
server_name: "Assistenzsystem"
host: "0.0.0.0"
port: 8080
protocol: "websocket"  # "websocket", "http", "mqtt"
ssl:
  enabled: false
  cert_path: "./certs/server.crt"
  key_path: "./certs/server.key"

authentication:
  enabled: false
  method: "token"  # "token", "basic", "oauth"
  token_expiry_hours: 24
  allowed_devices:
    - device_id: "*"  # Alle Geräte erlauben

camera:
  max_resolution: 1280x720
  quality: 80
  allowed_formats:
    - "jpg"
    - "png"
  max_frame_rate: 15
  stream_timeout_seconds: 300

voice:
  max_audio_duration_seconds: 30
  allowed_formats:
    - "wav"
    - "mp3"
    - "ogg"
  auto_transcribe: true

notifications:
  enabled: true
  max_per_minute: 10
  vibration_enabled: true
  sound_enabled: true

privacy:
  data_retention_days: 1
  audio_retention_enabled: false
  image_retention_enabled: false
  location_tracking_enabled: false
```

### logging.yaml
```yaml
# config/logging.yaml
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
  detailed:
    format: "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: standard
    stream: ext://sys.stdout

  file:
    class: logging.handlers.RotatingFileHandler
    level: DEBUG
    formatter: detailed
    filename: ./logs/assistant.log
    maxBytes: 10485760  # 10 MB
    backupCount: 5
    encoding: utf8

  error_file:
    class: logging.handlers.RotatingFileHandler
    level: ERROR
    formatter: detailed
    filename: ./logs/error.log
    maxBytes: 10485760  # 10 MB
    backupCount: 5
    encoding: utf8

loggers:
  orchestrator:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  brain_module:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  voice_module:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  vision_module:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  digital_module:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  mobile_module:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

  event_bus:
    level: INFO
    handlers: [console, file, error_file]
    propagate: false

root:
  level: WARNING
  handlers: [console, file, error_file]
  propagate: false
```

## 10. Modelle herunterladen

### Download-Skript erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\download_models.py`:

```python
# scripts/download_models.py
import os
import sys
import requests
from tqdm import tqdm
import zipfile
import tarfile
import gzip
import shutil
import torch
from transformers import AutoTokenizer, AutoModel
from huggingface_hub import hf_hub_download
import whisper

# Pfade definieren
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
LLM_DIR = os.path.join(MODELS_DIR, "llm")
STT_DIR = os.path.join(MODELS_DIR, "stt")
TTS_DIR = os.path.join(MODELS_DIR, "tts")
VISION_DIR = os.path.join(MODELS_DIR, "vision")
WAKE_WORD_DIR = os.path.join(MODELS_DIR, "wake_word")

# URLs für die Modelle
MODEL_URLS = {
    "llama3-8b-q4.gguf": "https://huggingface.co/TheBloke/Llama-3-8B-GGUF/resolve/main/llama-3-8b.Q4_K_M.gguf",
    "qwen-reasoning-q4.gguf": "https://huggingface.co/TheBloke/Qwen1.5-0.5B-Chat-GGUF/resolve/main/qwen1.5-0.5b-chat.Q4_K_M.gguf",
    "wake_word": "https://github.com/Picovoice/porcupine/archive/refs/tags/v2.2.0.zip",
    "clip-vit": "CLIP"  # Spezialfall für Hugging Face
}

def download_file(url, destination, filename=None):
    """Eine Datei von URL herunterladen mit Fortschrittsanzeige"""
    if filename is None:
        filename = os.path.basename(url)
    
    filepath = os.path.join(destination, filename)
    
    # Verzeichnis erstellen, falls es nicht existiert
    os.makedirs(destination, exist_ok=True)
    
    # Prüfen, ob die Datei bereits existiert
    if os.path.exists(filepath):
        print(f"Datei {filename} existiert bereits in {destination}")
        return filepath
    
    # Datei herunterladen
    print(f"Lade {filename} herunter...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    
    with open(filepath, "wb") as file, tqdm(
        desc=filename,
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
    
    return filepath

def extract_archive(filepath, destination):
    """Extrahiert ein Archiv (ZIP, TAR, TGZ, etc.)"""
    print(f"Entpacke {filepath}...")
    
    if filepath.endswith(".zip"):
        with zipfile.ZipFile(filepath, "r") as zip_ref:
            zip_ref.extractall(destination)
    
    elif filepath.endswith((".tar.gz", ".tgz")):
        with tarfile.open(filepath, "r:gz") as tar_ref:
            tar_ref.extractall(destination)
    
    elif filepath.endswith(".tar"):
        with tarfile.open(filepath, "r") as tar_ref:
            tar_ref.extractall(destination)
    
    elif filepath.endswith(".gz") and not filepath.endswith(".tar.gz"):
        with gzip.open(filepath, "rb") as f_in:
            with open(filepath[:-3], "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
    
    print(f"Archiv {filepath} erfolgreich entpackt")

def download_huggingface_model(model_name, destination):
    """Ein Modell von Hugging Face herunterladen"""
    print(f"Lade Hugging Face-Modell {model_name} herunter...")
    
    # Verzeichnis erstellen, falls es nicht existiert
    os.makedirs(destination, exist_ok=True)
    
    # Tokenizer und Modell herunterladen
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    # Modell und Tokenizer speichern
    tokenizer.save_pretrained(destination)
    model.save_pretrained(destination)
    
    print(f"Hugging Face-Modell {model_name} erfolgreich heruntergeladen und gespeichert")

def download_whisper_model(model_name, destination):
    """Whisper-Modell herunterladen"""
    print(f"Lade Whisper-Modell {model_name} herunter...")
    
    # Verzeichnis erstellen, falls es nicht existiert
    os.makedirs(destination, exist_ok=True)
    
    # Modell herunterladen
    model = whisper.load_model(model_name)
    
    print(f"Whisper-Modell {model_name} erfolgreich heruntergeladen")
    return model

def main():
    """Hauptfunktion zum Herunterladen aller Modelle"""
    print("Starte Download der Modelle...")
    
    # Verzeichnisse erstellen
    os.makedirs(LLM_DIR, exist_ok=True)
    os.makedirs(STT_DIR, exist_ok=True)
    os.makedirs(TTS_DIR, exist_ok=True)
    os.makedirs(VISION_DIR, exist_ok=True)
    os.makedirs(WAKE_WORD_DIR, exist_ok=True)
    
    # LLM-Modelle herunterladen
    download_file(MODEL_URLS["llama3-8b-q4.gguf"], LLM_DIR)
    download_file(MODEL_URLS["qwen-reasoning-q4.gguf"], LLM_DIR)
    
    # Wake-Word-Modell herunterladen und extrahieren
    wake_word_zip = download_file(MODEL_URLS["wake_word"], WAKE_WORD_DIR)
    extract_archive(wake_word_zip, WAKE_WORD_DIR)
    
    # CLIP-Modell von Hugging Face herunterladen
    download_huggingface_model("openai/clip-vit-large-patch14", os.path.join(VISION_DIR, "clip-vit-large-patch14"))
    
    # MiniLM (für Einbettungen) herunterladen
    download_huggingface_model("sentence-transformers/all-MiniLM-L6-v2", os.path.join(MODELS_DIR, "embeddings"))
    
    # Whisper-Modell herunterladen
    download_whisper_model("small", STT_DIR)
    
    print("Alle Modelle wurden erfolgreich heruntergeladen und installiert.")

if __name__ == "__main__":
    main()
```

### Start-Skript erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\start.py`:

```python
# scripts/start.py
import os
import sys
import argparse
import logging
import logging.config
import yaml
import time
import importlib.util
import threading

# Pfad zum Hauptverzeichnis hinzufügen
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

def load_logging_config():
    """Lädt die Logging-Konfiguration"""
    logging_config_path = os.path.join(BASE_DIR, "config", "logging.yaml")
    
    if os.path.exists(logging_config_path):
        with open(logging_config_path, 'r') as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
    else:
        # Standardkonfiguration, falls keine Konfigurationsdatei vorhanden
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(os.path.join(BASE_DIR, "logs", "assistant.log"))
            ]
        )

def check_dependencies():
    """Überprüft, ob alle erforderlichen Abhängigkeiten installiert sind"""
    logger = logging.getLogger("startup")
    
    # Prüfen, ob Python-Packages installiert sind
    required_packages = [
        "torch", "numpy", "zmq", "websockets", "protobuf", 
        "pyyaml", "tqdm", "pyttsx3", "whisper", "pytesseract"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
    
    if missing_packages:
        logger.error(f"Fehlende Abhängigkeiten: {', '.join(missing_packages)}")
        logger.error("Bitte installieren Sie die fehlenden Abhängigkeiten mit: pip install -r requirements.txt")
        return False
    
    # Prüfen, ob Tesseract installiert ist
    if importlib.util.find_spec("pytesseract") is not None:
        import pytesseract
        try:
            pytesseract.get_tesseract_version()
        except Exception:
            logger.error("Tesseract OCR ist nicht installiert oder nicht im PATH")
            logger.error("Bitte installieren Sie Tesseract OCR und stellen Sie sicher, dass es im PATH ist")
            return False
    
    return True

def monitor_resources():
    """Überwacht und beschränkt Ressourcennutzung"""
    import psutil
    import time
    logger = logging.getLogger("resources")
    
    # Maximale Ressourcennutzung
    MAX_CPU_PERCENT = 85
    MAX_MEMORY_PERCENT = 80
    
    while True:
        # CPU-Auslastung prüfen
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        
        if cpu_percent > MAX_CPU_PERCENT:
            logger.warning(f"Hohe CPU-Auslastung: {cpu_percent}%")
            # Hier könnten Maßnahmen zur Drosselung implementiert werden
        
        if memory_percent > MAX_MEMORY_PERCENT:
            logger.warning(f"Hohe Speicherauslastung: {memory_percent}%")
            # Hier könnten Maßnahmen zur Speicherfreigabe implementiert werden
        
        time.sleep(5)

def start_orchestrator():
    """Startet den Orchestrator"""
    logger = logging.getLogger("startup")
    
    try:
        # Orchestrator-Modul dynamisch importieren
        spec = importlib.util.spec_from_file_location(
            "orchestrator",
            os.path.join(BASE_DIR, "assistant", "orchestrator.py")
        )
        orchestrator_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(orchestrator_module)
        
        # Orchestrator instanziieren
        orchestrator = orchestrator_module.Orchestrator(
            config_path=os.path.join(BASE_DIR, "config", "orchestrator.yaml")
        )
        
        # Orchestrator starten
        logger.info("Starte Orchestrator...")
        import asyncio
        asyncio.run(orchestrator.start())
        
        # Hauptschleife, um den Prozess am Laufen zu halten
        logger.info("Orchestrator gestartet. Drücken Sie Strg+C zum Beenden.")
        
        try:
            # Einfache Warteschleife
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Beende Orchestrator...")
            asyncio.run(orchestrator.stop())
            logger.info("Orchestrator beendet.")
    
    except Exception as e:
        logger.error(f"Fehler beim Starten des Orchestrators: {e}")
        return False
    
    return True

def main():
    """Hauptfunktion zum Starten des Assistenzsystems"""
    # Logging konfigurieren
    load_logging_config()
    logger = logging.getLogger("startup")
    
    logger.info("Starte Assistenzsystem...")
    
    # Abhängigkeiten prüfen
    if not check_dependencies():
        logger.error("Abhängigkeitsprüfung fehlgeschlagen. Starte trotzdem...")
    
    # Verzeichnisse erstellen, falls sie nicht existieren
    for directory in ["logs", "data/cache", "data/embeddings", "data/knowledge"]:
        os.makedirs(os.path.join(BASE_DIR, directory), exist_ok=True)
    
    # Ressourcenüberwachung starten
    threading.Thread(target=monitor_resources, daemon=True).start()
    
    # Orchestrator starten
    if not start_orchestrator():
        logger.error("Fehler beim Starten des Orchestrators.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Modelle herunterladen

1. Öffnen Sie die Eingabeaufforderung und navigieren Sie zum Projektverzeichnis:
   ```
   cd C:\AssistenzSystem
   venv\Scripts\activate
   ```

2. Führen Sie das Skript zum Herunterladen der Modelle aus:
   ```
   python scripts\download_models.py
   ```

3. Dieser Vorgang kann je nach Internetverbindung 20-60 Minuten dauern, da einige Modelle mehrere GB groß sind.

## 11. Audioressourcen erstellen

Erstellen Sie die folgenden Audiodateien für akustisches Feedback:

1. Erstellen Sie folgendes Python-Skript `C:\AssistenzSystem\scripts\create_sounds.py`:
   ```python
   # Create empty audio files
   import numpy as np
   import soundfile as sf
   import os

   # Create directory
   os.makedirs("C:\\AssistenzSystem\\data\\sounds", exist_ok=True)

   # Create audio files with different sounds
   sample_rate = 44100

   # Activation sound (short beep)
   t = np.linspace(0, 0.2, int(0.2 * sample_rate), False)
   activation = 0.5 * np.sin(2 * np.pi * 1000 * t)
   activation = np.concatenate([activation, np.zeros(int(0.05 * sample_rate))])
   sf.write("C:\\AssistenzSystem\\data\\sounds\\activation.wav", activation, sample_rate)
   print("Activation sound created")

   # Acknowledgement sound (double beep)
   t1 = np.linspace(0, 0.1, int(0.1 * sample_rate), False)
   t2 = np.linspace(0, 0.1, int(0.1 * sample_rate), False)
   beep1 = 0.5 * np.sin(2 * np.pi * 800 * t1)
   beep2 = 0.5 * np.sin(2 * np.pi * 1000 * t2)
   ack = np.concatenate([beep1, np.zeros(int(0.05 * sample_rate)), beep2])
   sf.write("C:\\AssistenzSystem\\data\\sounds\\acknowledgement.wav", ack, sample_rate)
   print("Acknowledgement sound created")

   # Error sound (descending tone)
   t = np.linspace(0, 0.3, int(0.3 * sample_rate), False)
   freqs = np.linspace(800, 200, len(t))
   error = 0.5 * np.sin(2 * np.pi * freqs * t / 50)
   sf.write("C:\\AssistenzSystem\\data\\sounds\\error.wav", error, sample_rate)
   print("Error sound created")

   # Success sound (ascending tone)
   t = np.linspace(0, 0.3, int(0.3 * sample_rate), False)
   freqs = np.linspace(200, 800, len(t))
   success = 0.5 * np.sin(2 * np.pi * freqs * t / 50)
   sf.write("C:\\AssistenzSystem\\data\\sounds\\success.wav", success, sample_rate)
   print("Success sound created")

   print("All sound files created successfully")
   ```

2. Führen Sie das Skript aus:
   ```
   python scripts\create_sounds.py
   ```

## 12. Wissensbasis initialisieren

Erstellen Sie die grundlegenden Wissensdateien, die vom System verwendet werden:

### System-Wissensbasis
Erstellen Sie die Datei `C:\AssistenzSystem\data\knowledge\system.yaml`:

```yaml
system_name: "Assistenzsystem für Sehbehinderte"
version: "1.0.0"
description: "Ein modulares Assistenzsystem zur Unterstützung von Menschen mit Sehbehinderung"
commands:
  - name: "Bildschirm vorlesen"
    description: "Liest den aktuellen Bildschirminhalt vor"
    examples: ["Lies den Bildschirm vor", "Vorlesen", "Text vorlesen"]
  
  - name: "Webseite öffnen"
    description: "Öffnet eine Webseite im Browser"
    examples: ["Öffne Google", "Gehe zu Wikipedia", "Zeige mir heise.de"]
  
  - name: "Bildschirm vergrößern"
    description: "Aktiviert die Bildschirmlupe oder ändert den Zoom-Faktor"
    examples: ["Vergrößere den Bildschirm", "Zoom aktivieren", "Stärker vergrößern"]

preferences:
  default_voice: "Stefan"
  default_zoom: 2.0
  default_browser: "chrome"
```

### Benutzer-Wissensbasis
Erstellen Sie die Datei `C:\AssistenzSystem\data\knowledge\user.yaml`:

```yaml
# Diese Datei wird durch das System bei der ersten Nutzung angepasst
name: "Benutzer"
preferences:
  voice: "Stefan"
  zoom_level: 2.0
  wake_word_sensitivity: 0.7
frequently_used_apps:
  - name: "Browser"
    path: "chrome.exe"
  - name: "Mail"
    path: "outlook.exe"
  - name: "Editor"
    path: "notepad.exe"
```

## 13. Systemberechtigungen einrichten

### Mikrofon-Zugriff aktivieren
1. Öffnen Sie die Windows-Einstellungen (Windows-Taste + I)
2. Navigieren Sie zu **Datenschutz > Mikrofon**
3. Aktivieren Sie **Zugriff auf das Mikrofon auf diesem Gerät zulassen**
4. Aktivieren Sie **Desktop-Apps Zugriff auf Ihr Mikrofon erlauben**

### Bildschirmaufnahme aktivieren
1. Öffnen Sie die Windows PowerShell als Administrator
2. Führen Sie folgenden Befehl aus:
   ```
   Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy" -Name "LetAppsAccessGraphicsCapture" -Type DWord -Value 1 -Force
   ```
   
   Falls der Pfad nicht existiert, erstellen Sie ihn zuerst:
   ```
   New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy" -Force
   ```

### Barrierefreiheitsfunktionen aktivieren
1. Öffnen Sie **Einstellungen > Erleichterte Bedienung > Vergrößerungsglas**
2. Aktivieren Sie **Anderen Apps erlauben, das Vergrößerungsglas zu steuern**

## 14. Firewall-Konfiguration

### Firewall-Skript erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\setup_firewall.ps1`:

```powershell
# Als Administrator ausführen

# Prüfen, ob das Skript als Administrator ausgeführt wird
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "Dieses Skript muss als Administrator ausgeführt werden." -ForegroundColor Red
    exit
}

# Event-Bus-Port freigeben
New-NetFirewallRule -DisplayName "Assistenzsystem Event-Bus" -Direction Inbound -LocalPort 5555 -Protocol TCP -Action Allow -Profile Private,Domain
Write-Host "Firewall-Regel für Event-Bus (Port 5555) erstellt" -ForegroundColor Green

# Mobile-API-Port freigeben (optional)
New-NetFirewallRule -DisplayName "Assistenzsystem Mobile-API" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow -Profile Private,Domain
Write-Host "Firewall-Regel für Mobile-API (Port 8080) erstellt" -ForegroundColor Green

Write-Host "Firewall-Konfiguration abgeschlossen" -ForegroundColor Green
```

### Firewall-Regeln hinzufügen
1. Öffnen Sie die PowerShell als Administrator
2. Navigieren Sie zum Skriptverzeichnis:
   ```
   cd C:\AssistenzSystem\scripts
   ```
3. Führen Sie das Skript aus:
   ```
   .\setup_firewall.ps1
   ```

## 15. Erster Start und Tests

### __init__.py-Dateien erstellen
Erstellen Sie leere `__init__.py`-Dateien in allen Modulverzeichnissen:

```
C:\AssistenzSystem\assistant\__init__.py
C:\AssistenzSystem\assistant\modules\__init__.py
C:\AssistenzSystem\assistant\common\__init__.py
C:\AssistenzSystem\assistant\services\__init__.py
C:\AssistenzSystem\assistant\adapters\__init__.py
C:\AssistenzSystem\assistant\utils\__init__.py
```

### Module-Dateien erstellen
Erstellen Sie die Kernmodule basierend auf den detaillierten Implementierungen aus dem Proof of Concept:

1. `C:\AssistenzSystem\assistant\orchestrator.py`
2. `C:\AssistenzSystem\assistant\modules\brain_module.py`
3. `C:\AssistenzSystem\assistant\modules\voice_module.py`
4. `C:\AssistenzSystem\assistant\modules\vision_module.py`
5. `C:\AssistenzSystem\assistant\modules\digital_module.py`
6. `C:\AssistenzSystem\assistant\common\event_bus.py`
7. `C:\AssistenzSystem\assistant\common\shortcut_registry.py`
8. `C:\AssistenzSystem\assistant\common\config_manager.py`
9. `C:\AssistenzSystem\assistant\services\tts_service.py`
10. `C:\AssistenzSystem\assistant\services\stt_service.py`
11. `C:\AssistenzSystem\assistant\services\ocr_service.py`
12. `C:\AssistenzSystem\assistant\services\llm_service.py`

Verwenden Sie für jede Datei den entsprechenden Code aus dem Proof of Concept-Dokument.

### System starten
1. Öffnen Sie die Eingabeaufforderung und navigieren Sie zum Projektverzeichnis:
   ```
   cd C:\AssistenzSystem
   venv\Scripts\activate
   ```

2. Führen Sie das Startskript aus:
   ```
   python scripts\start.py
   ```

3. Beim ersten Start:
   - Das System lädt alle Konfigurationen
   - Die Module werden initialisiert
   - Die Modelle werden in den Speicher geladen (dauert einige Minuten)
   - Das EventBus-System wird gestartet
   - Alle Module verbinden sich miteinander

### Funktionsprüfung
Testen Sie die grundlegenden Funktionen des Systems:

1. **Wake-Word-Erkennung**: Sprechen Sie "Assistent" oder "Computer"
2. **Einfache Befehle**: Nach Erkennung des Wake-Words sagen Sie z.B.:
   - "Hallo"
   - "Wie geht es dir?"
   - "Öffne Google"
   - "Vergrößere den Bildschirm"

3. **OCR-Test**: Sagen Sie "Lies den Bildschirm vor"

## 16. Desktop-Verknüpfung und Autostart

### Startskript-Batch erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\start_assistant.bat`:

```batch
@echo off
echo Starte Assistenzsystem...
cd /d %~dp0
call venv\Scripts\activate
python scripts\start.py
pause
```

### Desktop-Verknüpfung erstellen
1. Klicken Sie mit der rechten Maustaste auf den Desktop
2. Wählen Sie **Neu > Verknüpfung**
3. Geben Sie als Speicherort ein: `C:\AssistenzSystem\start_assistant.bat`
4. Klicken Sie auf **Weiter**
5. Geben Sie einen Namen ein: **Assistenzsystem starten**
6. Klicken Sie auf **Fertig stellen**

### Icon hinzufügen (optional)
1. Klicken Sie mit der rechten Maustaste auf die erstellte Verknüpfung
2. Wählen Sie **Eigenschaften**
3. Klicken Sie auf **Anderes Symbol**
4. Wählen Sie ein passendes Icon aus, z.B. aus `%SystemRoot%\System32\shell32.dll`

### Autostart einrichten (optional)
1. Drücken Sie **Windows+R** und geben Sie `shell:startup` ein
2. Kopieren Sie die erstellte Verknüpfung in diesen Ordner

### Minimiertes Autostart-Skript (optional)
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\autostart.vbs`:

```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\AssistenzSystem\start_assistant.bat" & Chr(34), 0
Set WshShell = Nothing
```

Erstellen Sie dann eine Verknüpfung zu dieser Datei im Autostart-Ordner.

## 17. Ressourcenmanagement und Updates

### Update-Skript erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\update.py`:

```python
# scripts/update.py
import os
import sys
import subprocess
import requests
import json
from datetime import datetime

def check_for_updates():
    """Prüft, ob Updates für das System verfügbar sind"""
    print("Prüfe auf Updates...")
    
    # Lokale Version ermitteln
    current_version = "1.0.0"
    local_version_file = os.path.join("data", "version.txt")
    
    if os.path.exists(local_version_file):
        with open(local_version_file, "r") as f:
            current_version = f.read().strip()
    
    # Dependencies aktualisieren
    print("Aktualisiere Python-Abhängigkeiten...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"])
    
    # Zeitstempel des letzten Updates speichern
    with open(os.path.join("data", "last_update.txt"), "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    print("Update abgeschlossen.")

if __name__ == "__main__":
    check_for_updates()
```

### Backup-Skript erstellen
Erstellen Sie die Datei `C:\AssistenzSystem\scripts\backup.py`:

```python
# scripts/backup.py
import os
import shutil
import datetime
import zipfile

def create_backup():
    """Erstellt ein Backup der wichtigen Systemdaten"""
    backup_dir = os.path.join("backups")
    os.makedirs(backup_dir, exist_ok=True)
    
    # Aktuelles Datum für den Backup-Namen
    current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"assistant_backup_{current_date}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Zu sichernde Verzeichnisse
    dirs_to_backup = [
        "config",
        "data/knowledge",
        "data/embeddings"
    ]
    
    # Backup erstellen
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for dir_path in dirs_to_backup:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path)
                    zipf.write(file_path, arcname)
    
    print(f"Backup erstellt: {backup_path}")
    
    # Alte Backups bereinigen (optional)
    backup_files = sorted([f for f in os.listdir(backup_dir) if f.startswith("assistant_backup_")])
    
    # Maximal 5 Backups behalten
    max_backups = 5
    if len(backup_files) > max_backups:
        for old_backup in backup_files[:-max_backups]:
            os.remove(os.path.join(backup_dir, old_backup))
            print(f"Altes Backup entfernt: {old_backup}")
    
    return backup_path

if __name__ == "__main__":
    create_backup()
```

## 18. Mobile App (optional)

### Voraussetzungen für die Mobile App
1. Installieren Sie [Flutter SDK](https://flutter.dev/docs/get-started/install/windows)
2. Installieren Sie [Android Studio](https://developer.android.com/studio) mit Android SDK
3. Konfigurieren Sie Flutter gemäß der offiziellen Dokumentation

### Flutter-Projekt erstellen
1. Öffnen Sie die Eingabeaufforderung und navigieren Sie in ein gewünschtes Verzeichnis
2. Führen Sie den Befehl aus:
   ```
   flutter create assistant_mobile
   ```

3. Navigieren Sie in das erstellte Verzeichnis:
   ```
   cd assistant_mobile
   ```

### Abhängigkeiten hinzufügen
Bearbeiten Sie die Datei `pubspec.yaml` im Projektordner und fügen Sie folgende Abhängigkeiten hinzu:

```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  web_socket_channel: ^2.4.0
  camera: ^0.10.5+2
  path_provider: ^2.0.15
  speech_to_text: ^6.3.0
  flutter_tts: ^3.7.0
  shared_preferences: ^2.2.0
  provider: ^6.0.5
  image_picker: ^1.0.0
  permission_handler: ^10.4.3
```

Führen Sie dann den Befehl aus, um die Abhängigkeiten zu installieren:
```
flutter pub get
```

### Mobile-Modul aktivieren
Um die Mobile App zu verwenden, müssen Sie das mobile_module im Assistenzsystem aktivieren:

1. Bearbeiten Sie die Datei `C:\AssistenzSystem\config\orchestrator.yaml`
2. Ändern Sie die Einstellungen für das Mobile-Modul:
   ```yaml
   mobile_module:
     enabled: true  # Auf true ändern
     class: "assistant.modules.mobile_module.MobileModule"
     config_path: "./config/mobile_module.yaml"
   
   mobile_api:
     enabled: true  # Auf true ändern
     host: "0.0.0.0"
     port: 8080
     allowed_origins: ["*"]
     auth_required: false
   ```

3. Starten Sie das Assistenzsystem neu

### App starten
1. Verbinden Sie ein Android-Gerät oder starten Sie einen Emulator
2. Führen Sie den Befehl aus:
   ```
   flutter run
   ```

### App mit dem Assistenzsystem verbinden
1. Finden Sie die IP-Adresse Ihres Computers im lokalen Netzwerk (z.B. 192.168.1.100)
2. Geben Sie in der App die Verbindungsdaten ein:
   - Server-IP: Ihre lokale IP-Adresse
   - Port: 8080

## 19. Fehlerbehebung

### Problem: System startet nicht
**Mögliche Lösungen:**
1. Überprüfen Sie die Protokolldateien in `C:\AssistenzSystem\logs\`
2. Stellen Sie sicher, dass alle `__init__.py`-Dateien in den Modulverzeichnissen vorhanden sind
3. Prüfen Sie, ob alle Abhängigkeiten korrekt installiert sind: `pip list`
4. Aktivieren Sie Debug-Logging in `config/logging.yaml` durch Setzen aller Log-Level auf `DEBUG`
5. Starten Sie das System mit explizitem CPU-Modus:
   - Bearbeiten Sie alle Konfigurationsdateien und setzen Sie `device: "cpu"`

### Problem: Python-Abhängigkeiten können nicht installiert werden
**Mögliche Lösungen:**
1. Stellen Sie sicher, dass Sie Administrator-Rechte haben
2. Prüfen Sie Ihre Internetverbindung
3. Aktualisieren Sie pip: `python -m pip install --upgrade pip`
4. Versuchen Sie, die Abhängigkeiten einzeln zu installieren
5. Verwenden Sie alternative Paketquellen, falls bestimmte Server nicht erreichbar sind

### Problem: CUDA wird nicht erkannt
**Mögliche Lösungen:**
1. Überprüfen Sie Ihre NVIDIA-Treiberinstallation mit `nvidia-smi`
2. Stellen Sie sicher, dass die CUDA-Version mit Ihrer PyTorch-Version kompatibel ist
3. Prüfen Sie die Umgebungsvariablen (PATH und CUDA_PATH)
4. Installieren Sie PyTorch neu mit dem passenden CUDA-Build:
   ```
   pip uninstall torch torchvision torchaudio
   pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
   ```

### Problem: Tesseract OCR funktioniert nicht
**Mögliche Lösungen:**
1. Überprüfen Sie, ob Tesseract korrekt installiert ist: `tesseract --version`
2. Stellen Sie sicher, dass der Pfad in `vision_module.yaml` korrekt ist:
   ```yaml
   ocr:
     tesseract_path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   ```
3. Prüfen Sie, ob die erforderlichen Sprachpakete installiert sind
4. Fügen Sie den Tesseract-Pfad zur PATH-Umgebungsvariable hinzu
5. Starten Sie Ihren Computer neu, um sicherzustellen, dass PATH-Änderungen übernommen wurden

### Problem: Spracherkennung funktioniert nicht
**Mögliche Lösungen:**
1. Prüfen Sie, ob Ihr Mikrofon in Windows funktioniert
2. Stellen Sie sicher, dass die richtigen Mikrofonberechtigungen aktiviert sind
3. Erhöhen Sie die Wake-Word-Sensitivität in `voice_module.yaml`:
   ```yaml
   wake_word:
     sensitivity: 0.7  # Erhöhen Sie diesen Wert für empfindlichere Erkennung
   ```
4. Prüfen Sie, ob das Whisper-Modell korrekt heruntergeladen wurde
5. Überprüfen Sie die Audio-Eingabegeräte in der Systemsteuerung

### Problem: Browser-Automatisierung funktioniert nicht
**Mögliche Lösungen:**
1. Stellen Sie sicher, dass der ChromeDriver installiert und im PATH ist
2. Prüfen Sie, ob die ChromeDriver-Version mit Ihrer Chrome-Version übereinstimmt
3. Überprüfen Sie die Konfigurationsdatei `digital_module.yaml`
4. Starten Sie Chrome manuell, um zu sehen, ob es Probleme gibt
5. Deaktivieren Sie vorübergehend Windows Defender SmartScreen

### Problem: System ist langsam oder instabil
**Mögliche Lösungen:**
1. Überprüfen Sie die Ressourcennutzung mit dem Task-Manager
2. Reduzieren Sie die Modellgröße in `brain_module.yaml` durch Verwendung kleinerer Modelle
3. Deaktivieren Sie nicht benötigte Module in `orchestrator.yaml`
4. Reduzieren Sie die Aktualisierungsrate in `vision_module.yaml`:
   ```yaml
   screen_analysis:
     update_interval_ms: 1000  # Höherer Wert = weniger häufige Updates
   ```
5. Stellen Sie sicher, dass ausreichend Arbeitsspeicher und Festplattenplatz verfügbar ist

## 20. Sicherung und Wiederherstellung

### Regelmäßige Backups erstellen
1. Führen Sie regelmäßig das Backup-Skript aus:
   ```
   cd C:\AssistenzSystem
   venv\Scripts\activate
   python scripts\backup.py
   ```

2. Speichern Sie die erstellten Backup-Dateien an einem sicheren Ort

### System wiederherstellen
1. Installieren Sie das Assistenzsystem gemäß dieser Anleitung
2. Führen Sie alle Schritte bis zum Erstellen der Konfigurationsdateien aus
3. Anstatt neue Konfigurationsdateien zu erstellen, extrahieren Sie die Dateien aus dem Backup
4. Fahren Sie mit der Installation fort (Modelle herunterladen, etc.)

### Wartung und Updates
1. Führen Sie regelmäßig das Update-Skript aus:
   ```
   cd C:\AssistenzSystem
   venv\Scripts\activate
   python scripts\update.py
   ```

2. Prüfen Sie die Protokolldateien auf Warnungen oder Fehler
3. Überprüfen Sie den Festplattenplatz im Modell- und Datenordner

## 21. Weiterführende Anpassungen

### Hinzufügen neuer Sprachmodelle
1. Laden Sie neue GGUF-Modelle von [Hugging Face](https://huggingface.co) herunter
2. Speichern Sie sie im Verzeichnis `C:\AssistenzSystem\models\llm`
3. Aktualisieren Sie die Konfigurationsdatei `brain_module.yaml`:
   ```yaml
   language_model:
     model_path: "./models/llm/neues-modell.gguf"
   ```

### Ändern des Wake-Words
1. Öffnen Sie `C:\AssistenzSystem\config\voice_module.yaml`
2. Ändern Sie die Keywords-Liste:
   ```yaml
   wake_word:
     keywords:
       - "assistent"
       - "computer"
       - "neues-wort"  # Fügen Sie Ihr neues Wake-Word hinzu
   ```

### Anpassen der Sprachausgabe
1. Öffnen Sie `C:\AssistenzSystem\config\voice_module.yaml`
2. Ändern Sie die Sprachausgabe-Einstellungen:
   ```yaml
   text_to_speech:
     voice: "ihre-bevorzugte-stimme"  # Namen der gewünschten Stimme
     rate: -10  # Niedrigere Werte = langsamer, höhere Werte = schneller
     volume: 100  # Lautstärke (0-100)
     pitch: 5  # Tonhöhe (-10 bis 10)
   ```

### Systemleistung optimieren
1. Passen Sie die Ressourcennutzung in `scripts\start.py` an:
   ```python
   def monitor_resources():
       # Maximale Ressourcennutzung
       MAX_CPU_PERCENT = 70  # Niedrigerer Wert = weniger CPU-Nutzung
       MAX_MEMORY_PERCENT = 60  # Niedrigerer Wert = weniger Speichernutzung
   ```

2. Verwenden Sie kleinere Modelle in `brain_module.yaml`:
   ```yaml
   language_model:
     model_path: "./models/llm/kleineres-modell.gguf"  # Wählen Sie ein kleineres Modell
     num_gpu_layers: 10  # Begrenzen Sie die Anzahl der GPU-Schichten
   ```

### Funktionalität erweitern
1. Implementieren Sie neue Module im Verzeichnis `C:\AssistenzSystem\assistant\modules`
2. Erstellen Sie entsprechende Konfigurationsdateien
3. Registrieren Sie neue Module in `orchestrator.yaml`

Diese umfassende Installationsanleitung führt Sie durch alle Schritte, um das Assistenzsystem für Sehbehinderte auf einem Windows 10-System einzurichten. Befolgen Sie die Anweisungen sorgfältig und beachten Sie die Fehlerbehebungshinweise, falls Probleme auftreten.