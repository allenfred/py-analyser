CREATE TABLE `trade_calendar` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `exchange` varchar(255) NOT NULL COMMENT '交易所 SSE上交所 SZSE深交所 HK 港交所 US 美交所',
  `cal_date` date NOT NULL COMMENT '日历日期',
  `is_open` tinyint NOT NULL COMMENT '是否交易 0休市 1交易',
  `pretrade_date` date COMMENT '上一个交易日',
  `candle_ready` tinyint NOT NULL DEFAULT 0 COMMENT '日K是否获取完成 0否 1是',
  `basic_ready` tinyint NOT NULL DEFAULT 0 COMMENT '每日指标是获取完成 0否 1是',
  `talib_ready` tinyint NOT NULL DEFAULT 0 COMMENT 'talib指标是计算完成 0否 1是'
);

CREATE UNIQUE INDEX `trade_calendar_unique` ON `trade_calendar` (`exchange`, `cal_date`);
