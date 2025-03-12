subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], 
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # requirements.txt installieren
            self.update_log("Installiere Python-Abhängigkeiten in der virtuellen Umgebung...\n")
            
            if platform.system() == "Windows":
                pip_path = venv_dir / "Scripts" / "pip.exe"
                python_path = venv_dir / "Scripts" / "python.exe"
            else:
                pip_path = venv_dir / "bin" / "pip"
                python_path = venv_dir / "bin" / "python"
            
            # Upgrade pip, setuptools, wheel
            subprocess.run([str(pip_path), "install", "--upgrade", "pip", "setuptools", "wheel"],
                         check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Abhängigkeiten installieren
            subprocess.run([str(pip_path), "install", "-r", str(install_dir / "requirements.txt")],
                         check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # OWL installieren
            if (install_dir / "owl").exists():
                self.update_log("Installiere OWL...\n")
                subprocess.run([str(pip_path), "install", "-e", str(install_dir / "owl")],
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Playwright-Browser installieren
            self.update_log("Installiere Playwright-Browser...\n")
            subprocess.run([str(python_path), "-m", "playwright", "install", "chromium"],
                         check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Logdatei erstellen
            log_file = install_dir / "logs" / "install.log"
            with open(log_file, "w") as f:
                for log_entry in self.installation_log:
                    f.write(log_entry)
            
            # README erstellen
            readme_file = install_dir / "README.md"
            with open(readme_file, "w") as f:
                f.write("# HelfQWL Assistenzsystem\n\n")
                f.write(f"Installiert am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("## Starten des Systems\n\n")
                
                if platform.system() == "Windows":
                    f.write("1. Doppelklick auf `start_helfqwl.bat`\n\n")
                else:
                    f.write("1. Terminal öffnen\n")
                    f.write(f"2. `cd {install_dir}`\n")
                    f.write("3. `./start_helfqwl.sh`\n\n")
                
                f.write("## Konfiguration\n\n")
                f.write("Die Konfigurationsdateien befinden sich im Verzeichnis `configs/`.\n\n")
                
                f.write("## Problembehandlung\n\n")
                f.write("Logdateien befinden sich im Verzeichnis `logs/`.\n")
            
            # Einfachen Starter für Anfänger erstellen
            self.create_easy_starter(install_dir)
            
            self.update_log("Abschließende Einrichtung erfolgreich durchgeführt.\n")
        
        except Exception as e:
            self.update_log(f"Fehler bei der abschließenden Einrichtung: {str(e)}\n")
            raise Exception("Fehler bei der abschließenden Einrichtung.")

    def create_easy_starter(self, install_dir):
        """Erstellt einen einfachen Starter für Anfänger mit GUI."""
        self.update_log("Erstelle einfachen Starter für Anfänger...\n")
        
        # Starter-Skript erstellen
        starter_file = install_dir / "helfqwl_starten.py"
        
        starter_code = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HelfQWL Easy Starter
===================

Ein einfacher Starter für das HelfQWL-Assistenzsystem.
"""

import os
import sys
import subprocess
import platform
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
import threading
import time
import signal

class HelfQWLStarter:
    """Ein einfacher Starter für das HelfQWL-Assistenzsystem."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("HelfQWL Starter")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Bestimme den Installationsordner
        self.install_dir = Path(__file__).parent
        self.running = False
        self.process = None
        
        # Style konfigurieren
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))
        style.configure('Big.TButton', font=('Arial', 14, 'bold'))
        style.configure('TLabel', font=('Arial', 12))
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Title.TLabel', font=('Arial', 24, 'bold'))
        
        # Hauptframe
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titel
        title_label = ttk.Label(main_frame, text="HelfQWL Assistenzsystem", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Beschreibung
        desc_text = "Ihr intelligenter Assistent für barrierefreien Zugang zu Ihrem Computer."
        desc_label = ttk.Label(main_frame, text=desc_text, font=('Arial', 14))
        desc_label.pack(pady=(0, 30))
        
        # Start-Button
        self.start_button = ttk.Button(
            main_frame, 
            text="HelfQWL starten", 
            command=self.toggle_helfqwl,
            style='Big.TButton',
            width=30
        )
        self.start_button.pack(pady=10)
        
        # Status-Anzeige
        self.status_var = tk.StringVar(value="Bereit zum Start")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, font=('Arial', 12))
        status_label.pack(pady=10)
        
        # Fortschrittsanzeige (im Startzustand versteckt)
        self.progress_var = tk.DoubleVar(value=0)
        self.progress = ttk.Progressbar(
            main_frame,
            orient="horizontal",
            length=300,
            mode="indeterminate",
            variable=self.progress_var
        )
        
        # Log-Anzeige
        log_frame = ttk.LabelFrame(main_frame, text="Ausgabe", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.config(state=tk.DISABLED)
        
        # Aktivierungswort anzeigen
        try:
            import dotenv
            dotenv.load_dotenv(self.install_dir / ".env")
            wake_word = os.environ.get("WAKE_WORD", "helf quell")
        except:
            wake_word = "helf quell"
        
        wake_frame = ttk.Frame(main_frame)
        wake_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(wake_frame, text=f"Aktivierungswort:", font=('Arial', 12, 'bold')).pack(side=tk.LEFT)
        ttk.Label(wake_frame, text=f" {wake_word}", font=('Arial', 12)).pack(side=tk.LEFT)
        
        # Info-Label mit Hilfe
        help_text = (
            f"Sagen Sie '{wake_word}', um den Assistenten zu aktivieren.\n"
            f"Beispiele für Befehle: 'Wie ist das Wetter?', 'Öffne den Browser', 'Lies diesen Text'"
        )
        help_label = ttk.Label(main_frame, text=help_text, justify=tk.CENTER)
        help_label.pack(pady=10)
        
        # Copyright
        copyright_label = ttk.Label(
            main_frame, 
            text=f"HelfQWL v1.0.0 - Installiert in: {self.install_dir}",
            font=('Arial', 8)
        )
        copyright_label.pack(side=tk.BOTTOM, pady=(20, 0))
        
        # Fenster zentrieren
        self.center_window()
        
        # Beim Schließen sicherstellen, dass der Prozess beendet wird
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def center_window(self):
        """Zentriert das Fenster auf dem Bildschirm."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def toggle_helfqwl(self):
        """Startet oder stoppt HelfQWL."""
        if not self.running:
            self.start_helfqwl()
        else:
            self.stop_helfqwl()
    
    def start_helfqwl(self):
        """Startet HelfQWL."""
        self.log("HelfQWL wird gestartet...\n")
        self.status_var.set("Starte HelfQWL...")
        self.start_button.config(text="HelfQWL stoppen")
        
        # Fortschrittsanzeige anzeigen
        self.progress.pack(pady=10)
        self.progress.start()
        
        # Thread starten, um die GUI nicht zu blockieren
        self.running = True
        threading.Thread(target=self._run_helfqwl, daemon=True).start()
    
    def _run_helfqwl(self):
        """Führt HelfQWL im Hintergrund aus."""
        try:
            # Virtuelles Environment bestimmen
            if platform.system() == "Windows":
                python_path = self.install_dir / "venv" / "Scripts" / "python.exe"
                activate_cmd = f"{self.install_dir / 'venv' / 'Scripts' / 'activate.bat'}"
            else:
                python_path = self.install_dir / "venv" / "bin" / "python"
                activate_cmd = f"source {self.install_dir / 'venv' / 'bin' / 'activate'}"
            
            # Prüfen, ob virtuelles Environment existiert
            if not python_path.exists():
                self.log_error("Virtuelles Environment nicht gefunden! Bitte HelfQWL neu installieren.\n")
                self.root.after(0, self._reset_ui)
                return
            
            # Run-Skript bestimmen
            run_script = self.install_dir / "run.py"
            
            if not run_script.exists():
                self.log_error("Start-Skript nicht gefunden! Bitte HelfQWL neu installieren.\n")
                self.root.after(0, self._reset_ui)
                return
            
            # Befehl zusammenstellen und ausführen
            if platform.system() == "Windows":
                cmd = [str(python_path), str(run_script)]
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    cwd=str(self.install_dir)
                )
            else:
                cmd = [str(python_path), str(run_script)]
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    cwd=str(self.install_dir)
                )
            
            # Output verarbeiten
            while self.running:
                line = self.process.stdout.readline()
                if not line and self.process.poll() is not None:
                    break
                if line:
                    self.log(line)
            
            # Prüfen, ob der Prozess noch läuft
            if self.process.poll() is None:
                # Prozess läuft noch, beenden
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Prozess reagiert nicht, hart abbrechen
                    if platform.system() == "Windows":
                        subprocess.run(['taskkill', '/F', '/T', '/PID', str(self.process.pid)])
                    else:
                        os.kill(self.process.pid, signal.SIGKILL)
            
            self.root.after(0, self._reset_ui)
        
        except Exception as e:
            self.log_error(f"Fehler beim Starten von HelfQWL: {str(e)}\n")
            self.root.after(0, self._reset_ui)
    
    def stop_helfqwl(self):
        """Stoppt HelfQWL."""
        if not self.running:
            return
        
        self.log("HelfQWL wird gestoppt...\n")
        self.status_var.set("Stoppe HelfQWL...")
        self.running = False
        
        if self.process and self.process.poll() is None:
            # Prozess beenden
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                # Prozess reagiert nicht, hart abbrechen
                if platform.system() == "Windows":
                    subprocess.run(['taskkill', '/F', '/T', '/PID', str(self.process.pid)])
                else:
                    os.kill(self.process.pid, signal.SIGKILL)
        
        # UI zurücksetzen
        self._reset_ui()
    
    def _reset_ui(self):
        """Setzt die UI nach dem Stoppen zurück."""
        self.running = False
        self.process = None
        self.start_button.config(text="HelfQWL starten")
        self.status_var.set("Bereit zum Start")
        self.progress.stop()
        self.progress.pack_forget()
    
    def log(self, message):
        """Fügt eine Nachricht zum Log hinzu."""
        self.root.after(0, lambda: self._update_log(message))
    
    def log_error(self, message):
        """Fügt eine Fehlermeldung zum Log hinzu."""
        formatted_message = f"FEHLER: {message}"
        self.root.after(0, lambda: self._update_log(formatted_message))
    
    def _update_log(self, message):
        """Aktualisiert das Log-Textfeld."""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def on_close(self):
        """Handler für das Schließen des Fensters."""
        if self.running:
            if messagebox.askyesno("HelfQWL beenden", 
                                  "HelfQWL läuft noch. Möchten Sie HelfQWL beenden und den Starter schließen?"):
                self.stop_helfqwl()
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    root = tk.Tk()
    app = HelfQWLStarter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
"""
        
        with open(starter_file, "w") as f:
            f.write(starter_code)
        
        # Ausführbar machen (für Linux/Mac)
        if platform.system() != "Windows":
            starter_file.chmod(starter_file.stat().st_mode | 0o755)
        
        # Verknüpfung erstellen
        if platform.system() == "Windows":
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            shortcut_path = os.path.join(desktop_path, "HelfQWL Starten.lnk")
            
            try:
                import win32com.client
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = str(sys.executable)
                shortcut.Arguments = f'"{starter_file}"'
                shortcut.WorkingDirectory = str(install_dir)
                shortcut.IconLocation = f"{sys.executable}, 0"
                shortcut.Description = "HelfQWL Assistenzsystem starten"
                shortcut.save()
            except:
                self.update_log("Konnte keine Desktop-Verknüpfung für den einfachen Starter erstellen.\n")
        
        self.update_log("Einfacher Starter erstellt.\n")

    def installation_complete(self):
        """Zeigt den Abschlussbildschirm nach erfolgreicher Installation an."""
        frame = ttk.Frame(self.main_frame)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titel
        title_label = ttk.Label(
            frame, 
            text="Installation abgeschlossen", 
            style='Header.TLabel'
        )
        title_label.pack(pady=10)
        
        # Erfolgsmeldung
        success_frame = ttk.Frame(frame)
        success_frame.pack(fill=tk.X, pady=20)
        
        success_message = ttk.Label(
            success_frame,
            text="HelfQWL wurde erfolgreich installiert!",
            foreground="green",
            font=('Arial', 12, 'bold')
        )
        success_message.pack()
        
        # Installationsinformationen
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill=tk.X, pady=10)
        
        install_dir = self.config['installation']['install_dir']
        
        info_text = (
            f"Installation abgeschlossen in: {install_dir}\n\n"
            "Sie können HelfQWL nun auf zwei Arten starten:\n"
        )
        
        if platform.system() == "Windows":
            info_text += f"• Über die Desktop-Verknüpfung 'HelfQWL Starten'\n"
            info_text += f"• Oder direkt über: {os.path.join(install_dir, 'helfqwl_starten.py')}\n"
        else:
            info_text += f"• Durch Ausführen von: {os.path.join(install_dir, 'helfqwl_starten.py')}\n"
            info_text += f"• Oder durch Ausführen von: {os.path.join(install_dir, 'start_helfqwl.sh')}\n"
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT)
        info_label.pack(pady=10, anchor=tk.W)
        
        # Wake-Word-Information
        wake_word = self.config['voice']['wake_word']
        wake_info = ttk.Label(
            info_frame,
            text=f"Aktivierungswort: '{wake_word}'\n"
                 "Sagen Sie dieses Wort, um mit HelfQWL zu sprechen.",
            justify=tk.LEFT
        )
        wake_info.pack(pady=10, anchor=tk.W)
        
        # Schaltflächen
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=20)
        
        # Schaltfläche zum Öffnen des Installationsverzeichnisses
        open_dir_button = ttk.Button(
            button_frame, 
            text="Installationsverzeichnis öffnen", 
            command=lambda: self.open_directory(install_dir)
        )
        open_dir_button.pack(side=tk.LEFT, padx=5)
        
        # Schaltfläche zum Starten von HelfQWL
        start_button = ttk.Button(
            button_frame, 
            text="HelfQWL jetzt starten", 
            command=lambda: self.start_helfqwl_easy(install_dir)
        )
        start_button.pack(side=tk.RIGHT, padx=5)
        
        # Schaltfläche zum Beenden
        exit_button = ttk.Button(
            button_frame, 
            text="Beenden", 
            command=self.root.destroy
        )
        exit_button.pack(side=tk.RIGHT, padx=5)
        
        # Status aktualisieren
        self.status_var.set("Installation erfolgreich abgeschlossen")
        
        # Fortschritt vollständig
        self.progress_var.set(100)
    
    def open_directory(self, directory):
        """Öffnet ein Verzeichnis im Dateiexplorer."""
        try:
            if platform.system() == "Windows":
                os.startfile(directory)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", directory], check=True)
            else:  # Linux
                subprocess.run(["xdg-open", directory], check=True)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Öffnen des Verzeichnisses: {str(e)}")
    
    def start_helfqwl_easy(self, install_dir):
        """Startet den einfachen HelfQWL-Starter."""
        try:
            starter_file = os.path.join(install_dir, "helfqwl_starten.py")
            
            if platform.system() == "Windows":
                # Für Windows: direkt mit Python ausführen
                subprocess.Popen([sys.executable, starter_file], cwd=install_dir)
            else:
                # Für Linux/macOS: als ausführbare Datei ausführen
                subprocess.Popen([starter_file], cwd=install_dir)
            
            # Installer beenden
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Starten von HelfQWL: {str(e)}")


def main():
    """Hauptfunktion zum Starten des Installationsassistenten."""
    # Installationszustand prüfen
    resume_file = Path("helfqwl_install_resume.json")
    resume_config = None
    
    if resume_file.exists():
        try:
            with open(resume_file, "r") as f:
                resume_config = json.load(f)
            
            # Datei löschen
            resume_file.unlink()
        except Exception:
            pass
    
    # GUI erstellen
    root = tk.Tk()
    root.title(APP_TITLE)
    
    # Programm-Icon setzen
    try:
        # Wenn verfügbar, Icon laden
        icon_file = "helfqwl_icon.ico"
        if os.path.exists(icon_file):
            root.iconbitmap(icon_file)
    except Exception:
        pass
    
    # Installationsassistent erstellen
    app = EasyInstaller(root)
    
    # Wenn Wiederaufnahme möglich, Konfiguration laden
    if resume_config:
        app.config = resume_config
        messagebox.showinfo("Installation fortsetzen", 
                         "Die letzte Installation wurde unterbrochen. Die Konfiguration wurde wiederhergestellt.")
    
    # Hauptschleife starten
    root.mainloop()


if __name__ == "__main__":
    main()
