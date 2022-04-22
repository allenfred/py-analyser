CREATE TABLE `weekly_candles` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `open` float,
  `high` float,
  `low` float,
  `close` float,
  `pre_close` float,
  `change` float,
  `pct_chg` float,
  `vol` float,
  `amount` float,
  `ma5` float,
  `ma10` float,
  `ma20` float,
  `ma30` float,
  `ma60` float,
  `ema5` float,
  `ema10` float,
  `ema20` float,
  `ema30` float,
  `ema60` float,
  `diff` float,
  `dea` float,
  `macd` float
);

CREATE INDEX `weekly_candles_index_23` ON `weekly_candles` (`ts_code`);
CREATE INDEX `weekly_candles_index_24` ON `weekly_candles` (`trade_date`);
CREATE UNIQUE INDEX `weekly_candle_unique` ON `weekly_candles` (`ts_code`, `trade_date`);
