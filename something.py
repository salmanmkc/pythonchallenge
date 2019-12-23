
import re
import urllib.request
def replace(s: str):
    count = 12345
    for i in range(12345, 12745):
        link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(i)
        fp = urllib.request.urlopen(link)
        i += 1
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        print(mystr)
        #print(link)

    







    # news = ""
    # for i in range(len(s)):
    #     if s[i] == 'y':
    #         news = news + 'a'
    #     elif s[i] == 'z':
    #         news = news + 'b'
    #     elif s[i].isalpha():
    #         news = news + chr(ord(s[i]) + 2)
    #     else:
    #         news = news + s[i]
    # print(news)
   
    #Hey Hey
    
    #transtab = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    #print(s.translate("jvon"))  
    #print(ord('%'))
    # f = open("help2.txt", "r")
    # content = f.read()
    # print(''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content)))
    # s1 = ""
    # s2 = ""
    # for i in range(len(content)):
    #     if content[i] in "abcdefhijklmnopqrstuvwxyz":
    #         s1 = s1 + content[i]
    #     else:
    #         s2 = s2 + content[i]
    # print(s1)
    # print(s2)
    # values = {}
    # for i in range(len(content)):
    #     if not content[i] in values:
    #         values[content[i]] = 1
    #     else:
    #         values[content[i]] += 1
    # valuesSorted = sorted(values, key=values.get, reverse=True)
    # print(valuesSorted)
    # for i in range(len(valuesSorted)):
    #     print(valuesSorted[i])

#replace("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
replace("http://www.pythonchallenge.com/pc/def/map.html")
