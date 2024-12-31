import numpy as np
import soundfile as sf
import logging
from ..config.settings import SAMPLE_RATE

logger = logging.getLogger(__name__)

def load_audio_file(file_path):
    """Carga un archivo de audio de forma segura"""
    try:
        data, sr = sf.read(file_path)
        if sr != SAMPLE_RATE:
            # Realizar resampling si es necesario
            # Implementar lógica de resampling
            pass
        return data, sr
    except Exception as e:
        logger.error(f"Error al cargar archivo de audio: {e}")
        return None, None

def normalize_audio(y):
    """Normaliza el audio a un rango [-1, 1]"""
    try:
        return y / np.max(np.abs(y))
    except Exception as e:
        logger.error(f"Error al normalizar audio: {e}")
        return y

def split_audio(y, sr, segment_duration=10):
    """Divide el audio en segmentos"""
    try:
        segment_length = int(sr * segment_duration)
        segments = []
        for i in range(0, len(y), segment_length):
            segment = y[i:i + segment_length]
            if len(segment) == segment_length:
                segments.append(segment)
        return segments
    except Exception as e:
        logger.error(f"Error al dividir audio: {e}")
        return []

def apply_fade(y, sr, fade_duration=0.1):
    """Aplica fade in/out al audio"""
    try:
        fade_length = int(sr * fade_duration)
        fade_in = np.linspace(0, 1, fade_length)
        fade_out = np.linspace(1, 0, fade_length)
        
        y[:fade_length] *= fade_in
        y[-fade_length:] *= fade_out
        return y
    except Exception as e:
        logger.error(f"Error al aplicar fade: {e}")
        return y