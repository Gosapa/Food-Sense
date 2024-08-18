from django.template import Template, Context
from django.template.defaultfilters import safe
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

def md_to_html(payload):
    template = Template("{{ payload | markdown | safe}}")
    context = Context({'payload': payload})
    return template.render(context)