import unittest
import numpy as np
from src.core.audio_analyzer import AudioAnalyzer

class TestAudioAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = AudioAnalyzer()
        # Crear datos de prueba
        self.sample_rate = 44100
        self.duration = 3
        self.t = np.linspace(0, self.duration, self.sample_rate * self.duration)
        self.test_signal = np.sin(2 * np.pi * 440 * self.t)  # Tono A 440Hz

    def test_load_audio(self):
        # Test con datos inválidos
        result = self.analyzer.load_audio("nonexistent_file.wav")
        self.assertFalse(result)
        
        # TODO: Agregar test con archivo válido
        
    def test_detect_tempo(self):
        self.analyzer.y = self.test_signal
        self.analyzer.sr = self.sample_rate
        tempo = self.analyzer.detect_tempo()
        self.assertIsNotNone(tempo)
        self.assertTrue(0 < tempo < 300)  # Rango razonable de BPM

    def test_get_waveform(self):
        self.analyzer.y = self.test_signal
        waveform = self.analyzer.get_waveform()
        self.assertIsNotNone(waveform)
        self.assertEqual(len(waveform), len(self.test_signal))

    def test_get_spectrum(self):
        self.analyzer.y = self.test_signal
        spectrum = self.analyzer.get_spectrum()
        self.assertIsNotNone(spectrum)
        self.assertTrue(isinstance(spectrum, np.ndarray))

if __name__ == '__main__':
    unittest.main()