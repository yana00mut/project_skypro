from decorators import log

@log(filename="my_log.log")
def divide(a, b):
    return a / b