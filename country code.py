print("south asian country code")
country_code={'bangladesh': '880', 'india': '91', 'pakistan': '92', 'nepal': '977', 'bhutan': '975', 'srilanka': '94', 'maldives': '960', 'afghanistan': '93'}

def get_country_code(country):
    return country_code.get(country, 'Country not found')

country_name = input('Enter country name: ').lower()

print(f"The country code for {country_name} is {get_country_code(country_name)}")

