from datetime import datetime, date


#Create a date creation helper function
def make_date(date_string):
    raw_year, raw_month, raw_day = date_string.split('-')
    year = int(raw_year)
    month = int(raw_month)
    day = int(raw_day)
    return date(year, month, day)


#Create empty list
all_presidents = []

# Open data file and read each record
with open("./presidents.txt") as PRES:
    for rec in PRES:
        _, last_name, first_name, birthday, _, _, _, inauguration_day, *_ = rec.split(
            ":")
        birth_date = make_date(birthday)
        took_office_date = make_date(inauguration_day)
        raw_age_at_inauguration = took_office_date - birth_date
        age_at_inauguration = round(raw_age_at_inauguration.days / 365.25, 1)
        full_name = '{} {}'.format(first_name, last_name)
        all_presidents.append((age_at_inauguration, full_name))

for age, name in sorted(all_presidents):
    print(name, age)
