"""
Configuraciones globales de la aplicación
"""

# Información de la aplicación
APP_NAME = "HarmonyWhisperer"
VERSION = "1.0.0"
AUTHOR = "Tu Nombre"

# Configuraciones de audio
SAMPLE_RATE = 22050
WINDOW_SIZE = 2048
HOP_LENGTH = 512
CHUNK_SIZE = 1024

# Configuraciones de UI
WINDOW_SIZE = "800x600"
THEME = "default"
BACKGROUND_COLOR = "#f0f0f0"
TEXT_COLOR = "#333333"

# Directorios
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
SAMPLES_DIR = os.path.join(RESOURCES_DIR, 'samples')
ICONS_DIR = os.path.join(RESOURCES_DIR, 'icons')

# Extensiones de archivo permitidas
ALLOWED_AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.flac']