

class CalculatorError(Exception):
    """ Base error  """
    pass


class NonEmpty(CalculatorError):
    """ Check for non empty string """
    pass


def re_runCal(): 
    while True:
        calVal = input('Calcu').strip()
        if calVal is not "":
            raise NonEmpty("Calculator input can't be empty")
        break
            

    