module.exports = {
  apps: [
    {
      name: 'klines_CN',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/daily/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 16 * * *', // 每个交易日下午 16:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn-dividend',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/daily/cn_dividend.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '35 16 * * *', // 每个交易日下午 16:35
      watch: false,
      autorestart: false,
    },
    {
      name: 'klines_HK',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/daily/hk.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 18 * * *', // 每个交易日下午 18:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'klines_US',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/daily/us.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 13 * * *', // 每天下午 13:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn-weekly',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/weekly/analysis.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 22 * * *', // 每天下午 22:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn-basic',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/candles/daily/cn_basic.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'analysis_CN',
      log_date_format：'YYYY-MM-DD HH:mm Z',
      script: 'jobs/analysis/daily/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '0 17 * * *', // 每个交易日下午 17:00
      watch: false,
      autorestart: false,
    },
    {
      name: 'analysis_HK',
      log_date_format：'YYYY-MM-DD HH:mm Z',
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
      log_date_format：'YYYY-MM-DD HH:mm Z',
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
