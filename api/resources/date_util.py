from datetime import date, timedelta

# get an array of all days between two dates
def get_all_dates_between(start, end):
    
    # number of days between the two dates
    nb_days = (end-start).days
    
    days = []
    
    for i in range(0, nb_days+1):
        days.append(start + timedelta(days=i))
    
    return days