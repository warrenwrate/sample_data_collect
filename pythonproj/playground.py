import re
from datetime import datetime

a = 5
b = 'blah'

if type(a) is not int:
    print('hello')
else:
    print('what')

# if type(b) is str:
#     print('is string')
# else:
#     print('is not string')

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
datetime_object = datetime.strptime('2014-05-13 01:25:07', '%Y-%m-%d %H:%M:%S')
print(datetime_object, type(datetime_object))



email = 'warren123@test.sljgslkgj'

if re.match(r'[a-z|0-9|\.]+@[a-z|0-9]+(.com|.net|.org)',email):
    print('found match')
else:
    print('no match found')

#phone 
# string = '(334)-313-3322'

# if re.match(r'\d{3}-\d{3}-\d{4}$',string) or re.match(r'\(\d{3}\)-\d{3}-\d{4}$',string):
#     print('found match')
# else:
#     print('no match found')