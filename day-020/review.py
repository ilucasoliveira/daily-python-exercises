from datetime import datetime

def parse_date(text):
    try:
        result = datetime.strptime(text, "%d/%m/%Y").date()
    except ValueError:
        return None
    return result

def days_between(date1, date2):
    return abs(date1 - date2)

def is_valid_date(text):
    data = parse_date(text)
    return data is not None
