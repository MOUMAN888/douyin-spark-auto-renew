from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime
from tqdm import tqdm
import random
import string

# -------------------------- 配置区 --------------------------

cookies_list = [] # 填入cookie
friends_list = [] # 要续火花的好友昵称
OFF_ON_Aaiqky_TEXT = True
OFF_ON_ERROR_Email = True

# 邮箱配置 [163邮箱]
my_sender = '13750209771@163.com'
my_pass = 'FGaW6AtCQKsBNvD5'
my_user = 'liusiman648@163.com'


# 你提供的元素类名
CLASS_NAMES = {
    "私信按钮": "Df5pRYjC",
    "私信面板容器": "vgonMAXk _VnLWL_m",
    "好友名称容器": "FUWX84Hq",
    "输入发送容器": "ydJNDKKc",
    "消息输入框": "H8u9D1cC",
    "发送按钮": "PygT7Ced e2e-send-msg-btn"
}
# --------------------------------------------------------------------------------

# 初始化浏览器
service = Service(executable_path=r'C:\WebDriver\edge\msedgedriver.exe')
options = webdriver.EdgeOptions()

# 防封策略
def unban_config():
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'useAutomationExtension'])
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.page_load_strategy = 'eager'

unban_config()
driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(15)

# 自定义文案函数
def AiqingGongyu_text():
    custom_quotes = [
        "今日份火花已续费，我们的故事还在继续～",
        "不管多久，火花都不会灭，因为有我呀✨",
        "续火花啦～今天也要开开心心的！",
        "专属火花续费成功，今日限定温柔已送达～",
        "你的专属小火苗，由我来守护❤️"
        "火花续费成功，愿我们的故事永不熄灭～",
    ]
    return random.choice(custom_quotes)

# 邮件发送函数
def Email_Send(ERROR_TEXT: str):
    try:
        html_content = f"""
        <html>
        <head>
            <style>
                body {{font-family: 'Microsoft YaHei', Arial, sans-serif; color: #2c3e50;}}
                .container {{max-width: 600px; margin: 0 auto; background: #fff; border-radius: 16px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);}}
                .header {{text-align: center; padding: 20px; background: linear-gradient(120deg, #3a7bd5 0%, #00d2ff 100%); color: #fff;}}
                .content {{padding: 20px; line-height: 1.6;}}
                .error {{background: #f8fafc; padding: 15px; border-radius: 8px; color: #dc2626; font-family: Consolas;}}
                .footer {{text-align: center; padding: 15px; background: #2c5282; color: #fff; font-size: 14px;}}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header"><h1>⚠️ 抖音续火花出现异常</h1></div>
                <div class="content">
                    <p>尊敬的用户，检测到抖音自动续火花出现异常，请及时处理。</p>
                    <p>错误日志：</p>
                    <div class="error">{ERROR_TEXT}</div>
                </div>
                <div class="footer"><p>抖音续火花BOT | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div>
            </div>
        </body>
        </html>
        """
        msg = MIMEText(html_content, 'html', 'utf-8')
        msg['From'] = formataddr(["抖音自动续费火花", my_sender])
        msg['To'] = formataddr(["用户", my_user])
        msg['Subject'] = f"抖音续火花异常通知 {datetime.now().strftime('%Y-%m-%d')}"
        
        server = smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
        print("✅ 异常通知邮件发送成功")
    except Exception as e:
        print(f'⚠️ 邮件发送错误: {str(e)}')

# 获取Cookies函数
def Get_Cooke():
    driver.get('https://www.douyin.com/')
    print('🕰️ 请登录抖音[保持浏览器全屏].....')
    while True:
        try:
            WebDriverWait(driver, 120, 0.5).until_not(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"登录")]'))
            )
            cookies = driver.get_cookies()
            print(f'✅ Cookie获取成功, 请复制到cookies_list变量中:\n{cookies}')
            return cookies
        except TimeoutException:
            print("⚠️ 登录超时，请重新尝试")
            continue
        except Exception as e:
            print(f"⚠️ 获取Cookie出错: {e}")
            continue

# -------------------------- 核心修复函数 --------------------------
def click_private_msg_button():
    """点击私信按钮"""
    print(f"🔍 定位私信按钮 [class={CLASS_NAMES['私信按钮']}]")
    try:
        msg_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, CLASS_NAMES['私信按钮']))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", msg_button)
        time.sleep(1)
        msg_button.click()
        print("✅ 私信按钮点击成功")
        
        # 验证私信面板打开
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CLASS_NAME, CLASS_NAMES['私信面板容器'].split()[0]))
        )
        print("✅ 私信面板已成功打开")
        return True
    except Exception as e:
        raise Exception(f"❌ 点击私信按钮失败: {str(e)}")

def find_and_click_friend(friend_name_target):
    """查找并点击单个好友"""
    print(f"🔍 查找好友 [{friend_name_target}]")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, CLASS_NAMES['好友名称容器']))
        )

        friend_container_elements = driver.find_elements(By.CLASS_NAME, CLASS_NAMES['好友名称容器'])
        print(f"📋 共找到 {len(friend_container_elements)} 个好友容器")

        friend_names = []
        target_friend_elem = None

        for idx, container_elem in enumerate(friend_container_elements):
            try:
                name = driver.execute_script(
                    "return arguments[0].innerText.trim() || arguments[0].textContent.trim();",
                    container_elem
                )

                if not name:
                    continue

                friend_names.append(name)
                print(f"✅ 容器{idx+1}：{name}")

                if name == friend_name_target:
                    target_friend_elem = container_elem
                    break

            except:
                continue

        if not target_friend_elem:
            raise Exception(f"❌ 未找到好友 [{friend_name_target}]，列表: {friend_names}")

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target_friend_elem)
        time.sleep(0.6)
        driver.execute_script("arguments[0].click();", target_friend_elem)

        print(f"✅ 已打开 [{friend_name_target}] 聊天窗口")
        time.sleep(3)
        return True

    except Exception as e:
        raise Exception(f"❌ 查找/点击好友失败: {str(e)}")

def activate_input_container():
    """激活输入发送容器"""
    print(f"🔍 定位并激活输入发送容器 [class={CLASS_NAMES['输入发送容器']}]")
    try:
        # 等待容器出现
        input_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, CLASS_NAMES['输入发送容器']))
        )
        
        # 滚动到容器可见
        driver.execute_script("arguments[0].scrollIntoView(true);", input_container)
        time.sleep(1)
        
        # 强制点击激活容器
        driver.execute_script("arguments[0].click();", input_container)
        time.sleep(2)
        
        print("✅ 输入发送容器激活成功，等待元素渲染...")
        return True
    except Exception as e:
        raise Exception(f"❌ 激活输入发送容器失败: {str(e)}")

def simulate_real_input(input_box, text):
    """核心修复：模拟真人逐字符输入 + 触发输入事件"""
    print(f"🎯 模拟真人输入文本: {text}")
    
    # 步骤1：清空输入框（触发清空事件）
    driver.execute_script("""
        const el = arguments[0];
        el.innerText = '';
        // 触发抖音需要的输入事件
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('compositionend', { bubbles: true }));
    """, input_box)
    time.sleep(1)
    
    # 步骤2：逐字符输入（模拟真人打字）
    for char in text:
        try:
            # 单个字符输入
            input_box.send_keys(char)
            # 每输入一个字符触发一次input事件
            driver.execute_script("""
                const el = arguments[0];
                el.dispatchEvent(new Event('input', { bubbles: true }));
            """, input_box)
            time.sleep(0.1)  # 模拟真人打字间隔
        except Exception as e:
            # 备用方案：JS输入单个字符
            driver.execute_script("""
                const el = arguments[0];
                el.innerText += arguments[1];
                el.dispatchEvent(new Event('input', { bubbles: true }));
            """, input_box, char)
            time.sleep(0.1)
    
    # 步骤3：最终触发确认事件
    driver.execute_script("""
        const el = arguments[0];
        el.dispatchEvent(new Event('compositionend', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
    """, input_box)
    time.sleep(2)  # 等待发送按钮渲染
    
    # 验证输入是否成功
    actual_text = driver.execute_script("return arguments[0].innerText;", input_box).strip()
    if actual_text != text:
        raise Exception(f"❌ 输入验证失败：预期[{text}]，实际[{actual_text}]")
    print(f"✅ 输入验证成功，输入框内容：{actual_text}")
    return True

def send_message_to_friend():
    activate_input_container()

    # ① 锁定真正可输入的编辑器（contenteditable）
    input_box = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//div[@contenteditable="true" and @role="textbox"]'
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", input_box)
    time.sleep(0.5)
    input_box.click()
    time.sleep(0.5)

    send_text = AiqingGongyu_text()

    # ② 输入文字（唯一正确方式）
    input_box.send_keys(send_text)

    # ③ 给 React 时间生成发送按钮
    time.sleep(1.2)

    # ④ 重新查找发送按钮（必须重新找）
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//span[contains(@class,"e2e-send-msg-btn")]'
        ))
    )

    # ⑤ 点击发送
    driver.execute_script("arguments[0].click();", send_button)

    # ⑥ 验证消息真的出现在聊天中
    WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((
            By.XPATH,
            f'//div[.//text()[contains(., "{send_text}")]]'
        ))
    )

    print(f'🎉 火花续成功 | 发送内容: {send_text} | 时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def send_message():
    try:
        print(f"\n==================== 开始执行续火花任务 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ====================")

        click_private_msg_button()

        for name in friends_list:
            print(f"\n🔥 处理好友：{name}")
            find_and_click_friend(name)
            send_message_to_friend()
            time.sleep(3)

        print(f"\n==================== 续火花任务执行完成 ====================\n")

    except Exception as e:
        error_msg = f"❌ 续火花失败: {str(e)}"
        print(error_msg)
        if OFF_ON_ERROR_Email:
            Email_Send(error_msg)


# -------------------------- 主程序 --------------------------
if __name__ == "__main__":
    try:
        driver.get('https://www.douyin.com/')

        # 加载 Cookies
        if cookies_list and len(cookies_list) > 0:
            print("📥 开始加载Cookies...")
            for cookie in tqdm(cookies_list, desc="Cookie载入中.."):
                if 'name' in cookie and 'value' in cookie:
                    driver.add_cookie(cookie)

            driver.refresh()
            time.sleep(10)

            # 验证登录
            try:
                driver.find_element(By.XPATH, '//button[contains(text(),"登录")]')
                print('⚠️ Cookie无效, 请重新获取登录后的Cookie!')
                driver.quit()
                exit()
            except NoSuchElementException:
                print('✅ Cookie有效, 登录成功!')

        else:
            cookies = Get_Cooke()
            driver.quit()
            print("\n⚠️ 请将上面获取的Cookie填入 cookies_list 后重新运行")
            exit()

        # ======= 只执行一次 =======
        print("\n🔥 执行续火花任务...")
        send_message()

    except Exception as e:
        print(f"\n❌ 程序异常: {str(e)}")
        if OFF_ON_ERROR_Email:
            Email_Send(f"程序异常: {str(e)}")

    finally:
        print("\n🔌 关闭浏览器")
        driver.quit()

    try:
        driver.get('https://www.douyin.com/')
        
        # 加载Cookies
        if cookies_list and len(cookies_list) > 0:
            print("📥 开始加载Cookies...")
            for cookie in tqdm(cookies_list, desc="Cookie载入中.."):
                if 'name' in cookie and 'value' in cookie:
                    driver.add_cookie(cookie)
            
            driver.refresh()
            time.sleep(10)
            
            # 验证登录
            try:
                driver.find_element(By.XPATH, '//button[contains(text(),"登录")]')
                print('⚠️ Cookie无效, 请重新获取登录后的Cookie!')
                driver.quit()
                exit()
            except NoSuchElementException:
                print('✅ Cookie有效, 登录成功! [请勿操作浏览器]')
        else:
            cookies = Get_Cooke()
            driver.quit()
            print("\n⚠️ 请将上面获取的Cookie填入 cookies_list 变量后重新运行程序")
            exit()
        
        # 设置定时任务
        play_time = input('🕰️ 输入每日续火花时间[默认为 22:00] :').strip()
        play_time = play_time.replace('：', ':') if play_time else '22:00'
        
        schedule.every().day.at(play_time).do(send_message)
        print(f'\n✅ 定时任务已设置 | 每日 {play_time} 执行续火花 | 好友: {friends_list}')
        print('📌 程序将持续运行，按 Ctrl+C 退出')
        
        # 立即测试
        print("\n🔍 立即执行一次续火花测试...")
        send_message()
        
        # 循环运行
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 用户手动终止程序")
    except Exception as e:
        print(f"\n❌ 程序异常: {str(e)}")
        if OFF_ON_ERROR_Email:
            Email_Send(f"程序主流程异常: {str(e)}")
    finally:
        print("\n🔌 关闭浏览器")
        driver.quit()