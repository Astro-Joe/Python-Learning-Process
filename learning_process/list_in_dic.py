fav_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }
for name, languages in fav_language.items():
    print('\n' + name.title() + "'s favourite languages are: ")
    for language in languages:
        if len(language) == 1:
            print('\nThis means you\'re an expert in ' + language.title())
        else:
            print('\t' + language.title())