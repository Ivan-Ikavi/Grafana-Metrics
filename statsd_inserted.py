import time
import random
import statsd

statsd_host='127.0.0.1'
statsd_port=8125

client = statsd.StatsClient(statsd_host, statsd_port)

while 1:
    value = random.randint(50, 60)
    bool_val = random.randint(0, 1)
    print(f'inserting {value}')
    metric_name = 'random.number'
    metric_name_2 = 'bool.flag'
    client.set(metric_name_2, bool_val)
    client.gauge(metric_name, value)
    time.sleep(5)
