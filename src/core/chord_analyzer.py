import librosa
import numpy as np
import logging
from ..config.settings import SAMPLE_RATE

logger = logging.getLogger(__name__)

class ChordAnalyzer:
    """Analizador de acordes y armonía"""
    
    def __init__(self):
        self.chord_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.common_progressions = {
            'C': ['C', 'F', 'G', 'C'],  # I-IV-V-I
            'G': ['G', 'C', 'D', 'G'],
            'D': ['D', 'G', 'A', 'D'],
            'A': ['A', 'D', 'E', 'A'],
        }

    def analyze_chords(self, y, sr):
        """Analiza los acordes presentes en el audio"""
        try:
            harmonic = librosa.effects.harmonic(y)
            chroma = librosa.feature.chroma_cqt(y=harmonic, sr=sr)
            return self._detect_chords(chroma)
        except Exception as e:
            logger.error(f"Error en análisis de acordes: {e}")
            return []

    def _detect_chords(self, chroma):
        """Detecta acordes a partir de cromagramas"""
        chord_detection = []
        for i in range(chroma.shape[1]):
            chord_idx = np.argmax(chroma[:,i])
            chord_detection.append(self.chord_names[chord_idx])
        return self._simplify_chord_sequence(chord_detection)
    
    def _simplify_chord_sequence(self, chord_sequence, window_size=8):
        """Simplifica la secuencia de acordes"""
        from collections import Counter
        simplified = []
        for i in range(0, len(chord_sequence), window_size):
            window = chord_sequence[i:i+window_size]
            most_common = Counter(window).most_common(1)[0][0]
            simplified.append(most_common)
        return simplified

    def suggest_progression(self, root_chord):
        """Sugiere una progresión de acordes"""
        return self.common_progressions.get(root_chord, ['C', 'F', 'G', 'C'])