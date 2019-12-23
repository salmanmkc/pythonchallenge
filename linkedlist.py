import re
import urllib3

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
number = 12345

pool = urllib3.PoolManager()

def get_data(number_recieved):
    req = pool.request("GET",base_url+number_recieved)
    print(req.data)
    return req.data

first_run = pool.request("GET",base_url+number)


def getnumber(data):
    result = re.search("nothing is [0-9]*",data)
    print(result.group())
    number = re.search("[0-9]*$",result.group())
    return number.group()



while True:
    data = get_data()





