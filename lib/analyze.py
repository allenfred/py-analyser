# -- coding: utf-8 -

from .long_analyze import long_analyze
from .short_analyze import short_analyze
from .pattern_analyze import pattern_analyze
from .ma_analyze import ma_analyze

"""
df: indicators with signals (long signals or short signals)
"""


def analyze(org_df):

    org_df = long_analyze(org_df)
    org_df = short_analyze(org_df)
    org_df = pattern_analyze(org_df)
    org_df = ma_analyze(org_df)

    return org_df

