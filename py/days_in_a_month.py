
from datetime import date, datetime, timedelta
import locale
# import requests  # pip install requests
import os
import sys

# args[0] = "200101"

USE_HOLIDAYS = False


def set_locale():
    if os.name == 'nt':
        locale.setlocale(locale.LC_ALL, '')
    else:
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    # print(locale.getlocale(locale.LC_TIME))


def main(args):

    today = date.today()

    yyyymmdd = ""
    if len(args) == 0:
        dt_start = date(today.year, today.month, 1)
        yyyymmdd = dt_start.strftime("%Y%m%d")
    else:
        yyyymmdd = args[0] + "01"
        dt_start = datetime.strptime(yyyymmdd, "%Y%m%d")

    # print("{}年{}月".format(dt_start.year, dt_start.month))

    set_locale()
    
    holidays, date_format = get_holidays(dt_start.year)

    for i in range(31):
        dt = dt_start + timedelta(days=i)

        if dt.month > dt_start.month:
            break

        w = dt.strftime('%a')
        dt_str = dt.strftime(date_format)
        if dt_str in holidays:
            w = '祝'

        print("{}/{}({})".format(dt.month, dt.day, w))


def get_holidays(year) -> (dict, str) :
    url = f'https://holidays-jp.github.io/api/v1/{year}/date.json'
    date_format = '%Y-%m-%d'

    if not USE_HOLIDAYS:
        return {}, date_format

    import requests
    response = requests.get(url.format(year))
    return response.json(), date_format

if __name__ == '__main__':
    main(sys.argv[1:])
    # input("Press any key to exit.")
