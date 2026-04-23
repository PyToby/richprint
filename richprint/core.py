from richprint.formatters.formatter import format_list, format_dict, format_primitive, format_table


class _RichPrint:
    '''
    Class that handles execution and detection of values and formatted values

    possible kwargs: sorting, indentation, encoding, showonly, switch_rows, startat (0 or 1 indexing)
    '''
    def __call__(self, value, **kwargs):
        '''Is called when user types in simply rprint(value)
        
        :return: Prints the formatted output into the console.
        '''
        formatter = self._detect_formatter(value)
        output = formatter(value, **kwargs)
        print(output)
    
    def __repr__(self):
        return f"rprint(value, sort=True/False, startat=int, sort=True, showonly=instance)"
 
    def _detect_formatter(self, value):
        '''
        Function to detect of what type the value is.

        :param value:
        :return: The appropriate function
        '''
        if isinstance(value, (list, tuple)): return format_list
        if isinstance(value, dict): return format_dict
        if isinstance(value, (str, int, bool, None)): return format_primitive
    
    def table(self, value, **kwargs):
        output = format_table(value, **kwargs)
        print(output) 

    def configure(self, **kwargs): pass



rprint = _RichPrint()