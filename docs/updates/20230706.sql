alter table stock_signals add COLUMN up_trend tinyint DEFAULT null COMMENT '上涨趋势';
alter table stock_signals add COLUMN down_trend tinyint DEFAULT null COMMENT '下跌趋势';
alter table stock_signals add COLUMN strong_decline tinyint DEFAULT null COMMENT '强势下跌';

alter table stock_daily_signals add COLUMN up_trend tinyint DEFAULT null COMMENT '上涨趋势';
alter table stock_daily_signals add COLUMN down_trend tinyint DEFAULT null COMMENT '下跌趋势';
alter table stock_daily_signals add COLUMN strong_decline tinyint DEFAULT null COMMENT '强势下跌';

alter table weekly_signals add COLUMN up_trend tinyint DEFAULT null COMMENT '上涨趋势';
alter table weekly_signals add COLUMN down_trend tinyint DEFAULT null COMMENT '下跌趋势';
alter table weekly_signals add COLUMN strong_decline tinyint DEFAULT null COMMENT '强势下跌';
