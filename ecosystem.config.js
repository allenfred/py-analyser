module.exports = {
  apps: [
    {
      name: 'stockCN-daily',
      script: 'jobs/candles/daily/cn_stock_daily.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 16 * * *', // 每个交易日下午 16:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'stockHK-daily',
      script: 'jobs/candles/daily/hk_stock_daily.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 18 * * *', // 每个交易日下午 18:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'stockUS-daily',
      script: 'jobs/candles/daily/us_stock_daily.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 10 * * *', // 每天上午 10:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'stockCN-weekly',
      script: 'jobs/candles/weekly/cn_stock_weekly.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 22 * * 5', // 每周五下午 22:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'stockCN-basic',
      script: 'jobs/candles/daily/cn_stock_daily_basic.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'CNdaily-analysis',
      script: 'jobs/analysis/daily/stock_cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'HKdaily-analysis',
      script: 'jobs/analysis/daily/stock_hk.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 20 * * *', // 每个交易日下午 20:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'USdaily-analysis',
      script: 'jobs/analysis/daily/stock_us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 11 * * *', // 每天上午 11:00
      watch: false,
      autorestart: false,
    },
  ],
};
