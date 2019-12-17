# Python自动化发送邮件步骤


#1. 安装python
------

1.1 下载python, 官网 https://www.python.org/downloads/  
1.2 python安装完成后，配置环境变量，步骤如图"env_config.png"  
1.3 在命令行执行"python --version",能够看到python版本号，表示配置环境变量  

#2. 将需要发送的附件添加到"attachment"目录;
------  

#3. 使用"pip3 install exchangelib"安装exchangelib
------  

#4. 将脚本中的"total_to_recievers"和"total_cc_recievers"修改成对应的接收者和抄送者
------  

#5. 所有配置完成后，在命令行进入"send_email"目录，执行"python batch_send_exchange_email.py"即可
------  