import arabic_reshaper
from bidi.algorithm import get_display


def ConvertToFarsi(text='سلام دوست من کمیلیان هستم'):
    persian_text = text
    reshaped_text = arabic_reshaper.reshape(persian_text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)


ConvertToFarsi()

print(F'\n')

ConvertToFarsi('این یک تست است')
