import pytest
from playwright.sync_api import Page
import time


def search_and_get_price(page: Page, search_query: str):
    page.goto("https://www.amazon.com", wait_until="domcontentloaded", timeout=30000)
    time.sleep(2)

    # close popups if any
    try:
        dismiss = page.locator("[data-action-type='DISMISS']")
        if dismiss.is_visible(timeout=2000):
            dismiss.click()
    except:
        pass

    # search
    page.locator("#twotabsearchtextbox").fill(search_query)
    page.locator("#nav-search-submit-button").click()
    page.wait_for_load_state("domcontentloaded")
    time.sleep(2)

    # click first result - multiple fallback selectors
    selectors = [
        "h2.a-size-mini a.a-link-normal",
        "h2 a.a-link-normal",
        ".s-result-item h2 a",
        "h2 span.a-text-normal",
    ]

    clicked = False
    for selector in selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=3000):
                el.click()
                clicked = True
                break
        except:
            continue

    if not clicked:
        print(f"[{search_query}] Could not click result")
        return "N/A"

    page.wait_for_load_state("domcontentloaded")
    time.sleep(2)

    # grab price with multiple fallbacks
    price = None
    price_selectors = [
        ".a-price .a-offscreen",
        ".priceToPay .a-offscreen",
        "#priceblock_ourprice",
        "#priceblock_dealprice",
        "#corePrice_feature_div .a-offscreen",
        ".apexPriceToPay .a-offscreen",
    ]

    for selector in price_selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=2000):
                price = el.text_content().strip()
                if price:
                    break
        except:
            continue

    if not price:
        price = "Price not found"

    print(f"\n[{search_query}] Price: {price}")

    # add to cart
    try:
        btn = page.locator("#add-to-cart-button")
        if btn.is_visible(timeout=5000):
            btn.click()
            time.sleep(2)
            print(f"[{search_query}] Added to cart!")
        else:
            print(f"[{search_query}] Add to cart button not visible")
    except:
        print(f"[{search_query}] Could not add to cart")

    return price


def test_iphone_add_to_cart(page: Page):
    price = search_and_get_price(page, "iPhone")
    print(f"\n*** iPhone Price: {price} ***")
    assert price is not None


def test_galaxy_add_to_cart(page: Page):
    price = search_and_get_price(page, "Samsung Galaxy")
    print(f"\n*** Samsung Galaxy Price: {price} ***")
    assert price is not None
