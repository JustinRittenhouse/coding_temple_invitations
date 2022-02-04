import pip._vendor.requests
import statistics

api_link = f'https://ct-mock-tech-assessment.herokuapp.com/'
data = pip._vendor.requests.get(api_link).json()

# # United_States_partners = []
# # for partner in data['partners']:
# #     if partner['country'] == 'United States':
# #         United_States_partners.append(partner)
# # print(United_States_partners)

# print(data['partners'][0])

# globals()[apple]] = 50
# print(apple)
# print(type(apple))

# United States  = 1
# print(United States)

# print('2017-06-23'[8:])


# days_in_month = {
#     '01': '31',
#     '02': '28',
#     '03': '31',
#     '04': '30',
#     '05': '31',
#     '06': '30',
#     '07': '31',
#     '08': '31',
#     '09': '30',
#     '10': '31',
#     '11': '30',
#     '12': '31'
# }

# def date_after(date1):
#     if date1[8:] != days_in_month[date1[5:7]]:
#         day = str(int(date1[8:]) + 1)
#         if int(day) < 10:
#             day = '0' + day
#         return date1[0:8] + day
#     elif date1[8:] == days_in_month[date1[5:7]]:
#         month = str(int(date1[5:7]) + 1)
#         if int(month) < 10:
#             month = '0' + month
#         return date1[0:5] + month + '-01'

# def find_date(x):
#     workable_dates = []
#     for partner in x:
#         for date in partner:
#             if date_after(date) in partner:
#                 workable_dates.append(date)
#     return statistics.mode(workable_dates)

# partner1 = ['2017-06-30', '2017-07-01', '2017-07-02', '2017-07-03']
# partner2 = ['2017-06-29', '2017-06-30', '2017-07-01']
# partner3 = ['2017-05-20', '2017-05-21']

# partners = [partner1, partner2, partner3]

# print(find_date(partners))