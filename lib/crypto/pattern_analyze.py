# -- coding: utf-8 -

import talib as lib
import lib.signal.crypto.candle as patterns


def pattern_analyze(df):
    """
    加密货币 K线形态分析
    吞没
    螺旋桨
    锤头线
    射击之星
    射击十字星
    较长影线(1/2)
    光头光脚

    :param df:
    :return:
    """

    open = df.open.to_numpy()
    high = df.high.to_numpy()
    low = df.low.to_numpy()
    close = df.close.to_numpy()

    candle = df[['open', 'high', 'low', 'close', 'pct_chg', 'pct_range', 'trade_date']].to_numpy()

    hammer = []
    t_line = []
    pour_hammer = []
    short_end = []
    swallow_up = []
    attack_short = []
    first_light = []
    sunrise = []
    flat_base = []
    down_screw = []
    long_end = []
    swallow_down = []
    hang_neck = []
    shooting = []
    shooting_doji = []
    up_screw = []
    down_rise = []

    up_cross3ma = []
    up_cross4ma = []
    up_cross5ma = []
    drop_cross3ma = []
    drop_cross4ma = []
    drop_cross5ma = []

    resistance_shadow = []
    support_shadow = []
    down_pour = []
    marubozu = []
    long_line = []

    for index in range(len(candle)):
        # 锤子线
        hammer.insert(index, patterns.hammer(index, candle))
        # T字线
        t_line.insert(index, patterns.t_line(index, candle))
        # 倒锤子线
        pour_hammer.insert(index, patterns.pour_hammer(index, candle))
        # 看涨尽头线
        short_end.insert(index, patterns.short_end(index, candle))
        # 下探上涨
        down_rise.insert(index, patterns.down_rise(index, candle))
        # 看涨吞没
        swallow_up.insert(index, patterns.swallow_up(index, candle))
        # 好友反攻
        attack_short.insert(index, patterns.attack_short(index, candle))
        # 曙光初现
        first_light.insert(index, patterns.first_light(index, candle))
        # 旭日东升
        sunrise.insert(index, patterns.sunrise(index, candle))
        # 平底
        flat_base.insert(index, patterns.flat_base(index, candle))
        # 下跌螺旋桨
        down_screw.insert(index, patterns.down_screw(index, candle))
        # 看跌尽头线
        long_end.insert(index, patterns.long_end(index, candle))
        # 看跌吞没
        swallow_down.insert(index, patterns.swallow_down(index, candle))
        # 吊颈线
        hang_neck.insert(index, patterns.hang_neck(index, candle))
        # 射击之星
        shooting.insert(index, patterns.shooting(index, candle))
        # 射击十字星
        shooting_doji.insert(index, patterns.shooting_doji(index, candle))
        # 看跌螺旋桨
        up_screw.insert(index, patterns.up_screw(index, candle))
        # 一阳穿三线
        up_cross3ma.insert(index, patterns.up_cross3ma(index, candle, df))
        # 一阳穿四线
        up_cross4ma.insert(index, patterns.up_cross4ma(index, candle, df))
        # 一阳穿五线
        up_cross5ma.insert(index, patterns.up_cross5ma(index, candle, df))
        # 一阴穿三线
        drop_cross3ma.insert(index, patterns.drop_cross3ma(index, candle, df))
        # 一阴穿四线
        drop_cross4ma.insert(index, patterns.drop_cross4ma(index, candle, df))
        # 一阴穿五线
        drop_cross5ma.insert(index, patterns.drop_cross5ma(index, candle, df))
        # 阻力线
        resistance_shadow.insert(index, patterns.resistance_shadow(index, candle))
        # 支撑线
        support_shadow.insert(index, patterns.support_shadow(index, candle))
        # 倾盆大雨
        down_pour.insert(index, patterns.down_pour(index, candle))
        # 光头光脚
        marubozu.insert(index, patterns.marubozu(index, candle))
        # 大阳线/大阴线
        long_line.insert(index, patterns.long_line(index, candle))

    df['hammer'] = hammer
    df['t_line'] = t_line
    df['pour_hammer'] = pour_hammer
    df['short_end'] = short_end
    df['swallow_up'] = swallow_up
    df['attack_short'] = attack_short
    df['first_light'] = first_light
    df['sunrise'] = sunrise
    df['flat_base'] = flat_base
    df['down_screw'] = down_screw
    df['long_end'] = long_end
    df['swallow_down'] = swallow_down
    df['hang_neck'] = hang_neck
    df['shooting'] = shooting
    df['shooting_doji'] = shooting_doji
    df['up_screw'] = up_screw
    df['down_rise'] = down_rise

    df['up_cross3ma'] = up_cross3ma
    df['up_cross4ma'] = up_cross4ma
    df['up_cross5ma'] = up_cross5ma
    df['drop_cross3ma'] = drop_cross3ma
    df['drop_cross4ma'] = drop_cross4ma
    df['drop_cross5ma'] = drop_cross5ma

    df['resistance_shadow'] = resistance_shadow
    df['support_shadow'] = support_shadow
    df['down_pour'] = down_pour
    df['marubozu'] = marubozu
    df['long_line'] = long_line

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

    # # Closing Marubozu 收盘缺影线
    # df['CDLCLOSINGMARUBOZU'] = lib.CDLCLOSINGMARUBOZU(open, high, low, close)
    #
    # # Doji 十字
    # df['CDLDOJI'] = lib.CDLDOJI(open, high, low, close)
    #
    # # Doji Star 十字星 预示趋势反转
    # df['CDLDOJISTAR'] = lib.CDLDOJISTAR(open, high, low, close)
    #
    # 蜻蜓十字/T形十字 预示趋势反转
    # df['CDLDRAGONFLYDOJI'] = lib.CDLDRAGONFLYDOJI(open, high, low, close)
    #
    # 墓碑十字/倒T十字 底部反转
    # df['CDLGRAVESTONEDOJI'] = lib.CDLGRAVESTONEDOJI(open, high, low, close)
    #
    # Hammer 锤头
    # df['CDLHAMMER'] = lib.CDLHAMMER(open, high, low, close)
    #
    # # Hanging Man 上吊线
    # df['CDLHANGINGMAN'] = lib.CDLHANGINGMAN(open, high, low, close)
    #
    # # Inverted Hammer 倒锤头
    # df['CDLINVERTEDHAMMER'] = lib.CDLINVERTEDHAMMER(open, high, low, close)
    #
    # # Long Legged Doji 长脚十字
    # df['CDLLONGLEGGEDDOJI'] = lib.CDLLONGLEGGEDDOJI(open, high, low, close)
    #
    # # Long Line Candle 长蜡烛
    # df['CDLLONGLINE'] = lib.CDLLONGLINE(open, high, low, close)
    #
    # # Marubozu 光头光脚/缺影线
    # df['CDLMARUBOZU'] = lib.CDLMARUBOZU(open, high, low, close)
    #
    # # Rickshaw Man 黄包车夫
    # df['CDLRICKSHAWMAN'] = lib.CDLRICKSHAWMAN(open, high, low, close)
    #
    # Shooting Star 射击之星
    # df['CDLSHOOTINGSTAR'] = lib.CDLSHOOTINGSTAR(open, high, low, close)
    #
    # # Short Line Candle 短蜡烛
    # df['CDLSHORTLINE'] = lib.CDLSHORTLINE(open, high, low, close)
    #
    # Takuri (Dragonfly Doji with very long lower shadow) 探水竿
    # df['CDLTAKURI'] = lib.CDLTAKURI(open, high, low, close)
    #
    # """
    # 二日K线模式
    # """
    #
    # # Counterattack 反击线
    # df['CDLCOUNTERATTACK'] = lib.CDLCOUNTERATTACK(open, high, low, close)
    #
    # # Dark Cloud Cover 乌云压顶
    # df['CDLDARKCLOUDCOVER'] = lib.CDLDARKCLOUDCOVER(open, high, low, close)
    #
    # # Up/Down-gap side-by-side white lines 向上/下跳空并列阳线
    # df['CDLGAPSIDESIDEWHITE'] = lib.CDLGAPSIDESIDEWHITE(open, high, low, close)
    #
    # 孕线
    # df['CDLHARAMI'] = lib.CDLHARAMI(open, high, low, close)
    #
    # 十字孕线
    # df['CDLHARAMICROSS'] = lib.CDLHARAMICROSS(open, high, low, close)
    #
    # # 家鸽
    # df['CDLHOMINGPIGEON'] = lib.CDLHOMINGPIGEON(open, high, low, close)
    #
    # # In-Neck Pattern 颈内线
    # df['CDLINNECK'] = lib.CDLINNECK(open, high, low, close)
    #
    # # Kicking 反冲形态
    # df['CDLKICKING'] = lib.CDLKICKING(open, high, low, close)
    #
    # # Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态
    # df['CDLKICKINGBYLENGTH'] = lib.CDLKICKINGBYLENGTH(open, high, low, close)
    #
    # # Matching Low 相同低价
    # df['CDLMATCHINGLOW'] = lib.CDLMATCHINGLOW(open, high, low, close)
    #
    # # On-Neck Pattern 颈上线
    # df['CDLONNECK'] = lib.CDLONNECK(open, high, low, close)
    #
    # # Separating Lines 分离线
    # df['CDLSEPARATINGLINES'] = lib.CDLSEPARATINGLINES(open, high, low, close)
    #
    # # Thrusting Pattern 插入
    # df['CDLTHRUSTING'] = lib.CDLTHRUSTING(open, high, low, close)
    #
    # # Belt-hold 捉腰带线
    # df['CDLBELTHOLD'] = lib.CDLBELTHOLD(open, high, low, close)
    #
    # Engulfing Pattern 吞噬模式
    # df['CDLENGULFING'] = lib.CDLENGULFING(open, high, low, close)
    #
    # Piercing Pattern 刺透形态
    df['CDLPIERCING'] = lib.CDLPIERCING(open, high, low, close)
    #
    # """
    # 三日K线模式
    # """
    #
    # # 两只乌鸦
    # df['CDL2CROWS'] = lib.CDL2CROWS(open, high, low, close)
    #
    # # 三只乌鸦
    # df['CDL3BLACKCROWS'] = lib.CDL3BLACKCROWS(open, high, low, close)
    #
    # # 三内部上涨和下跌
    # df['CDL3INSIDE'] = lib.CDL3INSIDE(open, high, low, close)
    #
    # # 三外部上涨和下跌
    # df['CDL3OUTSIDE'] = lib.CDL3OUTSIDE(open, high, low, close)
    #
    # # 南方三星  底部反转
    # df['CDL3STARSINSOUTH'] = lib.CDL3STARSINSOUTH(open, high, low, close)
    #
    # # Abandoned Baby 弃婴
    # df['CDLABANDONEDBABY'] = lib.CDLABANDONEDBABY(open, high, low, close)
    #
    # # 奇特三川
    # df['CDLUNIQUE3RIVER'] = lib.CDLUNIQUE3RIVER(open, high, low, close)
    #
    # # 早晨之星  底部反转
    # df['CDLMORNINGSTAR'] = lib.CDLMORNINGSTAR(open, high, low, close)
    #
    # # 早晨十字星  底部反转
    # df['CDLMORNINGDOJISTAR'] = lib.CDLMORNINGDOJISTAR(open, high, low, close)
    #
    # 黄昏之星
    df['CDLEVENINGSTAR'] = lib.CDLEVENINGSTAR(open, high, low, close)
    #
    # 黄昏十字星
    df['CDLEVENINGDOJISTAR'] = lib.CDLEVENINGDOJISTAR(open, high, low, close)
    #
    # # Three Advancing White Soldiers 三个白兵
    # df['CDL3WHITESOLDIERS'] = lib.CDL3WHITESOLDIERS(open, high, low, close)
    #
    # # Advance Block 大敌当前
    # df['CDLADVANCEBLOCK'] = lib.CDLADVANCEBLOCK(open, high, low, close)
    #
    # # High-Wave Candle 风高浪大线
    # df['CDLHIGHWAVE'] = lib.CDLHIGHWAVE(open, high, low, close)
    #
    # # Hikkake Pattern 陷阱
    # df['CDLHIKKAKE'] = lib.CDLHIKKAKE(open, high, low, close)
    #
    # # Modified Hikkake Pattern 修正陷阱
    # df['CDLHIKKAKEMOD'] = lib.CDLHIKKAKEMOD(open, high, low, close)
    #
    # # Identical Three Crows 三胞胎乌鸦
    # df['CDLIDENTICAL3CROWS'] = lib.CDLIDENTICAL3CROWS(open, high, low, close)
    #
    # # Spinning Top 纺锤
    # df['CDLSPINNINGTOP'] = lib.CDLSPINNINGTOP(open, high, low, close)
    #
    # # Stalled Pattern 停顿形态
    # df['CDLSTALLEDPATTERN'] = lib.CDLSTALLEDPATTERN(open, high, low, close)
    #
    # # Stick Sandwich 条形三明治
    # df['CDLSTICKSANDWICH'] = lib.CDLSTICKSANDWICH(open, high, low, close)
    #
    # # Tasuki Gap 跳空并列阴阳线
    # df['CDLTASUKIGAP'] = lib.CDLTASUKIGAP(open, high, low, close)
    #
    # # Tristar Pattern 三星
    # df['CDLTRISTAR'] = lib.CDLTRISTAR(open, high, low, close)
    #
    # # Upside Gap Two Crows 向上跳空的两只乌鸦
    # df['CDLUPSIDEGAP2CROWS'] = lib.CDLUPSIDEGAP2CROWS(open, high, low, close)
    #
    # """
    # 四日K线模式
    # """
    #
    # # Three-Line Strike 三线打击
    # df['CDL3LINESTRIKE'] = lib.CDL3LINESTRIKE(open, high, low, close)
    #
    # # 藏婴吞没  底部反转
    # df['CDLCONCEALBABYSWALL'] = lib.CDLCONCEALBABYSWALL(open, high, low, close)
    #
    # """
    # 五日K线模式
    # """
    #
    # # Breakaway 脱离  预示价格上涨
    # df['CDLBREAKAWAY'] = lib.CDLBREAKAWAY(open, high, low, close)
    #
    # Ladder Bottom 梯底 底部反转
    # df['CDLLADDERBOTTOM'] = lib.CDLLADDERBOTTOM(open, high, low, close)
    #
    # # Mat Hold 铺垫
    # df['CDLMATHOLD'] = lib.CDLMATHOLD(open, high, low, close)
    #
    # # Rising/Falling Three Methods 上升/下降三法
    # df['CDLRISEFALL3METHODS'] = lib.CDLRISEFALL3METHODS(open, high, low, close)
    #
    # # Upside/Downside Gap Three Methods 上升/下降跳空三法
    # df['CDLXSIDEGAP3METHODS'] = lib.CDLXSIDEGAP3METHODS(open, high, low, close)

    return df
