CREATE TABLE `hk_daily_candles` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `open` float,
  `high` float,
  `low` float,
  `close` float,
  `pre_close` float COMMENT '昨收价',
  `chg` float COMMENT '涨跌额',
  `pct_chg` float COMMENT '涨跌幅',
  `vol` float COMMENT '成交量',
  `amount` float COMMENT '成交额',
  `turnover_rate` float COMMENT '换手率',
  `turnover_rate_f` float COMMENT '换手率(自由流通股)',
  `volume_ratio` float COMMENT '量比',
  `pe` float COMMENT '市盈率（总市值/净利润）',
  `pe_ttm` float COMMENT '市盈率（TTM）',
  `pb` float COMMENT '市净率（总市值/净资产）',
  `ps` float COMMENT '市销率',
  `ps_ttm` float COMMENT '市销率（TTM）',
  `dv_ratio` float COMMENT '股息率（%）',
  `dv_ttm` float COMMENT '股息率（TTM)（%）',
  `total_share` float COMMENT '总股本',
  `float_share` float COMMENT '流通股本',
  `free_share` float COMMENT '自由流通股本',
  `total_mv` float COMMENT '总市值',
  `circ_mv` float COMMENT '流通市值'
);

CREATE INDEX `hk_daily_candles_index_ts_code` ON `hk_daily_candles` (`ts_code`);
CREATE INDEX `hk_daily_candles_index_trade_date` ON `hk_daily_candles` (`trade_date`);
CREATE UNIQUE INDEX `hk_daily_candles_unique` ON `hk_daily_candles` (`ts_code`, `trade_date`);
