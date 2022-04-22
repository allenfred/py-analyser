CREATE TABLE `daily_kline_signals` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `hammer` tinyint(1) COMMENT '锤头线(long)',
  `pour_hammer` tinyint(1) COMMENT '倒锤头线(long)',
  `short_end` tinyint(1) COMMENT '尽头线(long)',
  `long_end` tinyint(1) COMMENT '尽头线(short)',
  `swallow_up` tinyint(1) COMMENT '看涨吞没(long)',
  `swallow_down` tinyint(1) COMMENT '看跌吞没(short)',
  `attack_short` tinyint(1) COMMENT '好友反攻(long)',
  `first_light` tinyint(1) COMMENT '曙光初现(long)',
  `sunrise` tinyint(1) COMMENT '旭日东升(long)',
  `flat_base` tinyint(1) COMMENT '平底(long)',
  `hang_neck` tinyint(1) COMMENT '吊颈线(short)',
  `shooting` tinyint(1) COMMENT '射击之星(short)',
  `rise_line` tinyint(1) COMMENT '涨停一字线(long)',
  `jump_line` tinyint(1) COMMENT '跌停一字线(short)',
  `up_screw` tinyint(1) COMMENT '上涨螺旋桨(short)',
  `down_screw` tinyint(1) COMMENT '下跌螺旋桨(long)'
);

CREATE INDEX `daily_kline_signals_index_ts_code` ON `daily_kline_signals` (`ts_code`);
CREATE INDEX `daily_kline_signals_index_trade_date` ON `daily_kline_signals` (`trade_date`);
CREATE UNIQUE INDEX `daily_kline_signals_unique` ON `daily_kline_signals` (`ts_code`, `trade_date`);
