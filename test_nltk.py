import html2text
import re
from tinydb import TinyDB, Query


def clean_non_unicode_chars(tstring):
    regex = re.compile('[a-zA-Z\[\.]*')
    #First parameter is the replacement, second parameter is your input string
    tstring = regex.sub('', html2text.html2text(html))
    tstring = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,\%\[\]\_\*\’\&\/\©\\\‘]", "", tstring)
    tstring = re.sub(r"[1234567890]", "", tstring)
    tstring = tstring.split('\n')
    tstring = filter(lambda x: not re.match(r'^\s*$', x), tstring)
    tstring = "\n".join(tstring)
    return tstring

def insert_into_tinydb(record, db_path="db.json"):
    """
    record should be { 'word': word_value }
    """
    db = TinyDB('db.json')
    qr =  Query()
    sl = db.search(qr.word == record.get("word"))
    if len(sl) == 0:
        print(word)
        db.insert(record)


html = open("./samples/1.html").read()
tstring = clean_non_unicode_chars(html)
test  = open("create_text.txt", "w")
test.write(tstring)
test.close()

# open the file

fd = open("create_text.txt", "r")
lines_in_text = fd.readlines()
lines_in_text = [x.strip("\n").strip() for x in lines_in_text if x != ""]
print(lines_in_text)

db = TinyDB('db.json')

for line in lines_in_text:
    for word in line.split(" "):
        insert_into_tinydb({ 'word' : word })
