import logging

def create_logger(level='DEBUG', filename='app.log'):
    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level=logging._nameToLevel[level], filename=filename, format=fmt)
    return logging.getLogger()
