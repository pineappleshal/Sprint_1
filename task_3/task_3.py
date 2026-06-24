def get_champions():
    world_champions = {
        2002: 'Бразилия',
        2006: 'Италия',
        2010: 'Испания',
        2014: 'Германия',
        2018: 'Франция',
    }
    world_champions[2022] = 'Аргентина'
    return world_champions


def check_country(world_champions, country):
    if country in world_champions.values():
        return f'{country} cтановилась чемпионом мира по футболу в 21 веке!'
    return f'{country} не выигрывала чемпионат мира по футболу в 21 веке.'


if __name__ == '__main__':
    champions = get_champions()
    for year, country_name in champions.items():
        print(f'{year} - {country_name}')

    country = 'Италия'
    print(check_country(champions, country))