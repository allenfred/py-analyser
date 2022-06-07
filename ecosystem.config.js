module.exports = {
  apps: [
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
      cron_restart: '0 16 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_basic',
      script: 'jobs/candles/daily/cn_basic.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '5 16 * * *', // 每个交易日上午 16:05 获取A股每日指标
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_dividend',
      script: 'jobs/candles/daily/cn_dividend.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 16 * * *', // 每个交易日上午 9:30 获取每日除权除息
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_limit_list',
      script: 'jobs/candles/daily/cn_limit_limit.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 18 * * *', // 每个交易日下午 18:00 获取每日涨跌停统计
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_analysis',
      script: 'jobs/analysis/daily/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 18:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn_weekly',
      script: 'jobs/candles/weekly/analysis.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 22 * * *', // 每天下午 22:30
      watch: false,
      autorestart: false,
    }
    {
      name: 'hk_klines',
      script: 'jobs/candles/daily/hk.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 18 * * *', // 每个交易日下午 18:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'us_klines',
      script: 'jobs/candles/daily/us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 13 * * *', // 每天下午 13:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'analysis_HK',
      script: 'jobs/analysis/daily/hk.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 20 * * *', // 每个交易日下午 20:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'analysis_US',
      script: 'jobs/analysis/daily/us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 11 * * *', // 每天上午 11:00
      watch: false,
      autorestart: false,
    },
  ],
};
