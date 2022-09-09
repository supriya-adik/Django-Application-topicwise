from django import template
register=template.Library()

@register.filter(name='t_n')
def truncate_n(value,n) :
    result=value[0:n]
    return result

