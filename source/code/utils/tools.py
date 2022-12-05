# Other often used functions
import random
import threading
import time
import os
import difflib
import datetime

from .ENV_VARS import PATH
from .file import DataFile


def random_id(type='N'):
    """
    Generate id with type and 10 random digits:
    [type]XXXXXXXXXX (type = 'N'/'P')
    """

    sequence = [str(random.randint(0, 9)) for _ in range(10)]
    return type+''.join(sequence)


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def run_periodically(function, period=5.0):
    """
    Use threading and time.sleep() to run function
    with delay while not affecting the runtime of an app.
    """

    background_timer = threading.Timer(float(period), function)
    background_timer.start()


def callback(function, delay):
    """Run function forever with delays between each run."""

    while True:
        function()
        time.sleep(delay)


def str_price(price: float, amount=1):
    """Return total price string - with 2 decimal places."""

    return "%.2f" % (price*amount)


def find_image(image_name: str):
    """Return absolute path of root/assets/images/[image_name]."""

    return os.path.join(PATH, "assets", "images", image_name)


def find_icon(icon_name: str):
    """Return absolute path of root/assets/icons/[icon_name]."""

    return os.path.join(PATH, "assets", "icons", icon_name)


def validate_int(input_field, invalid_cmd=None):
    """
    Return input text if it is integer 
    else run invalid_cmd() function.
    """

    if input_field.text().isdigit():
        return input_field.text()
    elif invalid_cmd != None:
        invalid_cmd()


def validate_price(input_field, invalid_cmd=None):
    """
    Return input text if it is valid price 
    format else run invalid_cmd() function.
    """

    try:
        price = float(input_field.text())
    except:
        if invalid_cmd != None:
            invalid_cmd()
    else:
        return "%.2f" % price


def search_items(query='', data={}):
    """
    Search for items in TOVAR.txt matching with search
    term (query) and return it joined with data in dict format.
    """

    goods = DataFile('tovar').data
    result = {}

    for key, val in goods.items():
        for q in query.split():
            code, ratio = get_match(q, key, val)

            if ratio > 0.2+code:
                result[key] = val
                data_list = data.get(key)

                if data_list != None:
                    result[key] += data_list

    return result


def get_match(query, key, val):
    code = len(query)/6 if query.isdigit() else 0.2
    ratio = difflib.SequenceMatcher(
        None, query, key if query.isdigit() else val[0]).ratio()

    return code, ratio


def camelify(input_string: str):
    """
    Make the input string camelCased so that 
    it is valid PyQt5 object name.
    """

    camel = input_string.title().replace(" ", "")
    return ''.join([camel[0].lower(), camel[1:]])
