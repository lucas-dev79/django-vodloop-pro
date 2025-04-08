import re
from django.core.exceptions import ValidationError

class UppercaseValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError("Must contain at least one uppercase letter.")

    def get_help_text(self):
        return "Must contain at least one uppercase letter."

class SpecialCharacterValidator:
    def validate(self, password, user=None):
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Must contain at least one special character (!@#$%^&* etc.).")

    def get_help_text(self):
        return "Must contain at least one special character (!@#$%^&* etc.)."
