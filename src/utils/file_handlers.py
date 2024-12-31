import os
import json
import csv
import logging
from ..config.settings import ALLOWED_AUDIO_EXTENSIONS

logger = logging.getLogger(__name__)

class FileHandler:
    """Manejador de archivos del proyecto"""
    
    @staticmethod
    def is_valid_audio_file(file_path):
        """Verifica si el archivo es un formato de audio válido"""
        ext = os.path.splitext(file_path)[1].lower()
        return ext in ALLOWED_AUDIO_EXTENSIONS
    
    @staticmethod
    def save_analysis_results(results, output_path):
        """Guarda los resultados del análisis"""
        try:
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=4)
            logger.info(f"Resultados guardados en: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error al guardar resultados: {e}")
            return False
    
    @staticmethod
    def export_to_csv(data, output_path):
        """Exporta datos a CSV"""
        try:
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            logger.info(f"Datos exportados a CSV: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error al exportar a CSV: {e}")
            return False
    
    @staticmethod
    def create_project_directory(project_name):
        """Crea un directorio de proyecto"""
        try:
            project_path = os.path.join(os.getcwd(), project_name)
            os.makedirs(project_path, exist_ok=True)
            return project_path
        except Exception as e:
            logger.error(f"Error al crear directorio: {e}")
            return None