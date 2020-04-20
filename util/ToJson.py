import re


def qrCodeToJson(strs):
    '''
    为了针对不同的返回内容，做了不同的处理,该方法是因为银联接口返回的字段中包括signature字段也包含=，会导致使用=分割错误.
    :param strs:
    :return:
    '''
    strs = re.sub('[{}""]|==', '', strs)
    strs_dict = dict(tmp.split('=') for tmp in strs.split(', '))
    return strs_dict
