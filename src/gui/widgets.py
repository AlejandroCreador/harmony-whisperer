import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(__name__)

class ControlPanel(ttk.Frame):
    """Panel de control personalizado"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_widgets()
        
    def setup_widgets(self):
        # Botones de control
        self.analyze_btn = ttk.Button(
            self,
            text="Analizar",
            command=self.master.analyze_audio
        )
        self.analyze_btn.pack(pady=5)
        
        # Controles de visualización
        self.view_var = tk.StringVar(value="waveform")
        self.create_view_controls()
        
    def create_view_controls(self):
        """Crea controles para cambiar la visualización"""
        views = [
            ("Forma de onda", "waveform"),
            ("Espectrograma", "spectrogram"),
            ("Acordes", "chords")
        ]
        
        for text, value in views:
            ttk.Radiobutton(
                self,
                text=text,
                value=value,
                variable=self.view_var
            ).pack(anchor=tk.W)

class StatusBar(ttk.Frame):
    """Barra de estado personalizada"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_widgets()
        
    def setup_widgets(self):
        self.status_label = ttk.Label(
            self,
            text="Listo",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X)
        
    def set_status(self, text):
        """Actualiza el texto de estado"""
        self.status_label.config(text=text)

class ProgressBar(ttk.Frame):
    """Barra de progreso personalizada"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_widgets()
        
    def setup_widgets(self):
        self.progress = ttk.Progressbar(
            self,
            orient=tk.HORIZONTAL,
            length=200,
            mode='determinate'
        )
        self.progress.pack(pady=5)
        
    def update_progress(self, value):
        """Actualiza el valor de la barra de progreso"""
        self.progress['value'] = value
        self.update_idletasks()