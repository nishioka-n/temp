
# 1日分の UNIX Time データ作成

from datetime import date, datetime, timezone
import locale

# 日付の指定書式
DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S%z"
# 作成する時間
HOURS = 24

# 設定項目 ここから -----------------------------

# 開始日時（UTC）
START_DATETIME = '2021/4/5 22:02:45+0000'  # 書式は、上記の DATETIME_FORMAT

# 何分ごとに作成するか
INTERVAL_MINITES = 5

# 設定項目 ここまで -----------------------------


# 開始日時のUNIX時間を取得
def get_start_unixtime() -> int:
    dt = datetime.strptime(START_DATETIME, DATETIME_FORMAT)
    ts = dt.timestamp()
    return int(ts)


# 指定時間内のインターバルごとのUNIX時間を作成してリストで返す
def get_unixtime_list(start_ts, term, interval) -> list:

    # 作成件数
    item_count = int(term / interval)
    print(f'作成件数:{item_count}')

    items = []
    for i in range(item_count):
        items.append(start_ts + (i * interval))

    return items


def main(args=None):

    # 開始日時のUNIX時間
    start_ts = get_start_unixtime()
    
    # 作成時間の秒数
    term = HOURS * 60 * 60

    # 加算する秒数
    interval = INTERVAL_MINITES * 60

    unixtime_list = get_unixtime_list(start_ts, term, interval)
    for ut in unixtime_list:
        ts = datetime.fromtimestamp(ut, timezone.utc)
        print(ut, ts)


if __name__ == '__main__':
    main()
