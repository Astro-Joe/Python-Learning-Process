def get_formatted_name(firstName, lastName):
    """Return a full name neatly formatted"""
    full_name = firstName + ' ' + lastName
    return full_name.title()


while True:
    print('\nTell me your name:')
    print("(enter 'q' at any time to quit)")
    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')



# def city_country(city, country):
#     """Returns the city and it's country"""
#     output = city.title() + ', ' + country.title()
#     return output


# city_0 = city_country('Lagos', 'nigeria\n')
# city_1 =city_country('new york', 'america\n')
# city_2 = city_country('tokyo', 'japan')

# print(city_0, city_1, city_2)