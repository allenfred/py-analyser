# -- coding: utf-8 -
import talib as lib


def pattern_analyze(df):
    open = df.open.to_numpy()
    high = df.high.to_numpy()
    low = df.low.to_numpy()
    close = df.close.to_numpy()

    """
    +200 bullish pattern with confirmation
    +100 bullish pattern (most cases)
    0 none
    -100 bearish pattern
    -200 bearish pattern with confirmation
    """

    """
    一日K线模式
    """

    # Closing Marubozu 收盘缺影线
    df['CDLCLOSINGMARUBOZU'] = lib.CDLCLOSINGMARUBOZU(open, high, low, close)

    # Doji 十字
    df['CDLDOJI'] = lib.CDLDOJI(open, high, low, close)

    # Doji Star 十字星 预示趋势反转
    df['CDLDOJISTAR'] = lib.CDLDOJISTAR(open, high, low, close)

    # 蜻蜓十字/T形十字 预示趋势反转
    df['CDLDRAGONFLYDOJI'] = lib.CDLDRAGONFLYDOJI(open, high, low, close)

    # 墓碑十字/倒T十字 底部反转
    df['CDLGRAVESTONEDOJI'] = lib.CDLGRAVESTONEDOJI(open, high, low, close)

    # Hammer 锤头
    df['CDLHAMMER'] = lib.CDLHAMMER(open, high, low, close)

    # Hanging Man 上吊线
    df['CDLHANGINGMAN'] = lib.CDLHANGINGMAN(open, high, low, close)

    # Inverted Hammer 倒锤头
    df['CDLINVERTEDHAMMER'] = lib.CDLINVERTEDHAMMER(open, high, low, close)

    # Long Legged Doji 长脚十字
    df['CDLLONGLEGGEDDOJI'] = lib.CDLLONGLEGGEDDOJI(open, high, low, close)

    # Long Line Candle 长蜡烛
    df['CDLLONGLINE'] = lib.CDLLONGLINE(open, high, low, close)

    # Marubozu 光头光脚/缺影线
    df['CDLMARUBOZU'] = lib.CDLMARUBOZU(open, high, low, close)

    # Rickshaw Man 黄包车夫
    df['CDLRICKSHAWMAN'] = lib.CDLRICKSHAWMAN(open, high, low, close)

    # Shooting Star 射击之星
    df['CDLSHOOTINGSTAR'] = lib.CDLSHOOTINGSTAR(open, high, low, close)

    # Short Line Candle 短蜡烛
    df['CDLSHORTLINE'] = lib.CDLSHORTLINE(open, high, low, close)

    # Takuri (Dragonfly Doji with very long lower shadow) 探水竿
    df['CDLTAKURI'] = lib.CDLTAKURI(open, high, low, close)

    """
    二日K线模式
    """

    # Counterattack 反击线
    df['CDLCOUNTERATTACK'] = lib.CDLCOUNTERATTACK(open, high, low, close)

    # Dark Cloud Cover 乌云压顶
    df['CDLDARKCLOUDCOVER'] = lib.CDLDARKCLOUDCOVER(open, high, low, close)

    # Up/Down-gap side-by-side white lines 向上/下跳空并列阳线
    df['CDLGAPSIDESIDEWHITE'] = lib.CDLGAPSIDESIDEWHITE(open, high, low, close)

    # 孕线
    df['CDLHARAMI'] = lib.CDLHARAMI(open, high, low, close)

    # 十字孕线
    df['CDLHARAMICROSS'] = lib.CDLHARAMICROSS(open, high, low, close)

    # 家鸽
    df['CDLHOMINGPIGEON'] = lib.CDLHOMINGPIGEON(open, high, low, close)

    # In-Neck Pattern 颈内线
    df['CDLINNECK'] = lib.CDLINNECK(open, high, low, close)

    # Kicking 反冲形态
    df['CDLKICKING'] = lib.CDLKICKING(open, high, low, close)

    # Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态
    df['CDLKICKINGBYLENGTH'] = lib.CDLKICKINGBYLENGTH(open, high, low, close)

    # Matching Low 相同低价
    df['CDLMATCHINGLOW'] = lib.CDLMATCHINGLOW(open, high, low, close)

    # On-Neck Pattern 颈上线
    df['CDLONNECK'] = lib.CDLONNECK(open, high, low, close)

    # Separating Lines 分离线
    df['CDLSEPARATINGLINES'] = lib.CDLSEPARATINGLINES(open, high, low, close)

    # Thrusting Pattern 插入
    df['CDLTHRUSTING'] = lib.CDLTHRUSTING(open, high, low, close)

    # Belt-hold 捉腰带线
    df['CDLBELTHOLD'] = lib.CDLBELTHOLD(open, high, low, close)

    # Engulfing Pattern 吞噬模式
    df['CDLENGULFING'] = lib.CDLENGULFING(open, high, low, close)

    # Piercing Pattern 刺透形态
    df['CDLPIERCING'] = lib.CDLPIERCING(open, high, low, close)

    """
    三日K线模式
    """

    # 两只乌鸦
    df['CDL2CROWS'] = lib.CDL2CROWS(open, high, low, close)

    # 三只乌鸦
    df['CDL3BLACKCROWS'] = lib.CDL3BLACKCROWS(open, high, low, close)

    # 三内部上涨和下跌
    df['CDL3INSIDE'] = lib.CDL3INSIDE(open, high, low, close)

    # 三外部上涨和下跌
    df['CDL3OUTSIDE'] = lib.CDL3OUTSIDE(open, high, low, close)

    # 南方三星  底部反转
    df['CDL3STARSINSOUTH'] = lib.CDL3STARSINSOUTH(open, high, low, close)

    # Abandoned Baby 弃婴
    df['CDLABANDONEDBABY'] = lib.CDLABANDONEDBABY(open, high, low, close)

    # 奇特三川
    df['CDLUNIQUE3RIVER'] = lib.CDLUNIQUE3RIVER(open, high, low, close)

    # 早晨之星  底部反转
    df['CDLMORNINGSTAR'] = lib.CDLMORNINGSTAR(open, high, low, close)

    # 早晨十字星  底部反转
    df['CDLMORNINGDOJISTAR'] = lib.CDLMORNINGDOJISTAR(open, high, low, close)

    # 黄昏之星
    df['CDLEVENINGSTAR'] = lib.CDLEVENINGSTAR(open, high, low, close)

    # 黄昏十字星
    df['CDLEVENINGDOJISTAR'] = lib.CDLEVENINGDOJISTAR(open, high, low, close)

    # Three Advancing White Soldiers 三个白兵
    df['CDL3WHITESOLDIERS'] = lib.CDL3WHITESOLDIERS(open, high, low, close)

    # Advance Block 大敌当前
    df['CDLADVANCEBLOCK'] = lib.CDLADVANCEBLOCK(open, high, low, close)

    # High-Wave Candle 风高浪大线
    df['CDLHIGHWAVE'] = lib.CDLHIGHWAVE(open, high, low, close)

    # Hikkake Pattern 陷阱
    df['CDLHIKKAKE'] = lib.CDLHIKKAKE(open, high, low, close)

    # Modified Hikkake Pattern 修正陷阱
    df['CDLHIKKAKEMOD'] = lib.CDLHIKKAKEMOD(open, high, low, close)

    # Identical Three Crows 三胞胎乌鸦
    df['CDLIDENTICAL3CROWS'] = lib.CDLIDENTICAL3CROWS(open, high, low, close)

    # Spinning Top 纺锤
    df['CDLSPINNINGTOP'] = lib.CDLSPINNINGTOP(open, high, low, close)

    # Stalled Pattern 停顿形态
    df['CDLSTALLEDPATTERN'] = lib.CDLSTALLEDPATTERN(open, high, low, close)

    # Stick Sandwich 条形三明治
    df['CDLSTICKSANDWICH'] = lib.CDLSTICKSANDWICH(open, high, low, close)

    # Tasuki Gap 跳空并列阴阳线
    df['CDLTASUKIGAP'] = lib.CDLTASUKIGAP(open, high, low, close)

    # Tristar Pattern 三星
    df['CDLTRISTAR'] = lib.CDLTRISTAR(open, high, low, close)

    # Upside Gap Two Crows 向上跳空的两只乌鸦
    df['CDLUPSIDEGAP2CROWS'] = lib.CDLUPSIDEGAP2CROWS(open, high, low, close)

    """
    四日K线模式
    """

    # Three-Line Strike 三线打击
    df['CDL3LINESTRIKE'] = lib.CDL3LINESTRIKE(open, high, low, close)

    # 藏婴吞没  底部反转
    df['CDLCONCEALBABYSWALL'] = lib.CDLCONCEALBABYSWALL(open, high, low, close)

    """
    五日K线模式
    """

    # Breakaway 脱离  预示价格上涨
    df['CDLBREAKAWAY'] = lib.CDLBREAKAWAY(open, high, low, close)

    # Ladder Bottom 梯底 底部反转
    df['CDLLADDERBOTTOM'] = lib.CDLLADDERBOTTOM(open, high, low, close)

    # Mat Hold 铺垫
    df['CDLMATHOLD'] = lib.CDLMATHOLD(open, high, low, close)

    # Rising/Falling Three Methods 上升/下降三法
    df['CDLRISEFALL3METHODS'] = lib.CDLRISEFALL3METHODS(open, high, low, close)

    # Upside/Downside Gap Three Methods 上升/下降跳空三法
    df['CDLXSIDEGAP3METHODS'] = lib.CDLXSIDEGAP3METHODS(open, high, low, close)

    return df
