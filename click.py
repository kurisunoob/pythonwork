from Myconfig import *
import datetime

def log(fun):
    def wrapper(*args, **kw):
        print(f"{bcolors.OKBLUE}Call Function: {fun.__name__}{bcolors.ENDC}")
        fun(*args, **kw)
        print(f"{bcolors.FAIL}Call Functionend: {fun.__name__}{bcolors.ENDC}")

    return wrapper


@log
def now(x, *, y=1, z=1):
    print(f"{bcolors.OKGREEN}{x * 2 + y + z}{bcolors.ENDC}")

if __name__ == "__main__":
    onwork = datetime.time(10,0,0)
    standard = datetime.time(9,0,0)
    times = datetime.datetime.combine(datetime.datetime.today(),onwork) - datetime.datetime.combine(datetime.datetime.today(),standard)
    print(f'{onwork=}')

