import tkinter as tk
from tkinter import ttk, filedialog
import logging
from ..core.audio_analyzer import AudioAnalyzer
from ..core.chord_analyzer import ChordAnalyzer
from .visualizations import WaveformVisualizer
from ..config.settings import APP_NAME, WINDOW_SIZE

logger = logging.getLogger(__name__)

class HarmonyWhispererGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.root.geometry(WINDOW_SIZE)
        
        self.audio_analyzer = AudioAnalyzer()
        self.chord_analyzer = ChordAnalyzer()
        self.visualizer = WaveformVisualizer()
        
        self.setup_gui()
        
    def setup_gui(self):
        """Configura la interfaz gráfica"""
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        
    def create_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.load_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        
        # Menú Análisis
        analysis_menu = tk.Menu(menubar, tearoff=0)
        analysis_menu.add_command(label="Analizar Audio", command=self.analyze_audio)
        menubar.add_cascade(label="Análisis", menu=analysis_menu)
        
        self.root.config(menu=menubar)
    
    def create_main_frame(self):
        """Crea el frame principal"""
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Área de resultados
        self.result_text = tk.Text(self.main_frame, height=10, width=50)
        self.result_text.grid(row=0, column=0, pady=5)
        
    def create_status_bar(self):
        """Crea la barra de estado"""
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.status_var.set("Listo")
    
    def load_file(self):
        """Carga un archivo de audio"""
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Audio Files", "*.mp3 *.wav")]
            )
            if file_path:
                if self.audio_analyzer.load_audio(file_path):
                    self.status_var.set(f"Archivo cargado: {file_path}")
                else:
                    self.status_var.set("Error al cargar el archivo")
        except Exception as e:
            logger.error(f"Error al cargar archivo: {e}")
            self.status_var.set("Error al cargar el archivo")
    
    def analyze_audio(self):
        """Realiza el análisis del audio"""
        pass  # Implementar análisis
        
    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()