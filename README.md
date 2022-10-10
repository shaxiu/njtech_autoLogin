# 南京工业大学无线网自动登录脚本

🎈脚本主要用于自动连接学校无线网 `Njtech-home` `Njtech`

- [x] 支持 `Njtch` `Njtech-home`

- [x] 支持验证码识别

### 环境配置

- Python3

- selenium

- ddddocr

- configparser

- chromedriver

- chrome

### 安装

默认已安装好python3 以及 chrome

#### 安装相应库

`pip install selenium`

`pip install ddddocr`

`pip install configparser`

#### 下载chromedriver

根据自己电脑上的chrome版本下载对应版本的驱动


| [**ChromeDriver 107.0.5304.18**](https://registry.npmmirror.com/binary.html?path=chromedriver/107.0.5304.18/) | [**ChromeDriver 106.0.5249.61**](https://registry.npmmirror.com/binary.html?path=chromedriver/106.0.5249.61/) | [**ChromeDriver 106.0.5249.21**](https://chromedriver.storage.googleapis.com/index.html?path=106.0.5249.21/) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [**ChromeDriver 105.0.5195.52**](https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52) | [**ChromeDriver 105.0.5195.19**](https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.19/) | [**ChromeDriver 104.0.5112.79**](https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/) |           


  更多版本请访问：http://npm.taobao.org/mirrors/chromedriver/

## 脚本配置

- **将代码中的`chromedriver路径`替换为已下载到本地的路径/替换项目中的Chromedriver.exe**

  `driver=webdriver.Chrome(executable_path="chromedriver相对路径", options=option)`

- **修改`config.ini`**

  ```ini
  [accountInfo]
  account = 学号
  password = 密码
  channel= 1
  headless=false
  ```

  ```ini
  [附加说明]
  ------------------
  channel=0 校园网
  channel=1 中国移动
  channel=2 中国电信
  ------------------
  headless=true 无GUI 适用于服务器或自动运行脚本
  headless=false 有GUI 可以看到登录情况
  ```

- 理论上代码适配全平台,`MAC` `Linux` 用户可自行调整代码，不单独进行打包，现已将适配 Windows 的版本 打包成`exe`发布
