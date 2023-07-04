def is_macd_zero_gold_cross(index, df):
    """
    MACD 零轴金叉

    :param index:
    :param df:
    :return:
    """
    macd = df['macd'].to_numpy()
    diff = df['diff'].to_numpy()
    dea = df['dea'].to_numpy()
    
    return 1


def is_macd_gold_cross(index, df):
    """
    MACD 金叉

    :param index:
    :param df:
    :return:
    """

    return 1
