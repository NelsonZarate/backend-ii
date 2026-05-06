"""Session 7 exercise: logging at various levels and rotating example."""
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_basic_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def setup_rotating_logger(logfile='session7.log'):
    logger = logging.getLogger('session7')
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(logfile, when='midnight', backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    setup_basic_logger()
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    l = setup_rotating_logger()
    l.info('Rotating logger test')
