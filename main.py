import time
import os
import subprocess
import cv2
import api

#软件名
softWareName = "猿如意"
# 启动应用软件
app_path = rf"D:\devit\devbit\{softWareName}.exe"#前缀r告诉Python将其视为原始字符串，不会对其中的反斜杠进行转义处理
subprocess.Popen(app_path)
time.sleep(2)
template = cv2.imread(template_path, 0)




# 调用close_software函数，并指定要关闭的软件进程名称
api.close_software(f"{softWareName}.exe")
