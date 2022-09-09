from django import template

register=template.Library()

def truncate5(value) :
    result =value[:5]
    return result

register.filter('trun',truncate5)

@register.filter(name='t_n')
def trun_n(value,n) :
    result =value[:n]
    return result