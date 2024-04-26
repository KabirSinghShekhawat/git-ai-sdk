import random
import string
import time


def generate_random_filename():
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = f"{current_time}_{random_string}"
    return filename
