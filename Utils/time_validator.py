from PIL.ImImagePlugin import number
from PySide6.QtGui import QValidator
from re import match


class TimeValidator(QValidator):
    def validate(self, input_str, pos):
        # Validate the input based on your criteria
        if len(input_str) <= 5:
            if self.chceck_validity(input_str):
                return QValidator.State.Acceptable, input_str, pos
        return QValidator.State.Invalid, input_str, pos

    def chceck_validity(self, input_str: str):
        patterns = [r"\d{3}$", r"\d{2}$", r"\d$", r"\d{4}$", r"\d{2}\:\d{2}$", r"\d{2}:\d$", r"\d{2}\:$"]
        number_1 = 0
        number_2 = 0
        try:
            number_1 =int(input_str[0:2])
            number_2 = int(input_str[2:].replace(':', ''))
        except:
            pass

        # Check if the input matches the pattern
        for pattern in patterns:
            if match(pattern, input_str) and number_1 <= 24 and number_2<=60 or input_str == "":
                return True
        return False