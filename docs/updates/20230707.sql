alter table stock_signals add COLUMN macd_zero_gold_cross tinyint DEFAULT null COMMENT '零轴金叉';
alter table stock_signals add COLUMN macd_gold_cross tinyint DEFAULT null COMMENT '金叉';

alter table stock_daily_signals add COLUMN macd_zero_gold_cross tinyint DEFAULT null COMMENT '零轴金叉';
alter table stock_daily_signals add COLUMN macd_gold_cross tinyint DEFAULT null COMMENT '金叉';

alter table weekly_signals add COLUMN macd_zero_gold_cross tinyint DEFAULT null COMMENT '零轴金叉';
alter table weekly_signals add COLUMN macd_gold_cross tinyint DEFAULT null COMMENT '金叉';
