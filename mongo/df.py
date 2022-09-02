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
    else:
        return InstrumentInfo.find(
            {},
        ).sort("volume_24h", -1)


def get_tickers():
    return InstrumentInfo.aggregate([
        {"$sort": {"exchange": 1}},
        {
            "$group": {
                "_id": "$base_currency",
                "base_currency": {"$first": "$base_currency"},
                "quote_currency": {"$first": "$quote_currency"},
                "exchange": {"$first": "$exchange"},
                "volume_24h": {"$first": "$volume_24h"},
                "instrument_id": {"$first": "$instrument_id"},
            }
        }, {"$sort": {"volume_24h": -1}},
        {
            "$project": {
                "instrument_id": "$instrument_id",
                "base_currency": "$base_currency",
                "quote_currency": "$quote_currency",
                "exchange": "$exchange",
                "volume_24h": "$volume_24h"
            }
        }
    ])
