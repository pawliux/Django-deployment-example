from django import template


## using Library
register = template.Library()

def cut(value, arg):
    """
    This cuts out all values of "arg" from string!
    """

    return value.replace(arg, '')

register.filter('my_cut', cut)


## using decorators
@register.filter(name='my_cut2')
def cut2(value, arg):
    """
    This cuts out all values of "arg" from string!
    """

    return value.replace(arg, '')
