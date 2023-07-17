import time

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception as e:
        return e
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')
        
class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'
    
class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'
    
def raiseServerError():
    raise ServerError()

print('Exceptions')
print('try/except')
print(causeError())
print(raiseServerError())