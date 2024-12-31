import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import logging

logger = logging.getLogger(__name__)

class WaveformVisualizer:
    """Clase para visualizar formas de onda y espectrogramas"""
    
    def __init__(self):
        self.fig = None
        self.canvas = None
        
    def setup_canvas(self, master):
        """Configura el canvas de matplotlib"""
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        return self.canvas.get_tk_widget()
        
    def plot_waveform(self, y, sr):
        """Dibuja la forma de onda"""
        try:
            if self.ax is None:
                return
                
            self.ax.clear()
            time = np.arange(len(y)) / sr
            self.ax.plot(time, y)
            self.ax.set_xlabel('Tiempo (s)')
            self.ax.set_ylabel('Amplitud')
            self.ax.set_title('Forma de Onda')
            self.canvas.draw()
        except Exception as e:
            logger.error(f"Error al dibujar forma de onda: {e}")
            
    def plot_spectrogram(self, D):
        """Dibuja el espectrograma"""
        try:
            if self.ax is None:
                return
                
            self.ax.clear()
            self.ax.imshow(D, aspect='auto', origin='lower')
            self.ax.set_xlabel('Tiempo (frames)')
            self.ax.set_ylabel('Frecuencia (bins)')
            self.ax.set_title('Espectrograma')
            self.canvas.draw()
        except Exception as e:
            logger.error(f"Error al dibujar espectrograma: {e}")
            
    def plot_chord_progression(self, chords, times):
        """Visualiza la progresión de acordes"""
        try:
            if self.ax is None:
                return
                
            self.ax.clear()
            self.ax.set_yticks(range(len(chords)))
            self.ax.set_yticklabels(chords)
            self.ax.grid(True)
            self.ax.set_title('Progresión de Acordes')
            self.canvas.draw()
        except Exception as e:
            logger.error(f"Error al visualizar acordes: {e}")