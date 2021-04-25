import pandas as pd
import datetime

start_date = datetime.date(year=2021, month=4, day=17)
end_date = datetime.date(year=2021, month=4,  day=18)

current_date = start_date
while current_date <= end_date:
    print(current_date)
    current_date += datetime.timedelta(days=1)
