# HelfQWL: Vollständige Installationsanleitung für Windows 10

Diese Anleitung führt Sie durch die Installation des HelfQWL-Assistenzsystems auf einem frischen Windows 10-Laptop. Alle Schritte sind detailliert erklärt und für Anfänger verständlich.

## Teil 1: Systemvoraussetzungen und Vorbereitung

### Benötigte Hardware
- Laptop mit Intel i7 Prozessor oder vergleichbar
- Mindestens 16 GB RAM
- NVIDIA GeForce 2080 Grafikkarte (oder vergleichbar) mit 8 GB VRAM
- Mindestens 50 GB freier Festplattenspeicher (SSD empfohlen)
- Mikrofon und Lautsprecher

### Systemvorbereitungen

1. **Windows-Updates installieren**:
   - Drücken Sie `Windows-Taste + I`, um die Einstellungen zu öffnen
   - Wählen Sie "Update und Sicherheit"
   - Klicken Sie auf "Nach Updates suchen" und installieren Sie alle verfügbaren Updates
   - Starten Sie den Computer neu

2. **NVIDIA-Treiber installieren**:
   - Besuchen Sie [nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)
   - Wählen Sie Ihre Grafikkarte aus und laden Sie den aktuellen Treiber herunter
   - Führen Sie die Installationsdatei aus und folgen Sie den Anweisungen
   - Starten Sie den Computer nach der Installation neu

## Teil 2: Einrichtung von Windows Subsystem für Linux (WSL)

1. **WSL aktivieren**:
   - Drücken Sie `Windows-Taste + X` und wählen Sie "Windows PowerShell (Administrator)"
   - Geben Sie folgenden Befehl ein und drücken Sie Enter:
     ```
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```
   - Geben Sie dann diesen Befehl ein:
     ```
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```
   - Starten Sie Ihren Computer neu

2. **WSL 2 als Standardversion festlegen**:
   - Laden Sie das WSL2-Kernel-Update herunter: [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)
   - Installieren Sie das Update
   - Öffnen Sie die PowerShell als Administrator und führen Sie aus:
     ```
     wsl --set-default-version 2
     ```

3. **Ubuntu 22.04 installieren**:
   - Öffnen Sie den Microsoft Store
   - Suchen Sie nach "Ubuntu 22.04 LTS"
   - Klicken Sie auf "Installieren"
   - Nach der Installation auf "Starten" klicken
   - Warten Sie, bis die Installation abgeschlossen ist
   - Legen Sie einen Benutzernamen und Passwort fest (merken Sie sich diese!)

## Teil 3: Ubuntu-Umgebung einrichten

1. **Grundlegende Pakete installieren**:
   - Öffnen Sie Ubuntu über das Startmenü
   - Aktualisieren Sie das Paketsystem mit:
     ```
     sudo apt update && sudo apt upgrade -y
     ```
   - Installieren Sie die benötigten Pakete:
     ```
     sudo apt install -y python3-pip python3-venv build-essential libpq-dev portaudio19-dev ffmpeg git curl wget
     ```

2. **NVIDIA CUDA für WSL einrichten**:
   - Besuchen Sie die NVIDIA-Website für [CUDA on WSL](https://developer.nvidia.com/cuda/wsl)
   - Laden Sie das CUDA Toolkit für WSL herunter
   - Installieren Sie es mit folgenden Befehlen:
     ```
     wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
     sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
     wget https://developer.download.nvidia.com/compute/cuda/12.2.0/local_installers/cuda-repo-wsl-ubuntu-12-2-local_12.2.0-1_amd64.deb
     sudo dpkg -i cuda-repo-wsl-ubuntu-12-2-local_12.2.0-1_amd64.deb
     sudo cp /var/cuda-repo-wsl-ubuntu-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/
     sudo apt-get update
     sudo apt-get -y install cuda
     ```
   - Fügen Sie CUDA zum Pfad hinzu:
     ```
     echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
     echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
     source ~/.bashrc
     ```
   - Überprüfen Sie die Installation:
     ```
     nvcc --version
     ```

## Teil 4: PostgreSQL einrichten

1. **PostgreSQL installieren**:
   ```
   sudo apt install -y postgresql postgresql-contrib
   ```

2. **PostgreSQL-Dienst starten**:
   ```
   sudo service postgresql start
   ```

3. **Datenbank für HelfQWL erstellen**:
   ```
   sudo -u postgres psql -c "CREATE USER helfqwl WITH PASSWORD 'sicheres-passwort';"
   sudo -u postgres psql -c "CREATE DATABASE helfqwl OWNER helfqwl;"
   sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE helfqwl TO helfqwl;"
   ```

4. **PostgreSQL für Netzwerkzugriff konfigurieren**:
   ```
   sudo nano /etc/postgresql/*/main/postgresql.conf
   ```
   - Ändern Sie die Zeile `#listen_addresses = 'localhost'` zu `listen_addresses = '*'`
   - Speichern Sie mit STRG+O, Enter und beenden Sie mit STRG+X
   ```
   sudo nano /etc/postgresql/*/main/pg_hba.conf
   ```
   - Fügen Sie am Ende der Datei hinzu: `host all all 0.0.0.0/0 md5`
   - Speichern Sie mit STRG+O, Enter und beenden Sie mit STRG+X
   ```
   sudo service postgresql restart
   ```

## Teil 5: HelfQWL installieren

1. **Git-Repository klonen**:
   ```
   mkdir -p ~/projekte
   cd ~/projekte
   git clone https://github.com/username/helfqwl.git
   cd helfqwl
   ```

2. **Virtuelle Python-Umgebung erstellen**:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel
   ```

3. **Abhängigkeiten installieren**:
   ```
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen konfigurieren**:
   ```
   cp .env.example .env
   nano .env
   ```
   - Passen Sie die Umgebungsvariablen an (z.B. API-Schlüssel)
   - Achten Sie besonders auf diese Einstellungen:
     ```
     POSTGRES_USER=helfqwl
     POSTGRES_PASSWORD=sicheres-passwort
     POSTGRES_DB=helfqwl
     POSTGRES_HOST=localhost
     
     OPENAI_API_KEY=ihr-openai-schlüssel  # Optional, falls verwendet
     QWEN_API_KEY=ihr-qwen-api-schlüssel  # Wichtig für Qwen-Modell
     
     WAKE_WORD=helf quell  # Oder Ihr bevorzugtes Aktivierungswort
     ```
   - Speichern Sie mit STRG+O, Enter und beenden Sie mit STRG+X

## Teil 6: Modelle herunterladen und System initialisieren

1. **Notwendige Modelle herunterladen**:
   ```
   mkdir -p models/{qwen,spark-tts,vosk,mistral-ocr,wake_word}
   python scripts/download_models.py
   ```
   - Dieser Vorgang kann je nach Internetgeschwindigkeit 30-60 Minuten dauern
   - Die Modelle haben eine Gesamtgröße von etwa 15-20 GB

2. **Datenbank initialisieren**:
   ```
   python scripts/manage_database.py initialize
   ```

3. **Wake-Word-Modell einrichten**:
   ```
   python scripts/setup_wake_word.py --keyword "helf quell"
   ```
   - Alternativ können Sie ein anderes Aktivierungswort verwenden

## Teil 7: System starten und konfigurieren

1. **Kamera und Mikrofon einrichten**:
   - Stellen Sie sicher, dass Ihre Webcam und Ihr Mikrofon funktionieren
   - Testen Sie sie in Windows, um sicherzustellen, dass sie richtig eingerichtet sind

2. **HelfQWL zum ersten Mal starten**:
   ```
   cd ~/projekte/helfqwl
   source venv/bin/activate
   python run.py
   ```

3. **Erste Konfiguration durchführen**:
   - Das System startet mit einer Ersteinrichtung
   - Folgen Sie den Anweisungen auf dem Bildschirm zur Konfiguration von:
     - Sprache und Stimme
     - Bildschirmanalyse-Einstellungen
     - Vergrößerungsfaktoren
     - Smartphone-Verbindung (optional)
     - IoT-Geräteeinrichtung (optional)

4. **Benutzeranleitung anzeigen lassen**:
   - Sagen Sie: "Hey Quell, zeige mir die Benutzeranleitung"
   - Alternativ können Sie eingeben: "Zeige Benutzeranleitung"

## Teil 8: Android-App installieren (optional)

1. **APK herunterladen**:
   ```
   cd ~/projekte/helfqwl
   python scripts/generate_app_qr.py
   ```
   - Ein QR-Code wird angezeigt, den Sie mit Ihrem Smartphone scannen können

2. **App auf dem Smartphone installieren**:
   - Scannen Sie den QR-Code mit Ihrem Android-Smartphone
   - Laden Sie die APK-Datei herunter
   - Öffnen Sie die heruntergeladene Datei und installieren Sie die App
   - Sie müssen möglicherweise die Installation von Apps aus unbekannten Quellen zulassen

3. **App mit HelfQWL verbinden**:
   - Öffnen Sie die HelfQWL-App auf Ihrem Smartphone
   - Gehen Sie zu "Einstellungen" > "Verbindung"
   - Geben Sie die IP-Adresse Ihres Computers ein (angezeigt in der Konsole von HelfQWL)
   - Klicken Sie auf "Verbinden"
   - Bestätigen Sie die Verbindung am Computer, wenn Sie dazu aufgefordert werden

## Teil 9: Mit HelfQWL interagieren

1. **System aktivieren**:
   - Sagen Sie laut und deutlich: "Hey Quell" (oder Ihr gewähltes Aktivierungswort)
   - Das System sollte mit einem Ton antworten, der die Erkennung bestätigt

2. **Erste Kommandos**:
   - Nach der Aktivierung können Sie Fragen stellen oder Befehle geben, zum Beispiel:
     - "Wie ist das Wetter heute?"
     - "Öffne den Browser und suche nach aktuellen Nachrichten"
     - "Vergrößere den Bildschirminhalt"
     - "Lies mir den Text auf dem Bildschirm vor"

3. **Systemsteuerung**:
   - Um das System zu pausieren: "Hey Quell, Pause"
   - Um das System zu beenden: "Hey Quell, beenden"
   - Um die Lautstärke anzupassen: "Hey Quell, lauter" oder "Hey Quell, leiser"

4. **Hilfe erhalten**:
   - Bei Fragen zur Bedienung: "Hey Quell, wie kann ich dich benutzen?"
   - Für eine Liste der Befehle: "Hey Quell, zeige alle Befehle"

5. **Websuche und Browser-Steuerung**:
   - "Suche im Internet nach [Thema]"
   - "Öffne die Webseite [URL]"
   - "Scrolle nach unten" oder "Scrolle nach oben"
   - "Klicke auf den Link [Linkname]"

6. **Bildschirmanalyse**:
   - "Beschreibe, was auf dem Bildschirm zu sehen ist"
   - "Lies den Text im markierten Bereich"
   - "Finde den Button zum Anmelden"

7. **Smartphone-Steuerung (falls verbunden)**:
   - "Zeige mir das Kamerabild meines Smartphones"
   - "Mache ein Foto mit meinem Smartphone"
   - "Lese die Benachrichtigungen auf meinem Smartphone"

## Fehlerbehebung

### Das System startet nicht
1. Überprüfen Sie, ob PostgreSQL läuft:
   ```
   sudo service postgresql status
   ```
   Falls nicht, starten Sie es mit:
   ```
   sudo service postgresql start
   ```

2. Überprüfen Sie die CUDA-Installation:
   ```
   nvcc --version
   ```
   Falls nicht gefunden, installieren Sie CUDA erneut.

3. Überprüfen Sie die Python-Umgebung:
   ```
   which python
   python --version
   ```
   Vergewissern Sie sich, dass Sie in der virtuellen Umgebung sind.

### Das Wake-Word wird nicht erkannt
1. Testen Sie Ihr Mikrofon in Windows
2. Prüfen Sie die Mikrofoneinstellungen in Ubuntu:
   ```
   arecord -l
   ```
3. Trainieren Sie das Wake-Word erneut:
   ```
   python scripts/setup_wake_word.py --retrain --keyword "helf quell"
   ```

### Die Verbindung zur App funktioniert nicht
1. Überprüfen Sie, ob Computer und Smartphone im selben Netzwerk sind
2. Prüfen Sie die Firewall-Einstellungen in Windows
3. Überprüfen Sie die IP-Adresse und den Port

### Das System reagiert langsam
1. Überprüfen Sie die GPU-Nutzung:
   ```
   nvidia-smi
   ```
2. Prüfen Sie die CPU- und Speichernutzung:
   ```
   top
   ```
3. Passen Sie die Konfiguration in `configs/orchestrator.yaml` an, um weniger ressourcenintensive Modelle zu verwenden

## Nächste Schritte

1. **System anpassen**:
   - Bearbeiten Sie die Konfigurationsdateien im Verzeichnis `configs/`
   - Fügen Sie benutzerdefinierte Skripte hinzu für spezifische Szenarien

2. **Neue Module hinzufügen**:
   - Folgen Sie der Dokumentation zur Modulentwicklung
   - Platzieren Sie neue Module im Verzeichnis `helfqwl/modules/`

3. **Updates installieren**:
   ```
   cd ~/projekte/helfqwl
   git pull
   source venv/bin/activate
   pip install -r requirements.txt
   python scripts/download_models.py --check-updates
   ```

4. **Backups erstellen**:
   ```
   python scripts/create_backup.py
   ```

---

Herzlichen Glückwunsch! Sie haben HelfQWL erfolgreich installiert und konfiguriert. Das System ist nun bereit, Ihnen bei der barrierefreien Computer- und Gerätenutzung zu helfen. Bei Fragen können Sie jederzeit "Hey Quell, ich brauche Hilfe" sagen, um Unterstützung zu erhalten.
