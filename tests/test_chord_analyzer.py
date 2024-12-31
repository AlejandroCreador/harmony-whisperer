import unittest
import numpy as np
from src.core.chord_analyzer import ChordAnalyzer

class TestChordAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ChordAnalyzer()
        # Crear datos de prueba
        self.sample_rate = 44100
        self.duration = 3
        self.t = np.linspace(0, self.duration, self.sample_rate * self.duration)
        
        # Crear un acorde simple (C mayor)
        self.c_freq = 261.63  # C4
        self.e_freq = 329.63  # E4
        self.g_freq = 392.00  # G4
        self.test_chord = (np.sin(2 * np.pi * self.c_freq * self.t) +
                          np.sin(2 * np.pi * self.e_freq * self.t) +
                          np.sin(2 * np.pi * self.g_freq * self.t))

    def test_analyze_chords(self):
        chords = self.analyzer.analyze_chords(self.test_chord, self.sample_rate)
        self.assertIsNotNone(chords)
        self.assertTrue(len(chords) > 0)
        
    def test_detect_chords(self):
        # Crear un cromagrama de prueba
        test_chroma = np.zeros((12, 10))
        test_chroma[0, :] = 1  # Simular una nota C fuerte
        
        chords = self.analyzer._detect_chords(test_chroma)
        self.assertEqual(chords[0], 'C')
        
    def test_simplify_chord_sequence(self):
        test_sequence = ['C', 'C', 'F', 'F', 'G', 'G', 'C', 'C']
        simplified = self.analyzer._simplify_chord_sequence(test_sequence, window_size=2)
        self.assertEqual(simplified, ['C', 'F', 'G', 'C'])

if __name__ == '__main__':
    unittest.main()