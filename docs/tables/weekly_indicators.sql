CREATE TABLE `weekly_indicators` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
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

CREATE INDEX `weekly_indicators_index_ts_code` ON `weekly_indicators` (`ts_code`);
CREATE INDEX `weekly_indicators_index_trade_date` ON `weekly_indicators` (`trade_date`);
CREATE UNIQUE INDEX `weekly_indicators_unique` ON `weekly_indicators` (`ts_code`, `trade_date`);