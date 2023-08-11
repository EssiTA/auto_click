import os
import pyautogui
import cv2
#关闭指定的应用程序
def close_software(process_name):
    os.system(f"taskkill /f /im {process_name}")

# 找到图片并且触发点击
def find_and_click_image(template_path):
    # 加载模板图像
    template = cv2.imread(template_path, 0)
    template_width, template_height = template.shape[::-1]

    while True:
        # 截取屏幕图像
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

        # 将屏幕图像转换为灰度图像
        screenshot_gray = cv2.cvtColor(cv2.imread("screenshot.png"), cv2.COLOR_BGR2GRAY)

        # 在屏幕图像中寻找模板图像
        res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        # 如果找到匹配的位置，则点击它
        if len(loc[0]) > 0:
            x, y = loc[1][0], loc[0][0]
            click_x, click_y = x + template_width // 2, y + template_height // 2
            pyautogui.click(click_x, click_y)
            break

# 调用函数，并指定模板图像的路径
find_and_click_image("template.png")
