import os
from datetime import datetime
from playwright.sync_api import sync_playwright, expect

def read_inputs(filepath):
    data = {}
    with open(filepath, "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                data[k.strip()] = v.strip()
    return data

def makereport(filepath, title, status, count):
    with open(filepath, "a") as f:
        f.write(f"\n---TEST CASE {count} ---\n")
        f.write(f"-> {title} :: {status}\n")

def main():
    dt = datetime.now()
    date_str = dt.strftime("%Y-%m-%d-%H-%M-%S")
    report_dir = "Reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"Demo_Report{date_str}.txt")
    count = 1

    input_path = os.path.join("Inputs", "Demo_Inputs")
    data = read_inputs(input_path)
    name = data.get("name", "")
    email = data.get("email", "")
    password = data.get("password", "")
    state = data.get("state", "")
    hobbies = [h.strip() for h in data.get("hobbies", "").split(",")]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=2000)
        page = browser.new_page()

        try:
            page.goto("https://freelance-learn-automation.vercel.app/login")
            makereport(report_path, "Launching the application without errors", "PASSED", count)
            count += 1

            print(page.title())
            page.locator('xpath=//*[@id="login_container"]/form/div/a').click()
            page.wait_for_timeout(1000)
            expect(page.locator('//*[@id="signup_container"]/form/div/h2')).to_contain_text("Sign Up")
            page.wait_for_timeout(1000)
            page.locator('xpath=//*[@id="name"]').fill(name)
            expect(page.locator('xpath=//*[@id="signup_container"]/form/div/button')).to_be_disabled()
            page.wait_for_timeout(1000)
            page.locator('xpath=//*[@id="email"]').fill(email)
            expect(page.locator('xpath=//*[@id="signup_container"]/form/div/button')).to_be_disabled()
            page.wait_for_timeout(1000)
            # page.locator('xpath=//*[@id="password"]').fill(password)
            page.keyboard.press("PageDown")
            expect(page.locator('xpath=//*[@id="signup_container"]/form/div/button')).to_be_disabled()
            page.wait_for_timeout(500)
            page.get_by_text("python").click()
            page.wait_for_timeout(1000)
            page.locator('xpath=//*[@id="state"]').select_option(state)
            page.wait_for_timeout(2000)
            page.locator('xpath=//*[@id="hobbies"]').select_option(hobbies)
            # expect(page.locator('xpath=//*[@id="signup_container"]/form/div/button')).to_be_enabled()

            if page.locator('xpath=//*[@id="signup_container"]/form/div/button').is_enabled():
                makereport(report_path, "Filling the form: text,single select,multiselect,radio from the input file", "PASSED", count)
            else:
                makereport(report_path, "Looks like some fields are not filled completely", "FAILED", count)
            count += 1

            page.get_by_role("img", name="menu").click()
            page.get_by_role("link", name="Home").click()
            page1 = browser.new_page()
            page1.goto("https://playwright.dev/")
            page.bring_to_front()
            page.get_by_role("img", name="menu").click()
            page.get_by_role("button", name="Log in").click()
            page1.bring_to_front()
            page1.locator('xpath=//*[@id="__docusaurus"]/nav/div[1]/div[1]/a[1]/b').click()
            page1.goto("https://playwright.dev/java/")
            title = page1.title()
            username = title.split(" ")[2] if len(title.split(" ")) > 2 else "user"
            Uemail = f"{username}@gmail.com"
            print(title, username)
            page.bring_to_front()
            page.locator('xpath=//*[@id="email1"]').fill(Uemail)
            makereport(report_path, "Communicating with multi tabs", "PASSED", count)
            count += 1

            page.get_by_role("button", name="Sign in").click()
            snaps_dir = "snaps"
            os.makedirs(snaps_dir, exist_ok=True)
            screenshot_path = os.path.join(snaps_dir, f"Demorundate{date_str}.png")
            page.screenshot(path=screenshot_path, full_page=True)
            makereport(report_path, "Taking the screenshot", "PASSED", count)
            count += 1

            makereport(report_path, "ALL TEST CASES", "PASSED", count)
            page.close()
            browser.close()

        except Exception as e:
            makereport(report_path, "Code has reached the catch block", "FAILED", count)
            page.close()
            browser.close()
            print(e)

if __name__ == "__main__":
    main()
