import Data as globaldata
from persondata import *
def SkipDate(JoinDateTime:datetime):
    for date in globaldata.ContainInfoDate:
        if date == JoinDateTime:
            return False
    for date in globaldata.SkipInfoDate:
        if date == globaldata.SkipInfoDate:
            return True

    if JoinDateTime.weekday() == 6 or JoinDateTime.weekday() == 7:
        return True
    return False
