def log_error(message):
    file = open('error.log', 'a')
    file.write(message)
    file.close()