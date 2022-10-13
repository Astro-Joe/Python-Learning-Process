def city_country(city, country, population=''):
    if population:
        description  = city + ',' + ' ' + country + '- population ' + str(population)
    else:
        description = city + ',' + ' ' + country
    return description.title()