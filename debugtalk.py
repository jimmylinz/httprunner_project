import hashlib
import time
from random import random

from httprunner import __version__
from httprunner.response import ResponseObject


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n

def get_token(phone,password,timestamp):
    s = "".join([phone,password,str(timestamp)])
    token = hashlib.md5(s.encode("utf-8")).hexdigest()
    print(f"token: {token}")
    return token

def sleep(n_secs):
    time.sleep(n_secs)

def get_folders_num(response:ResponseObject):
    print("response===",response.resp_obj.json())
    resp_json = response.resp_obj.json()
    folders = resp_json["data"]["folders"]
    return len(folders)

def get_random_title():
    return f"demo-{random.randint(1,999999999)}"

def get_doc_titles(num):
    return [get_random_title() for _ in range(num)]