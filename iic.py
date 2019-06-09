from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import subprocess
import time
import socket
import psutil  # 监控数据读取
from time import sleep  # 控制刷新时间
import os

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,1);

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_cpu_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close();
    return temp

def get_gpu_temp():
    temp = subprocess.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=','').replace('\'C','')
    return float(temp)

def cpu():
    cpu_temp = psutil.cpu_percent()
    return cpu_temp

def disk():
    disk_u = psutil.disk_usage("/").percent
    disk_u = str(disk_u)
    return disk_u

def mem():
    mem_p = psutil.virtual_memory().percent  # 读取内存使用率
    #mem=mem_u / mem_t
    return mem_p

def net_info():
    net_in = psutil.net_io_counters().bytes_recv/1024/1024
    net_in = round(net_in, 2)
    net_out = psutil.net_io_counters().bytes_sent/1024/1024
    net_out = round(net_out, 2)
    net = str(net_in)+"MB / "+str(net_out)+"MB"
    return net

M = 1048576 # 一 M 所包含的字节数              
def net_speed():
    s1 = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    s2 = psutil.net_io_counters().bytes_recv
    result = s2 - s1
    if (result > M):
        return str('%.2f'%(result / 1024 / 1024)) + ' M/s'
    else:
        return str('%.2f'%(result / 1024)) + ' kb/s'

ip_addr = get_ip()

while True:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box)
        draw.text((0,0),"Emin and Leslie :)",fill="white")
        draw.text((0,15),'ip:' + ip_addr,fill="white")
        draw.text((0,25),'cpu:' + str( get_cpu_temp()),fill="white")
        draw.text((70,25),'gpu:' + str( get_gpu_temp()),fill="white")

        draw.text((0,35),'CMD: ',fill="white")
        draw.text((30,35),str(cpu()) ,fill="white")
        draw.text((60,35), str( mem()),fill="white")
        draw.text((90,35), disk(),fill="white")
        draw.text((0,45),'NS: ' + net_speed(),fill="white")
    time.sleep(second);

while(True):
    pass
