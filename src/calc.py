

def add(a: (str, int, float), b: (str, int, float)) -> (int, float):
    try:
        return a+b
    except TypeError:
        return float(a) + float(b)


def sub(a: (str, int, float), b: (str, int, float)) -> (int, float):
    try:
        return a-b
    except TypeError:
        return float(a) - float(b)
