from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddddocr
import configparser


def main():
    channelsName=['校园网','中国移动','中国电信']
    option = webdriver.ChromeOptions()
    if user_headless=='true':
        option.add_argument('--headless')
    option.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')
    driver = webdriver.Chrome(
        executable_path="./chromedriver.exe", options=option)
    driver.get('http://i.njtech.edu.cn/')
    time.sleep(2)
    img = driver.find_element(By.ID,"pc-captcha")
    image_bytes = img.screenshot_as_png
    captchaCode = ocr.classification(image_bytes)
    accountInput = driver.find_element(By.ID,"username")
    passwdInput = driver.find_element(By.ID,"password")
    captchaInput = driver.find_element(By.ID,'imgcaptcha')
    longinButton = driver.find_element(By.ID,'login')
    accountInput.send_keys(user_account)
    passwdInput.send_keys(user_password)
    captchaInput.send_keys(captchaCode)
    try:
        # 通道选择
        channelSelect = driver.find_element(By.ID,'channelshow')
        channels = driver.find_elements(By.TAG_NAME,'span')[user_channel]
        channelSelect.click()
        channels.click()
        print('正在连接 njtech-home ...')
        print('服务商为:'+channelsName[user_channel])
    except:
        print('正在连接 njtech ...')
    longinButton.click()
    print('执行成功')
    driver.quit()


if __name__ == '__main__':
    print('-----------------------------')
    print('南京工业大学无线网登陆脚本')
    print('designed by coderxiu')
    print('Github地址:https://github.com/shaxiu/njtech_autoLogin')
    print('-----------------------------')
    print('正在读取初始化配置文件')
    # 导入模型文件
    ocr = ddddocr.DdddOcr(det=False, ocr=False, import_onnx_path="./models/captcha_1.0_3053_19000_2022-10-09-13-35-56.onnx",
                          charsets_path="./models/charsets.json",show_ad=False)
    # 读取配置文件
    CONF_FILE = './config.ini'
    cf = configparser.ConfigParser()
    cf.read(CONF_FILE)
    user_account = cf.get("accountInfo", "account")
    user_password = cf.get("accountInfo", "password")
    user_channel = int(cf.get("accountInfo", "channel")) if int(cf.get("accountInfo", "channel")) in [0,1,2] else 0
    user_headless = cf.get("accountInfo", "headless") if cf.get("accountInfo", "headless") in ['true','false'] else 'true'
    main()
