import arabic_reshaper
from bidi.algorithm import get_display


def fprint(text='سلام من کمیلیان هستم'):
    persian_text = text
    reshaped_text = arabic_reshaper.reshape(persian_text)
    bidi_text = get_display(reshaped_text)
    # print(bidi_text)
    return bidi_text


print(fprint(), '\n')

# print(F'\n')

print(fprint('سلام من یک فانکشن هستم'))
