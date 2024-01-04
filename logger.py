import datetime


def log(func):
    def wrapper(*args, **qwargs):
        try:
            func(*args, **qwargs)
            now = datetime.datetime.now()
            entry = 'Command ' + func.__name__ + ' executed at: ' + str(now) + ' with args: ' + str(func.__code__.co_varnames)
        except Exception as error:
            entry = 'Command ' + func.__name__ + ' failed to run at: ' + str(now) + ' with args: ' + str(func.__code__.co_varnames) + '\n---> error: '+ str(error)
        with open(logFileName,'w') as logfile:
            logfile.write(entry)
        print(entry)
    return wrapper

'''
How to use:
1) put the decorator @log or @logger.log before the function definition
Example:

@log
def test(*args, **qwargs):
    #some code here...
    return *args, **qwargs

'''
