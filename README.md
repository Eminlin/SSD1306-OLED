# SSD1306-OLED
### 使用 python 的 luma.old 驱动树莓派 SSD-1306 屏幕，并显示 CPU/GPU 温度使用率、内存使用率、硬盘使用率、IP 地址
* ```sudo apt-get install python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential```  
* ```sudo pip3 install psutil```  
* ```sudo -H pip3 install --upgrade luma.oled```  
* ```python3 iic.py```  
### 加入开机启动
* 编辑 ```/etc/rc.local``` 文件，需要使用root或sudo
 * ```sudo vim /etc/rc.local```
* 在 exit 0 前添加 ```python3 /home/pi/iic/iic.py```  
> 注意：树莓派先要打开硬件 IIC 功能 具体操作可以参考：[timor.tech](http://timor.tech/mcu/oled/rpi-ssd1306-python.html)

* GitHub：[luma.oled](https://github.com/rm-hull/luma.oled)
* [Luma.oled 英文文档](https://luma-oled.readthedocs.io/en/latest/intro.html)
