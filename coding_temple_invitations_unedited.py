import json
import requests
import statistics

api_link = f'https://ct-mock-tech-assessment.herokuapp.com/'
raw_data = requests.get(api_link).json()
API_KEY = 'data'

# for partner in raw_data['partners']:
#     print(partner)

days_in_month = {
    '01': '31',
    '02': '28',
    '03': '31',
    '04': '30',
    '05': '31',
    '06': '30',
    '07': '31',
    '08': '31',
    '09': '30',
    '10': '31',
    '11': '30',
    '12': '31'
}

class Country:
    def __init__(self, country_name, meeting_date = None, partners = None, attending_count = 0):
        self.country_name = country_name
        self.partners = [] if partners == None else partners
        self.attending_count = attending_count
    
    # def get_partners(self): ### This used to be the name of the function, but it was more efficient to have it in the init
                              ### This defines each partner.
        for partner in raw_data['partners']:
            if partner['country'] == self.country_name:
                ### Made a list of available dates.
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

        ### This function adds up every date that people can go two days in a row for each person.
        ### Then the mode returns the most common starting date.
        workable_dates = []
        for partner in self.partners:
            for date in partner.available_dates:
                if self.date_after(date) in partner.available_dates:
                    workable_dates.append(date)
        self.meeting_date = statistics.mode(workable_dates)

        ### This function counts how many partners can make it to the meeting, and changes their value to True if so.
        for partner in self.partners:
            if self.meeting_date in partner.available_dates and self.date_after(self.meeting_date) in partner.available_dates:
                partner.availability = True
                self.attending_count += 1

    
    ### This function is JUST to determine the date after, even if it's in the next month. The days_in_month towards the top is for this.
    def date_after(self, date1):
        if date1[8:] != days_in_month[date1[5:7]]:
            day = str(int(date1[8:]) + 1)
            if int(day) < 10:
                day = '0' + day
            return date1[0:8] + day
        elif date1[8:] == days_in_month[date1[5:7]]:
            month = str(int(date1[5:7]) + 1)
            if int(month) < 10:
                month = '0' + month
            return date1[0:5] + month + '-01'

    ### Once more, I found this more helpful to be in the init.
    # def find_date(self):
    #     workable_dates = []
    #     for partner in self.partners:
    #         for date in partner.available_dates:
    #             if self.date_after(date) in partner.available_dates:
    #                 workable_dates.append(date)
    #     self.meeting_date =  statistics.mode(workable_dates)

class Partner:
    def __init__(self, first_name, last_name, country, email, available_dates = None, availability = False):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.available_dates = [] if available_dates == None else available_dates
        self.availability = availability

class Program():
    @classmethod
    def run(self):

        ### This makes a set of all of the countries present in the data.
        all_countries = set()
        for partner in raw_data['partners']:
            all_countries.add(partner['country'])

        ### This takes the set of country-name-strings and turns them into variables and defines them as a Country object.
        countries = []
        for country in all_countries:
            ### I got the following from DelftStack. This allows the country strings to be the names of variables to assign classes to.
            ### The .replace(' ', '_') I figured out myself because you can't have spaces in variable names.
            globals()[country.replace(' ', '_')] = Country(country_name=country)
            countries.append(globals()[country.replace(' ', '_')])

        ### This is how I both get the information for the partners, and group them by country.
        ### I cut this out because I just put the get_partners function in the init
        # for country in countries:
        #     country.get_partners()

        ### HOLY COW!!! THIS WORKS?!?!?!?!?! globals() is my new favorite thing!!!
        # print(United_States.partners[0].first_name)
        # print(Canada.attending_count)

        invitations = {}
        for country in countries:
            invitations[country.country_name] = {
                'starting date': country.meeting_date,
                'number of attendees': country.attending_count,
                'attendees': []
            }
            for partner in country.partners:
                if partner.availability == True:
                    a = {
                        'name': partner.first_name + ' ' + partner.last_name,
                        'email': partner.email
                    }
                    invitations[country.country_name]['attendees'].append(a)
        api_post = requests.post(api_link, data={'data':invitations})
        api_post
        ### This isn't working for any of my peers. I'm guessing there's something wrong on the other end.
        print(api_post)
        print("I'm sending the API to a website that cares.")
        radically_bodacious_api_post = requests.post(url = 'https://httpbin.org/post', data = {'data':invitations})
        radically_bodacious_api_post
        print(radically_bodacious_api_post)
        # for key in invitations.keys():
        #     print(key)
        #     print(invitations[key]['starting date'])

Program.run()
### I was having trouble with posting so I got this from an article Alex sent me.
# source_code = Program.run()
# data = {
#     'api_dev_key':API_KEY,
#     'api_option':'paste',
#     'api_paste_code': source_code,
#     'api_paste_format':'python'
# }
# r = requests.post(url = api_link, data=data)
# print(r.text)

