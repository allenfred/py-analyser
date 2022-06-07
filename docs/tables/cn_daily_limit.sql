CREATE TABLE `cn_daily_limit` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `pre_close` float COMMENT '昨日收盘价',
  `up_limit` float COMMENT '涨停价',
  `down_limit` float COMMENT '跌停价'
);

CREATE INDEX `cn_daily_limit_index_ts_code` ON `cn_daily_limit` (`ts_code`);
CREATE INDEX `cn_daily_limit_index_trade_date` ON `cn_daily_limit` (`trade_date`);
CREATE UNIQUE INDEX `cn_daily_limit_unique` ON `cn_daily_limit` (`ts_code`, `trade_date`);
