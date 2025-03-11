### Helfbert der sehende

# Modulares Assistenzsystem für Sehbehinderte: Umfassender Entwicklungsleitfaden

## 1. Einführung und Systemübersicht

Dieses Dokument beschreibt ein umfassendes Proof of Concept (PoC) für ein modulares Assistenzsystem, das speziell für Menschen mit Sehbehinderung entwickelt wurde. Das System kombiniert verschiedene Technologien wie Spracherkennung, Text-to-Speech, OCR und KI-basierte Bildanalyse, um eine umfassende digitale Unterstützung zu bieten.

### 1.1 Zielsetzung

Das System soll folgende Kernfunktionalitäten bieten:
- Verbesserte Bildschirmlupe mit kontextbewusster Vergrößerung
- Natürliche Sprachsteuerung für Windows und Webbrowser
- Intelligentes Vorlesen von Bildschirminhalten mit strukturierter Navigation
- Automatische Erkennung und Beschreibung von Bildinhalten (vom Bildschirm und von Kameras)
- Lokale Verarbeitung für Datenschutz und niedrige Latenz
- Zukunftssichere Schnittstellen für mobile Geräte und IoT-Integration

### 1.2 Architekturübersicht

Das System basiert auf einer modularen Architektur mit fünf Hauptkomponenten:

1. **Orchestrator**: Zentraler Koordinator für alle Module
2. **Hirn-Modul**: KI-basierte Entscheidungsfindung und Sprachverständnis
3. **Stimme/Ohren-Modul**: Spracherkennung und Sprachausgabe
4. **Augen-Modul**: Bildschirmanalyse und Kamerabild-Verarbeitung
5. **Digitalsinn-Modul**: Interaktion mit digitalen Schnittstellen (Browser, Apps)

Die Module können auf verschiedenen Geräten verteilt werden und kommunizieren über optimierte Kanäle.

## 2. Systemarchitektur und Design-Prinzipien

### 2.1 Architekturprinzipien

Das System basiert auf folgenden Designprinzipien:

1. **Modularität**: Klar getrennte Module mit definierten Schnittstellen
2. **Lokale Verarbeitung**: Datenschutz durch Verarbeitung auf lokalen Geräten
3. **Verteilte Ausführung**: Möglichkeit zur Ausführung auf mehreren Geräten
4. **Zustandslose Kommunikation**: Module kommunizieren über standardisierte Nachrichten
5. **Fehlertoleranz**: Robustheit gegen Ausfälle einzelner Komponenten
6. **Erweiterbarkeit**: Einfache Integration neuer Funktionen und Geräte

### 2.2 Kernkomponenten im Detail

```
┌───────────────────────────────────────────┐
│              Orchestrator                 │
│  (Zentrale Steuerung & Kommunikation)     │
└─────────────────┬─────────────────────────┘
        ┌─────────┴─────────┐
        │                   │
┌───────▼───────┐    ┌──────▼────────┐
│   Wissensbasis │    │  Event-Bus    │
│  (Langzeit-    │    │  (Echtzeit-   │
│   speicher)    │    │   ereignisse) │
└───────┬───────┘    └──────┬────────┘
        │                   │
┌───────┴───────────────────┴────────────────────┐
│                                                │
│              Service-Registry                  │
│     (Modulverwaltung & Schnittstellendoku)    │
│                                                │
└───┬───────────┬────────────┬─────────┬─────────┘
    │           │            │         │
┌───▼───┐   ┌───▼───┐    ┌───▼───┐ ┌───▼───┐
│ Hirn- │   │Augen- │    │Stimme/│ │Digital│
│ Modul │   │Modul  │    │Ohren  │ │sinn   │
└───┬───┘   └───┬───┘    └───┬───┘ └───┬───┘
    │           │            │         │
    └───────────┴────────────┴─────────┘
               │
    ┌──────────▼───────────┐
    │     Geräteadapter    │
    │(IoT, Mobile, externe │
    │      Hardware)       │
    └──────────────────────┘
```

### 2.3 Kommunikationspfade

Die Module kommunizieren über drei Hauptkanäle:

1. **Event-Bus**: Publisher-Subscriber-Muster für asynchrone Ereignisse
2. **gRPC-Schnittstellen**: Synchrone Dienstaufrufe zwischen Modulen
3. **Abkürzungspfade**: Optimierte Direktkommunikation für zeitkritische Operationen

### 2.4 Datenfluss

Der typische Datenfluss bei einer Nutzeranfrage:

1. Nutzer spricht einen Befehl
2. Stimme/Ohren-Modul erkennt Wake-Word und transkribiert Sprache
3. Hirn-Modul interpretiert die Anfrage und plant Aktionen
4. Aktionen werden an entsprechende Module delegiert
5. Ergebnisse werden gesammelt und als Sprachausgabe zurückgegeben

## 3. Vollständige Ordnerstruktur und Dateien

Um das System zu implementieren, wird folgende Dateistruktur benötigt:

```
assistant-system/
│
├── assistant/                # Hauptcode
│   ├── __init__.py
│   ├── orchestrator.py       # Zentraler Koordinator
│   ├── modules/              # Modulimplementierungen
│   │   ├── __init__.py
│   │   ├── brain_module.py   # Hirn-Modul
│   │   ├── voice_module.py   # Stimme/Ohren-Modul
│   │   ├── vision_module.py  # Augen-Modul
│   │   ├── digital_module.py # Digitalsinn-Modul
│   │   └── mobile_module.py  # Smartphone-Integration
│   │
│   ├── common/               # Gemeinsame Komponenten
│   │   ├── __init__.py
│   │   ├── event_bus.py      # Event-Bus-Implementierung
│   │   ├── shortcut_registry.py # Abkürzungspfad-Registry
│   │   ├── config_manager.py # Konfigurationsverwaltung
│   │   └── models/           # Datenmodelle
│   │       ├── __init__.py
│   │       └── messages.py    # Nachrichtenformate
│   │
│   ├── services/             # Externe Dienste
│   │   ├── __init__.py
│   │   ├── tts_service.py    # Text-zu-Sprache
│   │   ├── stt_service.py    # Sprache-zu-Text
│   │   ├── ocr_service.py    # OCR-Dienst
│   │   ├── wake_word_service.py # Wake-Word-Erkennung
│   │   ├── llm_service.py    # Sprachmodell-Dienst
│   │   ├── reasoning_service.py # Reasoning-Dienst
│   │   └── camera_service.py # Kamera-Dienst
│   │
│   ├── adapters/             # Adapter für externe Systeme
│   │   ├── __init__.py
│   │   ├── mobile_adapter.py # Smartphone-Adapter
│   │   ├── camera_adapter.py # Kamera-Adapter
│   │   ├── browser_adapter.py # Browser-Adapter
│   │   └── iot_adapter.py    # IoT-Adapter
│   │
│   └── utils/                # Hilfsfunktionen
│       ├── __init__.py
│       ├── logging_utils.py  # Logging-Funktionen
│       ├── accessibility_utils.py # Barrierefreiheit
│       └── audio_utils.py    # Audio-Funktionen
│
├── config/                   # Konfigurationsdateien
│   ├── orchestrator.yaml     # Orchestrator-Konfiguration
│   ├── brain_module.yaml     # Hirn-Modul-Konfiguration
│   ├── voice_module.yaml     # Stimme/Ohren-Konfiguration
│   ├── vision_module.yaml    # Augen-Modul-Konfiguration
│   ├── digital_module.yaml   # Digitalsinn-Konfiguration
│   ├── mobile_module.yaml    # Smartphone-Konfiguration
│   └── logging.yaml          # Logging-Konfiguration
│
├── models/                   # KI-Modelle
│   ├── llm/                  # Sprachmodelle
│   ├── stt/                  # Spracherkennungsmodelle
│   ├── tts/                  # Sprachsynthese-Modelle
│   └── vision/               # Bilderkennungsmodelle
│
├── data/                     # Datenspeicher
│   ├── cache/                # Cache-Verzeichnis
│   ├── embeddings/           # Vektoreinbettungen
│   └── db/                   # Datenbank-Dateien
│
├── protos/                   # Protokolldefinitionen
│   ├── event_bus.proto       # Event-Bus-Protokoll
│   ├── module_service.proto  # Modul-Dienst-Protokoll
│   └── mobile_api.proto      # Mobile-API-Protokoll
│
├── scripts/                  # Hilfsskripte
│   ├── setup.py              # Setup-Skript
│   ├── start.py              # Startet das System
│   ├── build_protos.py       # Generiert Protokoll-Code
│   └── download_models.py    # Lädt Modelle herunter
│
├── docker/                   # Docker-Konfiguration
│   ├── docker-compose.yml    # Haupt-Komposition
│   ├── Dockerfile.orchestrator # Orchestrator-Dockerfile
│   ├── Dockerfile.brain      # Hirn-Modul-Dockerfile
│   ├── Dockerfile.voice      # Stimme/Ohren-Dockerfile
│   ├── Dockerfile.vision     # Augen-Modul-Dockerfile
│   └── Dockerfile.digital    # Digitalsinn-Dockerfile
│
├── mobile_app/               # Mobile App
│   ├── lib/                  # App-Code
│   ├── assets/               # App-Assets
│   └── pubspec.yaml          # Flutter-Konfiguration
│
├── docs/                     # Dokumentation
│   ├── architecture.md       # Architekturübersicht
│   ├── api.md                # API-Dokumentation
│   ├── mobile_integration.md # Mobile-Integration
│   └── camera_integration.md # Kamera-Integration
│
├── tests/                    # Tests
│   ├── unit/                 # Unit-Tests
│   ├── integration/          # Integrationstests
│   └── e2e/                  # End-to-End-Tests
│
├── requirements.txt          # Python-Abhängigkeiten
├── setup.py                  # Paket-Setup
└── README.md                 # Projektübersicht
```

## 4. Kernmodule und ihre Implementierungen

### 4.1 Orchestrator (orchestrator.py)

Der Orchestrator ist die zentrale Komponente, die alle Module koordiniert und überwacht:

```python
# orchestrator.py
import asyncio
import logging
import time
import threading
import yaml
import json
from typing import Dict, List, Any, Optional

from assistant.common.event_bus import EventBus
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager

class Orchestrator:
    """
    Zentraler Koordinator des Assistenzsystems, der alle Module verwaltet
    und die Kommunikation zwischen ihnen steuert.
    """
    
    def __init__(self, config_path: str = "./config/orchestrator.yaml"):
        """
        Initialisiert den Orchestrator.
        
        Args:
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("orchestrator")
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Modulreferenzen
        self.modules = {}
        
        # Event-Bus initialisieren
        self.event_bus = EventBus(self.config.get("event_bus", {}))
        
        # Shortcut-Registry initialisieren
        self.shortcut_registry = ShortcutPathRegistry()
        
        # Status
        self.is_running = False
        
        # Überwachungsthreads
        self.monitoring_thread = None
        
        # Service-Registry für dynamische Modulidentifikation
        self.service_registry = {}
        
        # Ressourcenmanager für dynamische Ressourcenzuweisung
        self.resource_manager = ResourceManager(self.config.get("resources", {}))
        
        self.logger.info("Orchestrator initialisiert")
    
    async def start(self):
        """Startet den Orchestrator und alle Module."""
        self.logger.info("Starte Orchestrator")
        self.is_running = True
        
        # Module initialisieren
        await self._initialize_modules()
        
        # Event-Handling starten
        self.event_bus.start()
        
        # Überwachungsthread starten
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        
        # Mobile-API aktivieren (falls konfiguriert)
        if self.config.get("mobile_api", {}).get("enabled", False):
            await self._start_mobile_api()
        
        self.logger.info("Orchestrator und alle Module gestartet")
    
    async def stop(self):
        """Stoppt den Orchestrator und alle Module."""
        self.logger.info("Stoppe Orchestrator")
        self.is_running = False
        
        # Event-Bus stoppen
        self.event_bus.stop()
        
        # Module stoppen
        await self._stop_modules()
        
        # Mobile-API deaktivieren
        if hasattr(self, 'mobile_api') and self.mobile_api:
            await self.mobile_api.stop()
        
        self.logger.info("Orchestrator und alle Module gestoppt")
    
    async def _initialize_modules(self):
        """Initialisiert alle Module gemäß Konfiguration."""
        module_configs = self.config.get("modules", {})
        
        for module_name, module_config in module_configs.items():
            if module_config.get("enabled", True):
                self.logger.info(f"Initialisiere Modul: {module_name}")
                
                # Modul-Klasse dynamisch importieren
                module_class_path = module_config.get("class", "")
                module_class = self._import_class(module_class_path)
                
                if module_class:
                    # Modul-Konfigurationspfad
                    module_config_path = module_config.get("config_path", f"./config/{module_name}.yaml")
                    
                    # Modul instanziieren
                    module_instance = module_class(
                        event_bus=self.event_bus,
                        shortcut_registry=self.shortcut_registry,
                        config_path=module_config_path
                    )
                    
                    # Modul starten
                    await module_instance.start()
                    
                    # Modul registrieren
                    self.modules[module_name] = module_instance
                    
                    # Fähigkeiten in Service-Registry registrieren
                    capabilities = await module_instance.get_capabilities()
                    for capability in capabilities:
                        if capability not in self.service_registry:
                            self.service_registry[capability] = []
                        self.service_registry[capability].append(module_name)
                    
                    self.logger.info(f"Modul {module_name} erfolgreich initialisiert")
                else:
                    self.logger.error(f"Konnte Modul-Klasse nicht importieren: {module_class_path}")
    
    async def _start_mobile_api(self):
        """Startet die Mobile-API für die Smartphone-Integration."""
        from assistant.adapters.mobile_adapter import MobileAPIServer
        
        mobile_config = self.config.get("mobile_api", {})
        self.mobile_api = MobileAPIServer(
            event_bus=self.event_bus,
            host=mobile_config.get("host", "0.0.0.0"),
            port=mobile_config.get("port", 8080)
        )
        await self.mobile_api.start()
        self.logger.info(f"Mobile-API gestartet auf {mobile_config.get('host', '0.0.0.0')}:{mobile_config.get('port', 8080)}")

    def _monitoring_loop(self):
        """Überwachungsschleife für Module und Systemressourcen."""
        while self.is_running:
            try:
                # Modulstatus überwachen
                for module_name, module_instance in self.modules.items():
                    if not module_instance.is_healthy():
                        self.logger.warning(f"Modul {module_name} ist nicht gesund, versuche Neustart")
                        asyncio.run(self._restart_module(module_name))
                
                # Ressourcennutzung überwachen und optimieren
                self.resource_manager.optimize_resources(self.modules)
                
                # Netzwerkverbindungen prüfen (für verteilte Module)
                if self.config.get("distributed", {}).get("enabled", False):
                    self._check_network_connections()
                
                # Alle 30 Sekunden prüfen
                time.sleep(30)
            except Exception as e:
                self.logger.error(f"Fehler in der Überwachungsschleife: {e}")
                time.sleep(5)  # Kurze Pause bei Fehler

    async def route_request(self, capability, request_data):
        """
        Leitet eine Anfrage an das geeignete Modul basierend auf der Fähigkeit weiter.
        
        Args:
            capability: Benötigte Fähigkeit
            request_data: Anfragedaten
            
        Returns:
            Antwort des Moduls
        """
        if capability not in self.service_registry:
            return {"error": f"Keine Module mit Fähigkeit '{capability}' gefunden"}
        
        # Wähle ein geeignetes Modul für die Anfrage
        module_name = self.resource_manager.select_optimal_module(
            self.service_registry[capability], capability
        )
        
        module = self.modules.get(module_name)
        if not module:
            return {"error": f"Modul '{module_name}' nicht gefunden"}
        
        # Anfrage an das Modul weiterleiten
        try:
            result = await module.handle_request(capability, request_data)
            return result
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung der Anfrage durch {module_name}: {e}")
            return {"error": str(e)}
```

### 4.2 Event-Bus (event_bus.py)

Der Event-Bus implementiert das Publisher-Subscriber-Muster für die asynchrone Kommunikation zwischen Modulen:

```python
# event_bus.py
import asyncio
import logging
import threading
import time
import uuid
import zmq
import zmq.asyncio
from typing import Dict, List, Any, Callable, Optional
import json

class EventMessage:
    """Repräsentiert eine Nachricht im Event-Bus."""
    
    def __init__(self, 
                 topic: str, 
                 payload: Any, 
                 source_module: str = None, 
                 message_id: str = None,
                 message_type: str = "DATA",
                 metadata: Dict[str, Any] = None):
        self.message_id = message_id or str(uuid.uuid4())
        self.topic = topic
        self.source_module = source_module
        self.timestamp = time.time()
        self.message_type = message_type
        self.payload = payload
        self.metadata = metadata or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Konvertiert die Nachricht in ein Dictionary."""
        return {
            "message_id": self.message_id,
            "topic": self.topic,
            "source_module": self.source_module,
            "timestamp": self.timestamp,
            "message_type": self.message_type,
            "payload": self.payload,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EventMessage':
        """Erstellt eine Nachricht aus einem Dictionary."""
        return cls(
            topic=data["topic"],
            payload=data["payload"],
            source_module=data.get("source_module"),
            message_id=data.get("message_id"),
            message_type=data.get("message_type", "DATA"),
            metadata=data.get("metadata", {})
        )
    
    def to_json(self) -> str:
        """Konvertiert die Nachricht in einen JSON-String."""
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_json(cls, json_str: str) -> 'EventMessage':
        """Erstellt eine Nachricht aus einem JSON-String."""
        return cls.from_dict(json.loads(json_str))

class EventBus:
    """
    Event-Bus für die asynchrone Kommunikation zwischen Modulen.
    Implementiert das Publisher-Subscriber-Muster mit ZeroMQ.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisiert den Event-Bus.
        
        Args:
            config: Konfiguration für den Event-Bus
        """
        self.logger = logging.getLogger("event_bus")
        self.config = config or {}
        
        # ZeroMQ-Kontext
        self.context = zmq.Context()
        self.async_context = zmq.asyncio.Context()
        
        # Publisher-Socket
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.bind(f"tcp://*:{self.config.get('publisher_port', 5555)}")
        
        # Subscriber-Socket (asynchron)
        self.subscriber = self.async_context.socket(zmq.SUB)
        self.subscriber.connect(f"tcp://localhost:{self.config.get('publisher_port', 5555)}")
        
        # Callbacks für Themen
        self.topic_callbacks = {}
        
        # Queue für Event-Verarbeitung
        self.event_queue = asyncio.Queue()
        
        # Verteiltes Mode (für Netzwerkkommunikation)
        self.distributed_mode = self.config.get("distributed_mode", False)
        if self.distributed_mode:
            self.remote_publishers = {}
            self._setup_remote_connections()
        
        # Threads
        self.event_loop_thread = None
        self.is_running = False
        
        # Nachrichten-Historie für Debugging und Wiederherstellung
        self.message_history = {}
        self.history_enabled = self.config.get("history_enabled", False)
        self.history_size = self.config.get("history_size", 100)
        
        self.logger.info("Event-Bus initialisiert")
    
    def _setup_remote_connections(self):
        """Richtet Verbindungen zu entfernten Event-Bus-Instanzen ein."""
        remote_nodes = self.config.get("remote_nodes", [])
        for node in remote_nodes:
            node_id = node.get("id")
            node_host = node.get("host")
            node_port = node.get("port")
            
            if node_id and node_host and node_port:
                # Verbinde mit entferntem Publisher
                remote_sub = self.context.socket(zmq.SUB)
                remote_sub.connect(f"tcp://{node_host}:{node_port}")
                remote_sub.setsockopt_string(zmq.SUBSCRIBE, "")  # Alle Themen abonnieren
                
                self.remote_publishers[node_id] = {
                    "host": node_host,
                    "port": node_port,
                    "socket": remote_sub
                }
                
                self.logger.info(f"Mit entferntem Event-Bus verbunden: {node_id} ({node_host}:{node_port})")
    
    def start(self):
        """Startet den Event-Bus."""
        self.logger.info("Starte Event-Bus")
        self.is_running = True
        
        # Event-Loop-Thread starten
        self.event_loop_thread = threading.Thread(target=self._start_event_loop, daemon=True)
        self.event_loop_thread.start()
        
        self.logger.info("Event-Bus gestartet")
    
    def stop(self):
        """Stoppt den Event-Bus."""
        self.logger.info("Stoppe Event-Bus")
        self.is_running = False
        
        # Event-Loop-Thread beenden
        if self.event_loop_thread and self.event_loop_thread.is_alive():
            self.event_loop_thread.join(timeout=2.0)
        
        # Sockets schließen
        self.publisher.close()
        self.subscriber.close()
        
        # Remote-Sockets schließen
        if self.distributed_mode:
            for node_id, node_info in self.remote_publishers.items():
                node_info["socket"].close()
        
        self.logger.info("Event-Bus gestoppt")
    
    def _start_event_loop(self):
        """Startet die Event-Loop im Hintergrund-Thread."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            loop.run_until_complete(self._event_loop())
        except Exception as e:
            self.logger.error(f"Fehler in der Event-Loop: {e}")
        finally:
            loop.close()
    
    async def _event_loop(self):
        """Hauptschleife für Event-Verarbeitung."""
        # Task für das Empfangen von Nachrichten starten
        receive_task = asyncio.create_task(self._receive_messages())
        
        # Task für die Verarbeitung von Nachrichten starten
        process_task = asyncio.create_task(self._process_messages())
        
        # Task für entfernte Nachrichten (wenn im verteilten Modus)
        remote_task = None
        if self.distributed_mode:
            remote_task = asyncio.create_task(self._receive_remote_messages())
        
        # Auf Beendigung warten
        while self.is_running:
            await asyncio.sleep(0.1)
        
        # Tasks beenden
        receive_task.cancel()
        process_task.cancel()
        if remote_task:
            remote_task.cancel()
        
        try:
            await receive_task
            await process_task
            if remote_task:
                await remote_task
        except asyncio.CancelledError:
            pass
    
    async def _receive_messages(self):
        """Empfängt Nachrichten vom Subscriber-Socket."""
        while self.is_running:
            try:
                # Auf Nachrichten warten
                topic = await self.subscriber.recv_string()
                message_json = await self.subscriber.recv_string()
                
                # Nachricht parsen
                message = EventMessage.from_json(message_json)
                
                # Historie aktualisieren
                if self.history_enabled:
                    self._update_message_history(message)
                
                # Zur Verarbeitungswarteschlange hinzufügen
                await self.event_queue.put(message)
            except Exception as e:
                self.logger.error(f"Fehler beim Empfangen von Nachrichten: {e}")
                await asyncio.sleep(0.1)
    
    async def _receive_remote_messages(self):
        """Empfängt Nachrichten von entfernten Event-Bus-Instanzen."""
        if not self.distributed_mode:
            return
        
        # Poller für alle Remote-Sockets erstellen
        poller = zmq.Poller()
        for node_id, node_info in self.remote_publishers.items():
            poller.register(node_info["socket"], zmq.POLLIN)
        
        while self.is_running:
            try:
                # Auf Nachrichten von entfernten Nodes warten
                socks = dict(poller.poll(timeout=100))
                
                for node_id, node_info in self.remote_publishers.items():
                    socket = node_info["socket"]
                    if socket in socks and socks[socket] == zmq.POLLIN:
                        # Nachricht empfangen
                        topic = socket.recv_string()
                        message_json = socket.recv_string()
                        
                        # Nachricht parsen
                        message = EventMessage.from_json(message_json)
                        
                        # Remote-Source-Flag setzen
                        message.metadata["remote_source"] = node_id
                        
                        # Zur Verarbeitungswarteschlange hinzufügen
                        await self.event_queue.put(message)
            except Exception as e:
                self.logger.error(f"Fehler beim Empfangen von Remote-Nachrichten: {e}")
                await asyncio.sleep(0.1)
    
    def _update_message_history(self, message: EventMessage):
        """Aktualisiert die Nachrichtenhistorie."""
        topic = message.topic
        
        if topic not in self.message_history:
            self.message_history[topic] = []
        
        self.message_history[topic].append(message)
        
        # Begrenze die Historie auf die konfigurierte Größe
        if len(self.message_history[topic]) > self.history_size:
            self.message_history[topic].pop(0)
    
    async def _process_messages(self):
        """Verarbeitet empfangene Nachrichten."""
        while self.is_running:
            try:
                # Nächste Nachricht aus der Warteschlange holen
                message = await self.event_queue.get()
                
                # Callbacks für das Thema ausführen
                await self._execute_callbacks(message)
                
                # Nachricht als verarbeitet markieren
                self.event_queue.task_done()
            except Exception as e:
                self.logger.error(f"Fehler bei der Nachrichtenverarbeitung: {e}")
                await asyncio.sleep(0.1)
    
    async def _execute_callbacks(self, message: EventMessage):
        """Führt die Callbacks für eine Nachricht aus."""
        topic = message.topic
        
        # Callbacks für das Thema ausführen
        if topic in self.topic_callbacks:
            for callback in self.topic_callbacks[topic]:
                try:
                    # Callback asynchron ausführen
                    await callback(message)
                except Exception as e:
                    self.logger.error(f"Fehler bei Callback für Thema {topic}: {e}")
        
        # Callbacks für Wildcard-Abonnements ausführen
        for pattern, callbacks in self.topic_callbacks.items():
            if pattern.endswith(".*") and topic.startswith(pattern[:-1]):
                for callback in callbacks:
                    try:
                        await callback(message)
                    except Exception as e:
                        self.logger.error(f"Fehler bei Wildcard-Callback für Thema {topic}: {e}")
    
    def publish(self, topic: str, payload: Any, message_type: str = "DATA", 
               source_module: str = None, metadata: Dict[str, Any] = None,
               message_id: str = None):
        """
        Veröffentlicht eine Nachricht im Event-Bus.
        
        Args:
            topic: Thema der Nachricht
            payload: Nutzlast der Nachricht
            message_type: Typ der Nachricht (DATA, COMMAND, QUERY, RESPONSE, NOTIFICATION, ERROR)
            source_module: Quellmodul der Nachricht
            metadata: Zusätzliche Metadaten
            message_id: Optionale Nachrichten-ID
        """
        try:
            # Nachricht erstellen
            message = EventMessage(
                topic=topic,
                payload=payload,
                source_module=source_module,
                message_id=message_id,
                message_type=message_type,
                metadata=metadata
            )
            
            # Nachricht als JSON konvertieren
            message_json = message.to_json()
            
            # Nachricht veröffentlichen
            self.publisher.send_string(topic, zmq.SNDMORE)
            self.publisher.send_string(message_json)
            
            # Historie aktualisieren
            if self.history_enabled:
                self._update_message_history(message)
            
            self.logger.debug(f"Nachricht für Thema {topic} veröffentlicht: {message_id}")
        except Exception as e:
            self.logger.error(f"Fehler beim Veröffentlichen von Nachricht für Thema {topic}: {e}")
    
    def subscribe(self, topic: str, callback: Callable[[EventMessage], None]):
        """
        Abonniert ein Thema und registriert einen Callback.
        
        Args:
            topic: Zu abonnierendes Thema
            callback: Aufzurufende Funktion bei Empfang einer Nachricht
        """
        try:
            # Thema beim Subscriber registrieren
            self.subscriber.setsockopt_string(zmq.SUBSCRIBE, topic)
            
            # Callback registrieren
            if topic not in self.topic_callbacks:
                self.topic_callbacks[topic] = []
            
            self.topic_callbacks[topic].append(callback)
            
            self.logger.debug(f"Thema {topic} abonniert")
        except Exception as e:
            self.logger.error(f"Fehler beim Abonnieren von Thema {topic}: {e}")
    
    def unsubscribe(self, topic: str, callback: Callable[[EventMessage], None] = None):
        """
        Kündigt ein Abonnement für ein Thema.
        
        Args:
            topic: Abzumeldendes Thema
            callback: Zu entfernender Callback (wenn None, werden alle Callbacks entfernt)
        """
        try:
            if callback is None:
                # Alle Callbacks entfernen
                if topic in self.topic_callbacks:
                    del self.topic_callbacks[topic]
                
                # Thema beim Subscriber abmelden
                self.subscriber.setsockopt_string(zmq.UNSUBSCRIBE, topic)
            else:
                # Nur den angegebenen Callback entfernen
                if topic in self.topic_callbacks:
                    if callback in self.topic_callbacks[topic]:
                        self.topic_callbacks[topic].remove(callback)
                    
                    # Wenn keine Callbacks mehr vorhanden sind, Thema abmelden
                    if not self.topic_callbacks[topic]:
                        del self.topic_callbacks[topic]
                        self.subscriber.setsockopt_string(zmq.UNSUBSCRIBE, topic)
            
            self.logger.debug(f"Abonnement für Thema {topic} gekündigt")
        except Exception as e:
            self.logger.error(f"Fehler beim Kündigen des Abonnements für Thema {topic}: {e}")
    
    def get_message_history(self, topic: str = None, limit: int = None) -> List[EventMessage]:
        """
        Gibt die Nachrichtenhistorie für ein Thema zurück.
        
        Args:
            topic: Thema für die Historie (wenn None, werden alle Themen zurückgegeben)
            limit: Maximale Anzahl zurückzugebender Nachrichten pro Thema
            
        Returns:
            Liste von Nachrichten
        """
        if not self.history_enabled:
            return []
        
        if topic:
            # Historie für ein bestimmtes Thema
            messages = self.message_history.get(topic, [])
            if limit:
                return messages[-limit:]
            return messages
        else:
            # Historie für alle Themen
            all_messages = []
            for t, messages in self.message_history.items():
                if limit:
                    all_messages.extend(messages[-limit:])
                else:
                    all_messages.extend(messages)
            
            # Nach Zeitstempel sortieren
            all_messages.sort(key=lambda m: m.timestamp)
            return all_messages
```

### 4.3 Hirn-Modul (brain_module.py)

Das Hirn-Modul dient als zentrale Entscheidungskomponente und interpretiert Nutzereingaben mithilfe eines Sprachmodells:

```python
# brain_module.py
import asyncio
import logging
import time
import threading
import json
from typing import Dict, List, Any, Optional, Tuple

from assistant.common.event_bus import EventBus, EventMessage
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager
from assistant.services.llm_service import LLMService

class BrainModule:
    """
    Zentrales Entscheidungsmodul des Assistenzsystems. Verarbeitet Benutzereingaben,
    versteht Kontext und generiert Antworten basierend auf einem lokalen Sprachmodell.
    """
    
    def __init__(self, event_bus: EventBus, shortcut_registry: ShortcutPathRegistry,
                config_path: str = "./config/brain_module.yaml"):
        """
        Initialisiert das Hirn-Modul.
        
        Args:
            event_bus: Event-Bus für die Kommunikation
            shortcut_registry: Registry für direkte Kommunikationspfade
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("brain_module")
        
        # Referenzen speichern
        self.event_bus = event_bus
        self.shortcut_registry = shortcut_registry
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Sprachmodell-Service initialisieren
        self.llm_service = LLMService(self.config.get("language_model", {}))
        
        # Reasoning-Modell (für verbesserte Kontextanalyse)
        self.use_reasoning = self.config.get("reasoning_model", {}).get("enabled", False)
        self.reasoning_model = None
        if self.use_reasoning:
            from assistant.services.reasoning_service import ReasoningService
            self.reasoning_model = ReasoningService(self.config.get("reasoning_model", {}))
        
        # Kontext-Management
        self.context = []
        self.context_lock = threading.Lock()
        self.max_context_length = self.config.get("context", {}).get("max_entries", 10)
        
        # Antwort-Cache
        self.response_cache = {}
        self.cache_lock = threading.Lock()
        
        # Systemwissen für Entscheidungen
        self.knowledge_store = {}
        
        # Status
        self.start_time = None
        self.is_running = False
        self.health_status = True
        
        # Statistiken
        self.stats = {
            "total_queries": 0,
            "cache_hits": 0,
            "average_response_time_ms": 0,
            "reasoning_calls": 0
        }
        
        self.logger.info("Hirn-Modul initialisiert")
    
    async def start(self):
        """Startet das Hirn-Modul."""
        self.logger.info("Starte Hirn-Modul")
        self.is_running = True
        self.start_time = time.time()
        
        # Sprachmodell starten
        await self.llm_service.start()
        
        # Reasoning-Modell starten (falls aktiviert)
        if self.reasoning_model:
            await self.reasoning_model.start()
        
        # Event-Subscriptions einrichten
        self._setup_event_subscriptions()
        
        # Abkürzungspfade registrieren
        self._register_shortcuts()
        
        # Lade Systemwissen
        await self._load_knowledge()
        
        self.logger.info("Hirn-Modul gestartet")
    
    async def stop(self):
        """Stoppt das Hirn-Modul."""
        self.logger.info("Stoppe Hirn-Modul")
        self.is_running = False
        
        # Sprachmodell stoppen
        await self.llm_service.stop()
        
        # Reasoning-Modell stoppen (falls aktiviert)
        if self.reasoning_model:
            await self.reasoning_model.stop()
        
        self.logger.info("Hirn-Modul gestoppt")
    
    def _setup_event_subscriptions(self):
        """Richtet Event-Subscriptions ein."""
        # Spracherkennung verarbeiten
        self.event_bus.subscribe("event.speech_recognized", self._handle_speech_input)
        
        # Intentanalyse-Anfragen
        self.event_bus.subscribe("query.intent_classification", self._handle_intent_query)
        
        # Direkte Nutzereingaben
        self.event_bus.subscribe("query.user_input", self._handle_user_input)
        
        # Inhaltsaktualisierungen für Kontext
        self.event_bus.subscribe("data.screen_content", self._handle_screen_content)
        self.event_bus.subscribe("data.text_regions", self._handle_text_regions)
        
        # Anfragen für Bildbeschreibungen (z.B. von mobilen Geräten)
        self.event_bus.subscribe("query.describe_image", self._handle_image_description)
        
        # Systemereignisse und Aktualisierungen
        self.event_bus.subscribe("event.system_update", self._handle_system_update)
    
    def _register_shortcuts(self):
        """Registriert optimierte Abkürzungspfade."""
        # Direkter Pfad für häufige Befehle vom Stimme/Ohren-Modul
        self.shortcut_registry.register_shortcut(
            "voice_module",
            "brain_module",
            "common_commands",
            self._shortcut_handle_common_command
        )
        
        # Direkter Pfad für OCR-Ergebnisse vom Augen-Modul
        self.shortcut_registry.register_shortcut(
            "vision_module",
            "brain_module",
            "ocr_results",
            self._shortcut_handle_ocr_results
        )
        
        # Direkter Pfad für Browserergebnisse vom Digitalsinn-Modul
        self.shortcut_registry.register_shortcut(
            "digital_module",
            "brain_module",
            "browser_results",
            self._shortcut_handle_browser_results
        )
    
    async def _load_knowledge(self):
        """Lädt Systemwissen aus der Konfiguration und Dateien."""
        knowledge_path = self.config.get("knowledge", {}).get("path", "./data/knowledge")
        
        try:
            # Lade Grundwissen aus der Konfiguration
            self.knowledge_store["system"] = self.config.get("knowledge", {}).get("system_info", {})
            
            # Lade zusätzliches Wissen aus Dateien
            import os
            import yaml
            
            if os.path.exists(knowledge_path):
                for filename in os.listdir(knowledge_path):
                    if filename.endswith(".yaml") or filename.endswith(".yml"):
                        file_path = os.path.join(knowledge_path, filename)
                        with open(file_path, "r", encoding="utf-8") as f:
                            knowledge_data = yaml.safe_load(f)
                            
                            # Extrahiere Kategorie aus Dateiname
                            category = os.path.splitext(filename)[0]
                            self.knowledge_store[category] = knowledge_data
                        
                        self.logger.debug(f"Wissen aus {filename} geladen")
            
            self.logger.info(f"Systemwissen geladen: {len(self.knowledge_store)} Kategorien")
        except Exception as e:
            self.logger.error(f"Fehler beim Laden des Systemwissens: {e}")
    
    async def _handle_speech_input(self, event: EventMessage):
        """Verarbeitet erkannte Spracheingabe vom Event-Bus."""
        try:
            # Text extrahieren
            input_text = event.payload.decode('utf-8') if isinstance(event.payload, bytes) else event.payload
            
            # Metadaten extrahieren
            metadata = event.metadata or {}
            confidence = metadata.get("confidence", 0.0)
            
            # Statistik aktualisieren
            self.stats["total_queries"] += 1
            
            # Verarbeitungszeit messen
            start_time = time.time()
            
            # Kontextverwaltung
            with self.context_lock:
                self._add_to_context({"role": "user", "content": input_text})
                current_context = self._get_formatted_context()
            
            # Prüfe Cache für häufige Anfragen
            cache_key = self._compute_response_cache_key(input_text, current_context)
            cached_response = None
            
            with self.cache_lock:
                if cache_key in self.response_cache:
                    cached_response = self.response_cache[cache_key]
                    self.stats["cache_hits"] += 1
            
            if cached_response:
                # Verwende zwischengespeicherte Antwort
                response_text = cached_response
                self.logger.debug(f"Cache-Treffer für Eingabe: {input_text[:30]}...")
            else:
                # Generiere neue Antwort
                
                # Verwende Reasoning-Modell für verbesserte Kontextanalyse, falls aktiviert
                if self.use_reasoning and self.reasoning_model:
                    # Prompt für Reasoning vorbereiten
                    reasoning_prompt = self._prepare_reasoning_prompt(input_text, current_context)
                    
                    # Asynchrone Reasoning-Anfrage
                    reasoning_result = await self.reasoning_model.generate_reasoning(reasoning_prompt)
                    self.stats["reasoning_calls"] += 1
                    
                    # Prompt mit Reasoning erweitern
                    enhanced_prompt = f"{current_context}\n\nEingabe: {input_text}\n\nReasoning:\n{reasoning_result}\n\nAntwort:"
                else:
                    # Ohne Reasoning-Modell
                    enhanced_prompt = f"{current_context}\n\nEingabe: {input_text}\n\nAntwort:"
                
                # Generiere Antwort mit dem Sprachmodell
                response = await self.llm_service.generate_text(
                    enhanced_prompt,
                    max_tokens=self.config.get("language_model", {}).get("max_generation_tokens", 512),
                    temperature=self.config.get("language_model", {}).get("temperature", 0.7)
                )
                
                response_text = response.strip()
                
                # Speichere Antwort im Cache
                with self.cache_lock:
                    # Prüfe Cache-Größe und entferne ältesten Eintrag bei Bedarf
                    max_cache_size = self.config.get("cache", {}).get("max_size", 100)
                    if len(self.response_cache) >= max_cache_size:
                        oldest_key = next(iter(self.response_cache))
                        del self.response_cache[oldest_key]
                    
                    # Füge neue Antwort zum Cache hinzu
                    self.response_cache[cache_key] = response_text
            
            # Verarbeitungszeit berechnen
            processing_time_ms = (time.time() - start_time) * 1000
            
            # Aktualisiere durchschnittliche Antwortzeit
            self.stats["average_response_time_ms"] = (
                (self.stats["average_response_time_ms"] * (self.stats["total_queries"] - 1) + processing_time_ms) 
                / self.stats["total_queries"]
            )
            
            # Antwort zum Kontext hinzufügen
            with self.context_lock:
                self._add_to_context({"role": "assistant", "content": response_text})
            
            # Veröffentliche generierte Antwort
            self.event_bus.publish(
                "command.speak",
                response_text,
                "COMMAND",
                "brain_module",
                {
                    "original_message_id": event.message_id,
                    "confidence": confidence,
                    "processing_time_ms": processing_time_ms,
                    "cached": cached_response is not None
                }
            )
            
            # Prüfe auf Aktionen in der Antwort
            await self._check_for_actions(input_text, response_text)
            
            self.logger.debug(f"Antwort generiert in {processing_time_ms:.2f}ms für Eingabe: {input_text[:30]}...")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Spracheingabe: {e}")
            error_msg = "Entschuldigung, ich konnte deine Anfrage nicht verarbeiten. Bitte versuche es erneut."
            self.event_bus.publish("command.speak", error_msg, "COMMAND", "brain_module")
    
    async def _check_for_actions(self, input_text: str, response_text: str):
        """
        Prüft, ob die generierte Antwort Aktionen enthält, die ausgeführt werden sollten.
        
        Args:
            input_text: Nutzereingabe
            response_text: Generierte Antwort
        """
        # Intentanalyse für die Nutzereingabe
        intent = await self._classify_intent(input_text)
        
        # Prüfe nach bestimmten Aktionen basierend auf Intent
        if intent.get("type") == "OPEN_WEBSITE":
            url = intent.get("parameters", {}).get("url")
            if url:
                self.event_bus.publish(
                    "command.browse_website",
                    url,
                    "COMMAND",
                    "brain_module"
                )
        
        elif intent.get("type") == "MAGNIFY_SCREEN":
            region = intent.get("parameters", {}).get("region")
            self.event_bus.publish(
                "command.magnify_screen",
                json.dumps({"region": region}),
                "COMMAND",
                "brain_module"
            )
        
        elif intent.get("type") == "READ_SCREEN":
            self.event_bus.publish(
                "command.read_screen",
                "",
                "COMMAND",
                "brain_module"
            )
        
        elif intent.get("type") == "TAKE_PHOTO":
            self.event_bus.publish(
                "command.camera.take_photo",
                "",
                "COMMAND",
                "brain_module"
            )
        
        # Weitere Intents und Aktionen...
    
    async def _classify_intent(self, text: str) -> Dict[str, Any]:
        """
        Klassifiziert die Nutzereingabe nach Intent.
        
        Args:
            text: Nutzereingabe
            
        Returns:
            Dict mit Intent-Typ und Parametern
        """
        # Einfache Regeln für Intent-Erkennung
        text_lower = text.lower()
        
        # Website öffnen
        if "öffne" in text_lower and ("website" in text_lower or "seite" in text_lower or "webseite" in text_lower):
            # Extrahiere URL (vereinfachte Version)
            import re
            url_match = re.search(r'(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)(?:/[^\s]*)?', text)
            
            if url_match:
                url = url_match.group(0)
                if not url.startswith("http"):
                    url = "https://" + url
            else:
                # Versuche, Domain aus Text zu extrahieren
                words = text.split()
                for word in words:
                    if "." in word and not word.startswith(".") and not word.endswith("."):
                        url = word
                        if not url.startswith("http"):
                            url = "https://" + url
                        break
                else:
                    url = None
            
            return {
                "type": "OPEN_WEBSITE",
                "confidence": 0.8,
                "parameters": {"url": url}
            }
        
        # Bildschirm vergrößern
        elif any(word in text_lower for word in ["vergrößer", "zoom", "lupe"]):
            # Extrahiere Region (falls angegeben)
            region = None
            if "oben" in text_lower:
                region = "top"
            elif "unten" in text_lower:
                region = "bottom"
            elif "links" in text_lower:
                region = "left"
            elif "rechts" in text_lower:
                region = "right"
            elif "mitte" in text_lower:
                region = "center"
            
            return {
                "type": "MAGNIFY_SCREEN",
                "confidence": 0.9,
                "parameters": {"region": region}
            }
        
        # Bildschirm vorlesen
        elif any(word in text_lower for word in ["lies", "vorlesen", "text vorlesen"]):
            return {
                "type": "READ_SCREEN",
                "confidence": 0.9,
                "parameters": {}
            }
        
        # Foto aufnehmen
        elif any(phrase in text_lower for phrase in ["mach ein foto", "nimm ein bild auf", "fotografiere", "kamera"]):
            return {
                "type": "TAKE_PHOTO",
                "confidence": 0.8,
                "parameters": {}
            }
        
        # Standard: Keine spezifische Aktion
        return {
            "type": "GENERAL_QUERY",
            "confidence": 0.5,
            "parameters": {}
        }
    
    def _shortcut_handle_common_command(self, payload):
        """Verarbeitet häufige Befehle direkt ohne vollständige LLM-Verarbeitung."""
        try:
            # Befehl parsen
            command_data = json.loads(payload)
            command = command_data.get("command", "").lower()
            confidence = command_data.get("confidence", 0.0)
            
            # Niedrige Konfidenz ignorieren
            if confidence < 0.6:
                return {"success": False, "reason": "low_confidence"}
            
            # Häufige Befehle verarbeiten
            if command in ["hilfe", "help"]:
                response = "Ich kann dir bei verschiedenen Aufgaben helfen, zum Beispiel: Bildschirminhalte vorlesen, Webseiten zusammenfassen oder den Bildschirm vergrößern."
                self.event_bus.publish("command.speak", response, "COMMAND", "brain_module")
                return {"success": True, "response": response}
            
            elif command in ["stopp", "stop", "halt", "abbrechen"]:
                response = "Ich stoppe die aktuelle Aktion."
                self.event_bus.publish("command.stop_current_action", "", "COMMAND", "brain_module")
                self.event_bus.publish("command.speak", response, "COMMAND", "brain_module")
                return {"success": True, "response": response}
            
            # Weitere häufige Befehle...
            
            # Kein bekannter Befehl
            return {"success": False, "reason": "unknown_command"}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung eines häufigen Befehls: {e}")
            return {"success": False, "reason": str(e)}
    
    async def _handle_image_description(self, event: EventMessage):
        """
        Verarbeitet Anfragen zur Beschreibung von Bildern (z.B. von Kameras).
        
        Args:
            event: Event-Nachricht mit Bilddaten oder Bildpfad
        """
        try:
            # Bildverweisinformationen extrahieren
            image_data = event.payload
            metadata = event.metadata or {}
            image_source = metadata.get("source", "unknown")
            
            # Bild an Vision-Service weiterleiten
            self.event_bus.publish(
                "query.vision.describe_image",
                image_data,
                "QUERY",
                "brain_module",
                {
                    "original_message_id": event.message_id,
                    "source": image_source
                }
            )
            
            # Auf Antwort warten (asynchron mit Future)
            response_future = asyncio.Future()
            
            def response_callback(response_event):
                # Prüfe, ob die Antwort zu unserer Anfrage gehört
                if response_event.metadata.get("original_message_id") == event.message_id:
                    # Future mit Beschreibung erfüllen
                    description = response_event.payload.decode('utf-8') if isinstance(response_event.payload, bytes) else response_event.payload
                    response_future.set_result(description)
            
            # Registriere Callback für Antwort
            self.event_bus.subscribe("response.vision.image_description", response_callback)
            
            try:
                # Auf Antwort warten (mit Timeout)
                description = await asyncio.wait_for(response_future, timeout=10.0)
                
                # Beschreibung über Event-Bus zurücksenden
                self.event_bus.publish(
                    "response.image_description",
                    description,
                    "RESPONSE",
                    "brain_module",
                    {
                        "original_message_id": event.message_id,
                        "source": image_source
                    }
                )
                
                # Beschreibung vorlesen, wenn von einer Kamera
                if image_source in ["camera", "mobile_camera"]:
                    self.event_bus.publish(
                        "command.speak",
                        f"Ich sehe: {description}",
                        "COMMAND",
                        "brain_module"
                    )
            
            except asyncio.TimeoutError:
                # Timeout bei der Bildbeschreibung
                error_msg = "Die Bildbeschreibung dauert zu lange. Bitte versuche es erneut."
                self.event_bus.publish(
                    "response.image_description",
                    error_msg,
                    "RESPONSE",
                    "brain_module",
                    {"original_message_id": event.message_id, "error": "timeout"}
                )
                
                if image_source in ["camera", "mobile_camera"]:
                    self.event_bus.publish("command.speak", error_msg, "COMMAND", "brain_module")
            
            finally:
                # Callback deregistrieren
                self.event_bus.unsubscribe("response.vision.image_description", response_callback)
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Bildanfrage: {e}")
            error_msg = "Entschuldigung, ich konnte das Bild nicht verarbeiten."
            
            self.event_bus.publish(
                "response.image_description",
                error_msg,
                "RESPONSE",
                "brain_module",
                {"original_message_id": event.message_id, "error": str(e)}
            )
            
            if image_source in ["camera", "mobile_camera"]:
                self.event_bus.publish("command.speak", error_msg, "COMMAND", "brain_module")
    
    def _prepare_reasoning_prompt(self, input_text: str, context: str) -> str:
        """Bereitet den Prompt für das Reasoning-Modell vor."""
        return f"""Analysiere die folgende Nutzereingabe im gegebenen Kontext:

Kontext:
{context}

Nutzereingabe:
{input_text}

Analysiere die Intention, identifiziere relevante Entitäten und bestimme den Kontext der Anfrage.
"""
    
    def _compute_response_cache_key(self, input_text: str, context: str) -> str:
        """Berechnet einen eindeutigen Schlüssel für den Antwort-Cache."""
        import hashlib
        
        # Beschränke Kontext für den Hash auf die letzten paar Zeilen
        context_lines = context.split('\n')
        limited_context = '\n'.join(context_lines[-10:]) if len(context_lines) > 10 else context
        
        # Hash-Eingabe kombinieren
        hash_input = f"{input_text}_{limited_context}"
        
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    def _add_to_context(self, entry: Dict[str, Any]):
        """Fügt einen Eintrag zum Kontext hinzu."""
        self.context.append(entry)
        
        # Kontext auf maximale Länge begrenzen
        if len(self.context) > self.max_context_length:
            self.context.pop(0)
    
    def _get_formatted_context(self) -> str:
        """Gibt den formatierten Kontext für LLM-Anfragen zurück."""
        if not self.context:
            return ""
        
        formatted_context = "Konversationsverlauf:\n"
        for entry in self.context:
            role = "Nutzer" if entry["role"] == "user" else "Assistent"
            formatted_context += f"{role}: {entry['content']}\n"
        
        return formatted_context
    
    async def get_capabilities(self) -> List[str]:
        """Gibt die Fähigkeiten des Moduls zurück."""
        return [
            "text_understanding",
            "question_answering",
            "intent_classification",
            "response_generation",
            "context_management"
        ]
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob das Modul gesund ist."""
        return self.health_status and self.is_running and self.llm_service.is_healthy()
    
    def get_uptime(self) -> float:
        """Gibt die Laufzeit des Moduls in Sekunden zurück."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    def get_stats(self) -> Dict[str, Any]:
        """Gibt Statistiken zum Modul zurück."""
        return self.stats
```

### 4.4 Stimme/Ohren-Modul (voice_module.py)

Das Stimme/Ohren-Modul ist für die Spracherkennung und Sprachausgabe zuständig:

```python
# voice_module.py
import asyncio
import logging
import time
import threading
import queue
import numpy as np
import json
from typing import Dict, List, Any, Optional, Tuple

from assistant.common.event_bus import EventBus, EventMessage
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager
from assistant.services.tts_service import TTSService
from assistant.services.stt_service import STTService
from assistant.services.wake_word_service import WakeWordService
from assistant.utils.audio_utils import AudioFeedbackManager

class VoiceModule:
    """
    Verarbeitet Spracheingabe und -ausgabe, einschließlich Wake-Word-Erkennung,
    Spracherkennung und Text-to-Speech-Synthese.
    """
    
    def __init__(self, event_bus: EventBus, shortcut_registry: ShortcutPathRegistry,
                config_path: str = "./config/voice_module.yaml"):
        """
        Initialisiert das Stimme/Ohren-Modul.
        
        Args:
            event_bus: Event-Bus für die Kommunikation
            shortcut_registry: Registry für Abkürzungspfade
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("voice_module")
        
        # Referenzen speichern
        self.event_bus = event_bus
        self.shortcut_registry = shortcut_registry
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Dienste initialisieren
        self.tts_service = TTSService(self.config.get("text_to_speech", {}))
        self.stt_service = STTService(self.config.get("speech_recognition", {}))
        self.wake_word_service = WakeWordService(self.config.get("wake_word", {}))
        self.audio_feedback = AudioFeedbackManager(self.config.get("audio_feedback", {}))
        
        # Audio-Verarbeitung
        self.audio_queue = queue.Queue()
        self.speech_buffer = []
        self.is_listening = False
        self.audio_thread = None
        
        # TTS-Warteschlange für asynchrone Sprachausgabe
        self.tts_queue = asyncio.Queue()
        self.tts_task = None
        
        # Status
        self.start_time = None
        self.is_running = False
        self.health_status = True
        
        # Statistiken
        self.stats = {
            "wake_word_detections": 0,
            "speech_recognitions": 0,
            "tts_requests": 0,
            "average_stt_time_ms": 0
        }
        
        # Zustandsmanagement
        self.current_state = "idle"  # idle, listening, speaking
        self.state_lock = threading.Lock()
        
        self.logger.info("Stimme/Ohren-Modul initialisiert")
    
    async def start(self):
        """Startet das Stimme/Ohren-Modul."""
        self.logger.info("Starte Stimme/Ohren-Modul")
        self.is_running = True
        self.start_time = time.time()
        
        # Dienste starten
        await self.tts_service.start()
        await self.stt_service.start()
        await self.wake_word_service.start()
        
        # Event-Subscriptions einrichten
        self._setup_event_subscriptions()
        
        # Abkürzungspfade registrieren
        self._register_shortcuts()
        
        # Audio-Verarbeitung starten
        await self._start_audio_processing()
        
        # TTS-Verarbeitungsaufgabe starten
        self.tts_task = asyncio.create_task(self._process_tts_queue())
        
        self.logger.info("Stimme/Ohren-Modul gestartet")
    
    async def stop(self):
        """Stoppt das Stimme/Ohren-Modul."""
        self.logger.info("Stoppe Stimme/Ohren-Modul")
        self.is_running = False
        
        # Audio-Verarbeitung stoppen
        await self._stop_audio_processing()
        
        # TTS-Verarbeitungsaufgabe stoppen
        if self.tts_task:
            self.tts_task.cancel()
            try:
                await self.tts_task
            except asyncio.CancelledError:
                pass
        
        # Dienste stoppen
        await self.tts_service.stop()
        await self.stt_service.stop()
        await self.wake_word_service.stop()
        
        self.logger.info("Stimme/Ohren-Modul gestoppt")
    
    def _setup_event_subscriptions(self):
        """Richtet Event-Subscriptions ein."""
        # Text-to-Speech-Anfragen
        self.event_bus.subscribe("command.speak", self._handle_speak_command)
        
        # Status und Steuerung
        self.event_bus.subscribe("command.voice_module.start_listening", self._handle_start_listening)
        self.event_bus.subscribe("command.voice_module.stop_listening", self._handle_stop_listening)
        self.event_bus.subscribe("command.voice_module.adjust_volume", self._handle_adjust_volume)
        self.event_bus.subscribe("command.voice_module.change_voice", self._handle_change_voice)
        
        # Mobile-Integration
        self.event_bus.subscribe("mobile.voice_input", self._handle_mobile_voice_input)
        self.event_bus.subscribe("command.mobile.speak", self._handle_mobile_speak_command)
    
    def _register_shortcuts(self):
        """Registriert optimierte Abkürzungspfade."""
        # Direkter Pfad für häufige Antworten vom Hirn-Modul
        self.shortcut_registry.register_shortcut(
            "brain_module",
            "voice_module",
            "common_responses",
            self._shortcut_handle_common_response
        )
    
    def _shortcut_handle_common_response(self, payload):
        """Verarbeitet häufige Antworten direkt für schnellere Reaktion."""
        try:
            # Antwort parsen
            response_data = json.loads(payload)
            text = response_data.get("text", "")
            priority = response_data.get("priority", 1)
            
            # Direkt zur TTS-Warteschlange hinzufügen
            asyncio.run_coroutine_threadsafe(
                self.tts_queue.put({
                    "text": text,
                    "priority": priority,
                    "metadata": response_data.get("metadata", {})
                }),
                asyncio.get_event_loop()
            )
            
            return {"success": True}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer häufigen Antwort: {e}")
            return {"success": False, "reason": str(e)}
    
    async def _start_audio_processing(self):
        """Startet die Audio-Verarbeitung."""
        self.is_listening = True
        
        # Audio-Thread starten
        self.audio_thread = threading.Thread(target=self._audio_processing_loop, daemon=True)
        self.audio_thread.start()
        
        self.logger.debug("Audio-Verarbeitung gestartet")
    
    async def _stop_audio_processing(self):
        """Stoppt die Audio-Verarbeitung."""
        self.is_listening = False
        
        # Auf Beendigung des Audio-Threads warten
        if self.audio_thread and self.audio_thread.is_alive():
            self.audio_thread.join(timeout=2.0)
        
        self.logger.debug("Audio-Verarbeitung gestoppt")
    
    def _audio_processing_loop(self):
        """Kontinuierliche Audioüberwachung im Hintergrund."""
        try:
            # Audio-Capturing-Service initialisieren
            import sounddevice as sd
            
            sample_rate = self.config.get("audio", {}).get("sample_rate", 16000)
            frame_length = self.config.get("audio", {}).get("frame_length", 512)
            
            def audio_callback(indata, frames, time, status):
                if status:
                    self.logger.warning(f"Audio-Callback-Status: {status}")
                
                # Konvertiere in das für die Verarbeitung erwartete Format
                audio_data = np.frombuffer((indata * 32767).astype(np.int16), dtype=np.int16)
                self.audio_queue.put(audio_data)
                
                # Puffere die letzten Sekunden für schnellere Reaktion nach Wake-Word
                buffer_seconds = self.config.get("audio", {}).get("buffer_seconds", 3)
                max_buffer_size = buffer_seconds * (sample_rate // frame_length)
                
                self.speech_buffer.append(audio_data)
                while len(self.speech_buffer) > max_buffer_size:
                    self.speech_buffer.pop(0)
            
            with sd.InputStream(samplerate=sample_rate, channels=1, callback=audio_callback, blocksize=frame_length):
                self.logger.info("Audio-Stream gestartet")
                
                while self.is_listening:
                    try:
                        # Audio-Frame aus der Warteschlange holen
                        audio_frame = self.audio_queue.get(timeout=1.0)
                        
                        # Wake-Word-Erkennung
                        wake_word_detected = self.wake_word_service.process_frame(audio_frame)
                        
                        if wake_word_detected:
                            self.logger.info("Wake-Word erkannt!")
                            self.stats["wake_word_detections"] += 1
                            
                            # Ändere Zustand auf "Hören"
                            with self.state_lock:
                                self.current_state = "listening"
                            
                            # Bestätigungston abspielen
                            self.audio_feedback.play_activation_sound()
                            
                            # Benachrichtigung über Event-Bus senden
                            self.event_bus.publish(
                                "event.wake_word_detected",
                                "",
                                "NOTIFICATION",
                                "voice_module",
                                {"timestamp": time.time()}
                            )
                            
                            # Sammle Audio für Spracherkennung
                            speech_audio = self._collect_speech_audio(additional_seconds=2.0)
                            
                            # Erkenne die Sprache
                            start_time = time.time()
                            text, confidence = self.stt_service.recognize(speech_audio)
                            stt_time_ms = (time.time() - start_time) * 1000
                            
                            # Statistik aktualisieren
                            self.stats["speech_recognitions"] += 1
                            self.stats["average_stt_time_ms"] = (
                                (self.stats["average_stt_time_ms"] * (self.stats["speech_recognitions"] - 1) + stt_time_ms) 
                                / self.stats["speech_recognitions"]
                            )
                            
                            # Zurück zum Idle-Zustand
                            with self.state_lock:
                                self.current_state = "idle"
                            
                            if text:
                                self.logger.info(f"Erkannt: {text} (Konfidenz: {confidence:.2f})")
                                
                                # Prüfe, ob es sich um einen häufigen Befehl handelt
                                if self._process_common_command(text, confidence):
                                    # Bestätigungston abspielen
                                    self.audio_feedback.play_acknowledgement_sound()
                                    continue
                                
                                # Veröffentliche erkannten Text im Event-Bus
                                self.event_bus.publish(
                                    "event.speech_recognized",
                                    text,
                                    "DATA",
                                    "voice_module",
                                    {
                                        "confidence": confidence,
                                        "timestamp": time.time(),
                                        "processing_time_ms": stt_time_ms
                                    }
                                )
                                
                                # Bestätigungston abspielen
                                self.audio_feedback.play_acknowledgement_sound()
                            else:
                                self.logger.warning("Sprache nicht erkannt oder leere Eingabe")
                                # Fehlerton abspielen
                                self.audio_feedback.play_error_sound()
                    
                    except queue.Empty:
                        continue
                    except Exception as e:
                        self.logger.error(f"Fehler im Audio-Verarbeitungs-Loop: {e}")
                        time.sleep(0.1)
        
        except Exception as e:
            self.logger.error(f"Fehler beim Starten des Audio-Streams: {e}")
            self.health_status = False
    
    def _collect_speech_audio(self, additional_seconds=2.0) -> np.ndarray:
        """
        Sammelt Sprachaudio aus dem Puffer plus zusätzliche Sekunden.
        
        Args:
            additional_seconds: Zusätzliche Zeit in Sekunden
            
        Returns:
            Gesammeltes Audio als NumPy-Array
        """
        # Kopiere den vorhandenen Puffer
        buffer_audio = np.concatenate(self.speech_buffer) if self.speech_buffer else np.array([], dtype=np.int16)
        
        # Sammle zusätzliches Audio für die angegebene Zeit
        sample_rate = self.config.get("audio", {}).get("sample_rate", 16000)
        frame_length = self.config.get("audio", {}).get("frame_length", 512)
        frames_needed = int(additional_seconds * sample_rate / frame_length)
        
        additional_frames = []
        for _ in range(frames_needed):
            try:
                frame = self.audio_queue.get(timeout=1.0)
                additional_frames.append(frame)
            except queue.Empty:
                break
        
        # Wenn zusätzliche Frames gesammelt wurden, füge sie hinzu
        if additional_frames:
            additional_audio = np.concatenate(additional_frames)
            return np.concatenate([buffer_audio, additional_audio])
        else:
            return buffer_audio
    
    def _process_common_command(self, text: str, confidence: float) -> bool:
        """
        Verarbeitet häufige Befehle direkt ohne Umweg über das Hirn-Modul.
        
        Args:
            text: Erkannter Text
            confidence: Konfidenz der Spracherkennung
            
        Returns:
            True, wenn der Befehl direkt verarbeitet wurde, sonst False
        """
        # Schwellwert für Konfidenz
        if confidence < 0.6:
            return False
        
        # Text normalisieren
        text_lower = text.lower()
        
        # Lautstärke-Steuerung
        if "lauter" in text_lower:
            self._adjust_volume(increase=True)
            asyncio.run_coroutine_threadsafe(
                self.speak("Lautstärke erhöht"), 
                asyncio.get_event_loop()
            )
            return True
        elif "leiser" in text_lower:
            self._adjust_volume(increase=False)
            asyncio.run_coroutine_threadsafe(
                self.speak("Lautstärke verringert"), 
                asyncio.get_event_loop()
            )
            return True
        
        # Stopp-Befehle
        elif any(word in text_lower for word in ["stopp", "stop", "halt", "hör auf"]):
            # Veröffentliche Stopp-Befehl auf dem Event-Bus
            self.event_bus.publish(
                "command.stop_current_action",
                "",
                "COMMAND",
                "voice_module"
            )
            
            asyncio.run_coroutine_threadsafe(
                self.speak("Ich stoppe die aktuelle Aktion"),
                asyncio.get_event_loop()
            )
            return True
        
        # Stimme ändern
        elif "ändere deine stimme" in text_lower or "andere stimme" in text_lower:
            voices = self.tts_service.get_available_voices()
            
            # Wähle eine andere Stimme als die aktuelle
            current_voice = self.config.get("text_to_speech", {}).get("voice", "")
            new_voice = next((v for v in voices if v != current_voice), voices[0] if voices else "")
            
            if new_voice:
                self._change_voice(new_voice)
                asyncio.run_coroutine_threadsafe(
                    self.speak(f"Ich verwende jetzt die Stimme {new_voice}"),
                    asyncio.get_event_loop()
                )
                return True
        
        # Weitere einfache Befehle...
        
        # Kein bekannter Befehl
        return False
    
    async def _handle_speak_command(self, event: EventMessage):
        """Verarbeitet Sprachausgabe-Befehle vom Event-Bus."""
        try:
            # Text extrahieren
            text = event.payload.decode('utf-8') if isinstance(event.payload, bytes) else event.payload
            
            # Metadaten extrahieren
            metadata = event.metadata or {}
            priority = metadata.get("priority", 1)  # 1 = normal, 2 = hoch
            
            # Statistik aktualisieren
            self.stats["tts_requests"] += 1
            
            # Zur TTS-Warteschlange hinzufügen
            await self.tts_queue.put({
                "text": text,
                "priority": priority,
                "metadata": metadata,
                "message_id": event.message_id
            })
            
            self.logger.debug(f"Sprachausgabe-Befehl zur Warteschlange hinzugefügt: {text[:30]}...")
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung eines Sprachausgabe-Befehls: {e}")
    
    async def _handle_mobile_voice_input(self, event: EventMessage):
        """Verarbeitet Spracheingaben von mobilen Geräten."""
        try:
            # Audio-Daten extrahieren
            audio_data = event.payload
            metadata = event.metadata or {}
            
            # Audio an STT-Service übergeben
            start_time = time.time()
            text, confidence = await self.stt_service.recognize_audio_data(audio_data)
            stt_time_ms = (time.time() - start_time) * 1000
            
            # Statistik aktualisieren
            self.stats["speech_recognitions"] += 1
            self.stats["average_stt_time_ms"] = (
                (self.stats["average_stt_time_ms"] * (self.stats["speech_recognitions"] - 1) + stt_time_ms) 
                / self.stats["speech_recognitions"]
            )
            
            if text:
                self.logger.info(f"Mobile Spracheingabe erkannt: {text} (Konfidenz: {confidence:.2f})")
                
                # Veröffentliche erkannten Text im Event-Bus
                self.event_bus.publish(
                    "event.speech_recognized",
                    text,
                    "DATA",
                    "voice_module",
                    {
                        "confidence": confidence,
                        "timestamp": time.time(),
                        "processing_time_ms": stt_time_ms,
                        "source": "mobile",
                        "device_id": metadata.get("device_id")
                    }
                )
                
                # Bestätigung an das mobile Gerät senden
                self.event_bus.publish(
                    "mobile.voice_recognition_result",
                    json.dumps({"success": True, "text": text, "confidence": confidence}),
                    "RESPONSE",
                    "voice_module",
                    {"original_message_id": event.message_id}
                )
            else:
                self.logger.warning("Mobile Spracheingabe nicht erkannt oder leere Eingabe")
                
                # Fehlermeldung an das mobile Gerät senden
                self.event_bus.publish(
                    "mobile.voice_recognition_result",
                    json.dumps({"success": False, "error": "Sprache nicht erkannt"}),
                    "RESPONSE",
                    "voice_module",
                    {"original_message_id": event.message_id}
                )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer mobilen Spracheingabe: {e}")
            
            # Fehlermeldung an das mobile Gerät senden
            self.event_bus.publish(
                "mobile.voice_recognition_result",
                json.dumps({"success": False, "error": str(e)}),
                "RESPONSE",
                "voice_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_mobile_speak_command(self, event: EventMessage):
        """Verarbeitet Sprachausgabe-Befehle für mobile Geräte."""
        try:
            # Daten extrahieren
            data = json.loads(event.payload) if isinstance(event.payload, bytes) else json.loads(event.payload)
            text = data.get("text", "")
            device_id = data.get("device_id")
            
            if not device_id:
                self.logger.error("Mobile Sprachausgabe ohne Geräte-ID angefordert")
                return
            
            # Statistik aktualisieren
            self.stats["tts_requests"] += 1
            
            # Audio für Text generieren
            audio_data = await self.tts_service.synthesize_speech(text)
            
            # Audio an das mobile Gerät senden
            self.event_bus.publish(
                "mobile.audio_data",
                audio_data,
                "DATA",
                "voice_module",
                {
                    "device_id": device_id,
                    "format": "wav",
                    "text": text,
                    "original_message_id": event.message_id
                }
            )
            
            self.logger.debug(f"Sprachdaten an mobiles Gerät {device_id} gesendet: {text[:30]}...")
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung eines mobilen Sprachausgabe-Befehls: {e}")
            
            # Fehlermeldung an das mobile Gerät senden
            self.event_bus.publish(
                "mobile.error",
                json.dumps({"error": "Sprachsynthese fehlgeschlagen", "details": str(e)}),
                "ERROR",
                "voice_module",
                {"original_message_id": event.message_id}
            )
    
    async def _process_tts_queue(self):
        """Verarbeitet TTS-Anfragen asynchron in einer Schleife."""
        while self.is_running:
            try:
                # Warte auf die nächste TTS-Anfrage
                item = await self.tts_queue.get()
                
                # Extrahiere Daten
                text = item["text"]
                priority = item.get("priority", 1)
                metadata = item.get("metadata", {})
                message_id = item.get("message_id")
                
                # Setze Zustand auf "Sprechen"
                with self.state_lock:
                    previous_state = self.current_state
                    self.current_state = "speaking"
                
                # Benachrichtigung über Sprachausgabe-Start senden
                self.event_bus.publish(
                    "event.speech_started",
                    text,
                    "NOTIFICATION",
                    "voice_module",
                    {
                        "timestamp": time.time(),
                        "original_message_id": message_id
                    }
                )
                
                # Sprachausgabe durchführen
                start_time = time.time()
                await self.tts_service.speak(text)
                processing_time_ms = (time.time() - start_time) * 1000
                
                # Zurück zum vorherigen Zustand
                with self.state_lock:
                    self.current_state = previous_state
                
                # Benachrichtigung über Sprachausgabe-Ende senden
                self.event_bus.publish(
                    "event.speech_completed",
                    text,
                    "NOTIFICATION",
                    "voice_module",
                    {
                        "timestamp": time.time(),
                        "processing_time_ms": processing_time_ms,
                        "original_message_id": message_id
                    }
                )
                
                # Markiere Anfrage als erledigt
                self.tts_queue.task_done()
                
                self.logger.debug(f"Sprachausgabe abgeschlossen: {text[:30]}... ({processing_time_ms:.2f}ms)")
            
           ```python
                except asyncio.CancelledError:
                    # Task wurde abgebrochen (z.B. bei Modulstop)
                    break
                
                except Exception as e:
                    self.logger.error(f"Fehler bei der Sprachausgabe: {e}")
                    time.sleep(0.5)  # Kurze Pause bei Fehler
    
    async def speak(self, text: str, priority: int = 1, wait: bool = False):
        """
        Gibt Text als Sprache aus.
        
        Args:
            text: Der zu sprechende Text
            priority: Priorität (1 = normal, 2 = hoch)
            wait: Wenn True, wartet auf die Fertigstellung
        """
        item = {
            "text": text,
            "priority": priority,
            "metadata": {}
        }
        
        if wait:
            # Direktes Aussprechen im aktuellen Thread
            with self.state_lock:
                previous_state = self.current_state
                self.current_state = "speaking"
            
            try:
                await self.tts_service.speak(text)
            finally:
                with self.state_lock:
                    self.current_state = previous_state
        else:
            # Zur Warteschlange hinzufügen
            await self.tts_queue.put(item)
    
    def _adjust_volume(self, increase: bool = True):
        """Passt die Systemlautstärke an."""
        step = self.config.get("audio", {}).get("volume_step", 10)  # Prozentuale Änderung
        current_volume = self.config.get("text_to_speech", {}).get("volume", 100)
        
        if increase:
            new_volume = min(100, current_volume + step)
        else:
            new_volume = max(0, current_volume - step)
        
        # Aktualisiere Konfiguration
        self.config["text_to_speech"]["volume"] = new_volume
        
        # Aktualisiere TTS-Service
        self.tts_service.set_volume(new_volume)
        
        self.logger.debug(f"Lautstärke angepasst: {current_volume} -> {new_volume}")
    
    def _change_voice(self, voice_id: str):
        """Ändert die verwendete Stimme."""
        # Aktualisiere Konfiguration
        self.config["text_to_speech"]["voice"] = voice_id
        
        # Aktualisiere TTS-Service
        self.tts_service.set_voice(voice_id)
        
        self.logger.debug(f"Stimme geändert zu: {voice_id}")
    
    async def _handle_start_listening(self, event: EventMessage):
        """Behandelt den Befehl zum Starten des Zuhörens."""
        if not self.is_listening:
            self.is_listening = True
            
            # Starte Audio-Thread, falls noch nicht aktiv
            if not self.audio_thread or not self.audio_thread.is_alive():
                self.audio_thread = threading.Thread(target=self._audio_processing_loop, daemon=True)
                self.audio_thread.start()
            
            self.logger.info("Zuhören gestartet")
            
            # Bestätigung senden
            self.event_bus.publish(
                "event.listening_started",
                "",
                "NOTIFICATION",
                "voice_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_stop_listening(self, event: EventMessage):
        """Behandelt den Befehl zum Stoppen des Zuhörens."""
        if self.is_listening:
            self.is_listening = False
            
            self.logger.info("Zuhören gestoppt")
            
            # Bestätigung senden
            self.event_bus.publish(
                "event.listening_stopped",
                "",
                "NOTIFICATION",
                "voice_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_adjust_volume(self, event: EventMessage):
        """Behandelt den Befehl zur Lautstärkeanpassung."""
        try:
            # Daten extrahieren
            data = json.loads(event.payload) if isinstance(event.payload, bytes) else json.loads(event.payload)
            increase = data.get("increase", True)
            
            # Lautstärke anpassen
            self._adjust_volume(increase)
            
            # Bestätigung senden
            new_volume = self.config.get("text_to_speech", {}).get("volume", 100)
            self.event_bus.publish(
                "event.volume_adjusted",
                str(new_volume),
                "NOTIFICATION",
                "voice_module",
                {"original_message_id": event.message_id}
            )
        except Exception as e:
            self.logger.error(f"Fehler bei der Lautstärkeanpassung: {e}")
    
    async def _handle_change_voice(self, event: EventMessage):
        """Behandelt den Befehl zum Ändern der Stimme."""
        try:
            # Daten extrahieren
            data = json.loads(event.payload) if isinstance(event.payload, bytes) else json.loads(event.payload)
            voice_id = data.get("voice_id")
            
            if not voice_id:
                self.logger.error("Stimmenänderung ohne Stimmen-ID angefordert")
                return
            
            # Stimme ändern
            self._change_voice(voice_id)
            
            # Bestätigung senden
            self.event_bus.publish(
                "event.voice_changed",
                voice_id,
                "NOTIFICATION",
                "voice_module",
                {"original_message_id": event.message_id}
            )
        except Exception as e:
            self.logger.error(f"Fehler beim Ändern der Stimme: {e}")
    
    async def get_capabilities(self) -> List[str]:
        """Gibt die Fähigkeiten des Moduls zurück."""
        return [
            "text_to_speech",
            "speech_to_text",
            "wake_word_detection",
            "audio_feedback"
        ]
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob das Modul gesund ist."""
        return self.health_status and self.is_running and self.tts_service.is_healthy() and self.stt_service.is_healthy()
    
    def get_uptime(self) -> float:
        """Gibt die Laufzeit des Moduls in Sekunden zurück."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    def get_stats(self) -> Dict[str, Any]:
        """Gibt Statistiken zum Modul zurück."""
        return self.stats
```

### 4.5 Augen-Modul (vision_module.py)

Das Augen-Modul ist für die Bildschirmanalyse, OCR und Kamerabilderkennung zuständig:

```python
# vision_module.py
import asyncio
import logging
import time
import threading
import numpy as np
import json
from typing import Dict, List, Any, Optional, Tuple
import cv2

from assistant.common.event_bus import EventBus, EventMessage
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager
from assistant.services.ocr_service import OCRService
from assistant.services.camera_service import CameraService

class VisionModule:
    """
    Analysiert visuelle Informationen wie Bildschirminhalte und Kamerabilder,
    einschließlich OCR, UI-Elementenerkennung und Bildverständnis.
    """
    
    def __init__(self, event_bus: EventBus, shortcut_registry: ShortcutPathRegistry,
                config_path: str = "./config/vision_module.yaml"):
        """
        Initialisiert das Augen-Modul.
        
        Args:
            event_bus: Event-Bus für die Kommunikation
            shortcut_registry: Registry für Abkürzungspfade
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("vision_module")
        
        # Referenzen speichern
        self.event_bus = event_bus
        self.shortcut_registry = shortcut_registry
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Dienste initialisieren
        self.ocr_service = OCRService(self.config.get("ocr", {}))
        
        # Kamera-Service (optional)
        self.camera_enabled = self.config.get("camera", {}).get("enabled", False)
        self.camera_service = None
        if self.camera_enabled:
            self.camera_service = CameraService(self.config.get("camera", {}))
        
        # Bildschirmanalyse
        self.screen_analysis_enabled = self.config.get("screen_analysis", {}).get("enabled", True)
        self.screen_analyzer = None
        if self.screen_analysis_enabled:
            from assistant.services.screen_analyzer_service import ScreenAnalyzerService
            self.screen_analyzer = ScreenAnalyzerService(self.config.get("screen_analysis", {}))
        
        # Bildschirmlupe
        self.magnifier_enabled = self.config.get("magnifier", {}).get("enabled", True)
        self.magnifier = None
        if self.magnifier_enabled:
            from assistant.services.magnifier_service import MagnifierService
            self.magnifier = MagnifierService(self.config.get("magnifier", {}))
        
        # Bildverständnis (Vision-Modell)
        self.image_understanding_enabled = self.config.get("image_understanding", {}).get("enabled", False)
        self.image_understanding_service = None
        if self.image_understanding_enabled:
            from assistant.services.image_understanding_service import ImageUnderstandingService
            self.image_understanding_service = ImageUnderstandingService(
                self.config.get("image_understanding", {})
            )
        
        # Analyse-Thread
        self.analysis_active = False
        self.analysis_thread = None
        
        # Status
        self.start_time = None
        self.is_running = False
        self.health_status = True
        
        # Statistiken
        self.stats = {
            "screen_captures": 0,
            "ocr_requests": 0,
            "camera_captures": 0,
            "image_descriptions": 0,
            "average_ocr_time_ms": 0
        }
        
        # Regionen von Interesse (für OCR, etc.)
        self.regions_of_interest = {}
        
        self.logger.info("Augen-Modul initialisiert")
    
    async def start(self):
        """Startet das Augen-Modul."""
        self.logger.info("Starte Augen-Modul")
        self.is_running = True
        self.start_time = time.time()
        
        # Dienste starten
        await self.ocr_service.start()
        
        if self.camera_enabled and self.camera_service:
            await self.camera_service.start()
        
        if self.screen_analysis_enabled and self.screen_analyzer:
            await self.screen_analyzer.start()
        
        if self.magnifier_enabled and self.magnifier:
            await self.magnifier.start()
        
        if self.image_understanding_enabled and self.image_understanding_service:
            await self.image_understanding_service.start()
        
        # Event-Subscriptions einrichten
        self._setup_event_subscriptions()
        
        # Abkürzungspfade registrieren
        self._register_shortcuts()
        
        # Bildschirmanalyse starten (falls aktiviert)
        if self.screen_analysis_enabled:
            self.start_continuous_analysis()
        
        self.logger.info("Augen-Modul gestartet")
    
    async def stop(self):
        """Stoppt das Augen-Modul."""
        self.logger.info("Stoppe Augen-Modul")
        self.is_running = False
        
        # Bildschirmanalyse stoppen
        self.stop_continuous_analysis()
        
        # Dienste stoppen
        await self.ocr_service.stop()
        
        if self.camera_enabled and self.camera_service:
            await self.camera_service.stop()
        
        if self.screen_analysis_enabled and self.screen_analyzer:
            await self.screen_analyzer.stop()
        
        if self.magnifier_enabled and self.magnifier:
            await self.magnifier.stop()
        
        if self.image_understanding_enabled and self.image_understanding_service:
            await self.image_understanding_service.stop()
        
        self.logger.info("Augen-Modul gestoppt")
    
    def _setup_event_subscriptions(self):
        """Richtet Event-Subscriptions ein."""
        # OCR-Anfragen
        self.event_bus.subscribe("command.ocr.extract_text", self._handle_ocr_command)
        
        # Kamera-Befehle
        if self.camera_enabled:
            self.event_bus.subscribe("command.camera.take_photo", self._handle_take_photo_command)
            self.event_bus.subscribe("command.camera.start_video", self._handle_start_video_command)
            self.event_bus.subscribe("command.camera.stop_video", self._handle_stop_video_command)
        
        # Bildschirmlupe
        if self.magnifier_enabled:
            self.event_bus.subscribe("command.magnify_screen", self._handle_magnify_command)
            self.event_bus.subscribe("command.magnifier.set_zoom", self._handle_set_zoom_command)
        
        # Bildschirmanalyse
        if self.screen_analysis_enabled:
            self.event_bus.subscribe("command.screen.capture", self._handle_screen_capture_command)
            self.event_bus.subscribe("command.screen.analyze", self._handle_screen_analyze_command)
        
        # Bildbeschreibung
        if self.image_understanding_enabled:
            self.event_bus.subscribe("query.vision.describe_image", self._handle_describe_image_query)
    
    def _register_shortcuts(self):
        """Registriert optimierte Abkürzungspfade."""
        # Direkter Pfad für OCR-Ergebnisse zum Hirn-Modul
        self.shortcut_registry.register_shortcut(
            "vision_module",
            "brain_module",
            "ocr_results",
            self._shortcut_handle_ocr_results
        )
        
        # Direkter Pfad für Bildschirmregionen zum Digitalsinn-Modul
        self.shortcut_registry.register_shortcut(
            "vision_module",
            "digital_module",
            "screen_regions",
            self._shortcut_handle_screen_regions
        )
    
    def _shortcut_handle_ocr_results(self, payload):
        """Leitet OCR-Ergebnisse direkt an das Hirn-Modul weiter."""
        try:
            # OCR-Ergebnisse parsen
            ocr_data = json.loads(payload)
            
            # Konvertiere das Format für das Hirn-Modul
            processed_data = {
                "text": ocr_data.get("text", ""),
                "regions": ocr_data.get("regions", []),
                "confidence": ocr_data.get("confidence", 0.0),
                "source": ocr_data.get("source", "screen")
            }
            
            return {"success": True, "processed_data": processed_data}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung von OCR-Ergebnissen: {e}")
            return {"success": False, "reason": str(e)}
    
    def _shortcut_handle_screen_regions(self, payload):
        """Leitet erkannte Bildschirmregionen direkt an das Digitalsinn-Modul weiter."""
        try:
            # Regionsdaten parsen
            regions_data = json.loads(payload)
            
            # Konvertiere das Format für das Digitalsinn-Modul
            processed_data = {
                "ui_elements": regions_data.get("ui_elements", []),
                "text_regions": regions_data.get("text_regions", []),
                "interactive_elements": regions_data.get("interactive_elements", []),
                "timestamp": time.time()
            }
            
            return {"success": True, "processed_data": processed_data}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung von Bildschirmregionen: {e}")
            return {"success": False, "reason": str(e)}
    
    def start_continuous_analysis(self):
        """Startet kontinuierliche Bildschirmanalyse."""
        if self.analysis_active:
            return
            
        self.analysis_active = True
        self.analysis_thread = threading.Thread(target=self._analysis_loop, daemon=True)
        self.analysis_thread.start()
        
        self.logger.info("Kontinuierliche Bildschirmanalyse gestartet")
    
    def stop_continuous_analysis(self):
        """Stoppt kontinuierliche Bildschirmanalyse."""
        if not self.analysis_active:
            return
        
        self.analysis_active = False
        
        # Auf Beendigung des Analyse-Threads warten
        if self.analysis_thread and self.analysis_thread.is_alive():
            self.analysis_thread.join(timeout=2.0)
        
        self.logger.info("Kontinuierliche Bildschirmanalyse gestoppt")
    
    def _analysis_loop(self):
        """Kontinuierliche Bildschirmanalyse im Hintergrund."""
        update_interval = self.config.get("screen_analysis", {}).get("update_interval_ms", 500) / 1000.0
        
        while self.analysis_active and self.is_running:
            try:
                # Bildschirm erfassen
                screen = self.screen_analyzer.capture_screen()
                self.stats["screen_captures"] += 1
                
                # OCR durchführen (wenn aktiviert)
                if self.config.get("ocr", {}).get("continuous_analysis", True):
                    start_time = time.time()
                    ocr_result = self.ocr_service.extract_text(screen)
                    ocr_time_ms = (time.time() - start_time) * 1000
                    
                    # Statistik aktualisieren
                    self.stats["ocr_requests"] += 1
                    self.stats["average_ocr_time_ms"] = (
                        (self.stats["average_ocr_time_ms"] * (self.stats["ocr_requests"] - 1) + ocr_time_ms) 
                        / self.stats["ocr_requests"]
                    )
                    
                    # Textbereiche veröffentlichen
                    if ocr_result and ocr_result.get("text"):
                        self.event_bus.publish(
                            "data.text_regions",
                            json.dumps(ocr_result),
                            "DATA",
                            "vision_module",
                            {"count": len(ocr_result.get("regions", [])), "timestamp": time.time()}
                        )
                
                # UI-Elemente erkennen (wenn aktiviert)
                if self.screen_analyzer and self.config.get("screen_analysis", {}).get("detect_ui_elements", True):
                    ui_elements = self.screen_analyzer.detect_ui_elements(screen)
                    
                    # UI-Elemente veröffentlichen
                    if ui_elements:
                        self.event_bus.publish(
                            "data.ui_elements",
                            json.dumps(ui_elements),
                            "DATA",
                            "vision_module",
                            {"count": len(ui_elements), "timestamp": time.time()}
                        )
                
                # Verarbeitung der Regionen von Interesse (wenn vorhanden)
                for roi_id, roi_info in self.regions_of_interest.items():
                    if time.time() - roi_info.get("last_processed", 0) >= roi_info.get("interval", 1.0):
                        # Region extrahieren
                        region = roi_info["region"]
                        x, y, width, height = region
                        
                        # Bildausschnitt erstellen
                        roi_img = screen[y:y+height, x:x+width]
                        
                        # Region verarbeiten
                        if roi_info.get("type") == "ocr":
                            # OCR für Region durchführen
                            roi_text = self.ocr_service.extract_text(roi_img)
                            
                            # Ergebnis veröffentlichen
                            self.event_bus.publish(
                                f"data.roi.{roi_id}",
                                json.dumps(roi_text),
                                "DATA",
                                "vision_module",
                                {"roi_id": roi_id, "timestamp": time.time()}
                            )
                        
                        # Aktualisiere Zeitstempel
                        self.regions_of_interest[roi_id]["last_processed"] = time.time()
                
                # Pause vor nächstem Frame
                time.sleep(update_interval)
            
            except Exception as e:
                self.logger.error(f"Fehler im Analyse-Loop: {e}")
                time.sleep(1.0)  # Längere Pause bei Fehler
    
    async def _handle_ocr_command(self, event: EventMessage):
        """Behandelt OCR-Anfragen."""
        try:
            # Parameter extrahieren
            params = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            
            # Quelle bestimmen (Bildschirm, Datei, oder Bild)
            source = params.get("source", "screen")
            
            ocr_result = None
            
            if source == "screen":
                # Bildschirmbereich bestimmen
                region = params.get("region")
                
                # Bildschirm erfassen
                screen = self.screen_analyzer.capture_screen()
                
                # Wenn Region angegeben, Bildausschnitt erstellen
                if region:
                    x, y, width, height = region
                    screen = screen[y:y+height, x:x+width]
                
                # OCR durchführen
                ocr_result = self.ocr_service.extract_text(screen)
            
            elif source == "image":
                # Bild aus Daten laden
                image_data = params.get("image_data")
                if image_data:
                    img = np.frombuffer(image_data, dtype=np.uint8)
                    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                    
                    # OCR durchführen
                    ocr_result = self.ocr_service.extract_text(img)
                else:
                    self.logger.error("OCR-Anfrage ohne Bilddaten")
                    return
            
            elif source == "file":
                # Bilddatei laden
                file_path = params.get("file_path")
                if file_path:
                    img = cv2.imread(file_path)
                    
                    # OCR durchführen
                    ocr_result = self.ocr_service.extract_text(img)
                else:
                    self.logger.error("OCR-Anfrage ohne Dateipfad")
                    return
            
            # Ergebnis veröffentlichen
            if ocr_result:
                self.event_bus.publish(
                    "response.ocr.text",
                    json.dumps(ocr_result),
                    "RESPONSE",
                    "vision_module",
                    {"original_message_id": event.message_id}
                )
                
                # Wenn angefordert, Text vorlesen
                if params.get("read_aloud", False):
                    self.event_bus.publish(
                        "command.speak",
                        ocr_result.get("text", "Kein Text erkannt"),
                        "COMMAND",
                        "vision_module",
                        {"original_message_id": event.message_id}
                    )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der OCR-Verarbeitung: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.ocr.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "vision_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_take_photo_command(self, event: EventMessage):
        """Behandelt Anfragen zur Fotoaufnahme."""
        if not self.camera_enabled or not self.camera_service:
            self.logger.error("Kamera ist nicht aktiviert")
            return
        
        try:
            # Parameter extrahieren
            params = {}
            if event.payload:
                try:
                    params = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
                except:
                    pass
            
            # Foto aufnehmen
            photo = await self.camera_service.take_photo()
            self.stats["camera_captures"] += 1
            
            # Wenn beschreiben, dann Bildbeschreibung erstellen
            if params.get("describe", True) and self.image_understanding_enabled:
                description = await self.image_understanding_service.describe_image(photo)
                
                # Beschreibung veröffentlichen
                self.event_bus.publish(
                    "response.camera.photo_description",
                    json.dumps({"description": description}),
                    "RESPONSE",
                    "vision_module",
                    {"original_message_id": event.message_id}
                )
                
                # Beschreibung vorlesen, wenn angefordert
                if params.get("read_aloud", True):
                    self.event_bus.publish(
                        "command.speak",
                        f"Ich sehe: {description}",
                        "COMMAND",
                        "vision_module",
                        {"original_message_id": event.message_id}
                    )
            
            # Bilddaten oder Dateipfad zurückgeben
            if params.get("return_data", False):
                # Bild kodieren
                _, img_encoded = cv2.imencode(".jpg", photo)
                
                # Bilddaten zurückgeben
                self.event_bus.publish(
                    "response.camera.photo",
                    img_encoded.tobytes(),
                    "RESPONSE",
                    "vision_module",
                    {
                        "original_message_id": event.message_id,
                        "format": "jpg",
                        "width": photo.shape[1],
                        "height": photo.shape[0]
                    }
                )
            else:
                # Bild speichern
                import os
                import datetime
                
                save_dir = self.config.get("camera", {}).get("save_dir", "./data/camera")
                os.makedirs(save_dir, exist_ok=True)
                
                filename = f"photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                file_path = os.path.join(save_dir, filename)
                
                cv2.imwrite(file_path, photo)
                
                # Dateipfad zurückgeben
                self.event_bus.publish(
                    "response.camera.photo_path",
                    json.dumps({"file_path": file_path}),
                    "RESPONSE",
                    "vision_module",
                    {"original_message_id": event.message_id}
                )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Fotoaufnahme: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.camera.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "vision_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_magnify_command(self, event: EventMessage):
        """Behandelt Anfragen zur Bildschirmvergrößerung."""
        if not self.magnifier_enabled or not self.magnifier:
            self.logger.error("Bildschirmlupe ist nicht aktiviert")
            return
        
        try:
            # Parameter extrahieren
            params = {}
            if event.payload:
                try:
                    params = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
                except:
                    pass
            
            # Region bestimmen (falls angegeben)
            region_name = params.get("region")
            
            if region_name:
                # Vordefinierte Region verwenden
                if region_name == "center":
                    await self.magnifier.focus_center()
                elif region_name == "top":
                    await self.magnifier.focus_top()
                elif region_name == "bottom":
                    await self.magnifier.focus_bottom()
                elif region_name == "left":
                    await self.magnifier.focus_left()
                elif region_name == "right":
                    await self.magnifier.focus_right()
                else:
                    self.logger.warning(f"Unbekannte Region: {region_name}")
            else:
                # Benutzerdefinierte Region oder automatische Fokussierung
                if "x" in params and "y" in params:
                    # Benutzerdefinierte Koordinaten
                    x = params.get("x")
                    y = params.get("y")
                    await self.magnifier.focus_point(x, y)
                elif params.get("auto_focus", False):
                    # Automatische Fokussierung auf Text oder UI-Elemente
                    await self.magnifier.auto_focus()
                else:
                    # Standardmäßig Bildschirmmitte vergrößern
                    await self.magnifier.focus_center()
            
            # Zoom-Faktor einstellen (falls angegeben)
            zoom = params.get("zoom")
            if zoom:
                await self.magnifier.set_zoom(zoom)
            
            # Status-Update senden
            status = await self.magnifier.get_status()
            self.event_bus.publish(
                "event.magnifier.status",
                json.dumps(status),
                "NOTIFICATION",
                "vision_module",
                {"original_message_id": event.message_id}
            )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Bildschirmvergrößerung: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.magnifier.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "vision_module",
                {"original_message_id": event.message_id}
            )
    
    async def _handle_describe_image_query(self, event: EventMessage):
        """Behandelt Anfragen zur Bildbeschreibung."""
        if not self.image_understanding_enabled or not self.image_understanding_service:
            self.logger.error("Bildverständnis ist nicht aktiviert")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.vision.image_description",
                "Bildverständnis ist nicht aktiviert",
                "ERROR",
                "vision_module",
                {"original_message_id": event.message_id, "error": "service_disabled"}
            )
            return
        
        try:
            # Bilddaten extrahieren
            image_data = event.payload
            
            # Bild aus Daten laden
            if isinstance(image_data, bytes):
                img = np.frombuffer(image_data, dtype=np.uint8)
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            elif isinstance(image_data, str):
                # Prüfen, ob es sich um einen Dateipfad handelt
                if image_data.startswith("file://"):
                    file_path = image_data[7:]
                    img = cv2.imread(file_path)
                else:
                    # Versuche, als Base64-String zu interpretieren
                    import base64
                    img_data = base64.b64decode(image_data)
                    img = np.frombuffer(img_data, dtype=np.uint8)
                    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            else:
                # Als NumPy-Array oder OpenCV-Bild interpretieren
                img = image_data
            
            # Bildbeschreibung erstellen
            description = await self.image_understanding_service.describe_image(img)
            self.stats["image_descriptions"] += 1
            
            # Beschreibung zurücksenden
            self.event_bus.publish(
                "response.vision.image_description",
                description,
                "RESPONSE",
                "vision_module",
                {"original_message_id": event.message_id}
            )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Bildbeschreibung: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.vision.image_description",
                f"Fehler bei der Bildbeschreibung: {str(e)}",
                "ERROR",
                "vision_module",
                {"original_message_id": event.message_id, "error": str(e)}
            )
    
    async def get_capabilities(self) -> List[str]:
        """Gibt die Fähigkeiten des Moduls zurück."""
        capabilities = ["screen_capture", "ocr"]
        
        if self.camera_enabled:
            capabilities.append("camera")
        
        if self.magnifier_enabled:
            capabilities.append("screen_magnifier")
        
        if self.image_understanding_enabled:
            capabilities.append("image_understanding")
        
        return capabilities
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob das Modul gesund ist."""
        return self.health_status and self.is_running and self.ocr_service.is_healthy()
    
    def get_uptime(self) -> float:
        """Gibt die Laufzeit des Moduls in Sekunden zurück."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    def get_stats(self) -> Dict[str, Any]:
        """Gibt Statistiken zum Modul zurück."""
        return self.stats
```

### 4.6 Digitalsinn-Modul (digital_module.py)

Das Digitalsinn-Modul interagiert mit digitalen Schnittstellen wie Browsern und Apps:

```python
# digital_module.py
import asyncio
import logging
import time
import threading
import json
from typing import Dict, List, Any, Optional, Tuple

from assistant.common.event_bus import EventBus, EventMessage
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager

class DigitalModule:
    """
    Interagiert mit digitalen Schnittstellen wie Browsern, Apps und Betriebssystem.
    Ermöglicht automatisierte Aktionen und Extraktion von strukturierten Daten.
    """
    
    def __init__(self, event_bus: EventBus, shortcut_registry: ShortcutPathRegistry,
                config_path: str = "./config/digital_module.yaml"):
        """
        Initialisiert das Digitalsinn-Modul.
        
        Args:
            event_bus: Event-Bus für die Kommunikation
            shortcut_registry: Registry für Abkürzungspfade
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("digital_module")
        
        # Referenzen speichern
        self.event_bus = event_bus
        self.shortcut_registry = shortcut_registry
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Browser-Automation
        self.browser_automation_enabled = self.config.get("browser_automation", {}).get("enabled", True)
        self.browser_controller = None
        if self.browser_automation_enabled:
            from assistant.adapters.browser_adapter import BrowserController
            self.browser_controller = BrowserController(self.config.get("browser_automation", {}))
        
        # System-Automation
        self.system_automation_enabled = self.config.get("system_automation", {}).get("enabled", True)
        self.system_controller = None
        if self.system_automation_enabled:
            from assistant.adapters.system_adapter import SystemController
            self.system_controller = SystemController(self.config.get("system_automation", {}))
        
        # UI-Automation
        self.ui_automation_enabled = self.config.get("ui_automation", {}).get("enabled", True)
        self.ui_controller = None
        if self.ui_automation_enabled:
            from assistant.adapters.ui_adapter import UIController
            self.ui_controller = UIController(self.config.get("ui_automation", {}))
        
        # Prozess-Automation
        self.process_automation_enabled = self.config.get("process_automation", {}).get("enabled", False)
        self.process_controller = None
        if self.process_automation_enabled:
            from assistant.adapters.process_adapter import ProcessController
            self.process_controller = ProcessController(self.config.get("process_automation", {}))
        
        # Status
        self.start_time = None
        self.is_running = False
        self.health_status = True
        
        # Aktive Browser-Tabs
        self.active_tabs = {}
        
        # Zuletzt besuchte Webseiten (für Kontext)
        self.recent_pages = []
        self.max_recent_pages = self.config.get("browser_automation", {}).get("max_recent_pages", 10)
        
        # Gespeicherte Prozesse
        self.saved_processes = {}
        
        # Statistiken
        self.stats = {
            "web_navigations": 0,
            "web_extractions": 0,
            "ui_automations": 0,
            "system_commands": 0,
            "process_executions": 0
        }
        
        self.logger.info("Digitalsinn-Modul initialisiert")
    
    async def start(self):
        """Startet das Digitalsinn-Modul."""
        self.logger.info("Starte Digitalsinn-Modul")
        self.is_running = True
        self.start_time = time.time()
        
        # Browser-Controller starten (falls aktiviert)
        if self.browser_automation_enabled and self.browser_controller:
            await self.browser_controller.start()
        
        # System-Controller starten (falls aktiviert)
        if self.system_automation_enabled and self.system_controller:
            await self.system_controller.start()
        
        # UI-Controller starten (falls aktiviert)
        if self.ui_automation_enabled and self.ui_controller:
            await self.ui_controller.start()
        
        # Prozess-Controller starten (falls aktiviert)
        if self.process_automation_enabled and self.process_controller:
            await self.process_controller.start()
        
        # Event-Subscriptions einrichten
        self._setup_event_subscriptions()
        
        # Abkürzungspfade registrieren
        self._register_shortcuts()
        
        # Gespeicherte Prozesse laden
        await self._load_saved_processes()
        
        self.logger.info("Digitalsinn-Modul gestartet")
    
    async def stop(self):
        """Stoppt das Digitalsinn-Modul."""
        self.logger.info("Stoppe Digitalsinn-Modul")
        self.is_running = False
        
        # Browser-Controller stoppen
        if self.browser_automation_enabled and self.browser_controller:
            await self.browser_controller.stop()
        
        # System-Controller stoppen
        if self.system_automation_enabled and self.system_controller:
            await self.system_controller.stop()
        
        # UI-Controller stoppen
        if self.ui_automation_enabled and self.ui_controller:
            await self.ui_controller.stop()
        
        # Prozess-Controller stoppen
        if self.process_automation_enabled and self.process_controller:
            await self.process_controller.stop()
        
        self.logger.info("Digitalsinn-Modul gestoppt")
    
    def _setup_event_subscriptions(self):
        """Richtet Event-Subscriptions ein."""
        # Browser-Befehle
        if self.browser_automation_enabled:
            self.event_bus.subscribe("command.browse_website", self._handle_browse_website)
            self.event_bus.subscribe("command.browser.extract_content", self._handle_extract_content)
            self.event_bus.subscribe("command.browser.click", self._handle_browser_click)
            self.event_bus.subscribe("command.browser.fill_form", self._handle_fill_form)
        
        # System-Befehle
        if self.system_automation_enabled:
            self.event_bus.subscribe("command.system.open_app", self._handle_open_app)
            self.event_bus.subscribe("command.system.execute", self._handle_execute_command)
            self.event_bus.subscribe("command.system.copy_to_clipboard", self._handle_copy_to_clipboard)
        
        # UI-Automation
        if self.ui_automation_enabled:
            self.event_bus.subscribe("command.ui.click", self._handle_ui_click)
            self.event_bus.subscribe("command.ui.input", self._handle_ui_input)
            self.event_bus.subscribe("command.ui.find_element", self._handle_find_element)
        
        # Prozess-Automation
        if self.process_automation_enabled:
            self.event_bus.subscribe("command.process.save", self._handle_save_process)
            self.event_bus.subscribe("command.process.execute", self._handle_execute_process)
            self.event_bus.subscribe("command.process.list", self._handle_list_processes)
    
    def _register_shortcuts(self):
        """Registriert optimierte Abkürzungspfade."""
        # Direkter Pfad für Webseitenextraktion zum Hirn-Modul
        self.shortcut_registry.register_shortcut(
            "digital_module",
            "brain_module",
            "webpage_content",
            self._shortcut_handle_webpage_content
        )
        
        # Direkter Pfad für UI-Elemente vom Augen-Modul
        self.shortcut_registry.register_shortcut(
            "vision_module",
            "digital_module",
            "ui_elements",
            self._shortcut_handle_ui_elements
        )
    
    def _shortcut_handle_webpage_content(self, payload):
        """Leitet Webseiteninhalt direkt an das Hirn-Modul weiter."""
        try:
            # Webseiteninhalt parsen
            content_data = json.loads(payload)
            
            # Konvertiere das Format für das Hirn-Modul
            processed_data = {
                "title": content_data.get("title", ""),
                "url": content_data.get("url", ""),
                "main_content": content_data.get("main_content", ""),
                "summary": content_data.get("summary", ""),
                "links": content_data.get("links", [])
            }
            
            return {"success": True, "processed_data": processed_data}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung von Webseiteninhalt: {e}")
            return {"success": False, "reason": str(e)}
    
    def _shortcut_handle_ui_elements(self, payload):
        """Verarbeitet UI-Elemente direkt vom Augen-Modul."""
        try:
            # UI-Elemente parsen
            ui_data = json.loads(payload)
            
            # Elemente für UI-Automation registrieren
            if self.ui_controller:
                self.ui_controller.register_elements(ui_data)
            
            return {"success": True}
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung von UI-Elementen: {e}")
            return {"success": False, "reason": str(e)}
    
    async def _handle_browse_website(self, event: EventMessage):
        """Behandelt Befehle zum Öffnen einer Webseite."""
        if not self.browser_automation_enabled or not self.browser_controller:
            self.logger.error("Browser-Automation ist nicht aktiviert")
            return
        
        try:
            # URL extrahieren
            url = event.payload.decode('utf-8') if isinstance(event.payload, bytes) else event.payload
            
            # URL normalisieren (wenn nötig)
            if not url.startswith("http"):
                url = "https://" + url
            
            # Browser öffnen (falls noch nicht aktiv)
            if not self.browser_controller.is_browser_open():
                await self.browser_controller.open_browser()
            
            # Zu URL navigieren
            self.logger.info(f"Navigiere zu: {url}")
            page_content = await self.browser_controller.navigate_to_url(url)
            
            # Statistik aktualisieren
            self.stats["web_navigations"] += 1
            
            # Zu kürzlich besuchten Seiten hinzufügen
            self._add_to_recent_pages({
                "url": url,
                "title": page_content.get("title", ""),
                "timestamp": time.time()
            })
            
            # Extrahiere Hauptinhalt
            main_content = await self.browser_controller.extract_main_content()
            
            # Erstelle Zusammenfassung
            summary = await self._create_page_summary(main_content, url)
            
            # Extrahiere wichtige Links
            links = await self.browser_controller.extract_important_links()
            
            # Ergebnisse kombinieren
            result = {
                "url": url,
                "title": page_content.get("title", ""),
                "main_content": main_content,
                "summary": summary,
                "links": links,
                "timestamp": time.time()
            }
            
            # Ergebnis veröffentlichen
            self.event_bus.publish(
                "result.webpage_content",
                json.dumps(result),
                "DATA",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Optional: Sprachausgabe für Zusammenfassung
            if self.config.get("browser_automation", {}).get("speak_summary", True):
                self.event_bus.publish(
                    "command.speak",
                    f"Seite geladen. {summary}",
                    "COMMAND",
                    "digital_module"
                )
        
        except Exception as e:
            self.logger.error(f"Fehler beim Navigieren zur Webseite: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "result.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Fehlermeldung vorlesen
            self.event_bus.publish(
                "command.speak",
                f"Ich konnte die Webseite nicht öffnen: {str(e)}",
                "COMMAND",
                "digital_module"
            )
    
    async def _create_page_summary(self, content: str, url: str) -> str:
        """
        Erstellt eine Zusammenfassung der Webseite.
        
        Args:
            content: Hauptinhalt der Seite
            url: URL der Seite
            
        Returns:
            Zusammenfassung als Text
        """
        # Für komplexe Zusammenfassungen das Hirn-Modul verwenden
        summary_future = asyncio.Future()
        
        def summary_callback(event):
            summary = event.payload.decode('utf-8') if isinstance(event.payload, bytes) else event.payload
            summary_future.set_result(summary)
        
        # Anfrage an das Hirn-Modul senden
        request_id = f"summary_request_{time.time()}"
        
        self.event_bus.subscribe(f"response.summary.{request_id}", summary_callback)
        
        self.event_bus.publish(
            "query.summarize_text",
            json.dumps({
                "text": content[:10000],  # Beschränke auf die ersten 10000 Zeichen
                "url": url,
                "max_length": 200,
                "request_id": request_id
            }),
            "QUERY",
            "digital_module"
        )
        
        try:
            # Auf Antwort warten (mit Timeout)
            summary = await asyncio.wait_for(summary_future, timeout=5.0)
            return summary
        except asyncio.TimeoutError:
            # Bei Timeout einfache Zusammenfassung erstellen
            return self._create_simple_summary(content)
        finally:
            # Callback deregistrieren
            self.event_bus.unsubscribe(f"response.summary.{request_id}", summary_callback)
    
    def _create_simple_summary(self, content: str) -> str:
        """
        Erstellt eine einfache Zusammenfassung basierend auf den ersten Absätzen.
        
        Args:
            content: Textinhalt
            
        Returns:
            Einfache Zusammenfassung
        """
        # Einfache Zusammenfassung basierend auf den ersten Absätzen
        paragraphs = content.split("\n\n")
        summary_paragraphs = []
        
        for p in paragraphs:
            p = p.strip()
            if p and len(p) > 20:  # Nur Absätze mit mindestens 20 Zeichen
                summary_paragraphs.append(p)
                if len(summary_paragraphs) >= 2:  # Nur die ersten 2 Absätze
                    break
        
        if summary_paragraphs:
            summary = " ".join(summary_paragraphs)
            if len(summary) > 200:
                summary = summary[:197] + "..."
            return summary
        else:
            return "Keine Zusammenfassung verfügbar."
    
    def _add_to_recent_pages(self, page_info: Dict[str, Any]):
        """Fügt eine Seite zur Liste der kürzlich besuchten Seiten hinzu."""
        # Prüfe, ob die Seite bereits in der Liste ist
        for i, page in enumerate(self.recent_pages):
            if page.get("url") == page_info.get("url"):
                # Aktualisiere vorhandenen Eintrag und verschiebe nach vorne
                self.recent_pages.pop(i)
                self.recent_pages.insert(0, page_info)
                return
        
        # Füge neue Seite hinzu
        self.recent_pages.insert(0, page_info)
        
        # Begrenze die Größe der Liste
        if len(self.recent_pages) > self.max_recent_pages:
            self.recent_pages.pop()
    
    async def _load_saved_processes(self):
        """Lädt gespeicherte Prozesse aus der Datenbank."""
        if not self.process_automation_enabled or not self.process_controller:
            return
        
        try:
            processes = await self.process_controller.load_processes()
            self.saved_processes = {p["name"]: p for p in processes}
            self.logger.info(f"{len(processes)} gespeicherte Prozesse geladen")
        except Exception as e:
            self.logger.error(f"Fehler beim Laden gespeicherter Prozesse: {e}")
    
    async def _handle_save_process(self, event: EventMessage):
        """Behandelt Anfragen zum Speichern eines Prozesses."""
        if not self.process_automation_enabled or not self.process_controller:
            self.logger.error("Prozess-Automation ist nicht aktiviert")
            return
        
        try:
            # Prozessdaten extrahieren
            process_data = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            
            # Prozess speichern
            await self.process_controller.save_process(process_data)
            
            # Lokale Kopie aktualisieren
            process_name = process_data.get("name")
            self.saved_processes[process_name] = process_data
            
            # Bestätigung senden
            self.event_bus.publish(
                "response.process.saved",
                json.dumps({"name": process_name, "success": True}),
                "RESPONSE",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Bestätigung vorlesen
            self.event_bus.publish(
                "command.speak",
                f"Prozess '{process_name}' wurde gespeichert.",
                "COMMAND",
                "digital_module"
            )
        
        except Exception as e:
            self.logger.error(f"Fehler beim Speichern des Prozesses: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.process.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Fehlermeldung vorlesen
            self.event_bus.publish(
                "command.speak",
                f"Ich konnte den Prozess nicht speichern: {str(e)}",
                "COMMAND",
                "digital_module"
            )
    
    async def _handle_execute_process(self, event: EventMessage):
        """Behandelt Anfragen zur Ausführung eines gespeicherten Prozesses."""
        if not self.process_automation_enabled or not self.process_controller:
            self.logger.error("Prozess-Automation ist nicht aktiviert")
            return
        
        try:
            # Prozessname extrahieren
            process_name = event.payload.decode('utf-8') if isinstance(event.payload, bytes) else event.payload
            
            # Prozess suchen
            if process_name not in self.saved_processes:
                raise ValueError(f"Prozess '{process_name}' nicht gefunden")
            
            process_data = self.saved_processes[process_name]
            
            # Prozess ausführen
            self.event_bus.publish(
                "command.speak",
                f"Führe Prozess '{process_name}' aus.",
                "COMMAND",
                "digital_module"
            )
            
            # Statusmeldung senden
            self.event_bus.publish(
                "event.process.started",
                process_name,
                "NOTIFICATION",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Prozess asynchron ausführen
            success, result = await self.process_controller.execute_process(process_data)
            
            # Statistik aktualisieren
            self.stats["process_executions"] += 1
            
            # Ergebnis veröffentlichen
            self.event_bus.publish(
                "response.process.result",
                json.dumps({
                    "name": process_name,
                    "success": success,
                    "result": result
                }),
                "RESPONSE",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Ergebnis vorlesen
            if success:
                self.event_bus.publish(
                    "command.speak",
                    f"Prozess '{process_name}' erfolgreich ausgeführt.",
                    "COMMAND",
                    "digital_module"
                )
            else:
                self.event_bus.publish(
                    "command.speak",
                    f"Fehler bei der Ausführung von Prozess '{process_name}': {result}",
                    "COMMAND",
                    "digital_module"
                )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Ausführung des Prozesses: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.process.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "digital_module",
                {"original_message_id": event.message_id}
            )
            
            # Fehlermeldung vorlesen
            self.event_bus.publish(
                "command.speak",
                f"Ich konnte den Prozess nicht ausführen: {str(e)}",
                "COMMAND",
                "digital_module"
            )
    
    async def get_capabilities(self) -> List[str]:
        """Gibt die Fähigkeiten des Moduls zurück."""
        capabilities = []
        
        if self.browser_automation_enabled:
            capabilities.extend(["web_browsing", "web_content_extraction"])
        
        if self.system_automation_enabled:
            capabilities.extend(["system_control", "app_launching"])
        
        if self.ui_automation_enabled:
            capabilities.extend(["ui_interaction", "form_filling"])
        
        if self.process_automation_enabled:
            capabilities.extend(["process_automation", "workflow_execution"])
        
        return capabilities
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob das Modul gesund ist."""
        return self.health_status and self.is_running
    
    def get_uptime(self) -> float:
        """Gibt die Laufzeit des Moduls in Sekunden zurück."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    def get_stats(self) -> Dict[str, Any]:
        """Gibt Statistiken zum Modul zurück."""
        return self.stats
```

### 4.7 Mobile-Modul (mobile_module.py)

Das Mobile-Modul ermöglicht die Integration mit Smartphone-Geräten:

```python
# mobile_module.py
import asyncio
import logging
import time
import threading
import json
from typing import Dict, List, Any, Optional, Tuple
import base64

from assistant.common.event_bus import EventBus, EventMessage
from assistant.common.shortcut_registry import ShortcutPathRegistry
from assistant.common.config_manager import ConfigManager
from assistant.adapters.mobile_adapter import MobileAdapter

class MobileModule:
    """
    Ermöglicht die Integration mit mobilen Geräten (Smartphones, Tablets)
    für Kamerazugriff, Spracherkennung und Fernsteuerung.
    """
    
    def __init__(self, event_bus: EventBus, shortcut_registry: ShortcutPathRegistry,
                config_path: str = "./config/mobile_module.yaml"):
        """
        Initialisiert das Mobile-Modul.
        
        Args:
            event_bus: Event-Bus für die Kommunikation
            shortcut_registry: Registry für Abkürzungspfade
            config_path: Pfad zur Konfigurationsdatei
        """
        # Logger einrichten
        self.logger = logging.getLogger("mobile_module")
        
        # Referenzen speichern
        self.event_bus = event_bus
        self.shortcut_registry = shortcut_registry
        
        # Konfiguration laden
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load_config()
        
        # Mobile-Adapter
        self.mobile_adapter = MobileAdapter(self.config)
        
        # Verbundene Geräte
        self.connected_devices = {}
        
        # Aktive Kamerastreams
        self.active_camera_streams = {}
        
        # Status
        self.start_time = None
        self.is_running = False
        self.health_status = True
        
        # Statistiken
        self.stats = {
            "connected_devices": 0,
            "camera_captures": 0,
            "voice_inputs": 0,
            "tts_requests": 0
        }
        
        self.logger.info("Mobile-Modul initialisiert")
    
    async def start(self):
        """Startet das Mobile-Modul."""
        self.logger.info("Starte Mobile-Modul")
        self.is_running = True
        self.start_time = time.time()
        
        # Mobile-Adapter starten
        await self.mobile_adapter.start()
        
        # Event-Subscriptions einrichten
        self._setup_event_subscriptions()
        
        # Abkürzungspfade registrieren
        self._register_shortcuts()
        
        self.logger.info("Mobile-Modul gestartet")
    
    async def stop(self):
        """Stoppt das Mobile-Modul."""
        self.logger.info("Stoppe Mobile-Modul")
        self.is_running = False
        
        # Alle Kamerastreams beenden
        for device_id in list(self.active_camera_streams.keys()):
            await self._stop_camera_stream(device_id)
        
        # Mobile-Adapter stoppen
        await self.mobile_adapter.stop()
        
        self.logger.info("Mobile-Modul gestoppt")
    
    def _setup_event_subscriptions(self):
        """Richtet Event-Subscriptions ein."""
        # Verbindungsereignisse
        self.event_bus.subscribe("mobile.device_connected", self._handle_device_connected)
        self.event_bus.subscribe("mobile.device_disconnected", self._handle_device_disconnected)
        
        # Kamera-Steuerung
        self.event_bus.subscribe("command.mobile.camera.take_photo", self._handle_take_photo_command)
        self.event_bus.subscribe("command.mobile.camera.start_stream", self._handle_start_camera_stream)
        self.event_bus.subscribe("command.mobile.camera.stop_stream", self._handle_stop_camera_stream_command)
        
        # Sprachausgabe
        self.event_bus.subscribe("command.mobile.speak", self._handle_mobile_speak_command)
        
        # Benachrichtigungen
        self.event_bus.subscribe("command.mobile.notify", self._handle_notify_command)
        
        # Eingehende Ereignisse vom Mobilgerät
        self.mobile_adapter.set_message_handler(self._handle_mobile_message)
    
    def _register_shortcuts(self):
        """Registriert optimierte Abkürzungspfade."""
        # Direkter Pfad für Kamerabilder zum Vision-Modul
        self.shortcut_registry.register_shortcut(
            "mobile_module",
            "vision_module",
            "camera_image",
            self._shortcut_handle_camera_image
        )
        
        # Direkter Pfad für Spracherkennung zum Voice-Modul
        self.shortcut_registry.register_shortcut(
            "mobile_module",
            "voice_module",
            "voice_input",
            self._shortcut_handle_voice_input
        )
    
    def _shortcut_handle_camera_image(self, payload):
        """Leitet Kamerabilder direkt an das Vision-Modul weiter."""
        try:
            # Bilddaten parsen
            image_data = json.loads(payload)
            
            # Base64-Daten dekodieren
            image_bytes = base64.b64decode(image_data.get("image_data", ""))
            
            # Metadaten extrahieren
            device_id = image_data.get("device_id", "unknown")
            timestamp = image_data.get("timestamp", time.time())
            
            # Daten für Vision-Modul vorbereiten
            return {
                "success": True,
                "image_bytes": image_bytes,
                "metadata": {
                    "source": "mobile_camera",
                    "device_id": device_id,
                    "timestamp": timestamp
                }
            }
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung eines Kamerabildes: {e}")
            return {"success": False, "reason": str(e)}
    
    def _shortcut_handle_voice_input(self, payload):
        """Leitet Spracheingaben direkt an das Voice-Modul weiter."""
        try:
            # Audiodaten parsen
            audio_data = json.loads(payload)
            
            # Base64-Daten dekodieren
            audio_bytes = base64.b64decode(audio_data.get("audio_data", ""))
            
            # Metadaten extrahieren
            device_id = audio_data.get("device_id", "unknown")
            format = audio_data.get("format", "wav")
            
            # Daten für Voice-Modul vorbereiten
            return {
                "success": True,
                "audio_bytes": audio_bytes,
                "metadata": {
                    "source": "mobile_device",
                    "device_id": device_id,
                    "format": format
                }
            }
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Spracheingabe: {e}")
            return {"success": False, "reason": str(e)}
    
    async def _handle_device_connected(self, event: EventMessage):
        """Behandelt die Verbindung eines mobilen Geräts."""
        try:
            # Geräteinformationen extrahieren
            device_info = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            
            device_id = device_info.get("device_id")
            device_name = device_info.get("device_name", "Unbekanntes Gerät")
            device_type = device_info.get("device_type", "unknown")
            
            if not device_id:
                self.logger.error("Geräteinformationen ohne Geräte-ID")
                return
            
            # Gerät registrieren
            self.connected_devices[device_id] = {
                "device_id": device_id,
                "device_name": device_name,
                "device_type": device_type,
                "capabilities": device_info.get("capabilities", []),
                "connected_at": time.time(),
                "last_active": time.time()
            }
            
            # Statistik aktualisieren
            self.stats["connected_devices"] = len(self.connected_devices)
            
            self.logger.info(f"Mobiles Gerät verbunden: {device_name} ({device_id})")
            
            # Bestätigung an das Gerät senden
            await self.mobile_adapter.send_message(
                device_id,
                "device.connection_confirmed",
                json.dumps({
                    "status": "connected",
                    "server_name": self.config.get("server_name", "Assistenzsystem"),
                    "timestamp": time.time()
                })
            )
            
            # Systembereitschaftsmeldung
            await self.mobile_adapter.send_message(
                device_id,
                "system.status",
                json.dumps({
                    "status": "ready",
                    "available_commands": [
                        "camera.take_photo",
                        "camera.start_stream",
                        "voice.start_recognition",
                        "voice.stop_recognition"
                    ]
                })
            )
            
            # Benachrichtigung im System
            self.event_bus.publish(
                "event.mobile.device_connected",
                json.dumps({
                    "device_id": device_id,
                    "device_name": device_name,
                    "device_type": device_type
                }),
                "NOTIFICATION",
                "mobile_module"
            )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Geräteverbindung: {e}")
    
    async def _handle_device_disconnected(self, event: EventMessage):
        """Behandelt die Trennung eines mobilen Geräts."""
        try:
            # Geräteinformationen extrahieren
            device_info = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            device_id = device_info.get("device_id")
            
            if not device_id:
                self.logger.error("Geräteinformationen ohne Geräte-ID")
                return
            
            # Prüfen, ob das Gerät bekannt ist
            if device_id in self.connected_devices:
                device_name = self.connected_devices[device_id].get("device_name", "Unbekanntes Gerät")
                
                # Eventuell laufende Kamerastreams beenden
                if device_id in self.active_camera_streams:
                    await self._stop_camera_stream(device_id)
                
                # Gerät entfernen
                del self.connected_devices[device_id]
                
                # Statistik aktualisieren
                self.stats["connected_devices"] = len(self.connected_devices)
                
                self.logger.info(f"Mobiles Gerät getrennt: {device_name} ({device_id})")
                
                # Benachrichtigung im System
                self.event_bus.publish(
                    "event.mobile.device_disconnected",
                    json.dumps({
                        "device_id": device_id,
                        "device_name": device_name
                    }),
                    "NOTIFICATION",
                    "mobile_module"
                )
            else:
                self.logger.warning(f"Unbekanntes Gerät getrennt: {device_id}")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Gerätetrennung: {e}")
    
    async def _handle_mobile_message(self, device_id: str, message_type: str, payload: Any):
        """
        Behandelt eingehende Nachrichten von mobilen Geräten.
        
        Args:
            device_id: ID des sendenden Geräts
            message_type: Typ der Nachricht
            payload: Nutzlast der Nachricht
        """
        try:
            # Prüfen, ob das Gerät bekannt ist
            if device_id not in self.connected_devices:
                self.logger.warning(f"Nachricht von unbekanntem Gerät: {device_id}")
                return
            
            # Zeitstempel der letzten Aktivität aktualisieren
            self.connected_devices[device_id]["last_active"] = time.time()
            
            # Nachrichtentyp verarbeiten
            if message_type == "camera.photo":
                # Foto von der Kamera
                await self._handle_mobile_photo(device_id, payload)
            
            elif message_type == "camera.stream_frame":
                # Frame vom Kamerastream
                await self._handle_stream_frame(device_id, payload)
            
            elif message_type == "voice.audio_data":
                # Spracheingabe
                await self._handle_voice_data(device_id, payload)
            
            elif message_type == "device.status":
                # Statusaktualisierung
                await self._handle_device_status(device_id, payload)
            
            # Weitere Nachrichtentypen...
            
            else:
                self.logger.warning(f"Unbekannter Nachrichtentyp von Gerät {device_id}: {message_type}")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung einer Mobilgerätnachricht: {e}")
    
    async def _handle_mobile_photo(self, device_id: str, payload: Any):
        """
        Verarbeitet ein Foto von einem mobilen Gerät.
        
        Args:
            device_id: ID des Geräts
            payload: Fotodaten (Base64-kodiert)
        """
        try:
            # Bilddaten extrahieren
            photo_data = json.loads(payload) if isinstance(payload, bytes) or isinstance(payload, str) else payload
            image_base64 = photo_data.get("image_data")
            
            if not image_base64:
                self.logger.error(f"Keine Bilddaten in der Fotoanfrage von Gerät {device_id}")
                return
            
            # Base64-Daten dekodieren
            image_bytes = base64.b64decode(image_base64)
            
            # Statistik aktualisieren
            self.stats["camera_captures"] += 1
            
            # Bild zur Analyse an das Vision-Modul weiterleiten
            self.event_bus.publish(
                "query.vision.describe_image",
                image_bytes,
                "QUERY",
                "mobile_module",
                {
                    "source": "mobile_camera",
                    "device_id": device_id,
                    "timestamp": time.time()
                }
            )
            
            # Auf Antwort warten (asynchron)
            description_future = asyncio.Future()
            
            def description_callback(response_event):
                # Prüfe, ob die Antwort zu unserer Anfrage gehört
                if response_event.metadata.get("source") == "mobile_camera" and response_event.metadata.get("device_id") == device_id:
                    # Future mit Beschreibung erfüllen
                    description = response_event.payload.decode('utf-8') if isinstance(response_event.payload, bytes) else response_event.payload
                    description_future.set_result(description)
            
            # Callback für die Antwort registrieren
            self.event_bus.subscribe("response.vision.image_description", description_callback)
            
            try:
                # Auf Beschreibung warten (mit Timeout)
                description = await asyncio.wait_for(description_future, timeout=10.0)
                
                # Beschreibung an das Gerät senden
                await self.mobile_adapter.send_message(
                    device_id,
                    "camera.photo_description",
                    json.dumps({
                        "description": description,
                        "timestamp": time.time()
                    })
                )
                
                # Beschreibung vorlesen
                self.event_bus.publish(
                    "command.speak",
                    f"Vom Mobilgerät: {description}",
                    "COMMAND",
                    "mobile_module"
                )
            
            except asyncio.TimeoutError:
                # Timeout bei der Bildbeschreibung
                await self.mobile_adapter.send_message(
                    device_id,
                    "camera.photo_description",
                    json.dumps({
                        "error": "Timeout bei der Bildbeschreibung",
                        "timestamp": time.time()
                    })
                )
                
                self.event_bus.publish(
                    "command.speak",
                    "Die Analyse des Mobilgerätefotos dauert zu lange.",
                    "COMMAND",
                    "mobile_module"
                )
            
            finally:
                # Callback deregistrieren
                self.event_bus.unsubscribe("response.vision.image_description", description_callback)
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Verarbeitung eines Mobilgerätefotos: {e}")
            
            # Fehlermeldung an das Gerät senden
            await self.mobile_adapter.send_message(
                device_id,
                "camera.photo_error",
                json.dumps({
                    "error": str(e),
                    "timestamp": time.time()
                })
            )
    
    async def _handle_take_photo_command(self, event: EventMessage):
        """Behandelt Befehle zur Fotoaufnahme mit einem mobilen Gerät."""
        try:
            # Parameter extrahieren
            params = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            
            # Geräte-ID bestimmen
            device_id = params.get("device_id")
            
            # Wenn keine Geräte-ID angegeben, verwende das erste verbundene Gerät
            if not device_id and self.connected_devices:
                device_id = next(iter(self.connected_devices.keys()))
            
            if not device_id or device_id not in self.connected_devices:
                raise ValueError("Kein geeignetes mobiles Gerät verbunden")
            
            # Prüfen, ob das Gerät eine Kamera hat
            device_capabilities = self.connected_devices[device_id].get("capabilities", [])
            if "camera" not in device_capabilities:
                raise ValueError(f"Gerät {device_id} hat keine Kamera")
            
            # Fotoaufnahme anfordern
            await self.mobile_adapter.send_message(
                device_id,
                "command.camera.take_photo",
                json.dumps({
                    "quality": params.get("quality", "high"),
                    "flash": params.get("flash", False),
                    "camera": params.get("camera", "back"),  # "back" oder "front"
                    "timestamp": time.time()
                })
            )
            
            # Bestätigung senden
            self.event_bus.publish(
                "event.mobile.photo_requested",
                json.dumps({
                    "device_id": device_id,
                    "device_name": self.connected_devices[device_id].get("device_name", "Unbekanntes Gerät")
                }),
                "NOTIFICATION",
                "mobile_module",
                {"original_message_id": event.message_id}
            )
            
            # Sprachausgabe
            self.event_bus.publish(
                "command.speak",
                "Ich nehme ein Foto mit dem Mobilgerät auf.",
                "COMMAND",
                "mobile_module"
            )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Anforderung eines Mobilgerätefotos: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.mobile.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "mobile_module",
                {"original_message_id": event.message_id}
            )
            
            # Fehlermeldung vorlesen
            self.event_bus.publish(
                "command.speak",
                f"Ich konnte kein Foto mit dem Mobilgerät aufnehmen: {str(e)}",
                "COMMAND",
                "mobile_module"
            )
    
    async def _handle_mobile_speak_command(self, event: EventMessage):
        """Behandelt Sprachausgabe-Befehle für mobile Geräte."""
        try:
            # Parameter extrahieren
            params = json.loads(event.payload) if isinstance(event.payload, bytes) or isinstance(event.payload, str) else event.payload
            
            text = params.get("text", "")
            device_id = params.get("device_id")
            
            if not text:
                self.logger.error("Mobilgerät-Sprachausgabe ohne Text angefordert")
                return
            
            # Wenn keine Geräte-ID angegeben, an alle Geräte senden
            if not device_id:
                # An alle verbundenen Geräte senden
                for device_id in self.connected_devices:
                    await self.mobile_adapter.send_message(
                        device_id,
                        "command.speak",
                        json.dumps({
                            "text": text,
                            "voice": params.get("voice"),
                            "rate": params.get("rate"),
                            "pitch": params.get("pitch"),
                            "timestamp": time.time()
                        })
                    )
            else:
                # An das angegebene Gerät senden
                if device_id not in self.connected_devices:
                    raise ValueError(f"Gerät {device_id} nicht verbunden")
                
                await self.mobile_adapter.send_message(
                    device_id,
                    "command.speak",
                    json.dumps({
                        "text": text,
                        "voice": params.get("voice"),
                        "rate": params.get("rate"),
                        "pitch": params.get("pitch"),
                        "timestamp": time.time()
                    })
                )
            
            # Statistik aktualisieren
            self.stats["tts_requests"] += 1
            
            # Bestätigung senden
            self.event_bus.publish(
                "event.mobile.tts_sent",
                json.dumps({"text": text}),
                "NOTIFICATION",
                "mobile_module",
                {"original_message_id": event.message_id}
            )
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Mobilgerät-Sprachausgabe: {e}")
            
            # Fehlermeldung senden
            self.event_bus.publish(
                "response.mobile.error",
                json.dumps({"error": str(e)}),
                "ERROR",
                "mobile_module",
                {"original_message_id": event.message_id}
            )
    
    async def get_capabilities(self) -> List[str]:
        """Gibt die Fähigkeiten des Moduls zurück."""
        capabilities = ["mobile_integration", "device_management"]
        
        # Prüfe, ob verbundene Geräte bestimmte Fähigkeiten haben
        for device_id, device_info in self.connected_devices.items():
            device_capabilities = device_info.get("capabilities", [])
            
            if "camera" in device_capabilities and "mobile_camera" not in capabilities:
                capabilities.append("mobile_camera")
            
            if "microphone" in device_capabilities and "mobile_voice_input" not in capabilities:
                capabilities.append("mobile_voice_input")
            
            if "speaker" in device_capabilities and "mobile_tts" not in capabilities:
                capabilities.append("mobile_tts")
        
        return capabilities
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob das Modul gesund ist."""
        return self.health_status and self.is_running and self.mobile_adapter.is_connected()
    
    def get_uptime(self) -> float:
        """Gibt die Laufzeit des Moduls in Sekunden zurück."""
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time
    
    def get_stats(self) -> Dict[str, Any]:
        """Gibt Statistiken zum Modul zurück."""
        return self.stats
```

## 5. Konfigurationsdateien

### 5.1 Hauptkonfiguration (orchestrator.yaml)

```yaml
# orchestrator.yaml
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

### 5.2 Hirn-Modul-Konfiguration (brain_module.yaml)

```yaml
# brain_module.yaml
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

### 5.3 Stimme/Ohren-Modul-Konfiguration (voice_module.yaml)

```yaml
# voice_module.yaml
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
  engine: "espeak"  # "espeak", "pyttsx3", "coqui_tts", "system"
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

### 5.4 Augen-Modul-Konfiguration (vision_module.yaml)

```yaml
# vision_module.yaml
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
  tesseract_path: null  # null = auto-detect

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

### 5.5 Digitalsinn-Modul-Konfiguration (digital_module.yaml)

```yaml
# digital_module.yaml
browser_automation:
  enabled: true
  browser: "chrome"  # "chrome", "firefox", "edge"
  headless: false
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

### 5.6 Mobile-Modul-Konfiguration (mobile_module.yaml)

```yaml
# mobile_module.yaml
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

### 5.7 Logging-Konfiguration (logging.yaml)

```yaml
# logging.yaml
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

## 6. Dienst-Implementierungen

### 6.1 Text-zu-Sprache-Dienst (tts_service.py)

```python
# tts_service.py
import asyncio
import logging
import time
import os
import hashlib
from typing import Dict, List, Any, Optional, Tuple

class TTSService:
    """
    Text-zu-Sprache-Dienst, der verschiedene TTS-Engines unterstützt.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisiert den TTS-Dienst.
        
        Args:
            config: Konfiguration für den TTS-Dienst
        """
        self.config = config or {}
        self.logger = logging.getLogger("tts_service")
        
        # TTS-Engine
        self.engine_type = self.config.get("engine", "espeak")
        self.engine = None
        
        # Konfigurationsparameter
        self.voice = self.config.get("voice", "de")
        self.rate = self.config.get("rate", 0)
        self.volume = self.config.get("volume", 100)
        self.pitch = self.config.get("pitch", 0)
        
        # Cache
        self.use_cache = self.config.get("use_cache", True)
        self.cache_dir = self.config.get("cache_dir", "./data/cache/tts")
        self.audio_cache = {}
        
        # Status
        self.is_speaking = False
        self.is_initialized = False
        
        self.logger.info(f"TTS-Dienst initialisiert (Engine: {self.engine_type})")
    
    async def start(self):
        """Startet den TTS-Dienst."""
        if self.is_initialized:
            return
        
        try:
            # Cache-Verzeichnis erstellen (falls es nicht existiert)
            if self.use_cache:
                os.makedirs(self.cache_dir, exist_ok=True)
            
            # Engine initialisieren basierend auf Konfiguration
            if self.engine_type == "espeak":
                await self._init_espeak()
            elif self.engine_type == "pyttsx3":
                await self._init_pyttsx3()
            elif self.engine_type == "coqui_tts":
                await self._init_coqui_tts()
            elif self.engine_type == "system":
                await self._init_system_tts()
            else:
                self.logger.error(f"Unbekannte TTS-Engine: {self.engine_type}")
                return
            
            self.is_initialized = True
            self.logger.info(f"TTS-Dienst gestartet (Engine: {self.engine_type}, Voice: {self.voice})")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Starten des TTS-Dienstes: {e}")
    
    async def stop(self):
        """Stoppt den TTS-Dienst."""
        if not self.is_initialized:
            return
        
        try:
            # Engine stoppen
            if self.engine_type == "espeak":
                await self._stop_espeak()
            elif self.engine_type == "pyttsx3":
                await self._stop_pyttsx3()
            elif self.engine_type == "coqui_tts":
                await self._stop_coqui_tts()
            elif self.engine_type == "system":
                await self._stop_system_tts()
            
            self.is_initialized = False
            self.logger.info("TTS-Dienst gestoppt")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Stoppen des TTS-Dienstes: {e}")
    
    async def speak(self, text: str):
        """
        Spricht den angegebenen Text.
        
        Args:
            text: Der zu sprechende Text
        """
        if not self.is_initialized:
            self.logger.error("TTS-Dienst nicht initialisiert")
            return
        
        try:
            self.is_speaking = True
            
            # Cache-Schlüssel erstellen
            cache_key = self._compute_cache_key(text)
            
            # Prüfen, ob der Text im Cache ist
            if self.use_cache and cache_key in self.audio_cache:
                await self._play_cached_audio(cache_key)
            else:
                # Text in Sprache umwandeln und abspielen
                if self.engine_type == "espeak":
                    await self._speak_espeak(text, cache_key)
                elif self.engine_type == "pyttsx3":
                    await self._speak_pyttsx3(text, cache_key)
                elif self.engine_type == "coqui_tts":
                    await self._speak_coqui_tts(text, cache_key)
                elif self.engine_type == "system":
                    await self._speak_system_tts(text, cache_key)
            
            self.is_speaking = False
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Sprachausgabe: {e}")
            self.is_speaking = False
    
    async def synthesize_speech(self, text: str) -> bytes:
        """
        Erzeugt Audiodaten für den angegebenen Text ohne sie abzuspielen.
        
        Args:
            text: Der zu synthetisierende Text
            
        Returns:
            Audiodaten als Bytes
        """
        if not self.is_initialized:
            self.logger.error("TTS-Dienst nicht initialisiert")
            return b""
        
        try:
            # Cache-Schlüssel erstellen
            cache_key = self._compute_cache_key(text)
            
            # Prüfen, ob der Text im Cache ist
            if self.use_cache and cache_key in self.audio_cache:
                return await self._load_cached_audio(cache_key)
            
            # Text in Sprache umwandeln
            if self.engine_type == "espeak":
                return await self._synthesize_espeak(text, cache_key)
            elif self.engine_type == "pyttsx3":
                return await self._synthesize_pyttsx3(text, cache_key)
            elif self.engine_type == "coqui_tts":
                return await self._synthesize_coqui_tts(text, cache_key)
            elif self.engine_type == "system":
                return await self._synthesize_system_tts(text, cache_key)
            
            return b""
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Sprachsynthese: {e}")
            return b""
    
    def set_voice(self, voice: str):
        """Ändert die verwendete Stimme."""
        self.voice = voice
        
        # Anpassung der Engine
        if self.is_initialized:
            if self.engine_type == "espeak":
                self.engine.setProperty("voice", voice)
            elif self.engine_type == "pyttsx3":
                self.engine.setProperty("voice", voice)
            elif self.engine_type == "system":
                # System-TTS-Stimme anpassen
                pass
            # Weitere Engines...
    
    def set_volume(self, volume: int):
        """Ändert die Lautstärke (0-100)."""
        self.volume = max(0, min(100, volume))
        
        # Anpassung der Engine
        if self.is_initialized:
            if self.engine_type == "espeak":
                self.engine.setProperty("volume", self.volume / 100.0)
            elif self.engine_type == "pyttsx3":
                self.engine.setProperty("volume", self.volume / 100.0)
            # Weitere Engines...
    
    def get_available_voices(self) -> List[str]:
        """Gibt eine Liste der verfügbaren Stimmen zurück."""
        if not self.is_initialized:
            return []
        
        try:
            if self.engine_type == "espeak":
                return self._get_espeak_voices()
            elif self.engine_type == "pyttsx3":
                return self._get_pyttsx3_voices()
            elif self.engine_type == "coqui_tts":
                return self._get_coqui_tts_voices()
            elif self.engine_type == "system":
                return self._get_system_tts_voices()
            
            return []
        
        except Exception as e:
            self.logger.error(f"Fehler beim Abrufen der verfügbaren Stimmen: {e}")
            return []
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob der Dienst gesund ist."""
        return self.is_initialized and not self.is_speaking
    
    def _compute_cache_key(self, text: str) -> str:
        """Berechnet einen eindeutigen Schlüssel für den Cache."""
        # Hash aus Text und Sprachparametern erstellen
        hash_input = f"{text}_{self.voice}_{self.rate}_{self.volume}_{self.pitch}"
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    # Engine-spezifische Implementierungen
    
    async def _init_espeak(self):
        """Initialisiert die eSpeak-Engine."""
        try:
            import pyttsx3
            
            self.engine = pyttsx3.init()
            self.engine.setProperty("voice", self.voice)
            self.engine.setProperty("rate", self.rate)
            self.engine.setProperty("volume", self.volume / 100.0)
            
            self.logger.debug("eSpeak-Engine initialisiert")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Initialisierung der eSpeak-Engine: {e}")
            raise
    
    async def _stop_espeak(self):
        """Stoppt die eSpeak-Engine."""
        try:
            if self.engine:
                self.engine.stop()
            
            self.logger.debug("eSpeak-Engine gestoppt")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Stoppen der eSpeak-Engine: {e}")
    
    async def _speak_espeak(self, text: str, cache_key: str):
        """Spricht Text mit der eSpeak-Engine."""
        try:
            # In einem separaten Thread ausführen, um den Event-Loop nicht zu blockieren
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: self.engine.say(text))
            await loop.run_in_executor(None, self.engine.runAndWait)
            
            # In Cache speichern
            if self.use_cache:
                # eSpeak kann Audiodaten direkt speichern
                cache_path = os.path.join(self.cache_dir, f"{cache_key}.wav")
                self.audio_cache[cache_key] = cache_path
                
                # Audiodaten in Datei speichern (falls noch nicht vorhanden)
                if not os.path.exists(cache_path):
                    await loop.run_in_executor(None, lambda: self.engine.save_to_file(text, cache_path))
                    await loop.run_in_executor(None, self.engine.runAndWait)
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Sprachausgabe mit eSpeak: {e}")
            raise
    
    async def _init_pyttsx3(self):
        """Initialisiert die pyttsx3-Engine."""
        try:
            import pyttsx3
            
            self.engine = pyttsx3.init()
            self.engine.setProperty("voice", self.voice)
            self.engine.setProperty("rate", self.rate)
            self.engine.setProperty("volume", self.volume / 100.0)
            
            self.logger.debug("pyttsx3-Engine initialisiert")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Initialisierung der pyttsx3-Engine: {e}")
            raise
    
    # Weitere Engine-Implementierungen...
```

### 6.2 Sprach-zu-Text-Dienst (stt_service.py)

```python
# stt_service.py
import asyncio
import logging
import time
import os
import numpy as np
from typing import Dict, List, Any, Optional, Tuple

class STTService:
    """
    Sprach-zu-Text-Dienst, der verschiedene STT-Engines unterstützt.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisiert den STT-Dienst.
        
        Args:
            config: Konfiguration für den STT-Dienst
        """
        self.config = config or {}
        self.logger = logging.getLogger("stt_service")
        
        # STT-Engine
        self.model = self.config.get("model", "whisper-small")
        self.engine = None
        
        # Konfigurationsparameter
        self.language = self.config.get("language", "de")
        self.vad_enabled = self.config.get("vad_enabled", True)
        self.noise_suppression_level = self.config.get("noise_suppression_level", 2)
        self.sample_rate = self.config.get("sample_rate", 16000)
        
        # Gerät (CPU/GPU)
        self.device = self.config.get("device", "auto")
        if self.device == "auto":
            import torch
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Status
        self.is_recognizing = False
        self.is_initialized = False
        
        self.logger.info(f"STT-Dienst initialisiert (Modell: {self.model}, Sprache: {self.language}, Gerät: {self.device})")
    
    async def start(self):
        """Startet den STT-Dienst."""
        if self.is_initialized:
            return
        
        try:
            # Modell initialisieren basierend auf Konfiguration
            if "whisper" in self.model.lower():
                await self._init_whisper()
            else:
                self.logger.error(f"Unbekanntes STT-Modell: {self.model}")
                return
            
            # VAD (Voice Activity Detection) initialisieren
            if self.vad_enabled:
                await self._init_vad()
            
            self.is_initialized = True
            self.logger.info(f"STT-Dienst gestartet (Modell: {self.model}, Gerät: {self.device})")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Starten des STT-Dienstes: {e}")
    
    async def stop(self):
        """Stoppt den STT-Dienst."""
        if not self.is_initialized:
            return
        
        try:
            # Ressourcen freigeben
            self.engine = None
            self.vad = None
            
            self.is_initialized = False
            self.logger.info("STT-Dienst gestoppt")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Stoppen des STT-Dienstes: {e}")
    
    def recognize(self, audio_data: np.ndarray) -> Tuple[str, float]:
        """
        Erkennt Sprache in Audiodaten (synchron).
        
        Args:
            audio_data: Audiodaten als NumPy-Array
            
        Returns:
            Tuple aus erkanntem Text und Konfidenz
        """
        if not self.is_initialized:
            self.logger.error("STT-Dienst nicht initialisiert")
            return "", 0.0
        
        try:
            self.is_recognizing = True
            
            # VAD anwenden (falls aktiviert)
            if self.vad_enabled and hasattr(self, 'vad'):
                audio_data = self._apply_vad(audio_data)
            
            # Wenn keine Sprache erkannt wurde
            if len(audio_data) == 0:
                self.is_recognizing = False
                return "", 0.0
            
            # Spracherkennung durchführen
            if "whisper" in self.model.lower():
                text, confidence = self._recognize_whisper(audio_data)
            else:
                text, confidence = "", 0.0
            
            self.is_recognizing = False
            return text, confidence
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Spracherkennung: {e}")
            self.is_recognizing = False
            return "", 0.0
    
    async def recognize_audio_data(self, audio_data: bytes) -> Tuple[str, float]:
        """
        Erkennt Sprache in Audiodaten (asynchron).
        
        Args:
            audio_data: Audiodaten als Bytes (z.B. WAV-Datei)
            
        Returns:
            Tuple aus erkanntem Text und Konfidenz
        """
        if not self.is_initialized:
            self.logger.error("STT-Dienst nicht initialisiert")
            return "", 0.0
        
        try:
            # Audiodaten in NumPy-Array konvertieren
            import soundfile as sf
            import io
            
            with io.BytesIO(audio_data) as buffer:
                audio_array, sample_rate = sf.read(buffer)
                
                # Stereo zu Mono konvertieren (falls nötig)
                if len(audio_array.shape) > 1 and audio_array.shape[1] > 1:
                    audio_array = np.mean(audio_array, axis=1)
                
                # Abtastrate anpassen (falls nötig)
                if sample_rate != self.sample_rate:
                    import librosa
                    audio_array = librosa.resample(
                        audio_array, 
                        orig_sr=sample_rate, 
                        target_sr=self.sample_rate
                    )
            
            # Spracherkennung in einem separaten Thread durchführen
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda: self.recognize(audio_array))
            
            return result
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Audiodatenverarbeitung: {e}")
            return "", 0.0
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob der Dienst gesund ist."""
        return self.is_initialized and not self.is_recognizing
    
    async def _init_whisper(self):
        """Initialisiert das Whisper-Modell."""
        try:
            import torch
            import whisper
            
            # Modellgröße bestimmen
            model_size = self.model.split("-")[1] if "-" in self.model else "small"
            
            # Modell laden
            self.engine = whisper.load_model(model_size, device=self.device)
            
            self.logger.debug(f"Whisper-Modell ({model_size}) initialisiert auf {self.device}")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Initialisierung des Whisper-Modells: {e}")
            raise
    
    async def _init_vad(self):
        """Initialisiert Voice Activity Detection (VAD)."""
        try:
            import torch
            import torchaudio
            
            # Silero VAD laden
            model, utils = torch.hub.load(
                repo_or_dir="snakers4/silero-vad",
                model="silero_vad"
            )
            
            (get_speech_timestamps, _, _, _, _) = utils
            
            self.vad = {
                "model": model,
                "get_speech_timestamps": get_speech_timestamps,
                "threshold": 0.5,  # Anpassbar
                "sampling_rate": self.sample_rate
            }
            
            self.logger.debug("VAD initialisiert")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Initialisierung der VAD: {e}")
            self.vad_enabled = False
    
    def _apply_vad(self, audio_data: np.ndarray) -> np.ndarray:
        """Wendet Voice Activity Detection an."""
        try:
            import torch
            
            # Audio in korrektes Format konvertieren
            audio_tensor = torch.FloatTensor(audio_data)
            
            # Sprachbereiche ermitteln
            speech_timestamps = self.vad["get_speech_timestamps"](
                audio_tensor,
                self.vad["model"],
                threshold=self.vad["threshold"],
                sampling_rate=self.vad["sampling_rate"]
            )
            
            # Wenn keine Sprache erkannt wurde
            if not speech_timestamps:
                return np.array([])
            
            # Nur Bereiche mit Sprache verwenden
            speech_audio = []
            for segment in speech_timestamps:
                speech_audio.append(audio_data[segment["start"]:segment["end"]])
            
            return np.concatenate(speech_audio) if speech_audio else np.array([])
        
        except Exception as e:
            self.logger.error(f"Fehler bei der VAD-Anwendung: {e}")
            return audio_data  # Bei Fehler unveränderte Daten zurückgeben
    
    def _recognize_whisper(self, audio_data: np.ndarray) -> Tuple[str, float]:
        """Erkennt Sprache mit dem Whisper-Modell."""
        try:
            # Audiodaten normalisieren
            audio_data = audio_data / np.max(np.abs(audio_data))
            
            # Sprache erkennen
            result = self.engine.transcribe(
                audio_data,
                language=self.language,
                task="transcribe",
                fp16=False  # Für sicherere Ergebnisse
            )
            
            text = result["text"].strip()
            confidence = float(result.get("confidence", 0.7))  # Default-Wert falls nicht vorhanden
            
            return text, confidence
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Whisper-Spracherkennung: {e}")
            return "", 0.0
```

### 6.3 OCR-Dienst (ocr_service.py)

```python
# ocr_service.py
import asyncio
import logging
import time
import os
import numpy as np
import cv2
from typing import Dict, List, Any, Optional, Tuple

class OCRService:
    """
    OCR-Dienst, der verschiedene OCR-Engines unterstützt.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisiert den OCR-Dienst.
        
        Args:
            config: Konfiguration für den OCR-Dienst
        """
        self.config = config or {}
        self.logger = logging.getLogger("ocr_service")
        
        # OCR-Engine
        self.engine_type = self.config.get("engine", "tesseract")
        self.engine = None
        
        # Konfigurationsparameter
        self.language = self.config.get("language", "deu")
        self.confidence_threshold = self.config.get("confidence_threshold", 0.6)
        self.cache_enabled = self.config.get("cache_enabled", True)
        self.max_cache_size = self.config.get("max_cache_size", 20)
        
        # Gerät (CPU/GPU)
        self.use_gpu = self.config.get("use_gpu", True)
        self.device = self.config.get("device", "auto")
        if self.device == "auto":
            import torch
            self.device = "cuda" if torch.cuda.is_available() and self.use_gpu else "cpu"
        
        # Cache
        self.image_hash_cache = {}
        
        # Status
        self.is_processing = False
        self.is_initialized = False
        
        self.logger.info(f"OCR-Dienst initialisiert (Engine: {self.engine_type}, Sprache: {self.language}, Gerät: {self.device})")
    
    async def start(self):
        """Startet den OCR-Dienst."""
        if self.is_initialized:
            return
        
        try:
            # Engine initialisieren basierend auf Konfiguration
            if self.engine_type == "tesseract":
                await self._init_tesseract()
            elif self.engine_type == "easyocr":
                await self._init_easyocr()
            elif self.engine_type == "paddleocr":
                await self._init_paddleocr()
            else:
                self.logger.error(f"Unbekannte OCR-Engine: {self.engine_type}")
                return
            
            self.is_initialized = True
            self.logger.info(f"OCR-Dienst gestartet (Engine: {self.engine_type}, Gerät: {self.device})")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Starten des OCR-Dienstes: {e}")
    
    async def stop(self):
        """Stoppt den OCR-Dienst."""
        if not self.is_initialized:
            return
        
        try:
            # Ressourcen freigeben
            self.engine = None
            
            self.is_initialized = False
            self.logger.info("OCR-Dienst gestoppt")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Stoppen des OCR-Dienstes: {e}")
    
    def extract_text(self, image) -> Dict[str, Any]:
        """
        Extrahiert Text aus einem Bild.
        
        Args:
            image: Bild als NumPy-Array oder OpenCV-Bild
            
        Returns:
            Dict mit erkanntem Text und Regionen
        """
        if not self.is_initialized:
            self.logger.error("OCR-Dienst nicht initialisiert")
            return {"text": "", "regions": [], "confidence": 0.0}
        
        try:
            self.is_processing = True
            
            # Bild vorverarbeiten
            processed_image = self._preprocess_image(image)
            
            # Cache-Schlüssel erstellen
            image_hash = self._compute_image_hash(processed_image)
            
            # Prüfen, ob das Bild im Cache ist
            if self.cache_enabled and image_hash in self.image_hash_cache:
                self.is_processing = False
                return self.image_hash_cache[image_hash]
            
            # OCR durchführen
            if self.engine_type == "tesseract":
                result = self._extract_text_tesseract(processed_image)
            elif self.engine_type == "easyocr":
                result = self._extract_text_easyocr(processed_image)
            elif self.engine_type == "paddleocr":
                result = self._extract_text_paddleocr(processed_image)
            else:
                result = {"text": "", "regions": [], "confidence": 0.0}
            
            # In Cache speichern
            if self.cache_enabled:
                # Cache-Größe begrenzen
                if len(self.image_hash_cache) >= self.max_cache_size:
                    # Ersten Eintrag entfernen
                    self.image_hash_cache.pop(next(iter(self.image_hash_cache)))
                
                self.image_hash_cache[image_hash] = result
            
            self.is_processing = False
            return result
        
        except Exception as e:
            self.logger.error(f"Fehler bei der OCR: {e}")
            self.is_processing = False
            return {"text": "", "regions": [], "confidence": 0.0}
    
    async def extract_text_async(self, image) -> Dict[str, Any]:
        """
        Extrahiert Text aus einem Bild asynchron.
        
        Args:
            image: Bild als NumPy-Array, OpenCV-Bild oder Dateipfad
            
        Returns:
            Dict mit erkanntem Text und Regionen
        """
        if not self.is_initialized:
            self.logger.error("OCR-Dienst nicht initialisiert")
            return {"text": "", "regions": [], "confidence": 0.0}
        
        try:
            # Bild laden, falls es ein Pfad ist
            if isinstance(image, str):
                image = cv2.imread(image)
            
            # OCR in einem separaten Thread durchführen
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda: self.extract_text(image))
            
            return result
        
        except Exception as e:
            self.logger.error(f"Fehler bei der asynchronen OCR: {e}")
            return {"text": "", "regions": [], "confidence": 0.0}
    
    def is_healthy(self) -> bool:
        """Gibt zurück, ob der Dienst gesund ist."""
        return self.is_initialized and not self.is_processing
    
    def _preprocess_image(self, image):
        """Verarbeitet ein Bild für bessere OCR-Ergebnisse vor."""
        try:
            # Bild in Graustufen konvertieren
            if len(image.shape) > 2:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image
            
            # Rauschen reduzieren
            denoised = cv2.GaussianBlur(gray, (3, 3), 0)
            
            # Kontrast verbessern
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            enhanced = clahe.apply(denoised)
            
            # Binarisierung (adaptive Schwellenwerte)
            # thresh = cv2.adaptiveThreshold(enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            
            return enhanced
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Bildvorverarbeitung: {e}")
            return image
    
    def _compute_image_hash(self, image) -> str:
        """Berechnet einen Hash für ein Bild."""
        try:
            # Bild auf einheitliche Größe skalieren
            resized = cv2.resize(image, (32, 32))
            
            # pHash berechnen
            import imagehash
            from PIL import Image
            
            # OpenCV-Bild zu PIL-Bild konvertieren
            pil_image = Image.fromarray(resized)
            
            # Hash berechnen
            hash_value = str(imagehash.phash(pil_image))
            
            return hash_value
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Bildhasherzeugung: {e}")
            # Fallback: Zeitstempel
            return str(time.time())
    
    async def _init_tesseract(self):
        """Initialisiert die Tesseract-Engine."""
        try:
            import pytesseract
            
            # Tesseract-Pfad setzen (falls angegeben)
            tesseract_path = self.config.get("tesseract_path")
            if tesseract_path:
                pytesseract.pytesseract.tesseract_cmd = tesseract_path
            
            # Tesseract-Engine speichern
            self.engine = pytesseract
            
            self.logger.debug("Tesseract-Engine initialisiert")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Initialisierung der Tesseract-Engine: {e}")
            raise
    
    def _extract_text_tesseract(self, image) -> Dict[str, Any]:
        """Extrahiert Text mit Tesseract OCR."""
        try:
            # Textextraktion mit Tesseract
            ocr_result = self.engine.image_to_data(
                image,
                lang=self.language,
                output_type=self.engine.Output.DICT,
                config='--psm 6'
            )
            
            # Ergebnisse zusammenfassen
            text_parts = []
            regions = []
            confidence_values = []
            
            for i in range(len(ocr_result["text"])):
                text = ocr_result["text"][i].strip()
                confidence = float(ocr_result["conf"][i]) / 100.0 if ocr_result["conf"][i] >= 0 else 0.0
                
                if text and confidence >= self.confidence_threshold:
                    text_parts.append(text)
                    confidence_values.append(confidence)
                    
                    # Region (Bounding Box)
                    x = ocr_result["left"][i]
                    y = ocr_result["top"][i]
                    w = ocr_result["width"][i]
                    h = ocr_result["height"][i]
                    
                    regions.append({
                        "text": text,
                        "confidence": confidence,
                        "bbox": [x, y, w, h]
                    })
            
            # Gesamttext erstellen
            full_text = " ".join(text_parts)
            
            # Durchschnittliche Konfidenz berechnen
            avg_confidence = sum(confidence_values) / len(confidence_values) if confidence_values else 0.0
            
            return {
                "text": full_text,
                "regions": regions,
                "confidence": avg_confidence
            }
        
        except Exception as e:
            self.logger.error(f"Fehler bei der Texterkennung mit Tesseract: {e}")
            return {"text": "", "regions": [], "confidence": 0.0}
    
    # EasyOCR und PaddleOCR Implementierungen...
```

## 7. Mobile App Integration

Die Mobile App wird mit Flutter entwickelt und kommuniziert über WebSockets mit dem Backend:

### 7.1 Mobile API-Server (mobile_adapter.py)

```python
# mobile_adapter.py
import asyncio
import logging
import json
import websockets
import time
from typing import Dict, List, Any, Optional, Callable

class MobileAdapter:
    """
    Adapter für die Kommunikation mit mobilen Geräten über WebSockets.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisiert den Mobile-Adapter.
        
        Args:
            config: Konfiguration für den Mobile-Adapter
        """
        self.config = config or {}
        self.logger = logging.getLogger("mobile_adapter")
        
        # Server-Konfiguration
        self.host = self.config.get("host", "0.0.0.0")
        self.port = self.config.get("port", 8080)
        self.protocol = self.config.get("protocol", "websocket")
        
        # SSL-Konfiguration
        self.ssl_enabled = self.config.get("ssl", {}).get("enabled", False)
        self.ssl_context = None
        
        # Authentifizierung
        self.auth_enabled = self.config.get("authentication", {}).get("enabled", False)
        self.tokens = {}
        
        # Verbindungen
        self.connections = {}
        self.message_handler = None
        self.server = None
        
        # Status
        self.is_running = False
        
        self.logger.info(f"Mobile-Adapter initialisiert (Host: {self.host}, Port: {self.port})")
    
    async def start(self):
        """Startet den Mobile-Adapter."""
        if self.is_running:
            return
        
        try:
            # SSL-Kontext erstellen (falls aktiviert)
            if self.ssl_enabled:
                import ssl
                
                self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                
                cert_path = self.config.get("ssl", {}).get("cert_path")
                key_path = self.config.get("ssl", {}).get("key_path")
                
                if not cert_path or not key_path:
                    self.logger.error("SSL-Pfade nicht angegeben")
                    return
                
                self.ssl_context.load_cert_chain(cert_path, key_path)
            
            # WebSocket-Server starten
            if self.protocol == "websocket":
                self.server = await websockets.serve(
                    self._handle_websocket_connection,
                    self.host,
                    self.port,
                    ssl=self.ssl_context
                )
                
                self.logger.info(f"WebSocket-Server gestartet auf {self.host}:{self.port}")
            
            # Weitere Protokolle...
            
            self.is_running = True
        
        except Exception as e:
            self.logger.error(f"Fehler beim Starten des Mobile-Adapters: {e}")
    
    async def stop(self):
        """Stoppt den Mobile-Adapter."""
        if not self.is_running:
            return
        
        try:
            # Alle Verbindungen schließen
            for device_id, connection_info in list(self.connections.items()):
                await self._close_connection(device_id, connection_info.get("websocket"))
            
            # Server stoppen
            if self.server:
                self.server.close()
                await self.server.wait_closed()
            
            self.is_running = False
            self.logger.info("Mobile-Adapter gestoppt")
        
        except Exception as e:
            self.logger.error(f"Fehler beim Stoppen des Mobile-Adapters: {e}")
    
    def set_message_handler(self, handler: Callable[[str, str, Any], None]):
        """
        Setzt den Handler für eingehende Nachrichten.
        
        Args:
            handler: Funktion, die bei eingehenden Nachrichten aufgerufen wird
        """
        self.message_handler = handler
    
    async def send_message(self, device_id: str, message_type: str, payload: Any):
        """
        Sendet eine Nachricht an ein mobiles Gerät.
        
        Args:
            device_id: ID des Zielgeräts
            message_type: Typ der Nachricht
            payload: Nutzlast der Nachricht
        
        Returns:
            True bei Erfolg, False bei Fehler
        """
        if not self.is_running:
            self.logger.error("Mobile-Adapter nicht gestartet")
            return False
        
        try:
            # Gerät suchen
            if device_id not in self.connections:
                self.logger.error(f"Gerät nicht verbunden: {device_id}")
                return False
            
            connection_info = self.connections[device_id]
            websocket = connection_info.get("websocket")
            
            if not websocket:
                self.logger.error(f"Keine WebSocket-Verbindung für Gerät: {device_id}")
                return False
            
            # Nachricht erstellen
            message = {
                "type": message_type,
                "timestamp": time.time(),
                "payload": payload
            }
            
            # Nachricht senden
            await websocket.send(json.dumps(message))
            return True
        
        except Exception as e:
            self.logger.error(f"Fehler beim Senden der Nachricht an Gerät {device_id}: {e}")
            return False
    
    def is_connected(self) -> bool:
        """Gibt zurück, ob der Adapter verbunden ist."""
        return self.is_running
    
    async def _handle_websocket_connection(self, websocket, path):
        """
        Behandelt eingehende WebSocket-Verbindungen.
        
        Args:
            websocket: WebSocket-Verbindung
            path: Anfragepfad
        """
        device_id = None
        
        try:
            # Auf Registrierungsnachricht warten
            registration_message = await websocket.recv()
            registration_data = json.loads(registration_message)
            
            # Geräteinformationen extrahieren
            device_id = registration_data.get("device_id")
            device_name = registration_data.get("device_name", "Unbekanntes Gerät")
            device_type = registration_data.get("device_type", "unknown")
            
            if not device_id:
                self.logger.error("Registrierung ohne Geräte-ID")
                await websocket.close(1003, "Geräte-ID fehlt")
                return
            
            # Authentifizierung prüfen (falls aktiviert)
            if self.auth_enabled:
                token = registration_data.get("token")
                
                if not token or not self._validate_token(device_id, token):
                    self.logger.error(f"Authentifizierungsfehler für Gerät: {device_id}")
                    await websocket.close(1008, "Authentifizierungsfehler")
                    return
            
            # Gerät registrieren
            self.connections[device_id] = {
                "websocket": websocket,
                "device_name": device_name,
                "device_type": device_type,
                "connected_at": time.time(),
                "last_active": time.time(),
                "capabilities": registration_data.get("capabilities", [])
            }
            
            self.logger.info(f"Gerät verbunden: {device_name} ({device_id})")
            
            # Verbindungsereignis erzeugen (falls Handler registriert)
            if self.message_handler:
                await self.message_handler(device_id, "device.connected", registration_data)
            
            # Nachrichten-Loop
            async for message in websocket:
                try:
                    # Nachricht parsen
                    message_data = json.loads(message)
                    message_type = message_data.get("type")
                    
                    if not message_type:
                        self.logger.warning(f"Nachricht ohne Typ von Gerät {device_id}")
                        continue
                    
                    # Aktivitätszeitstempel aktualisieren
                    self.connections[device_id]["last_active"] = time.time()
                    
                    # Nachricht verarbeiten (falls Handler registriert)
                    if self.message_handler:
                        await self.message_handler(
                            device_id,
                            message_type,
                            message_data.get("payload")
                        )
                
                except json.JSONDecodeError:
                    self.logger.warning(f"Ungültiges JSON von Gerät {device_id}")
                
                except Exception as e:
                    self.logger.error(f"Fehler bei der Nachrichtenverarbeitung von Gerät {device_id}: {e}")
        
        except websockets.exceptions.ConnectionClosed:
            self.logger.info(f"Verbindung geschlossen für Gerät: {device_id}")
        
        except Exception as e:
            self.logger.error(f"Fehler bei der WebSocket-Verbindung: {e}")
        
        finally:
            # Verbindung schließen und Gerät entfernen
            if device_id:
                await self._close_connection(device_id, websocket)
    
    async def _close_connection(self, device_id: str, websocket):
        """
        Schließt eine Verbindung und entfernt das Gerät.
        
        Args:
            device_id: ID des Geräts
            websocket: WebSocket-Verbindung
        """
        try:
            # Verbindung schließen
            if websocket and not websocket.closed:
                await websocket.close()
            
            # Gerät entfernen
            if device_id in self.connections:
                device_info = self.connections[device_id]
                del self.connections[device_id]
                
                self.logger.info(f"Gerät getrennt: {device_info.get('device_name', 'Unbekanntes Gerät')} ({device_id})")
                
                # Trennungsereignis erzeugen (falls Handler registriert)
                if self.message_handler:
                    await self.message_handler(device_id, "device.disconnected", {"device_id": device_id})
        
        except Exception as e:
            self.logger.error(f"Fehler beim Schließen der Verbindung für Gerät {device_id}: {e}")
    
    def _validate_token(self, device_id: str, token: str) -> bool:
        """
        Validiert ein Authentifizierungstoken.
        
        Args:
            device_id: ID des Geräts
            token: Authentifizierungstoken
            
        Returns:
            True, wenn das Token gültig ist, sonst False
        """
        # Prüfen, ob alle Geräte erlaubt sind
        allowed_devices = self.config.get("authentication", {}).get("allowed_devices", [])
        for device in allowed_devices:
            if device.get("device_id") == "*":
                return True
        
        # Prüfen, ob das Gerät explizit erlaubt ist
        for device in allowed_devices:
            if device.get("device_id") == device_id:
                expected_token = device.get("token")
                
                # Prüfen, ob das Token übereinstimmt
                if expected_token == token:
                    return True
        
        return False
```

### 7.2 Mobile App (Flutter)

Die mobile App wird mit Flutter implementiert und bietet folgende Kernfunktionen:

1. Kamerazugriff für Bildaufnahme und -analyse
2. Spracherkennung und -ausgabe
3. Synchronisation mit dem Hauptsystem

## 8. Protokolldefinitionen

### 8.1 Event-Bus-Protokoll (event_bus.proto)

```protobuf
syntax = "proto3";

package eventbus;

message EventMessage {
  string message_id = 1;
  string topic = 2;
  string source_module = 3;
  int64 timestamp = 4;
  MessageType type = 5;
  bytes payload = 6;
  map<string, string> metadata = 7;
  
  enum MessageType {
    DATA = 0;
    COMMAND = 1;
    QUERY = 2;
    RESPONSE = 3;
    NOTIFICATION = 4;
    ERROR = 5;
  }
}

service EventBusService {
  // Empfängt einen Stream von Ereignissen
  rpc SubscribeEvents(SubscriptionRequest) returns (stream EventMessage);
  
  // Veröffentlicht ein Ereignis
  rpc PublishEvent(EventMessage) returns (PublishResponse);
}

message SubscriptionRequest {
  repeated string topics = 1;
  string subscriber_id = 2;
}

message PublishResponse {
  bool success = 1;
  string message_id = 2;
  string error = 3;
}
```

### 8.2 Modul-Dienst-Protokoll (module_service.proto)

```protobuf
syntax = "proto3";

package moduleservice;

service ModuleService {
  // Ruft den Status eines Moduls ab
  rpc GetStatus(StatusRequest) returns (StatusResponse);
  
  // Führt einen Befehl auf einem Modul aus
  rpc ExecuteCommand(CommandRequest) returns (CommandResponse);
  
  // Stellt eine Anfrage an ein Modul
  rpc Query(QueryRequest) returns (QueryResponse);
  
  // Registriert ein Modul beim Orchestrator
  rpc RegisterModule(ModuleRegistration) returns (RegistrationResponse);
}

message StatusRequest {
  string module_id = 1;
}

message StatusResponse {
  bool is_healthy = 1;
  double uptime = 2;
  map<string, string> metrics = 3;
  map<string, string> diagnostics = 4;
}

message CommandRequest {
  string module_id = 1;
  string command = 2;
  bytes parameters = 3;
  map<string, string> metadata = 4;
}

message CommandResponse {
  bool success = 1;
  bytes result = 2;
  string error = 3;
}

message QueryRequest {
  string module_id = 1;
  string query_type = 2;
  bytes parameters = 3;
  map<string, string> metadata = 4;
}

message QueryResponse {
  bool success = 1;
  bytes result = 2;
  string error = 3;
}

message ModuleRegistration {
  string module_id = 1;
  string module_type = 2;
  string host = 3;
  int32 port = 4;
  repeated string capabilities = 5;
}

message RegistrationResponse {
  bool success = 1;
  string orchestrator_id = 2;
  string error = 3;
}
```

### 8.3 Mobile API-Protokoll (mobile_api.proto)

```protobuf
syntax = "proto3";

package mobileapi;

service MobileAPIService {
  // Registriert ein mobiles Gerät
  rpc RegisterDevice(DeviceRegistration) returns (RegistrationResponse);
  
  // Sendet ein Bild zur Analyse
  rpc AnalyzeImage(ImageRequest) returns (ImageResponse);
  
  // Streamt Kamerabilder
  rpc StreamCamera(stream CameraFrame) returns (stream CameraResponse);
  
  // Sendet Audiodaten zur Spracherkennung
  rpc RecognizeSpeech(AudioRequest) returns (SpeechResponse);
  
  // Empfängt Text-to-Speech-Ausgabe
  rpc SynthesizeSpeech(TTSRequest) returns (TTSResponse);
  
  // Empfängt Push-Benachrichtigungen
  rpc SubscribeNotifications(NotificationRequest) returns (stream Notification);
}

message DeviceRegistration {
  string device_id = 1;
  string device_name = 2;
  string device_type = 3;
  repeated string capabilities = 4;
  string token = 5;
}

message RegistrationResponse {
  bool success = 1;
  string server_name = 2;
  string error = 3;
}

message ImageRequest {
  bytes image_data = 1;
  string format = 2;
  bool describe = 3;
  map<string, string> metadata = 4;
}

message ImageResponse {
  bool success = 1;
  string description = 2;
  bytes processed_image = 3;
  string error = 4;
}

message CameraFrame {
  bytes image_data = 1;
  int64 timestamp = 2;
  string camera_id = 3;
  map<string, string> metadata = 4;
}

message CameraResponse {
  bool success = 1;
  string message = 2;
  CommandType command = 3;
  
  enum CommandType {
    CONTINUE = 0;
    STOP = 1;
    CHANGE_RESOLUTION = 2;
    CHANGE_FRAMERATE = 3;
    TOGGLE_FLASH = 4;
  }
}

message AudioRequest {
  bytes audio_data = 1;
  string format = 2;
  int32 sample_rate = 3;
  map<string, string> metadata = 4;
}

message SpeechResponse {
  bool success = 1;
  string text = 2;
  float confidence = 3;
  string error = 4;
}

message TTSRequest {
  string text = 1;
  string voice = 2;
  float rate = 3;
  float pitch = 4;
}

message TTSResponse {
  bool success = 1;
  bytes audio_data = 2;
  string error = 3;
}

message NotificationRequest {
  string device_id = 1;
  repeated string channels = 2;
}

message Notification {
  string title = 1;
  string message = 2;
  string channel = 3;
  int64 timestamp = 4;
  map<string, string> data = 5;
}
```

## 9. System-Anforderungen und Installation

### 9.1 Hardware-Anforderungen

Minimale Anforderungen:
- CPU: Intel i5 (7. Generation) oder vergleichbar
- RAM: 8 GB
- Grafikkarte: NVIDIA GTX 1050 oder vergleichbar (für GPU-beschleunigte Modelle)
- Festplatte: 10 GB freier Speicherplatz
- Mikrofon und Lautsprecher

Empfohlene Anforderungen:
- CPU: Intel i7 (10. Generation) oder vergleichbar
- RAM: 16 GB
- Grafikkarte: NVIDIA GTX 2060 oder vergleichbar
- Festplatte: 20 GB freier Speicherplatz (SSD empfohlen)
- Qualitätsmikrofon und Lautsprecher

### 9.2 Software-Anforderungen

- Betriebssystem: Windows 10/11 (64-bit)
- Python 3.9 oder höher
- Docker (optional, für Container-Deployment)
- NVIDIA CUDA 11.7 oder höher (für GPU-Beschleunigung)
- Flutter SDK (für Mobile App-Entwicklung)

### 9.3 Installationsschritte

```bash
# 1. Repository klonen
git clone https://github.com/username/assistant-system.git
cd assistant-system

# 2. Python-Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Unter Windows: venv\Scripts\activate

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Modelle herunterladen
python scripts/download_models.py

# 5. Konfiguration anpassen
# Bearbeite die Dateien im Verzeichnis config/ nach Bedarf

# 6. System starten
python scripts/start.py
```

### 9.4 Docker-Installation

```bash
# Docker Compose verwenden
docker-compose up -d
```

## 10. Erweiterungsmöglichkeiten und Zukunftspläne

Das System wurde mit Blick auf zukünftige Erweiterungen entwickelt und bietet zahlreiche Möglichkeiten zur Verbesserung und Anpassung:

1. **Unterstützung weiterer Sprachen**: Hinzufügen von Sprachpaketen für die Spracherkennung und -ausgabe
2. **Integration mit Smart-Home-Geräten**: Anbindung an Smart-Home-Systeme über den IoT-Adapter
3. **Verbesserte Bilderkennung**: Integration spezialisierter Bilderkennungsmodelle für bestimmte Objektklassen
4. **Offline-KI-Modelle**: Optimierung der Modelle für schnellere Ausführung auf schwächerer Hardware
5. **Verhaltenslernen**: Anpassung des Systems an die Vorlieben und Gewohnheiten des Nutzers
6. **Multinutzer-Unterstützung**: Erweiterung des Systems für die Nutzung durch mehrere Personen mit individuellen Einstellungen
7. **VR/AR-Integration**: Anbindung an VR- oder AR-Brillen für immersive Unterstützung

## 11. Zusammenfassung

Dieses Proof of Concept beschreibt ein umfassendes modulares Assistenzsystem, das speziell für Menschen mit Sehbehinderung entwickelt wurde. Die modulare Architektur ermöglicht eine flexible Erweiterung und Anpassung an verschiedene Bedürfnisse und Hardwareumgebungen.

Das System bietet:
- Erweiterte Bildschirmlupenfunktionen mit intelligenter Fokussierung
- Natürliche Sprachsteuerung für Windows und Webbrowser
- Intelligentes Vorlesen von Bildschirminhalten und Webseiten
- Automatische Erkennung und Beschreibung von Bildinhalten
- Mobile Integration für Kameraunterstützung und unterwegs
- Automatisierung häufiger Abläufe

Durch die modulare Struktur und offenen Schnittstellen kann das System leicht um neue Funktionen erweitert werden und bietet somit eine zukunftssichere Lösung für digitale Barrierefreiheit.
