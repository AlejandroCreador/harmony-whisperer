import librosa
import numpy as np
import logging
from ..config.settings import SAMPLE_RATE, WINDOW_SIZE, HOP_LENGTH

logger = logging.getLogger(__name__)

class AudioAnalyzer:
    """Clase principal para el análisis de audio"""
    
    def __init__(self):
        self.audio_path = None
        self.y = None
        self.sr = None
        
    def load_audio(self, file_path):
        """Carga un archivo de audio"""
        try:
            self.audio_path = file_path
            self.y, self.sr = librosa.load(file_path, sr=SAMPLE_RATE)
            logger.info(f"Audio cargado: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error al cargar audio: {e}")
            return False
    
    def detect_tempo(self):
        """Detecta el tempo del audio"""
        if self.y is None:
            return None
        try:
            tempo, _ = librosa.beat.beat_track(
                y=self.y, 
                sr=self.sr,
                hop_length=HOP_LENGTH
            )
            return tempo
        except Exception as e:
            logger.error(f"Error al detectar tempo: {e}")
            return None
            
    def get_waveform(self):
        """Retorna la forma de onda del audio"""
        return self.y if self.y is not None else None
        
    def get_spectrum(self):
        """Calcula el espectro de frecuencias"""
        if self.y is None:
            return None
        D = librosa.stft(self.y, n_fft=WINDOW_SIZE)
        return librosa.amplitude_to_db(np.abs(D), ref=np.max)