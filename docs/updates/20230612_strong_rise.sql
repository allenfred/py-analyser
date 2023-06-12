alter table stock_signals add COLUMN strong_rise tinyint DEFAULT null COMMENT '强势上涨';

alter table stock_daily_signals add COLUMN strong_rise tinyint DEFAULT null COMMENT '强势上涨';

alter table weekly_signals add COLUMN strong_rise tinyint DEFAULT null COMMENT '强势上涨';
