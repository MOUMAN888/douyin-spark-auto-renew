from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

def get_douyin_cookies():

    # 1. 配置浏览器选项
    edge_options = Options()
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option("useAutomationExtension", False)
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--new-window")
    # 最大化窗口
    edge_options.add_argument("--start-maximized")

    # 2. 指定驱动路径（需要修改成自己的浏览器驱动路径）
    driver_path = r'C:\WebDriver\edge\msedgedriver.exe'
    service = Service(executable_path=driver_path)

    # 3. 启动浏览器
    try:
        driver = webdriver.Edge(service=service, options=edge_options)
    except Exception as e:
        print(f"❌ 浏览器启动失败：{e}")
        print("🔍 排查方向：驱动路径/版本是否匹配、是否关闭所有Edge窗口")
        return None

    driver.implicitly_wait(20)  # 延长等待时间到20秒

    try:
        # 4. 打开抖音网页版（强制跳转到主页，避免登录页跳转问题）
        driver.get("https://www.douyin.com/")
        print("="*60)
        print("✅ 已打开抖音主页，请完成扫码登录后，手动按Enter键继续！")
        print("📢 操作步骤：打开抖音APP → 扫一扫 → 扫描网页二维码 → 登录成功后按Enter")
        print("="*60)
        
        input("👉 登录成功后，请按下Enter键提取Cookie...")

        # 5. 强制刷新页面
        driver.refresh()
        time.sleep(3)

        # 6. 提取Cookie
        cookies = driver.get_cookies()
        if not cookies:
            print("❌ 未提取到任何Cookie！可能是登录未成功，或抖音限制了Cookie获取")
            return None

        # 7. 筛选出抖音核心Cookie并存入列表
        douyin_cookies_list = []  # 初始化空列表用于存储抖音Cookie
        for cookie in cookies:
            if 'douyin.com' in cookie.get('domain', ''):
                douyin_cookies_list.append(cookie)  # 将符合条件的Cookie添加到列表
        
        # 8. 打印整个Cookie列表
        print(f"\n🎉 成功提取到 {len(douyin_cookies_list)} 个抖音核心Cookie（完整列表）：")
        print("-"*60)
        print(douyin_cookies_list)  # 打印整个列表

        # 9. 打印可直接使用的Cookie字符串
        print("\n📌 可直接复制到请求头的Cookie字符串：")
        print("-"*60)
        cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in douyin_cookies_list])
        print(cookie_str)

        return douyin_cookies_list

    except Exception as e:
        print(f"\n❌ 程序异常：{str(e)}")
        return None

    finally:
        # 保留浏览器窗口，方便你验证
        print("\n💡 浏览器窗口已保留，你可手动验证登录状态")
        # driver.quit()  # 如需自动关闭，取消注释

if __name__ == "__main__":
    # 运行前提醒清理进程
    print("⚠️  第一步：请确保已关闭所有Edge浏览器窗口！")
    input("确认关闭后，按下Enter键启动程序...")
    get_douyin_cookies()