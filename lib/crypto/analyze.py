# -- coding: utf-8 -

from .long_analyze import long_analyze
from .short_analyze import short_analyze
from .vol_analyze import vol_analyze
from .pattern_analyze import pattern_analyze
from .ma_analyze import ma_analyze
from .rule_analyze import rule_analyze
from .hline_analyze import hline_analyze
from .trend_analyze import trend_analyze

"""
df: indicators with signals (long signals or short signals)
"""


def analyze(org_df):
    org_df = vol_analyze(org_df)
    org_df = pattern_analyze(org_df)
    org_df = long_analyze(org_df)
    org_df = short_analyze(org_df)
    org_df = ma_analyze(org_df)
    org_df = hline_analyze(org_df)
    org_df = trend_analyze(org_df)
    org_df = rule_analyze(org_df)

    return org_df
