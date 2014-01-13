#!/usr/bin/env python
# coding: utf-8

from mega import Mega


mega = Mega({'verbose': True})

m = mega.login('', '')

details = m.get_user()
quota = m.get_quota()
space = m.get_storage_space(mega=True)
files = m.get_files()

print files

# import pprint
# pprint.pprint(locals())

file = m.upload('test.txt')
print m.get_upload_link(file)
