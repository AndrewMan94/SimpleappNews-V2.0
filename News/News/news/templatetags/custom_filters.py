from django import template

register = template.Library()

censor_dict = {'man': 'm*n', 'woman': 'w****n'}

@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        result = str(value)
        for key in censor_dict.keys():
            result = result.replace(key, censor_dict[key])
        return result
    else:
        raise ValueError(f'Нельзя отфильтровать тип, отличный от {type(value)}')