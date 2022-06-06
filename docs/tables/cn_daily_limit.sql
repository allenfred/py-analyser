CREATE TABLE `cn_daily_limit` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `ts_code` varchar(255) NOT NULL COMMENT 'TS代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `name` varchar(255) NOT NULL COMMENT '股票名称',
  `close` float,
  `pct_chg` float COMMENT '涨跌幅',
  `amp` float COMMENT '振幅',
  `fc_ratio` float COMMENT '封单金额/日成交金额',
  `fl_ratio` float COMMENT '封单手数/流通股本',
  `fd_amount` float COMMENT '封单金额',
  `first_time` datetime NOT NULL COMMENT '首次涨停时间',
  `last_time` datetime NOT NULL COMMENT '最后封板时间',
  `open_times` integer COMMENT '打开次数',
  `strth` float COMMENT '涨跌停强度',
  `limit` varchar(2) COMMENT 'D跌停U涨停'
);

CREATE INDEX `cn_daily_limit_index_ts_code` ON `cn_daily_limit` (`ts_code`);
CREATE INDEX `cn_daily_limit_index_trade_date` ON `cn_daily_limit` (`trade_date`);
CREATE UNIQUE INDEX `cn_daily_limit_unique` ON `cn_daily_limit` (`ts_code`, `trade_date`);
