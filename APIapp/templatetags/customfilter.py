from django import template

register = template.Library()


def myfilter(value, arg):
    return value.replace(arg, 'vikas')


register.filter('MyFilter', myfilter)
