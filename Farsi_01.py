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
    

print(fprint(), '\n')

# print(F'\n')

print(fprint('سلام من یک فانکشن هستم'))
# Example usage:
farsi_text = "این یک متن فارسی است"
english_text = "This is an English text"
mixed_text = "این یک متن فارسی است. This is an English text."

print(fprint(farsi_text))    # این یک متن فارسی است
print(fprint(english_text))  # This is an English text
print(fprint(mixed_text))    # این یک متن فارسی است. This is an English text.