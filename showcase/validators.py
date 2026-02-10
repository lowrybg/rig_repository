from django.core.exceptions import ValidationError

def validate_no_console(value):
    if 'console' in value.lower():
        raise ValidationError("This is a PC Rig Repository! No consoles allowed.")
