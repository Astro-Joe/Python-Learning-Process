#The OrderedDict class is from the collections module
# When used it allows python remember the order in which the key-value was inputed.

from collections import OrderedDict

favourite_language = OrderedDict()

favourite_language['jen'] = 'python'
favourite_language['sarah'] = 'c'
favourite_language['edward'] = 'ruby'
favourite_language['phil'] = 'python'

for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is " + 
          language.title() + ".")