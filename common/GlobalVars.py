
def _init():
    global _correlationDict
    _correlationDict = {}

def set_value(key, value):
    _correlationDict[key] = value

def get_value(key):
    try:
        return _correlationDict[key]
    except KeyError:
        return None

def get_values():
    '''
    :return: 返回整个字典值
    '''
    return _correlationDict