import re
import mechanize

br = mechanize.Browser()
br.open("http://www.andhrabharati.com/dictionary/")
def select_form(form):
    return form.attrs.get('id', None) == 'abdict'

br.select_form(predicate=select_form)
print(br.title())

import pdb
pdb.set_trace()
