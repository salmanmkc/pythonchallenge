
import re
import urllib.request
import pickle

def replace(s: str):
    i = 36379
    count = 0

    link = "http://www.pythonchallenge.com/pc/def/banner.p"
    fp = urllib.request.urlopen(link)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    stuff = mystr.splitlines()    
    print(len(pickle.loads(mybytes)))
    print(23*95)

#replace("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
replace("http://www.pythonchallenge.com/pc/def/map.html")
