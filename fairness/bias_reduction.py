import re

def mask_personal_information(text):

    text = re.sub(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        '[EMAIL_MASKED]',
        text
    )

    text = re.sub(
        r'\+?\d[\d\s-]{8,}',
        '[PHONE_MASKED]',
        text
    )

    return text