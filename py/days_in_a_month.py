
from datetime import date, datetime, timedelta
import locale
import requests  # pip install requests
import sys

# args[0] = "200101"


def main(args):

    today = date.today()

    yyyymmdd = ""
    if len(args) == 0:
        dt_start = date(today.year, today.month, 1)
        yyyymmdd = dt_start.strftime("%Y%m%d")
    else:
        yyyymmdd = args[0] + "01"
        dt_start = datetime.strptime(yyyymmdd, "%Y%m%d")

    print("{}年{}月".format(dt_start.year, dt_start.month))

    locale.setlocale(locale.LC_ALL, '')
    # print(locale.getlocale(locale.LC_TIME))

    holidays = get_holidays(dt_start.year)
    date_format = '%Y-%m-%d'

    for i in range(31):
        dt = dt_start + timedelta(days=i)

        if dt.month > dt_start.month:
            break

        w = dt.strftime('%a')
        dt_str = dt.strftime(date_format)
        if dt_str in holidays:
            w = '祝'

        print("{}/{}({})".format(dt.month, dt.day, w))


def get_holidays(year) -> dict:
    url = f'https://holidays-jp.github.io/api/v1/{year}/date.json'
    response = requests.get(url.format(year))
    return response.json()

if __name__ == '__main__':
    main(sys.argv[1:])
    # input("Press any key to exit.")
