from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (you can see it with headless=False)
    browser = p.chromium.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Do something with the page
    page.goto("https://example.com")
    print(f"Page title: {page.title()}")

    # Close browser
    browser.close()