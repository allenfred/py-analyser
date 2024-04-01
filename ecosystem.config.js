module.exports = {
  apps: [
    {
      name: 'crypto_analyzer',
      script: 'src/server.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 0 * * *', // everyday
      watch: true,
      autorestart: true,
    },
    {
      name: 'cn_limit',
      script: 'jobs/candles/daily/cn_limit.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 9 * * *', // 每个交易日上午 9:30 获取每日涨跌停价格
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_klines',
      script: 'jobs/candles/daily/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 16,17,18 * * *', // 每个交易日下午 16:00 / 17:00 / 18:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_basic',
      script: 'jobs/candles/daily/cn_basic.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '5 16 * * *', // 每个交易日下午 16:05 获取A股每日指标
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_dividend',
      script: 'jobs/candles/daily/cn_dividend.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 16 * * *', // 每个交易日下午 16:30 获取每日除权除息
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_analysis',
      script: 'jobs/analysis/daily/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_limit_list',
      script: 'jobs/candles/daily/cn_limit_list.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 19 * * *', // 每个交易日下午 19:00 获取每日涨跌停统计
      watch: false,
      autorestart: false,
    },
    {
      name: 'weekly_candle',
      script: 'jobs/candles/weekly/history.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 22 * * 5', // 每周五 22:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'weekly_analysis',
      script: 'jobs/candles/weekly/analysis.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 22 * * 5', // 每周五 22:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'us_klines',
      script: 'jobs/candles/daily/us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 11,12,13 * * *', // 每天 11:00/12:00/13:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'us_daily_history',
      script: 'jobs/candles/history/us_daily.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 0 * * 7', // 每周日 0时
      watch: false,
      autorestart: false,
    },
    {
      name: 'us_analysis',
      script: 'jobs/analysis/daily/us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 13 * * *', // 每天 13:30
      watch: false,
      autorestart: false,
    },
  ],
};
