import logging

def setup_logger(log_file='system.log'):
    """Set up the logger configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_info(message):
    """Log an informational message."""
    logging.info(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)
