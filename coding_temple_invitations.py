import pip._vendor.requests

api_link = f'https://ct-mock-tech-assessment.herokuapp.com/'
data = pip._vendor.requests.get(api_link).json()

# for partner in data['partners']:
#     print(partner)

class Country:
    def __init__(self, country_name, partners = None):
        self.country_name = country_name
        self.partners = [] if partners == None else partners
    
    # def get_partners(self): ### This used to be the name of the function, but it was more efficient to have it in the init
                              ### This defines each partner.
        for partner in data['partners']:
            if partner['country'] == self.country_name:
                a_d = []
                for date in partner['availableDates']:
                    a_d.append(date)
                p = Partner(
                    first_name = partner['firstName'],
                    last_name = partner['lastName'],
                    country = self.country_name,
                    email = partner['email'],
                    available_dates= a_d
                )
                self.partners.append(p)

class Partner:
    def __init__(self, first_name, last_name, country, email, available_dates = None):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.available_dates = [] if available_dates == None else available_dates

# class Program:
#     @classmethod
#     def get_partner(self):

### This makes a set of all of the countries present in the data.
all_countries = set()
for partner in data['partners']:
    all_countries.add(partner['country'])

### This takes the set of country-name-strings and turns them into variables and defines them as a Country object.
countries = []
for country in all_countries:
    ### I got the following from DelftStack. This allows the country strings to be variables to assign classes to.
    globals()[country.replace(' ', '_')] = Country(country_name=country)
    countries.append(globals()[country.replace(' ', '_')])

### This is how I both get the information for the partners, and group them by country.
### I cut this out because I just put the get_partners function in the init
# for country in countries:
#     country.get_partners()

### HOLY COW!!! THIS WORKS?!?!?!?!?! globals() is my new favorite thing!!!
print(United_States.partners[0].first_name)
