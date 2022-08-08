import datetime
from .database import InstrumentInfo


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        # beijing = datetime.timezone(datetime.timedelta(hours=8))
        utc = datetime.timezone(datetime.timedelta(hours=0))
        return date.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")


def get_instruments(exchange=None):
    if exchange:
        return InstrumentInfo.find(
            {"exchange": exchange},
        ).sort("volume_24h", -1)

    return []
