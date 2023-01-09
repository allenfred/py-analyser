alter table stock_signals add COLUMN hlines varchar(255) DEFAULT null COMMENT '水平位';
alter table stock_signals add COLUMN limit_pullback tinyint DEFAULT null COMMENT '涨停回调';
alter table stock_signals add COLUMN up_pullback tinyint DEFAULT null COMMENT '上涨回调';
alter table stock_signals add COLUMN down_pullback tinyint DEFAULT null COMMENT '下跌反弹';
alter table stock_signals add COLUMN up_break tinyint DEFAULT null COMMENT '向上突破';
alter table stock_signals add COLUMN down_break tinyint DEFAULT null COMMENT '向下突破';
alter table stock_signals add COLUMN hline_support tinyint DEFAULT null COMMENT '水平支撑';
alter table stock_signals add COLUMN hline_resistance tinyint DEFAULT null COMMENT '水平阻力';


alter table stock_daily_signals add COLUMN hlines varchar(255) DEFAULT null COMMENT '水平位';
alter table stock_daily_signals add COLUMN limit_pullback tinyint DEFAULT null COMMENT '涨停回调';
alter table stock_daily_signals add COLUMN up_pullback tinyint DEFAULT null COMMENT '上涨回调';
alter table stock_daily_signals add COLUMN down_pullback tinyint DEFAULT null COMMENT '下跌反弹';
alter table stock_daily_signals add COLUMN up_break tinyint DEFAULT null COMMENT '向上突破';
alter table stock_daily_signals add COLUMN down_break tinyint DEFAULT null COMMENT '向下突破';
alter table stock_daily_signals add COLUMN hline_support tinyint DEFAULT null COMMENT '水平支撑';
alter table stock_daily_signals add COLUMN hline_resistance tinyint DEFAULT null COMMENT '水平阻力';


alter table weekly_signals add COLUMN hlines varchar(255) DEFAULT null COMMENT '水平位';
alter table weekly_signals add COLUMN limit_pullback tinyint DEFAULT null COMMENT '涨停回调';
alter table weekly_signals add COLUMN up_pullback tinyint DEFAULT null COMMENT '上涨回调';
alter table weekly_signals add COLUMN down_pullback tinyint DEFAULT null COMMENT '下跌反弹';
alter table weekly_signals add COLUMN up_break tinyint DEFAULT null COMMENT '向上突破';
alter table weekly_signals add COLUMN down_break tinyint DEFAULT null COMMENT '向下突破';
alter table weekly_signals add COLUMN hline_support tinyint DEFAULT null COMMENT '水平支撑';
alter table weekly_signals add COLUMN hline_resistance tinyint DEFAULT null COMMENT '水平阻力';
