def sandwiches(*sandwich):
    """Prints summary of a list"""
    print('These are the sandwiches that are being ordered: ')
    for item in sandwich:
        print('-', item)


sth = sandwiches('sddfdf', 'sfdgfsd', 'sddfsfdf')
