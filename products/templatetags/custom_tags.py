from django import template

register = template.Library()


@register.filter
def hash(h, key):
    try:
        ans = h[key]
        return ans
    except:
        return 0

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def div(value, div):
    if div == 0:
        return 'Na'
    return "{:.1f}".format(value / div)

@register.filter
def subtract(value, arg):
    return value - arg