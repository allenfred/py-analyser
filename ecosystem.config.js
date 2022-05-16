module.exports = {
  apps: [
    {
      name: 'klines_CN',
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
      script: 'jobs/candles/weekly/cn.py',
      interpreter: 'python3',
      instances: 1,
      exec_mode: 'fork',
      cron_restart: '30 22 * * 5', // 每周五下午 22:30
      watch: false,
      autorestart: false,
    },
    {
      name: 'cn-basic',
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
