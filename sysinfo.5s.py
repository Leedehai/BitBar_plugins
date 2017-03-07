#!/anaconda/bin/python2
# <bitbar.title>Sys info</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Haihong Li</bitbar.author>
# <bitbar.author.github>Leedehai</bitbar.author.github>
# <bitbar.desc>Shows the current system info</bitbar.desc>
# <bitbar.dependencies>python, psutil (>=5.2) </bitbar.dependencies>
# <bitbar.abouturl>https://https://github.com/Leedehai/BitBar_plugins</bitbar.abouturl>

import psutil

cpu_used_percent = psutil.cpu_percent(interval=0.5)

mem_report = psutil.virtual_memory()
total_mem = mem_report[0]/1073741824
avail_mem = mem_report[1]/1073741824
mem_used_percent = mem_report[2]



print "C %.2f M %.2f" % (cpu_used_percent/100, mem_used_percent/100)
print "---"
print "Used Mem: %.2f GB/16 GB" % (16-avail_mem)
