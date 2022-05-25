# -- coding: utf-8 -
import talib as lib
from lib.signal.crypto.candle import is_hammer, is_pour_hammer, is_short_end, is_swallow_up, \
    is_sunrise, is_first_light, is_attack_short, is_flat_base, is_rise_line, is_down_screw, \
    is_long_end, is_swallow_down, is_hang_neck, is_shooting, is_jump_line, is_up_screw, is_down_rise


def pattern_analyze(df):
    open = df.open.to_numpy()
    high = df.high.to_numpy()
    low = df.low.to_numpy()
    close = df.close.to_numpy()

    candle = df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    hammer = []
    pour_hammer = []
    short_end = []
    swallow_up = []
    attack_short = []
    first_light = []
    sunrise = []
    flat_base = []
    rise_line = []
    down_screw = []
    long_end = []
    swallow_down = []
    hang_neck = []
    shooting = []
    jump_line = []
    up_screw = []
    down_rise = []

    for index in range(len(candle)):
        # 锤子线
        if is_hammer(index, candle):
            hammer.insert(index, 1)
        else:
            hammer.insert(index, 0)

        # 倒锤子线
        if is_pour_hammer(index, candle):
            pour_hammer.insert(index, 1)
        else:
            pour_hammer.insert(index, 0)

        # 看涨尽头线
        if is_short_end(index, candle):
            short_end.insert(index, 1)
        else:
            short_end.insert(index, 0)

        # 下探上涨
        if is_down_rise(index, candle):
            down_rise.insert(index, 1)
        else:
            down_rise.insert(index, 0)

        # 看涨吞没
        if is_swallow_up(index, candle):
            swallow_up.insert(index, 1)
        else:
            swallow_up.insert(index, 0)

        # 好友反攻
        if is_attack_short(index, candle):
            attack_short.insert(index, 1)
        else:
            attack_short.insert(index, 0)

        # 曙光初现
        if is_first_light(index, candle):
            first_light.insert(index, 1)
        else:
            first_light.insert(index, 0)

        # 旭日东升
        if is_sunrise(index, candle):
            sunrise.insert(index, 1)
        else:
            sunrise.insert(index, 0)

        # 平底
        if is_flat_base(index, candle):
            flat_base.insert(index, 1)
        else:
            flat_base.insert(index, 0)

        # 涨停一字板
        if is_rise_line(index, candle):
            rise_line.insert(index, 1)
        else:
            rise_line.insert(index, 0)

        # 下跌螺旋桨
        if is_down_screw(index, candle):
            down_screw.insert(index, 1)
        else:
            down_screw.insert(index, 0)

        # 看跌尽头线
        if is_long_end(index, candle):
            long_end.insert(index, 1)
        else:
            long_end.insert(index, 0)

        # 看跌吞没
        if is_swallow_down(index, candle):
            swallow_down.insert(index, 1)
        else:
            swallow_down.insert(index, 0)

        # 吊颈线
        if is_hang_neck(index, candle):
            hang_neck.insert(index, 1)
        else:
            hang_neck.insert(index, 0)

        # 射击之星
        if is_shooting(index, candle):
            shooting.insert(index, 1)
        else:
            shooting.insert(index, 0)

        # 跌停一字板
        if is_jump_line(index, candle):
            jump_line.insert(index, 1)
        else:
            jump_line.insert(index, 0)

        # 看跌螺旋桨
        if is_up_screw(index, candle):
            up_screw.insert(index, 1)
        else:
            up_screw.insert(index, 0)

    df['hammer'] = hammer
    df['pour_hammer'] = pour_hammer
    df['short_end'] = short_end
    df['swallow_up'] = swallow_up
    df['attack_short'] = attack_short
    df['first_light'] = first_light
    df['sunrise'] = sunrise
    df['flat_base'] = flat_base
    df['rise_line'] = rise_line
    df['down_screw'] = down_screw
    df['long_end'] = long_end
    df['swallow_down'] = swallow_down
    df['hang_neck'] = hang_neck
    df['shooting'] = shooting
    df['jump_line'] = jump_line
    df['up_screw'] = up_screw
    df['down_rise'] = down_rise

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
