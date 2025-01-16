from django import template

register = template.Library()

@register.filter
def emotion_color(emotion):
    if emotion in ['anger', 'fear', 'sadness']:
        return 'red-500'
    elif emotion in ['happiness', 'joy', 'excitement']:
        return 'green-500'
    elif emotion == 'surprise':
        return 'orange-500'
    else:
        return 'gray-500'


