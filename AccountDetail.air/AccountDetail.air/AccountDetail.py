# -*- encoding=utf8 -*-

__author__ = "lenovo"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

auto_setup(__file__)

# 检查当前是否在【我的】模块界面
def check_whether_WoDe():
    try:
        wait(Template(r"tpl1582873438022.png", record_pos=(-0.301, 0.356), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("当前界面不是我的界面")
        poco(text="我的").click() #点击切换到我的界面
        print("手动切换到我的界面")
    else:
        print("当前界面是我的界面")
        
# 进入账号详情界面
def account_detail():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").click()#点击我的界面头像位置
    try:
        wait(Template(r"tpl1582874424022.png", record_pos=(0.0, 0.379), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未跳转进入账号详情界面")
    else:
        print("成功跳转进入账号详情界面")

# 触发修改头像弹窗
def image():
    poco(text="头像").click()#点击修改头像
    try:
        wait(Template(r"tpl1582876837887.png", record_pos=(0.017, 0.498), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未开启拍照或相册上传窗口")
    else:
        print("已开启拍照或相册上传窗口")

# 拍照上传头像
def take_picture():
    image()
    poco("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.TextView").click() #选择拍照上传
    carema_right()
    sleep(2)
    picture_right()
    take_picture_step1()
    take_picture_step2()
    take_picture_step3()
    back_to_account_detail()

# 相机权限的获取
def carema_right():
    try:
        wait(Template(r"tpl1585722546969.png", record_pos=(-0.001, 0.576), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("相机权限本来就处于已开启状态")     
    else:
        poco(text="启用").click() #点击启用相机权限
        print("准备启用相机权限")
        ask_for_carema_service()
        sleep(3.0)
        
# 允许使用相机权限             
def ask_for_carema_service(): 
    try:
        wait(Template(r"tpl1582877547622.png", record_pos=(0.004, 0.731), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未询问相机权限")
    else:
        poco(text="总是允许").click() #点击允许使用相机权限
        print("允许使用相机权限")
        try:
             wait(Template(r"tpl1582877547622.png", record_pos=(0.004, 0.731), resolution=(1080, 2220)),timeout=1.0)
        except TargetNotFoundError:
            print("点击有效")
        else:
            poco(text="总是允许").click()
            print("重试允许使用相机权限")
            
# 相册权限的获取           
def picture_right():
    try:
        wait(Template(r"tpl1585722546969.png", record_pos=(-0.001, 0.576), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("相册权限本来就处于已开启状态")
    else:
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].offspring("android.widget.TextView").click() #点击启用相册权限
        print("允许使用相册权限")
        ask_for_pictures_service()
        
# 允许使用相册权限
def ask_for_pictures_service():
    try:
        wait(Template(r"tpl1582879315790.png", record_pos=(0.015, 0.667), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未询问相册权限")
    else:
        poco(text="总是允许").click() #点击允许使用相册权限
        print("允许使用相册权限")
        try:
            wait(Template(r"tpl1582879315790.png", record_pos=(0.015, 0.667), resolution=(1080, 2220)),timeout=1.0)
        except TargetNotFoundError:
            print("点击有效")
        else:
            poco(text="总是允许").click()
            print("重试允许使用相册权限")

# 拍照步骤1
def take_picture_step1():        
    try:
        wait(Template(r"tpl1582880678676.png", record_pos=(0.11, 0.769), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("目标图片未出现")
    else:
        touch(Template(r"tpl1582880534890.png", record_pos=(0.006, 0.781), resolution=(1080, 2220)))#点击拍照
        sleep(1)
        
# 拍照步骤2        
def take_picture_step2():
    try:
        wait(Template(r"tpl1582881173656.png", record_pos=(0.005, 0.794), resolution=(1080, 2220)),timeout=2.0)
    except TargetNotFoundError:
        print("目标图片未出现")
    else:
        touch(Template(r"tpl1582881261235.png", record_pos=(0.215, 0.779), resolution=(1080, 2220)))#点击确定使用照片
        sleep(1)
        
# 拍照步骤3                
def take_picture_step3():  
    try:
        wait(Template(r"tpl1582881295125.png", record_pos=(0.273, -0.877), resolution=(1080, 2220)),timeout=2.0)
    except TargetNotFoundError:
        print("目标图片未出现")
    else:
        touch(Template(r"tpl1582881336893.png", record_pos=(0.427, -0.889), resolution=(1080, 2220)))#点击裁切照片
        sleep(1)
        
# 返回账号详情界面
def back_to_account_detail():
    try:
        wait(Template(r"tpl1582881605369.png", record_pos=(-0.188, -0.885), resolution=(1080, 2220)),timeout=1.0)        
    except TargetNotFoundError:
        print("未返回账号详情界面，头像修改可能失败")
    else:
        
        print("成功返回账号详情界面")
        sleep(2)
                     
# 从手机相册上传        
def phone_picture():
    image()
    poco("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].click()#点击选择从手机相册上传
    phone_picture_step1()
    phone_picture_step2()
    phone_picture_step3()
    phone_picture_step4()
    back_to_account_detail()

# 手机相册上传步骤1
def phone_picture_step1():
    try:
        wait(Template(r"tpl1582886147239.png", record_pos=(-0.415, -0.881), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("目标图标未找到")
    else:
        poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("显示根目录").click()
        sleep(1)
        
# 手机相册上传步骤2                
def phone_picture_step2():
    try:
        wait(Template(r"tpl1583046347538.png", record_pos=(-0.291, -0.053), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("目标图标未找到")
    else:
        touch(Template(r"tpl1583046434182.png", record_pos=(-0.282, -0.044), resolution=(1080, 2220)))
        sleep(1)
        
# 手机相册上传步骤3
def phone_picture_step3():
    try:
        wait(Template(r"tpl1583046587352.png", record_pos=(0.013, 0.815), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("目标图标未找到")
    else:
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sec.android.gallery3d:id/content").offspring("com.sec.android.gallery3d:id/my_recycler_view").child("com.sec.android.gallery3d:id/recycler_view_item")[0].child("com.sec.android.gallery3d:id/thumbnail").click()
        sleep(1)
        
# 手机相册上传步骤4
def phone_picture_step4():
    try:
        wait(Template(r"tpl1583047207150.png", record_pos=(0.432, -0.87), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("目标图标")
    else:
        poco("android.widget.LinearLayout").offspring("com.supor.SmartHome:id/crop_image_menu_crop").click()
        sleep(1)
        back_to_account_detail()

# 昵称修改
def update_nickname():
    try:
        wait(Template(r"tpl1583122876451.png", record_pos=(-0.383, -0.35), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未找到昵称位置")
    else:
        poco(text="昵称").click()#点击进入昵称修改界面
        print("点击进入修改昵称界面")
        check_nickname_page()
        
# 校验当前界面是否为昵称修改界面        
def check_nickname_page():
    try:
        wait(Template(r"tpl1583123062226.png", record_pos=(-0.312, -0.879), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未成功进入昵称修改界面")
    else:
        print("已经成功进入修改昵称界面")
        
# 昵称为空校验       
def nickname_null():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].offspring("android.widget.EditText")[0].set_text("")#将昵称输入框设置输入为空
    poco(text="更改昵称").click()#点击更改昵称
    try:
        wait(Template(r"tpl1583130133035.png", record_pos=(-0.266, -0.881), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("已做了非空校验")
    else:
        print("未做非空校验")
        
# 昵称输入限制校验
def nickname_limit():
    update_nickname()
    check_nickname_page()
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].offspring("android.widget.EditText")[0].set_text("ABC abc @#$%^ 测试 12345")#将昵称输入框设置输入为带中英文数字和特殊字符的昵称）但不包含emoji符号
    poco(text="更改昵称").click()#点击更改昵称
#     poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[1].click()#点击更改按钮
    try:
        wait(Template(r"tpl1583130604146.png", record_pos=(-0.269, -0.883), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未跳转回到账号详情界面=未修改成功")
    else:
        print("跳转回到账号详情界面=修改昵称成功")
        sleep(3.0)
        
# 性别设置
def sex():
    poco(text="性别").click()#点击进入性别设置界面
    try:
        wait(Template(r"tpl1583133142830.png", record_pos=(-0.328, -0.881), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未进入性别修改界面")
    else:
        print("已进入性别修改界面")
        
# 设置性别为男性              
def set_sex_male():
    poco(text="男").click()#选中性别为男性
    try:
        wait(Template(r"tpl1583133350068.png", record_pos=(0.406, -0.143), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("性别未成功设置为男性")
    else:
        print("性别已成功设置为男性")
# 设置性别为女性       
def set_sex_female():
    sex()
    poco(text="女").click()#选中性别为女性
    try:
        wait(Template(r"tpl1583133636590.png", record_pos=(0.394, -0.152), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("性别未成功设置为女性")
    else:
        print("性别已成功设置为女性")    

# 微信绑定（前提：当前手机有微信客户端，且微信与当前APP未绑定）     
def binging_yes_or_no():
    poco(text="微信绑定").click()#点击微信绑定按钮
    sleep(2.0)
    try:
        wait(Template(r"tpl1583138632039.png", record_pos=(-0.002, -0.085), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未绑定成功")
    else:
        print("绑定成功")
        sleep(3)
        
# 取消微信绑定
def unbind():
    poco(text="微信绑定").click()#点击微信绑定按钮
    try:
        wait(Template(r"tpl1583155500080.png", record_pos=(0.005, -0.164), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("未显示解绑弹窗")
    else:
        poco(text="删除").click()#确定解绑
        unbind_success()
        
# 确定取消绑定
def unbind_success():
    try:
        wait(Template(r"tpl1583155661925.png", record_pos=(-0.004, -0.084), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("未提示解绑成功")
    else:
        print("解绑成功")
        
# 进入注销账号界面  
def delete_account():
    poco(text="注销账号").click()
    try:
        wait(Template(r"tpl1583140796085.png", record_pos=(-0.269, -0.881), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未跳转注销账号界面")
    else:
        print("成功跳转注销登录界面")
        
# 验证码非空校验
def without_testcode():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.EditText")[0].set_text("")#验证码设置为空
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].click()#点击注销账号按钮
    try:
        wait(Template(r"tpl1583141008086.png", record_pos=(-0.008, -0.115), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未做非空校验")
    else:
        print("已做非空校验")
        
# 验证码错误校验        
def wrong_testcode():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.EditText")[0].set_text(1234)#验证码设置为任意数
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].click()#点击注销账号按钮
    try:
        wait(Template(r"tpl1583141117940.png", record_pos=(0.016, -0.066), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未校验验证码的正确性")
    else:
        print("有校验验证码的正确性")
        
# 验证码时效校验        
def overdue_testcode():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.EditText")[0].set_text("2406")#验证码设置为已过期验证码
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].click()#点击注销账号按钮
    try:
        wait(Template(r"tpl1583141117940.png", record_pos=(0.016, -0.066), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("未校验验证码的时效性")
    else:
        print("有校验验证码的时效性")
        sleep(1)
# 确定注销账号
def do_delete_account():
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[0].click()#点击验证码输入框
    get_delete_code_success()
    touch(Template(r"tpl1582799154455.png", record_pos=(-0.006, 0.702), resolution=(1080, 2220)))#移开焦点
    poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].click()#点击注销账号按钮
    try:
        wait(Template(r"tpl1583226587936.png", record_pos=(-0.009, -0.083), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("注销账号异常")
    else:
        print("注销账号成功")
        whether_back_to_login_in_page()
        
# 发送注销验证码        
def get_delete_code_success():
    try:
        wait(Template(r"tpl1582708968498.png", record_pos=(-0.027, -0.114), resolution=(1080, 2220)))
    except TargetNotFoundError:
        print("验证码发送失败")
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[0].click()#点击发送验证码
        get_testcode()
    else:
        print("验证码发送成功")    
        get_testcode()
        
# 校验注销后是否正确跳转到登录界面        
def whether_back_to_login_in_page():
    sleep(3.0)
    try:
        wait(Template(r"tpl1583226699695.png", record_pos=(0.002, 0.321), resolution=(1080, 2220)),timeout=1)
    except TargetNotFoundError:
        print("注销成功但未跳转回登录界面")
    else:
        print("注销账号成功且成功跳转回到登录界面") 
    
# 获取注销验证码
def get_testcode():
    driver.get("https://www.yunpian.com/entry")
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").click()#定位手机号输入框
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").send_keys("13777840318")#输入账号
    driver.find_element_by_xpath("//input[@type='password']").click()#定位密码输入框
    driver.find_element_by_xpath("//input[@type='password']").send_keys("jugonglu27#")#输入密码
    driver.find_element_by_xpath("//*[@id=\"__layout\"]/div/div/div/div/div[2]/div/div").click()#点击登录
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/div").click()#点击国内短信
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/ul/li[3]").click()#点击短信记录
    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").click()#定位关键字输入框
    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").send_keys("13710120320")#输入要哦搜索的手机号
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/form/div[6]/div/button").click()#点击搜索
    message=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div[3]/table/tbody/tr/td[3]/div/div/span").text#获取手机短信内容


    keyword = "#app#您的验证码是"#设置关键词
    keywordIndex = message.find(keyword)#获取关键词下标
    codeIndex = keywordIndex+len(keyword)#获取关键词长度
    code = message[codeIndex:codeIndex+4]#获取验证码
    print(code)
    textView = poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.EditText")[0];
    textView.set_text(code);#填写验证码

# 登录-验证码是否可发送校验
def make_PIN_ready_to_send():
    try:
        wait(Template(r"tpl1582697599588.png", record_pos=(-0.297, 0.327), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[3].child("android.view.ViewGroup").click()#点击勾选
        print("补充勾选")
    else:
        print("本来就处于已勾选状态")

# 登录-发送验证码
def PIN_send():
    sleep(30)
    poco(text="发送").wait_for_appearance()#找发送按钮
    poco(text="发送").click()#点击发送按钮
    try:
        wait(Template(r"tpl1582708968498.png", record_pos=(-0.027, -0.114), resolution=(1080, 2220)))
    except TargetNotFoundError:
        print("验证码发送失败")
    else:
        print("验证码发送成功")

# 登录-获取验证码
def get_it():
    
    driver.get("https://www.yunpian.com/entry")
    
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").click()
    driver.find_element_by_xpath("//input[@placeholder='您的注册手机号']").send_keys("13777840318")#输入账号
    
    driver.find_element_by_xpath("//input[@type='password']").click()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("jugonglu27#")#输入密码
    
    driver.find_element_by_xpath("//*[@id=\"__layout\"]/div/div/div/div/div[2]/div/div").click()
    
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/div").click()
    
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/ul/li[2]/ul/li/ul/li[3]").click()

    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").click()
    driver.find_element_by_xpath("//input[@placeholder='请填写正确手机号']").send_keys("13710120320")
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/form/div[6]/div/button").click()
    message=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div[3]/table/tbody/tr/td[3]/div/div/span").text


    keyword = "验证码是"
    keywordIndex = message.find(keyword)
    codeIndex = keywordIndex+len(keyword)
    code = message[codeIndex:codeIndex+6]
    poco("CODE").set_text(code)
    touch(Template(r"tpl1582799154455.png", record_pos=(-0.006, 0.702), resolution=(1080, 2220)))

# 登录
def login_in():
    poco(text="开始").click()
    print("点击登录")
    try:
        wait(Template(r"tpl1582797826759.png", record_pos=(0.008, 0.827), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("登录不成功")
    else:
        print("登录成功")
        check_whether_WoDe()
        account_detail()
        
# 触发退出登录弹窗
def login_out():
    poco(text="退出登录").click()
    try:
        wait(Template(r"tpl1583143763302.png", record_pos=(0.005, -0.169), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("为弹窗二次确认")
    else:
        print("弹窗二次确认")
# 取消退出登录
def cancel_login_out():
    login_out()
    touch(Template(r"tpl1583143874546.png", record_pos=(0.006, 0.464), resolution=(1080, 2220)))
    try:
        wait(Template(r"tpl1583143915395.png", record_pos=(0.007, 0.419), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("当前界面非账号详情界面")
    else:
        print("已取消退出登录")
# 确定退出登录
def do_login_out():
    login_out()
    touch(Template(r"tpl1583144081107.png", record_pos=(0.008, 0.234), resolution=(1080, 2220)))
    sleep(5.0)
    try:
        wait(Template(r"tpl1583144117078.png", record_pos=(0.012, 0.399), resolution=(1080, 2220)),timeout=1.0)
    except TargetNotFoundError:
        print("退出登录异常")
    else:
        print("成功退出登录")
    
    
#---
check_whether_WoDe() # 检查当前是否在【我的】模块界面
account_detail() # 进入账号详情界面
#image() # 触发修改头像弹窗
take_picture() # 拍照上传头像
#carema_right() # 相机权限的获取
#ask_for_carema_service() # 允许使用相机权限  
#picture_right() # 相册权限的获取 
#ask_for_pictures_service() # 允许使用相册权限
#take_picture_step1() # 拍照步骤1
#take_picture_step2() # 拍照步骤2 
#take_picture_step3() # 拍照步骤3
#back_to_account_detail() #返回账号详情界面
phone_picture() # 从手机相册上传
#phone_picture_step1() # 手机相册上传步骤1
#phone_picture_step2() # 手机相册上传步骤2
#phone_picture_step3() # 手机相册上传步骤3
#phone_picture_step4() # 手机相册上传步骤4

update_nickname() # 昵称修改 
#check_nickname_page() # 校验当前界面是否为昵称修改界面  
nickname_null() # 昵称为空校验     
nickname_limit() # 昵称输入限制校验

sex() # 性别设置
set_sex_male() # 设置性别为男性
set_sex_female() # 设置性别为女性

binging_yes_or_no() # 微信绑定 
unbind() # 取消微信绑定
#unbind_success() # 确定取消绑定

delete_account() # 进入注销账号界面  
without_testcode() # 验证码非空校验
wrong_testcode() # 验证码错误校验 
overdue_testcode() # 验证码时效校验 
do_delete_account() # 确定注销账号
#get_delete_code_success() # 发送注销验证码
#get_testcode() # 获取注销验证码
whether_back_to_login_in_page() # 校验注销后是否正确跳转到登录界面 
make_PIN_ready_to_send() # 登录-验证码是否可发送校验
PIN_send() # 登录-发送验证码
get_it() # 登录-获取验证码

login_in() # 登录
#login_out() # 触发退出登录弹窗
cancel_login_out() # 取消退出登录
do_login_out() # 确定退出登录
