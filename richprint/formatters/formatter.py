TYPE_MAP = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
}

ALLOWED_ENCODING_ERRORS = ['backslashreplace', 'ignore', 'namereplace', 'strict', 'replace', 'xmlcharrefreplace']

'''
LIST/TUPLE FORMATTING
'''
def format_list(value: list, **kwargs):
    list_kwargs = []

    startat = kwargs.get('startat', 0)
    sort = kwargs.get('sort', None)
    showonly = kwargs.get('showonly', None)
    encoding = kwargs.get('encoding', None)
    
    print(f"List/tuple: ")
    if sort:
        value = sorted(value, key=str)
    if showonly:
        target_type = TYPE_MAP.get(showonly)
        if target_type is None:
            raise ValueError(f"Unknown type '{showonly}'. Valid options: {list(TYPE_MAP.keys())}")
        value = [item for item in value if isinstance(item, target_type)]
    if encoding:
        try:
            value = [item.encode(encoding) for item in value]
        except LookupError:
            raise ValueError(f"Unknown encoding '{encoding}'. Please use an existing encoding.")

    for index, item in enumerate(value, start=startat):
        print("    item #{}     {}".format(index, item))    

'''
DICTIONARY FORMATTING
'''
def format_dict(value, **kwargs):
    pass

'''
PRIMITIVE FORMATTING
'''
def format_primitive(value, **kwargs):
    pass

'''
TABLE FORMATTING
'''
def format_table(value, **kwargs):
    pass

'''
TESTING
'''
if __name__ == '__main__':
    test = ['b', 'd', 'a', 'c', 1, 2]
    format_list(test, startat=2, sort=True, showonly='str', encoding='gbk')