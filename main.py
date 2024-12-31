from src.gui.main_window import HarmonyWhispererGUI
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Iniciando HarmonyWhisperer...")
        app = HarmonyWhispererGUI()
        app.run()
    except Exception as e:
        logger.error(f"Error en la aplicación: {e}")
        raise

if __name__ == "__main__":
    main()