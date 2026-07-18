from richprinted.formatters.formatter import format_list, format_dict, format_primitive


class _RichPrinted:
    '''
    Class that handles execution and detection of values and formatted values.\n
    
    Possible kwargs for primitive formatting: nullstr, encoding, errors, truncate, prefix, suffix \n
    Possible kwargs for list formatting: sorting, encoding, showonly, switch_rows, startat (0 or 1 indexing), encoding errors, nullstr, truncate, maxlength, show_indices, groupby \n
    Possible kwargs for dictionary formatting: maxlength, nullstr, truncate, sort, sort_by, reverse, showonly, exclude, style (either inline or block)\n
    '''
    def __call__(self, value, **kwargs):
        '''Is called when user types in simply rprint(value)
        
        :return: Prints the formatted output into the console.
        '''
        formatter = self._detect_formatter(value)
        formatter(value, **kwargs)
    
    def __repr__(self):
        return f"rprint(value, kwargs)"
 
    def _detect_formatter(self, value):
        '''
        Function to detect of what type the value is.

        :param value:
        :return: The appropriate function
        '''
        if isinstance(value, (list, tuple)): return format_list
        if isinstance(value, dict): return format_dict
        if isinstance(value, (str, int, float, bool, type(None))): return format_primitive

    def configure(self, **kwargs): pass



rprint = _RichPrinted()