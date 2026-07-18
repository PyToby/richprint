import json

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
    groupby: str = kwargs.get('groupby', "type")
    
    print("\n({}):\n".format(type(value)))
    if sort:
        value = sorted(value, key=str)
    if showonly:
        target_type = TYPE_MAP.get(showonly)
        if target_type is None:
            raise ValueError(f"Unknown type '{showonly}'. Valid options: {list(TYPE_MAP.keys())}")
        value = [item for item in value if isinstance(item, target_type)]
    if groupby.lower() == "type":
        value.sort(key=sort_fn)
    if maxlength:
        if maxlength < len(value):
            excess = len(value) - maxlength
            value = value[:maxlength]
    if truncate:
        for index, item in enumerate(value):
            if len(str(item)) > truncate and item not in [True, False, None]:
                chars_split = list(str(item))
                value[index] = "".join(chars_split[0: truncate]) + "..."
    if encoding:
        try:
            value = [item.encode(encoding, errors=errors or "strict").decode(encoding) if isinstance(item, str) else item for item in value]
        except LookupError:
            raise ValueError(f"Unknown encoding '{encoding}' or error '{errors}'. Please use an existing encoding.")
    if nullstr:
        value = [nullstr if item == None else item for item in value]
    
    if show_indices:
        for index, item in enumerate(value, start=startat):
            print("    item #{}     {}".format(index, item))
    else:
        for index, item in enumerate(value, start=startat):
            print(f"    {item}")
    
    try:
        if excess:
            print("")
            print(f"... ({excess} more)")
    except UnboundLocalError:
        pass

    print("")

def sort_fn(e):
    return str(type(e))

'''
DICTIONARY FORMATTING
'''
def format_dict(value: dict, **kwargs):
    maxlength: int = kwargs.get('maxlength', None)
    nullstr: str = kwargs.get('nullstr', None)
    truncate: int = kwargs.get('truncate', None)
    sort: bool = kwargs.get('sort')
    sort_by: str = kwargs.get('sort_by')
    reverse: bool = kwargs.get('reverse', False)
    showonly: list = kwargs.get('showonly')
    exclude: list = kwargs.get('exclude')
    style: str = kwargs.get('style', 'block')

    if showonly:
        value = {k: v for k, v in value.items() if k in showonly}
    if exclude:
        value = {k: v for k, v in value.items() if k not in exclude}
    if sort_by == 'values':
        value = dict(sorted(value.items(), key=lambda item: str(item[1]), reverse=reverse))
    elif sort_by == 'keys' or sort:
        value = dict(sorted(value.items(), key=lambda item: str(item[0]), reverse=reverse))
    if maxlength is not None:
        keys = list(value.keys())[:maxlength]
        value = {k: value[k] for k in keys}
    if truncate:
        length = len(list(value.keys()))
        new_length = length - truncate
        keys = list(value.keys())[:new_length]
        value = {k: value[k] for k in keys}
    if nullstr:
        value = {k: nullstr if value[k] == None else value[k] for k in keys}
    
    print("\n({}):".format(type(value)))
    if style == 'block':
        output = json.dumps(value, indent=4, default=str)
        output = output.replace('null', 'None').replace('true', 'True').replace('false', 'False')
        print(output + '\n')
    elif style == 'inline':
        print(value)
    else:
        output = json.dumps(value, indent=4, default=str)
        output = output.replace('null', 'None').replace('true', 'True').replace('false', 'False')
        print(output + '\n')

'''
PRIMITIVE FORMATTING
'''
def format_primitive(value, **kwargs):
    nullstr: str = kwargs.get('nullstr', None)
    encoding: str = kwargs.get('encoding', None)
    errors: str = kwargs.get('errors', None)
    truncate: int = kwargs.get('truncate', None)
    prefix: str = kwargs.get('prefix')
    suffix: str = kwargs.get('suffix')

    if nullstr and value == None:
        value = nullstr
    if encoding:
        try:
            value = value.encode(encoding=encoding, errors=errors or "strict").decode(encoding=encoding) if isinstance(value, str) else value
        except LookupError:
            raise ValueError(f"Unknown encoding '{encoding}' or error '{errors}'. Please use an existing encoding.") 
        except UnicodeEncodeError as e:
            raise ValueError(f"Could not encode value with encoding '{encoding}': {e}")
    if truncate:
        if len(str(value)) > truncate and type(value) != bool and value != None:
            value = value[:truncate] + "..."
    if prefix:
        value = prefix + value
    if suffix:
        value = value + suffix
        

    print('')
    print("({}): {}".format(type(value), value))
    print('')

'''
TESTING
'''
if __name__ == '__main__':
    test = ['āaaaaaaaa', 'ęweeeeeeeeeee', 'žaaaaaaa', 'čw', 1, 2456543521321, None]
    format_list(test, groupby="type")

    text = "Welcome to the new dark ages, I hope you're living right."
    #format_primitive(text, prefix="Yum! ", suffix=" YUM!")
    test = {
        'b': 5,
        'd': 10,
        'c': None,
        'a': 15,
        'e': 58,
        'g': 45,
        'f': 14,
    }
    format_dict(test)