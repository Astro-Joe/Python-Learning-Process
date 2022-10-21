def make_album(artist_name, album, no_track = ''):
    """A dic containing artist album"""
    content = {'artist': artist_name.upper(), 'album': album.title()}
    return content  

# content = {}
while True:
    name = input("\nEnter an artist name: \n(Enter 'q' anytime you wish to quit) ")
    if name == 'q':
        break

    title = input("Enter the album name: \n(Enter 'q' anytime you wish to quit) ")
    if title == 'q':
        break
    
    # content['artistName'] = name
    # content['album'] = title
    # print('\n')
    # print(content)
    output = make_album(name, title)
    print('\n')
    print(output)
 


# make_album()
