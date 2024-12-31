from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class MusicTheory:
    """Clase para manejar la teoría musical y análisis armónico"""
    
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # Estructuras de acordes comunes
    CHORD_STRUCTURES = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8],
        'major7': [0, 4, 7, 11],
        'minor7': [0, 3, 7, 10],
        'dominant7': [0, 4, 7, 10]
    }
    
    # Progresiones comunes por género
    COMMON_PROGRESSIONS = {
        'pop': [
            ['I', 'IV', 'V', 'I'],
            ['I', 'V', 'vi', 'IV'],
            ['ii', 'V', 'I']
        ],
        'jazz': [
            ['ii7', 'V7', 'Imaj7'],
            ['iii7', 'vi7', 'ii7', 'V7']
        ],
        'blues': [
            ['I7', 'IV7', 'I7', 'V7', 'IV7', 'I7']
        ]
    }
    
    @classmethod
    def get_scale_degrees(cls, key: str, scale_type: str = 'major') -> List[str]:
        """Retorna los grados de una escala"""
        try:
            start_idx = cls.NOTES.index(key)
            if scale_type == 'major':
                intervals = [0, 2, 4, 5, 7, 9, 11]
            elif scale_type == 'minor':
                intervals = [0, 2, 3, 5, 7, 8, 10]
            else:
                raise ValueError(f"Tipo de escala no soportado: {scale_type}")
                
            return [cls.NOTES[(start_idx + interval) % 12] for interval in intervals]
        except Exception as e:
            logger.error(f"Error al obtener grados de escala: {e}")
            return []

    @classmethod
    def get_chord_notes(cls, root: str, chord_type: str) -> List[str]:
        """Retorna las notas que componen un acorde"""
        try:
            if chord_type not in cls.CHORD_STRUCTURES:
                raise ValueError(f"Tipo de acorde no soportado: {chord_type}")
                
            root_idx = cls.NOTES.index(root)
            intervals = cls.CHORD_STRUCTURES[chord_type]
            return [cls.NOTES[(root_idx + interval) % 12] for interval in intervals]
        except Exception as e:
            logger.error(f"Error al obtener notas del acorde: {e}")
            return []

    @classmethod
    def suggest_chord_progression(cls, key: str, genre: str = 'pop') -> List[str]:
        """Sugiere una progresión de acordes basada en el género"""
        try:
            if genre not in cls.COMMON_PROGRESSIONS:
                raise ValueError(f"Género no soportado: {genre}")
                
            # Seleccionar una progresión aleatoria del género
            import random
            progression = random.choice(cls.COMMON_PROGRESSIONS[genre])
            
            # Convertir números romanos a acordes reales
            scale = cls.get_scale_degrees(key)
            real_progression = []
            
            for degree in progression:
                # Implementar la conversión de grado a acorde real
                # Esta es una implementación simplificada
                degree_idx = {'I': 0, 'ii': 1, 'iii': 2, 'IV': 3, 
                            'V': 4, 'vi': 5, 'vii': 6}
                base_degree = ''.join(c for c in degree if c.isalpha())
                if base_degree in degree_idx:
                    chord_root = scale[degree_idx[base_degree]]
                    real_progression.append(chord_root)
                    
            return real_progression
        except Exception as e:
            logger.error(f"Error al sugerir progresión: {e}")
            return []

    @staticmethod
    def calculate_harmony_complexity(chord_progression: List[str]) -> float:
        """Calcula la complejidad armónica de una progresión"""
        try:
            # Implementar método de cálculo de complejidad
            # Esta es una implementación simplificada
            unique_chords = len(set(chord_progression))
            progression_length = len(chord_progression)
            return unique_chords / progression_length
        except Exception as e:
            logger.error(f"Error al calcular complejidad: {e}")
            return 0.0

    @classmethod
    def analyze_chord_function(cls, chord: str, key: str) -> str:
        """Analiza la función armónica de un acorde en una tonalidad"""
        try:
            scale = cls.get_scale_degrees(key)
            chord_root = chord[0]  # Simplificado, solo considera la raíz
            
            if chord_root in scale:
                degree = scale.index(chord_root)
                roman_numerals = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
                return roman_numerals[degree]
            return "N/A"
        except Exception as e:
            logger.error(f"Error al analizar función del acorde: {e}")
            return "N/A"