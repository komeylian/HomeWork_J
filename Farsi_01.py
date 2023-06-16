#1402-03-26

import arabic_reshaper
from bidi.algorithm import get_display


def fprint(text='سلام من کمیلیان هستم'):
    if not isinstance(text, str):
        return text

    try:
        reshaped_text = arabic_reshaper.reshape(text)
        display_text = get_display(reshaped_text)
        return display_text
    except arabic_reshaper.ArabicReshaperError:
        return text
    

# Example usage:
farsi_text = "من یک فانکشن هستم"
english_text = "This is an English text"
mixed_text = "من یک فانکشن هستم. This is an English text."

print(fprint(farsi_text))    # من یک فانکشن هستم
print(fprint(english_text))  # This is an English text
print(fprint(mixed_text))    # من یک فانکشن هستم. This is an English text.