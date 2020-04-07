from crontab import CronTab
 
my_cron = CronTab(user='melina')
job = my_cron.new(command='python /home/melina/script/commit.py')
job.minute.every(1)
 
my_cron.write()
