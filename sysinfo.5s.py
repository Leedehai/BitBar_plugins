#!/anaconda/bin/python
# <bitbar.title>Sys info</bitbar.title>
# <bitbar.version>v1.1</bitbar.version>
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

print "C %s M %s" % (str(cpu_used_percent/100).lstrip('0')[0:3], str(mem_used_percent/100).lstrip('0')[0:3])
print "---"
print "Used Mem: %.2f GB/%.2f GB" % (total_mem-avail_mem, total_mem)
