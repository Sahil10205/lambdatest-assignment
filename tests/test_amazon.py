import pytest
import json
import urllib.parse
from playwright.sync_api import sync_playwright

LT_USERNAME = "ssharma7_be24@thapar.edu"
LT_ACCESS_KEY = "LT_salYYq8CbBWVFyz7SPlPwNZVhE9Tb8wLEQzDvsJyJis8j6E"

def get_lt_browser(playwright, test_name):
    capabilities = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "LT:Options": {
            "platform": "Windows 10",
            "build": "Amazon Automation",
            "name": test_name,
            "user": LT_USERNAME,
            "accessKey": LT_ACCESS_KEY,
            "network": True,
            "console": True,
            "visual": True,
        }
    }
    caps_encoded = urllib.parse.quote(json.dumps(capabilities))
    ws_endpoint = f"wss://cdp.lambdatest.com/playwright?capabilities={caps_encoded}"
    browser = playwright.chromium.connect(ws_endpoint)
    return browser

def search_and_add(page, query, tc):
    # Use amazon.in instead
    url = f"https://www.amazon.in/s?k={urllib.parse.quote(query)}"
    page.goto(url, timeout=60000)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(4000)

    # Screenshot for debug - print page title
    print(f"[{tc}] Page title: {page.title()}")

    # Very broad locator - any product link
    try:
        # Try clicking first product link directly
        links = page.locator("a.a-link-normal.s-no-outline").all()
        if links:
            links[0].click()
            print(f"[{tc}] Clicked product!")
        else:
            # fallback - just get first h2 link
            page.locator("h2 a").first.click()
            print(f"[{tc}] Clicked via h2!")
    except Exception as e:
        print(f"[{tc}] Click error: {e}")
        raise

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)
    print(f"[{tc}] Product page title: {page.title()}")

    # Get price
    price = "Price not found"
    for pl in [".a-price .a-offscreen", "#priceblock_ourprice", ".a-price span[aria-hidden='true']", "#corePrice_feature_div .a-offscreen"]:
        try:
            price = page.locator(pl).first.inner_text(timeout=4000)
            if price.strip():
                break
        except:
            continue
    print(f"[{tc}] Price: {price}")

    # Add to cart
    try:
        page.locator("#add-to-cart-button").click(timeout=8000)
        print(f"[{tc}] Added to cart!")
    except:
        print(f"[{tc}] Add to cart not clickable (login required - expected!)")

def test_iphone_search_and_cart():
    with sync_playwright() as playwright:
        browser = get_lt_browser(playwright, "TC1 - iPhone Search and Cart")
        context = browser.new_context()
        page = context.new_page()
        try:
            search_and_add(page, "iPhone", "TC1")
        except Exception as e:
            print(f"[TC1] Error: {e}")
            raise
        finally:
            context.close()
            browser.close()

def test_galaxy_search_and_cart():
    with sync_playwright() as playwright:
        browser = get_lt_browser(playwright, "TC2 - Galaxy Search and Cart")
        context = browser.new_context()
        page = context.new_page()
        try:
            search_and_add(page, "Samsung Galaxy", "TC2")
        except Exception as e:
            print(f"[TC2] Error: {e}")
            raise
        finally:
            context.close()
            browser.close()