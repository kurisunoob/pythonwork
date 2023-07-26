from Myconfig import *

def log(fun):
    def wrapper(*args, **kw):
        print(f"{bcolors.OKBLUE}Call Function: {fun.__name__}{bcolors.ENDC}")
        fun(*args, **kw)
        print(f"{bcolors.FAIL}Call Functionend: {fun.__name__}{bcolors.ENDC}")

    return wrapper


@log
def now(x, *, y=1, z=1):
    print(f"{bcolors.OKGREEN}{x * 2 + y + z}{bcolors.ENDC}")

now(2)
