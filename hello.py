from config import *
from datetime import datetime
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    Browser=p.chromium.launch(headless=False)
    # context = Browser.new_context(
    #     record_video_dir="videos/",  # folder to store videos
    #     record_video_size={"width": 1280, "height": 720}  # optional
    #     )
    page=Browser.new_page()
    page.goto("https://bootswatch.com/default/")
    docs_button=page.get_by_role("button",name="Default button")
    docs_button.click()
    heading=page.get_by_role("heading",name="Heading 3").highlight()
    page.get_by_role("radio",name="Option two can be something else and selecting it will deselect option one").check()
    
    page.get_by_label("Default checkbox").check()
    page.get_by_label("Default checkbox").is_checked()
    page.wait_for_timeout(5055)
    # file_input=page.get_by_label("Default file input example")
    # file_input.set_input_files("example.txt")

    #uncheck
    #.set_checked(True)
    #oprion selector 
    #page.get_by_label("Default file input example").set_input_files("C:\Users\araj1\PycharmProjects\PythonProject\PythonProject\PythonProject\playwright\example.png")
    # with page.expect_file_chooser() as fc_info:
    #     page.get_by_label("Default file input example").set_input_files("C:\Users\araj1\PycharmProjects\PythonProject\PythonProject\PythonProject\playwright\example.png")

#C:\Users\araj1\PycharmProjects\PythonProject\PythonProject\PythonProject\playwright\example.png
    page.get_by_label("Example select").select_option("5")

    # DropDown
    # page.locator("button#btnGrouopDrop1").click()



    # option/Select Menu 


    
    #page.l
    page.get_by_role("checkbox",name="Default checkbox").check()
    page.get_by_placeholder("Enter email").type(username , delay=200)
    #page.get_by_placeholder("Password").type(password)
    page.get_by_label("Example textarea").fill("Nothing to display")
    page.wait_for_timeout(3000)

    #page.get_by_label("Email address").fill("inknkdnkqw")
    i=page.get_by_label("Valid input").first.input_value()
    print(i)
    with open("input_value.txt", "w") as f:
        f.write(i)
    page.get_by_text("Small button").click()
    page.get_by_text("mphasis classes").highlight()
    page.get_by_title("attribute").highlight()
    page.locator("css=h1").highlight()
    page.locator("button.btn-outline-succes")
    page.locator("button#btnGroupDrop1")  ## for ID 
    m= page.locator("input[readonly]").first.input_value()  # attribute and value 
    page.locator("input[value='correct value']").highlight()
    page.locator("nav.bg-dark a.nav-link.active").highlight()
    page.locator("h1:text('Navbars)")
    page.locator("xpath=//h1[@id='navbars]")
    page.locator("//input[@readonly]").highlight()
   # page.locator("//input[@value='wrong value]").highlight()
    page.wait_for_timeout(7777)


    print(m)
    page.goto("https://playwright.dev/python/")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"screenshot_{timestamp}.png"
    page.screenshot(path=filename, full_page=True)
    print(f"Screenshot saved as: {filename}")
    # page.get_by_text("Get started").click()
    # page.click("a[aria-label='GitHub repository']")
    # page.click("text=Code")
    # page.click("a[href$='main.zip']")



    # video = page.video
    # if video:
    #     path = video.path()
    #     print(f"Video saved to: {path}")

    # context.close()
    page.wait_for_timeout(666)

    #Mouse action
    # page.get_by_role("button",name="Block button").first.highlight()
    # page.click(button="right")
    # page.hover()
    

   # page.get_by_alt_text().highlight()


    # page.get_by_label("Password").highlight()
#     # page.get_by_placeholder("ENter email")
#     <a class="prc-ActionList-ActionListContent-sg9-x prc-Link-Link-85e08" tabindex="0" aria-labelledby=":rj:--label  " id=":rj:" data-turbo="false" href="/microsoft/playwright-python/archive/refs/heads/main.zip" rel="nofollow">…</a>grid
# # <span data-component="text" class="prc-Button-Label-pTQ3x">Code</span>

# <a href="https://github.com/microsoft/playwright-python" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link header-github-link" aria-label="GitHub repository">…</a>
