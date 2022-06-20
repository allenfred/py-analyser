alter table stock_signals add COLUMN ma_rule_marker tinyint DEFAULT null COMMENT '葛南维买卖法则信号';
alter table stock_daily_signals add COLUMN ma_rule_marker tinyint DEFAULT null COMMENT '葛南维买卖法则信号';

CREATE INDEX `stock_signals_index_ma_rule_marker` ON `stock_signals` (`ma_rule_marker`);
CREATE INDEX `stock_daily_signals_index_ma_rule_marker` ON `stock_daily_signals` (`ma_rule_marker`);
