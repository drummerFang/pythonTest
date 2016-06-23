#coding:utf-8
#!/usr/bin/python
import rrdtool
import time,psutil

nics=psutil.net_io_counters(pernic=True)
nic_eth1=nics['eth1']
total_input_traffic = nic_eth1[1]
total_output_traffic = nic_eth1[0]
starttime=int(time.time())

update=rrdtool.updatev('/home/rrdtool/Flow.rrd','%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update 
