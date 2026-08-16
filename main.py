from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
import json
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("HCK HYPESQUAD", font="slant")
    print(Fore.GREEN + Style.BRIGHT + banner)
    print(Fore.YELLOW + "-" * 60)
    print(Fore.CYAN + "      Discord Hypesquad Ultimate - By Yazeed & Alpha")
    print(Fore.YELLOW + "-" * 60 + "\n")

def change_hypesquad_with_real_script(email, password, house_id):
    profile_dir = os.path.join(os.getcwd(), "temp_chrome_profile")
    if os.path.exists(profile_dir):
        shutil.rmtree(profile_dir, ignore_errors=True)
    
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    print(Fore.BLUE + "[*] Launching clean browser instance...")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://discord.com/login")
        
        print(Fore.BLUE + "[*] Entering credentials...")
        wait = WebDriverWait(driver, 25)
        
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        print(Fore.YELLOW + "[*] Please complete any CAPTCHA manually if it appears...")
        print(Fore.BLUE + "[*] Waiting for login to complete and dashboard to load...")
        
        # الانتظار حتى يدخل ديسكورد بالكامل
        wait.until(EC.url_contains("/channels/@me"))
        time.sleep(5) # إعطاء فرصة لتحميل الـ Webpack chunks بالكامل
        
        print(Fore.BLUE + "[*] Injecting your ultimate Webpack Hypesquad script...")
        
        # تحويل كودك الرهيب إلى وعد (Promise) جافاسكريبت يتم تنفيذه داخل المتصفح مباشرة
        script = f"""
        return new Promise(async (resolve, reject) => {{
            try {{
                let webpackRequire = webpackChunkdiscord_app.push([[Symbol()], {{}}, (r) => r]);
                webpackChunkdiscord_app.pop();
                let modules = webpackRequire.m;
                let cache = webpackRequire.c;
                
                function findByCode(src) {{
                    for (const [id, mod] of Object.entries(modules)) {{
                        if (mod.toString().includes(src)) {{
                            return cache[id].exports;
                        }}
                    }}
                }}
                
                function findObjectFromKey(exports, key) {{
                    if (!exports) return;
                    for (const exportKey in exports) {{
                        const obj = exports[exportKey];
                        if (obj && obj[key]) return obj;
                    }}
                }}
                
                const api = findObjectFromKey(findByCode('.set("X-Audit-Log-Reason",'), "patch");
                if (!api) {{
                    reject("API not found via Webpack!");
                    return;
                }}
                
                const res = await api.post({{
                    url: "/hypesquad/online",
                    body: {{ house_id: {house_id} }}
                }});
                
                resolve("SUCCESS");
            }} catch (e) {{
                reject(e.toString());
            }}
        }});
        """
        
        result = driver.execute_async_script(script)
        
        house_names = {1: "Bravery (Purple)", 2: "Brilliance (Red)", 3: "Balance (Green)"}
        selected_house_name = house_names.get(house_id, "Unknown")
        
        print(f"\n{Fore.GREEN}{Style.BRIGHT}[SUCCESS] Hypesquad House successfully changed to {selected_house_name} using your custom snippet! 🚀\n")
                
    except Exception as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}[ERROR] An error occurred: {e}\n")
        
    finally:
        print(Fore.YELLOW + "[*] Cleaning up and closing browser...")
        time.sleep(3)
        driver.quit()
        if os.path.exists(profile_dir):
            shutil.rmtree(profile_dir, ignore_errors=True)

if __name__ == "__main__":
    print_banner()
    user_email = input(Fore.MAGENTA + "Enter your email: " + Fore.WHITE).strip()
    user_password = input(Fore.MAGENTA + "Enter your password: " + Fore.WHITE).strip()
    
    print(Fore.CYAN + "\nSelect Hypesquad House:")
    print(Fore.MAGENTA + "  [1] Bravery (Purple)")
    print(Fore.RED + "  [2] Brilliance (Red)")
    print(Fore.GREEN + "  [3] Balance (Green)")
    
    try:
        house_choice = int(input(Fore.YELLOW + "Enter choice (1-3): " + Fore.WHITE).strip())
        if house_choice in [1, 2, 3]:
            change_hypesquad_with_real_script(user_email, user_password, house_choice)
        else:
            print(Fore.RED + "[ERROR] Invalid choice! Please select 1, 2, or 3.")
    except ValueError:
        print(Fore.RED + "[ERROR] Please enter a valid number.")
        
    input(Fore.YELLOW + "\nPress Enter to exit...")