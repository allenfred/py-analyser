alter table stock_signals change jump_line drop_line tinyint;
alter table stock_daily_signals change jump_line drop_line tinyint;

alter table stock_signals add COLUMN upward_jump tinyint DEFAULT null COMMENT '向上跳空';
alter table stock_signals add COLUMN downward_jump tinyint DEFAULT null COMMENT '向下跳空';
alter table stock_signals add COLUMN rise_limit tinyint DEFAULT null COMMENT '涨停板';
alter table stock_signals add COLUMN drop_limit tinyint DEFAULT null COMMENT '跌停板';
alter table stock_signals add COLUMN up_cross3ma tinyint DEFAULT null COMMENT '一阳穿三线';
alter table stock_signals add COLUMN up_cross4ma tinyint DEFAULT null COMMENT '一阳穿四线';
alter table stock_signals add COLUMN drop_cross3ma tinyint DEFAULT null COMMENT '一阴穿三线';
alter table stock_signals add COLUMN drop_cross4ma tinyint DEFAULT null COMMENT '一阴穿三线';

alter table stock_daily_signals add COLUMN upward_jump tinyint DEFAULT null COMMENT '向上跳空';
alter table stock_daily_signals add COLUMN downward_jump tinyint DEFAULT null COMMENT '向下跳空';
alter table stock_daily_signals add COLUMN rise_limit tinyint DEFAULT null COMMENT '涨停板';
alter table stock_daily_signals add COLUMN drop_limit tinyint DEFAULT null COMMENT '跌停板';
alter table stock_daily_signals add COLUMN up_cross3ma tinyint DEFAULT null COMMENT '一阳穿三线';
alter table stock_daily_signals add COLUMN up_cross4ma tinyint DEFAULT null COMMENT '一阳穿四线';
alter table stock_daily_signals add COLUMN drop_cross3ma tinyint DEFAULT null COMMENT '一阴穿三线';
alter table stock_daily_signals add COLUMN drop_cross4ma tinyint DEFAULT null COMMENT '一阴穿三线';
