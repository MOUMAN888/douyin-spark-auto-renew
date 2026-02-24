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

# cookies_list = [{'domain': '.douyin.com', 'expiry': 1768805002, 'httpOnly': False, 'name': 'home_can_add_dy_2_desktop', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%221%22'}, {'domain': '.douyin.com', 'expiry': 1773384202, 'httpOnly': False, 'name': 'bd_ticket_guard_client_data_v2', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJyZWVfcHVibGljX2tleSI6IkJCTUdrakJ6ZUwwZHBLR2NYMTFMV212RU41bnBjM09FNi9XZVlKQVhZY3JDSGpyNmZHMjVZN1o5WXBoS2Fmb2F5S2NZby9rSktYajhzb055N0R6MFVVdz0iLCJ0c19zaWduIjoidHMuMi4xYTRhMjcxOGQ3ODhjYzljNjNlOTk1Y2FhN2I3YmZmMzhlMDFmYmM0YjQzNGQ3OTI2NzQ3NWM1NDRmODNhZDdmYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJTdnh6VktoSlJnV3hGYXppNW8vOXUwVXI1NHozWk5yME5GcjIweUxkUGFnPSIsInNlY190cyI6IiNwWmFBdUJHcG9VQXVOQnZSb2p1TUJUMFFFRm1ERGU4UnBiQnBOYUdIOTgwNCtaWktHYXdNTUtRWkppQW0ifQ%3D%3D'}, {'domain': '.douyin.com', 'expiry': 1773384202, 'httpOnly': False, 'name': 'bd_ticket_guard_client_data', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQk1Ha2pCemVMMGRwS0djWDExTFdtdkVONW5wYzNPRTYvV2VZSkFYWWNyQ0hqcjZmRzI1WTdaOVlwaEthZm9heUtjWW8va0pLWGo4c29OeTdEejBVVXc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D'}, {'domain': '.douyin.com', 'expiry': 1768805000, 'httpOnly': False, 'name': 'IsDouyinActive', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': '.douyin.com', 'expiry': 1768804999, 'httpOnly': False, 'name': 'publish_badge_show_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%220%2C0%2C0%2C1768200199936%22'}, {'domain': '.douyin.com', 'expiry': 1799736200, 'httpOnly': False, 'name': 'SelfTabRedDotControl', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%5B%5D'}, {'domain': '.douyin.com', 'httpOnly': False, 'name': 'biz_trace_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '27eea0dc'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': False, 'name': '__security_server_data_status', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.douyin.com', 'expiry': 1802760158, 'httpOnly': False, 'name': 'UIFID_TEMP', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'c170a667ed3e6ea26418b502c576a64081038b1cd64e171a772bc7b8be1984b2f1d4e6ec3668cef29bf1f3b26b013f1695834615392ced30bc70cb0f826cd9eaae5acf68fbc4a0c9e939d18915e681b0'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_crypt_sdk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'bd0098d1-41de-aedf'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'is_staff_user', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'false'}, {'domain': '.douyin.com', 'expiry': 1799304199, 'httpOnly': True, 'name': 'ttwid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1%7Clzlrq8BE-gvemcSzXslSN75jIJLlORJfCnq_442bjCI%7C1768200166%7C9ef97ea06087e5ab5d2e11ccd0e389cbf97e5d23fd999802199e519c4cfcb0f5'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'sessionid_ss', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'c3a971c3ef963919b41af55db7403a6b'}, {'domain': 'www.douyin.com', 'httpOnly': False, 'name': '', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'douyin.com'}, {'domain': '.douyin.com', 'expiry': 1768200466, 'httpOnly': False, 'name': 'gulu_source_res', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJwX2luIjoiYzA4YTI4ZWE0Nzk4ZWI3NDA2ZjUxYzE0NWE1OWVhZWI3OTdlZDE5OGVkMWQ3MTZkYjQyYTkzYzRlMDdlMjgzMyJ9'}, {'domain': '.douyin.com', 'expiry': 1773384198, 'httpOnly': True, 'name': 'passport_mfa_token', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CjVi%2FtifAZF7NLrSMPecI41di%2BdoxweupMYEMs1hj8iMzIPp9qkYBq08ebjkYA7T6L%2FtQYYjeRpKCjwAAAAAAAAAAAAAT%2FEnvcPj3UmcmKXG99BOnuonTVo4hxe%2FrqGuhMZetYbV4l6DCchXnt6qSjBM1OepCk0QrNqGDhj2sdFsIAIiAQM75pvH'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'sid_tt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'c3a971c3ef963919b41af55db7403a6b'}, {'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'architecture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'amd64'}, {'domain': '.douyin.com', 'expiry': 1768804963, 'httpOnly': False, 'name': 'volume_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'uid_tt_ss', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'b4a6be667d1e4ebd336c540dd3a5839a'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'uid_tt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'b4a6be667d1e4ebd336c540dd3a5839a'}, {'domain': '.douyin.com', 'expiry': 1802760199, 'httpOnly': False, 'name': 'passport_assist_user', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Cj1vpmKwLhMgrVD3XnpB4fnO_aL5DBDbBGkaKSTmEtxwbYufgAxeAzmodydSY5GeATIH-mGENT6R0128770-GkoKPAAAAAAAAAAAAABP8RSXHAjYMeAhORItcafznikxMnj7AshwaYfku0aW_4KqLowKQr1p9mPBjeWmR_9sNhCj2IYOGImv1lQgASIBA7pyA2g%3D'}, {'domain': '.douyin.com', 'expiry': 1768805001, 'httpOnly': False, 'name': 'FOLLOW_LIVE_POINT_INFO', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%22MS4wLjABAAAAPkCMbeS_Tg9-P-CGR0QPDPhHDlg3lsBckrxaKTCIwj8%2F1768233600000%2F0%2F1768200201158%2F0%22'}, {'domain': '.douyin.com', 'expiry': 1799736199, 'httpOnly': True, 'name': 'odin_tt', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '940500816dd6ea0b64e27741df9707d6c49778fd3af508f4e0ad9f80f0805f77a5bafbbb5c0c41f426a7e173e369d10a1316314bc7140c7be651f43c41474427'}, {'domain': 'www.douyin.com', 'expiry': 1768805000, 'httpOnly': False, 'name': 'dy_sheight', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1067'}, {'domain': '.douyin.com', 'expiry': 1802760199, 'httpOnly': False, 'name': 'login_time', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1768200199374'}, {'domain': '.douyin.com', 'expiry': 1799736198, 'httpOnly': True, 'name': 'd_ticket', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'e51a91563354a3b6a33817f63fac52ed2182f'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': False, 'name': '_bd_ticket_crypt_cookie', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ef04c87da6e1f7169e39c0ded32d719a'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'session_tlb_tag', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'sttt%7C16%7Cw6lxw--WORm0GvVdt0A6a__________QpjruAKn9P95SJ0hgHif9ZaaS8GjfMY0yHXliLCwgxWY%3D'}, {'domain': 'www.douyin.com', 'expiry': 1802760166, 'httpOnly': False, 'name': 'UIFID', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'c170a667ed3e6ea26418b502c576a64081038b1cd64e171a772bc7b8be1984b2f1d4e6ec3668cef29bf1f3b26b013f160b8091faf2a903e4d08ecd8e718cb9809ce23cf6f30a397031b2cf9faae058f0086ee2d3acf85784b694276395d53ab596bfa204bdac5030c71e38e2be354a0a246dbd16a48ba92107a5ee6a101804e244d3b37b28fa3d455500f51fd0c34f3d194eed06b12e8182cb13838e8d8726f1'}, {'domain': '.douyin.com', 'expiry': 1768200406, 'httpOnly': False, 'name': 'passport_auth_mix_state', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'e29lhpl8z0qtkebjstoyyygw2ob706yaaujq2go6x8q8rf6w'}, {'domain': '.douyin.com', 'expiry': 1799304199, 'httpOnly': True, 'name': 'sid_guard', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'c3a971c3ef963919b41af55db7403a6b%7C1768200200%7C5184000%7CFri%2C+13-Mar-2026+06%3A43%3A20+GMT'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_cert_key', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8b7c1a89-4519-9586'}, {'domain': '.douyin.com', 'expiry': 1802760199, 'httpOnly': False, 'name': 'enter_pc_once', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1'}, {'domain': '.douyin.com', 'expiry': 1773384165, 'httpOnly': False, 'name': 'passport_csrf_token_default', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8cc587d6aba0e79f62a19a3274951152'}, {'domain': '.douyin.com', 'expiry': 1768200466, 'httpOnly': False, 'name': 'bit_env', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'heurG09Y4fgVNw-vBgCtQQI8GXua8p0-ayNbl0yKQAiCPVwydmMSX9qGzZIV9lmEGMX96wmNwn-OzZCqCF-gp-79tw8q6PgcDqofykeF_e9ka5qpqVo5NM4m3QESmELtwOFAL4XIKcNRQEo9-EKtZ4GcJryykzR-7YKMScC8N8RYBOg81Ntu02t_GGGVWu2s2glIN71rYuyq_6qkGigBbV92X4kJdE8Fg2LK6s1YcoWIh8VxT8wjr1mePamJYx-WWDWN-XcmaO5LdFHF1yX1d5h_rI8pqDmmuXjFatkGUO2reh4tW-wN6kciX0Oe4lQ8P8FXrMIeACCacjQvPpLTJ5hj7ysoGyL9GyqGHdHRJHvaipeQone1Mgnuq8P5V27nzCdN9c6S8JH17dJZof3WEhXBGWGvEtF3r2VRTcf4TjUvvZgp_gFSOhznUfFq6CTt7GGBmTh-p-sttjCsZJh3j6AbpfhQh0rM4Cy1VRuh-hlQ_0W_WQ-qp2RVK4bVmz-CuJOiBc7xcZxRkZvR52ndncB_IjhOZkd37FiZ8lecGq0%3D'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'ssid_ucp_v1', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.0.0-KDY1YmViYjI2ZjU4Y2M2MTMzNGNmYTVkMGE2ODQ5NDU2OGE0OTAzMTUKHwi4juzm_AIQiLCSywYY7zEgDDDbg_raBTgHQPQHSAQaAmxxIiBjM2E5NzFjM2VmOTYzOTE5YjQxYWY1NWRiNzQwM2E2Yg'}, {'domain': '.douyin.com', 'expiry': 1768805000, 'httpOnly': False, 'name': 'stream_recommend_feed_params', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.3%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A300%7D%22'}, {'domain': 'www.douyin.com', 'expiry': 1802760162, 'httpOnly': False, 'name': 'fpk1', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'U2FsdGVkX19d7ZakpmBzdoSqoJKX8q3c5CiVVuzwpP2MVzBYaCqIEVwb3edjpgvu2SnQFMDyVIDpbKsBpxVOkA=='}, {'domain': 'www.douyin.com', 'expiry': 1768201957, 'httpOnly': False, 'name': '__ac_nonce', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0696497de0021493595c2'}, {'domain': 'www.douyin.com', 'expiry': 1802760162, 'httpOnly': False, 'name': 'fpk2', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '15c1c3073e5c3cda0308b87e66c0c1e4'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'c3a971c3ef963919b41af55db7403a6b'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_sign_data_key_web_protect', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1ace9e38-4975-846a'}, {'domain': '.douyin.com', 'expiry': 1768805000, 'httpOnly': False, 'name': 'stream_player_status_params', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22'}, {'domain': '.douyin.com', 'expiry': 1773384165, 'httpOnly': False, 'name': 'passport_csrf_token', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '8cc587d6aba0e79f62a19a3274951152'}, {'domain': 'www.douyin.com', 'expiry': 1768805000, 'httpOnly': False, 'name': 'dy_swidth', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1707'}, {'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'device_web_cpu_core', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '16'}, {'domain': '.douyin.com', 'expiry': 1773384199, 'httpOnly': True, 'name': 'sid_ucp_v1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1.0.0-KDY1YmViYjI2ZjU4Y2M2MTMzNGNmYTVkMGE2ODQ5NDU2OGE0OTAzMTUKHwi4juzm_AIQiLCSywYY7zEgDDDbg_raBTgHQPQHSAQaAmxxIiBjM2E5NzFjM2VmOTYzOTE5YjQxYWY1NWRiNzQwM2E2Yg'}, {'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'device_web_memory_size', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8'}, {'domain': 'www.douyin.com', 'expiry': 1773384159, 'httpOnly': False, 'name': 's_v_web_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'verify_mkaspyvs_wn7CMgqo_B6Ip_4WsD_8o1l_ejgz1L2bqyK2'}, {'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'x-web-secsdk-uid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '5271df3f-3979-4467-9d4b-3196978ba03a'}, {'domain': '.douyin.com', 'expiry': 1768200466, 'httpOnly': False, 'name': 'sdk_source_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5927766069606b6c7068375927582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273230373333343535373d333234272927676c715a75776a716a666a69273f2763646976602778'}, {'domain': '.douyin.com', 'expiry': 1778568199, 'httpOnly': True, 'name': 'n_mh', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'kVTYQ5NfP0mUpK2yBEmoSFw4lcVlqR2z-1xjleEcH2Q'}, {'domain': '.douyin.com', 'expiry': 1768804961, 'httpOnly': False, 'name': 'strategyABtestKey', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%221768200161.274%22'}, {'domain': 'www.douyin.com', 'expiry': 1799736157, 'httpOnly': False, 'name': '__ac_signature', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '_02B4Z6wo00f01.yymnAAAIDCcfLj45guuOv8kp7AAJZRd2'}, {'domain': '.douyin.com', 'expiry': 1773384202, 'httpOnly': False, 'name': 'bd_ticket_guard_client_web_domain', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2'}] # 替换为你的抖音cookies
cookies_list = [
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_crypt_sdk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fa6a4721-4690-9429'},
{'domain': 'www.douyin.com', 'httpOnly': False, 'name': '', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'douyin.com'},
{'domain': '.douyin.com', 'expiry': 1802959381, 'httpOnly': True, 'name': 'sid_guard', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8d6a59be390006cab6199ea4b7c5a495%7C1771855382%7C5184000%7CFri%2C+24-Apr-2026+14%3A03%3A02+GMT'},
{'domain': '.douyin.com', 'expiry': 1806415381, 'httpOnly': False, 'name': 'passport_assist_user', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Cj1t1w4QaTKgCWB4cxHP6A8x1gYwPkK9QOgMwOh3NDiTPRyej5xYb12e4iTcogFhTtsIoc6_U-Ur8332uNC3GkoKPAAAAAAAAAAAAABQG5T7EH22_OBX4VSdlJ5xfqIr3Ic1YMMPLBabOTwg6PsQv9nnmL0ElLJW2m-g1h2bCxDUs4oOGImv1lQgASIBA6GMS1E%3D'},
{'domain': '.douyin.com', 'expiry': 1806415387, 'httpOnly': False, 'name': 'enter_pc_once', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1'},
{'domain': '.douyin.com', 'expiry': 1782223381, 'httpOnly': True, 'name': 'n_mh', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'kVTYQ5NfP0mUpK2yBEmoSFw4lcVlqR2z-1xjleEcH2Q'},
{'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'x-web-secsdk-uid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '11994aa4-f429-467a-b603-122aea47767e'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'session_tlb_tag', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'sttt%7C4%7CjWpZvjkABsq2GZ6kt8Wklf________-lCqE5IvqyKccvoc94Os7Aznyo4W8lXjzRmDqcRjsoRx0%3D'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'is_staff_user', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'false'},
{'domain': 'www.douyin.com', 'expiry': 1772460188, 'httpOnly': False, 'name': 'dy_sheight', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1067'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': False, 'name': '__security_server_data_status', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
{'domain': '.douyin.com', 'expiry': 1806415381, 'httpOnly': False, 'name': 'UIFID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '48df845ec17e24d3e136cf9cb5f33ae5ff0d6a60613b8e70d731bae9b37d4b93b54154fc95f1e9a0631666c7f00433b51033a0fb2c742a3d7c71b891745fb77d77517acff4a4e701e44783071a2ee23de182af68caeb3904b662359f658bc408d661ed3a08e500a219970cb81931660d67e91c851b0b4994fabf37b9d16a2c381d3cb842e464917985d177c48cbc1d4c5abb955275312c6618e0fc25d30639a5'},
{'domain': 'www.douyin.com', 'expiry': 1806415350, 'httpOnly': False, 'name': 'fpk2', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1077871f5a238c0cd9e1f788c8174192'},
{'domain': '.douyin.com', 'expiry': 1772460189, 'httpOnly': False, 'name': 'publish_badge_show_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%220%2C0%2C0%2C1771855389296%22'},
{'domain': '.douyin.com', 'expiry': 1777039351, 'httpOnly': False, 'name': 'passport_csrf_token_default', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b302be47db70ebeb9d5c85dc1cf10d50'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_sign_data_key_web_protect', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '68dc29de-44ce-8fbe'},
{'domain': '.douyin.com', 'expiry': 1777039389, 'httpOnly': False, 'name': 'bd_ticket_guard_client_data_v2', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJyZWVfcHVibGljX2tleSI6IkJLTzYzOFhFc3FBZmw2Vkw3eit3VDhIcU91Q1VSd2crczhrL0R0aFBPblpEcVpPQzJWSmNpTjh4bE95Mmc1cVlTV0xYdVJKT3Y4WEYwYWJ1bFdOTkc3OD0iLCJ0c19zaWduIjoidHMuMi41MDQ0MjhjZjIxZjFlODMxYjdjMjUwNTkwN2I4ODEyN2RlMjE0ZjVjOThhYzk4MDViNzlkN2I3N2I5MWQxMTE5YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiIzNUxHQ2ZLMEpob3V0V1JpNDYvN2dKTDBTZ2hTZkF2bXJjTXovTFVlNTRFPSIsInNlY190cyI6IiNLekllYjBicEFoT0MxdFNPMmFNbHNPcFVZM0hGRGQ0dkRGZVJXamwySDdmaTFoanNBTUM4MmxmM1FqaTMifQ%3D%3D'},
{'domain': '.douyin.com', 'expiry': 1803391390, 'httpOnly': True, 'name': 'odin_tt', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'f4d266d0b27914c33c7b7aa943470909215f415091ed09218728393a1e41dc3395904d87d103634b1d7e7b4f384a19da8845cbad5e377533827ef08e79657e10'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': False, 'name': '_bd_ticket_crypt_cookie', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '57467d2b582a28614194481f2344a9ff'},
{'domain': 'www.douyin.com', 'expiry': 1771857143, 'httpOnly': False, 'name': '__ac_nonce', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0699c5df000abd08fb324'},
{'domain': '.douyin.com', 'expiry': 1771855652, 'httpOnly': False, 'name': 'sdk_source_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5927766069606b6c706837592729592772606761776c7360775927582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2732363437303630303d34323234272927676c715a75776a716a666a69273f2763646976602778'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'sid_tt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8d6a59be390006cab6199ea4b7c5a495'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8d6a59be390006cab6199ea4b7c5a495'},
{'domain': '.douyin.com', 'expiry': 1772460188, 'httpOnly': False, 'name': 'stream_recommend_feed_params', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22'},
{'domain': '.douyin.com', 'expiry': 1777039380, 'httpOnly': True, 'name': 'passport_mfa_token', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CjVLiGJ49k%2FL9UUVc01p4yzgwWUFZNExsS87dSPsRPCCw5V6QodssbOKYFZ2i71pFDC%2Bx%2Bj79RpKCjwAAAAAAAAAAAAAUBvj7FO%2FUIEzyf77pUfbL3KLQYWMqdT2WqpWJVnFJGqJMRQhyMDrkPibK80t9gkw%2FJkQobWKDhj2sdFsIAIiAQO%2FCuX1'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'sid_ucp_v1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1.0.0-KGUxMmM5MWFlOTYzNDQ1MzA0ZmQwYzNiMjg4Y2U2ZmVmNmZjZWMxZWUKHwi4juzm_AIQlrzxzAYY7zEgDDDbg_raBTgHQPQHSAQaAmxmIiA4ZDZhNTliZTM5MDAwNmNhYjYxOTllYTRiN2M1YTQ5NQ'},
{'domain': '.douyin.com', 'expiry': 1803391380, 'httpOnly': True, 'name': 'd_ticket', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c7672a5c489a9f542dfe0a96adb3fdc84ef1b'},
{'domain': '.douyin.com', 'expiry': 1772460181, 'httpOnly': False, 'name': 'DiscoverFeedExposedAd', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%7D'},
{'domain': 'www.douyin.com', 'expiry': 1772460188, 'httpOnly': False, 'name': 'dy_swidth', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1707'},
{'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'device_web_cpu_core', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '16'},
{'domain': '.douyin.com', 'expiry': 1772460189, 'httpOnly': False, 'name': 'home_can_add_dy_2_desktop', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%221%22'},
{'domain': '.douyin.com', 'expiry': 1777039389, 'httpOnly': False, 'name': 'bd_ticket_guard_client_web_domain', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': False, 'name': '__security_mc_1_s_sdk_cert_key', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b23997b1-4090-ac7d'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'uid_tt_ss', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'f8f3e3bf01349ea84e80c9d2bef9e89f'},
{'domain': '.douyin.com', 'expiry': 1772460188, 'httpOnly': False, 'name': 'FOLLOW_LIVE_POINT_INFO', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%22MS4wLjABAAAAPkCMbeS_Tg9-P-CGR0QPDPhHDlg3lsBckrxaKTCIwj8%2F1771862400000%2F0%2F1771855383962%2F0%22'},
{'domain': '.douyin.com', 'expiry': 1806415344, 'httpOnly': False, 'name': 'UIFID_TEMP', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '48df845ec17e24d3e136cf9cb5f33ae5ff0d6a60613b8e70d731bae9b37d4b93b54154fc95f1e9a0631666c7f00433b506c73a509092698c78ae05450ae92c373e668ee3346ec73926af1832bc23bbca'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'uid_tt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'f8f3e3bf01349ea84e80c9d2bef9e89f'},
{'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'architecture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'amd64'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'ssid_ucp_v1', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.0.0-KGUxMmM5MWFlOTYzNDQ1MzA0ZmQwYzNiMjg4Y2U2ZmVmNmZjZWMxZWUKHwi4juzm_AIQlrzxzAYY7zEgDDDbg_raBTgHQPQHSAQaAmxmIiA4ZDZhNTliZTM5MDAwNmNhYjYxOTllYTRiN2M1YTQ5NQ'},
{'domain': '.douyin.com', 'expiry': 1777039389, 'httpOnly': False, 'name': 'bd_ticket_guard_client_data', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS082MzhYRXNxQWZsNlZMN3ord1Q4SHFPdUNVUndnK3M4ay9EdGhQT25aRHFaT0MyVkpjaU44eGxPeTJnNXFZU1dMWHVSSk92OFhGMGFidWxXTk5HNzg9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D'},
{'domain': 'www.douyin.com', 'expiry': 1806415350, 'httpOnly': False, 'name': 'fpk1', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'U2FsdGVkX1+0m3bYtQFzdpLHNayYvzoqgQNM8FuIX82xOnmJZZuom+N+fTUC4Z+AS3P9I1Lvr/Enp/B7oCvGqA=='},
{'domain': '.douyin.com', 'expiry': 1777039351, 'httpOnly': False, 'name': 'passport_csrf_token', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'b302be47db70ebeb9d5c85dc1cf10d50'},
{'domain': '.douyin.com', 'expiry': 1802959387, 'httpOnly': True, 'name': 'ttwid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1%7CsohqWhcwEuGiZv1Y7dzHT90hzm-rIcoED04Ra6awuQ0%7C1771855353%7Ca5c503b6591c74399b1ec16a3801ce1aa15d288c307dd1de447697e54d828b51'},
{'domain': 'www.douyin.com', 'expiry': 1803391343, 'httpOnly': False, 'name': '__ac_signature', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '_02B4Z6wo00f010GZEWgAAIDCzNlo-u1VJttBuTXAALoF9c'},
{'domain': '.douyin.com', 'expiry': 1772460188, 'httpOnly': False, 'name': 'IsDouyinActive', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'},
{'domain': '.douyin.com', 'expiry': 1777039381, 'httpOnly': True, 'name': 'sessionid_ss', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '8d6a59be390006cab6199ea4b7c5a495'},
{'domain': 'www.douyin.com', 'expiry': 1777039345, 'httpOnly': False, 'name': 's_v_web_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'verify_mlz8xafg_fT3ytEqU_2CeY_46MN_AxNa_tubrG0gmHPJ9'},
{'domain': '.douyin.com', 'expiry': 1771855652, 'httpOnly': False, 'name': 'gulu_source_res', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJwX2luIjoiMTFjNzA1YmRiZTExNmNmYjhiODQyNDUwNTVmMmJiZTEzYjg1MGIyMmUwYzcyMzk0MGM5NzVkNzY0YWFlNDU0YyJ9'},
{'domain': '.douyin.com', 'expiry': 1771855592, 'httpOnly': False, 'name': 'passport_auth_mix_state', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '4g74q51al1uy63zy5rttcg6a2aaoouatrmgf1fa7jx919dx1'},
{'domain': '.douyin.com', 'httpOnly': False, 'name': 'biz_trace_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'f0152e1d'},
{'domain': '.douyin.com', 'expiry': 1771855652, 'httpOnly': False, 'name': 'bit_env', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '4f2Ph06GYF-VMLctT-nLwXj-QBY3eiFJvSyFAQhRy1p1Y80fa07O_MeGoQN-6TZq72fZQMt3o-UaQfMfyTa9sX4QaVD7tFNzIL53Umfx9iqkNzjkWnnrfhviU5j26ICtbdzGiBCayOMd7cJsJ0MeNkb7NHWJG8wiBNpHVxhXXE8pMm_zWcMM2VkHULmk-rD4_0HrLuKuCUHfeMMo0Uaqkm4dlJ_YXU6c3KnjGz0Nd4vFI4zYjUfn4F0NtynVcuSuiT8O4orw2etD_8cxDlZzLE-sDlOXb_hMuJiChW_WEvXSg8b9eFzxfOA3myDNewtGW6ue3bwmoW6WQUJTe4o5PoiXBphpK8lvMh6-Wp1H_cd6jV0Ljn_8P_253IRJgUdF4RwIFZ3LZ8LZ9X9lVpqXNpZ1xhliTm13KLdBy6KaHRIjQipo0zanMr_c-mJOkZmqs9Pmh2SuAsBYAkQkxclvgJdPb8ewqZsgmGRuI4mU2AFMExZ63ljFE0zXYoln_4quMNEkMBfVTA1AsCv9INeUBzTMKFJcJOqF5zpVdC07a5k%3D'},
{'domain': '.douyin.com', 'expiry': 1806415381, 'httpOnly': False, 'name': 'login_time', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1771855381169'},
{'domain': '.douyin.com', 'expiry': 1772460150, 'httpOnly': False, 'name': 'strategyABtestKey', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%221771855350.442%22'},
{'domain': '.douyin.com', 'expiry': 1803391388, 'httpOnly': False, 'name': 'SelfTabRedDotControl', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%5B%5D'},
{'domain': 'www.douyin.com', 'httpOnly': False, 'name': 'device_web_memory_size', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8'}
]
friends_list = ["小利", "阿树", "猪猪三","小荔枝","好好学习小组"] # 要续火花的好友昵称
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