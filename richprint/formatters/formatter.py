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
    startat: int = kwargs.get('startat', 0)
    sort: bool = kwargs.get('sort', None)
    showonly: str = kwargs.get('showonly', None)
    encoding: str = kwargs.get('encoding', None)
    errors: str = kwargs.get('errors', None)
    nullstr: str = kwargs.get('nullstr', None)
    show_indices: bool = kwargs.get('show_indices', True)
    truncate: int = kwargs.get('truncate', 100)
    maxlength: int = kwargs.get('maxlength', 50)
    
    print(f"List/tuple: ")
    print("")
    if sort:
        value = sorted(value, key=str)
    if showonly:
        target_type = TYPE_MAP.get(showonly)
        if target_type is None:
            raise ValueError(f"Unknown type '{showonly}'. Valid options: {list(TYPE_MAP.keys())}")
        value = [item for item in value if isinstance(item, target_type)]
    if maxlength:
        excess = len(value) - maxlength
        value = value[:maxlength]
        #value.append("... ({} more)".format(excess))
        
    if truncate:
        for index, item in enumerate(value):
            if len(str(item)) > truncate and item not in [True, False, None]:
                chars_split = list(str(item))
                value[index] = "".join(chars_split[0: truncate]) + "..."
    if encoding:
        try:
            value = [item.encode(encoding, errors=errors).decode(encoding) if isinstance(item, str) else item for item in value]
        except LookupError:
            raise ValueError(f"Unknown encoding '{encoding}' or error '{errors}'. Please use an existing encoding.")
    if nullstr:
        value = [nullstr if item == None else item for item in value]
    
    if show_indices:
        for index, item in enumerate(value, start=startat):
            print("    item #{}     {}".format(index, item))
    else:
        for index, item in enumerate(value, start=startat):
            print("    {}".format(item))
    
    if excess:
        print("")
        print("... ({} more)".format(excess))

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
    test = ['āaaaaaaaa', 'ęweeeeeeeeeee', 'žaaaaaaa', 'čw', 1, 2456543521321, None]
    format_list(test, maxlength=3)