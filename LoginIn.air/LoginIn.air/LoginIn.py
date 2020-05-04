# -*- encoding=utf8 -*-

__author__ = "lenovo"

from airtest.core.api import *
#Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

auto_setup(__file__)

# 打开苏泊尔智慧家APP
def open_supor_app():
    poco("com.sec.android.app.launcher:id/workspace")\
    .child("android.view.ViewGroup")\
    .offspring("苏泊尔智慧家").click()#主页面点击启动苏泊尔智慧家
    print("已启动苏泊尔智慧家APP")
    sleep(5.0)  #启动页等候时间

# 校验当前界面是否为协议界面
def check_weather_first_start():
    try:
        wait(Template(r"tpl1582869317826.png", record_pos=(0.009, -0.797), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未出现软件许可及服务协议界面")
    else:
        print("当前界面为软件许可及服务协议界面")
        
#  校验软件协议界面点击不同意是否有退回到手机主页       
def disagree():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.TextView").click()#点击不同意按钮
    print("不同意软件许可及服务协议")
    try:
        wait(Template(r"tpl1587529160748.png", record_pos=(0.013, 0.443), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("点击不同意未跳转回到手机主页面")
    else:
        print("点击不同意跳转回到手机主页面")

# 软件协议界面点击同意
def agree():
    open_supor_app()
    check_weather_first_start()
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.widget.TextView").click()   #点击同意按钮
    print("同意软件许可及服务协议")
    check_weahter_loginIn_page()
    
# 校验是否成功跳转登录页   
def check_weahter_loginIn_page():
    try:
        wait(Template(r"tpl1587535937674.png", record_pos=(0.02, 0.413), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("跳转登录页存在异常")
    else:
        print("正常跳转登录页")
        
# 校验手机号：少于11位手机号 
def check_phonenum1():
    poco("ACCOUNT").wait_for_appearance() #定位到账号输入框
    poco("ACCOUNT").set_text("1591586678") #输入10位手机号
    click_check()
    poco(text="发送").wait_for_appearance() #定位到发送按钮位置
    poco(text="发送").click() #点击发送按钮
    try:
        wait(Template(r"tpl1582708968498.png", record_pos=(-0.027, -0.114), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("有校验手机号不能少于11位")
    else:
        print("没有校验手机号")
        
# 校验手机号：多于11位手机号      
def check_phonenum2():
    poco("ACCOUNT").wait_for_appearance() #定位到账号输入框
    poco("ACCOUNT").set_text("159158667830") #输入12位手机号
    click_check()
    poco(text="发送").wait_for_appearance() #定位到发送按钮位置
    poco(text="发送").click() #点击发送按钮
    try:
        wait(Template(r"tpl1582708968498.png", record_pos=(-0.027, -0.114), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("有校验手机号不能大于11位")
    else:
        print("没有校验手机号")
    
# 校验协议是否处于已勾选状态
def click_check():
    try:
        wait(Template(r"tpl1582697599588.png", record_pos=(-0.297, 0.327), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[3].child("android.view.ViewGroup").click() #勾选操作
        print("补充勾选")
    else:
        print("本来就处于已勾选状态")

# 发送验证码
def PIN_send():
    poco("ACCOUNT").wait_for_appearance() #定位到账号输入框
    poco("ACCOUNT").set_text("15915866783") #输入账号
    click_check()
    poco(text="发送").wait_for_appearance() #定位到发送按钮位置
    poco(text="发送").click() #点击发送按钮
    try:
        wait(Template(r"tpl1582708968498.png", record_pos=(-0.027, -0.114), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("验证码发送失败")
    else:
        print("验证码发送成功")
        
# 校验验证码的有效性        
def check_verification_code():
    poco("ACCOUNT").wait_for_appearance() #定位到账号输入框
    poco("ACCOUNT").set_text("15915866783") #输入账号
    click_check()
    poco("CODE").set_text("000000") #输入错误验证码
    sleep(1)
    poco(text="开始").click() #点击登录
    try:
        wait(Template(r"tpl1587538106602.png", record_pos=(0.003, -0.036), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("未校验验证码的有效性")
    else:
        print("有校验验证码的有效性")

# 丛云片获取验证码
def get_it():
    
    driver.get("https://www.yunpian.com/entry") #打开云片网
    
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").click() #点击账号输入框
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").send_keys("13777840318") #输入账号
    
    driver.find_element_by_xpath("//input[@type='password']").click()  #点击密码输入框
    driver.find_element_by_xpath("//input[@type='password']").send_keys("jugonglu27#") #输入密码
    
    driver.find_element_by_xpath("//*[@id=\"__layout\"]/div/div/div/div/div[2]/div/div").click()#点击登录按钮
    
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/div").click() #点击国内短信
    
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/ul/li[3]").click() #点击短信记录

    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").click() #定位到手机号输入框
    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").send_keys("15915866783") #输入手机号
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/form/div[6]/div/button").click()  #点击搜索对应手机号短信记录
    message=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div[3]/table/tbody/tr/td[3]/div/div/span").text #获取短信内容

    #获取验证码
    keyword = "验证码是" #设置关键词
    keywordIndex = message.find(keyword) #获取关键词下标
    codeIndex = keywordIndex+len(keyword) #获取关键词长度
    code = message[codeIndex:codeIndex+6] #获取验证码
    poco("CODE").set_text(code) #填写验证码
    touch(Template(r"tpl1582799154455.png", record_pos=(-0.006, 0.702), resolution=(1080, 2220))) #移开焦点

# 登录操作
def login_in():
    poco(text="开始").click() 
    print("点击登录")
    try:
        wait(Template(r"tpl1582797826759.png", record_pos=(0.008, 0.827), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("登录不成功")
    else:
        print("登录成功")

# 获取位置权限       
def  first_time_login_in():
    try:
        wait(Template(r"tpl1585711871674.png", record_pos=(0.008, 0.577), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("位置权限已开启")
    else:
        open_position()
        
# 打开位置权限        
def open_position():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].offspring("android.widget.TextView").click() #点击启用按钮
    print("点击启用按钮")
    try:
        wait(Template(r"tpl1582871390713.png", record_pos=(0.006, 0.72), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未询问权限")
    else:
        poco(text="总是允许").click()
        print("开启位置权限")

# 校验登陆是否成功
def whether_home_page():
    try:
        wait(Template(r"tpl1582871684220.png", record_pos=(0.006, 0.827), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("当前界面非首页，登陆跳转存在异常")
    else:
        print("当前界面为首页，登陆成功且跳转正常")


        
#-----
open_supor_app() # 打开苏泊尔智慧家APP
check_weather_first_start() # 校验当前界面是否为协议界面
disagree() #  校验软件协议界面点击不同意是否有退回到手机主页
agree() # 软件协议界面点击同意
check_weahter_loginIn_page() # 校验是否成功跳转登录页 
check_phonenum1() # 校验手机号：少于11位手机号  
check_phonenum2() # 校验手机号：多于11位手机号   
click_check() # 校验协议是否处于已勾选状态
PIN_send() # 发送验证码
#check_verification_code() # 校验验证码的有效性(接口目前没判断)
get_it() # 丛云片获取验证码
login_in() # 登录操作
first_time_login_in() # 获取位置权限
#open_position() # 打开位置权限（方法中被调用的方法）
whether_home_page() # 校验登陆是否成功