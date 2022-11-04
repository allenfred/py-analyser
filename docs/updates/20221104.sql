alter table stock_signals add COLUMN up_wave tinyint DEFAULT null COMMENT '逐浪上升';
alter table stock_signals add COLUMN limit_up_gene tinyint DEFAULT null COMMENT '涨停基因';
alter table stock_daily_signals add COLUMN up_wave tinyint DEFAULT null COMMENT '逐浪上升';
alter table stock_daily_signals add COLUMN limit_up_gene tinyint DEFAULT null COMMENT '涨停基因';

