alter table stock_signals add COLUMN down_rise tinyint DEFAULT null COMMENT '下探上涨';
alter table stock_daily_signals add COLUMN down_rise tinyint DEFAULT null COMMENT '下探上涨';