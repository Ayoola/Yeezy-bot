from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, os, json, pyperclip
import userinfo as u

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
product_link = "https://yeezysupply.com/"

def password_up():
    driver.get('http://yeezysupply.com/')
    try:
        driver.find_element_by_xpath("//input[@class='NL__field NL__email js-email']")
        print ("password page is up")
        os.system('say "password page is up"')
        time.sleep(5)
        password_up()
    except NoSuchElementException:
        print ("Alert! no password page.")
        os.system('say "buying yeezy now"')
        buy_yeezy()


def buy_yeezy():
    driver.get(product_link)

    try:
        assert "YEEZY" in driver.title
        os.system('say "Yeezy page confirmed"')
    except AssertionError:
        print ("attention: check link")

    #select Size
    try:
        size_dropdown = Select(driver.find_element_by_xpath("//select[@class='PI__select PI__input js-select js-select-SIZE js-select-SIZE-static']"))
        os.system('say "Selecting size"')
        size_dropdown.select_by_visible_text("7")
    except NoSuchElementException:
        os.system('say "Alert! unable to select a size"')
        input("Select size and press Enter")


    #click purchase
    purchase_button = driver.find_element_by_xpath("//input[@class='K__button']")
    purchase_button.click()

    #Wait one sec to make sure add to cart is successful
    time.sleep(1)

    #driver to cart page
    driver.forward()

    #click checkout
    checkout_button = driver.find_element_by_xpath("//input[@class='K__button CA__button-checkout']")
    checkout_button.click()

    #driver to checkout page
    driver.forward()

    #input info
    email = driver.find_element_by_id("checkout_email")
    email.send_keys(u.email)

    first_name = driver.find_element_by_id("checkout_shipping_address_first_name")
    first_name.send_keys(u.first_name)

    last_name = driver.find_element_by_id("checkout_shipping_address_last_name")
    last_name.send_keys(u.last_name)

    address = driver.find_element_by_id("checkout_shipping_address_address1")
    address.send_keys(u.shipping_address_1)

    apt_suite = driver.find_element_by_id("checkout_shipping_address_address2")
    apt_suite.send_keys(u.shipping_apt_suite)

    city = driver.find_element_by_id("checkout_shipping_address_city")
    city.send_keys(u.shipping_city)

    #country_dropdown = Select(driver.find_element_by_xpath("//select[@id='checkout_shipping_address_country']"))
    #country_dropdown.select_by_visible_text(u.shipping_country)
    country_dropdown = driver.find_element_by_xpath("//select[@id='checkout_shipping_address_country']")
    country_dropdown.send_keys(u.shipping_country)

    #state_dropdown = Select(driver.find_element_by_xpath("//select[@id='checkout_shipping_address_province']"))
    #state_dropdown.select_by_visible_text(u.shipping_state)
    state_dropdown = driver.find_element_by_xpath("//select[@id='checkout_shipping_address_province']")
    state_dropdown.send_keys(u.shipping_state)

    zip_code = driver.find_element_by_id("checkout_shipping_address_zip")
    zip_code.send_keys(u.shipping_zip)

    phone = driver.find_element_by_id("checkout_shipping_address_phone")
    phone.send_keys(u.phone_number)

    #check box ALL SALES FINAL NO RETURNS OR MODIFICATIONS
    checkbox_final = driver.find_element_by_xpath("//input[@id='salesFinal']")
    checkbox_final.click()

    #solve captcha manually
    try:
        driver.find_element_by_xpath("//div[@id='g-recaptcha']/div/div")
        print ("google recaptcha detected")
        os.system('say "Warning! Captcha box detected."')
        input("Solve Captcha and press Enter")
    except NoSuchElementException:
        print ("no google recaptcha detected")
        os.system('say "no captcha box detected."')

    #click continue to shipping
    continue_to_shipping_button = driver.find_element_by_css_selector("button.step__footer__continue-btn.btn")
    continue_to_shipping_button.click()

    #driver to shipping page
    driver.forward()

    #check box ground shipping
    checkbox_ground_shipping = driver.find_element_by_xpath("//input[@id='checkout_shipping_rate_id_shopify-standard20ground20shipping-2000']")
    checkbox_ground_shipping.click()

    #click continue to payment info
    continue_to_payment_info_button = driver.find_element_by_css_selector("button.step__footer__continue-btn")
    continue_to_payment_info_button.click()

    #driver to payment info page
    driver.forward()

    #check box same as shipping address
    checkbox_same_as_shipping = driver.find_element_by_xpath("//input[@id='checkout_different_billing_address_false']")
    checkbox_same_as_shipping.click()

    # input info
#    card_number = driver.find_element_by_id("number")
#    card_number.send_keys(u.card_number)

#    name_on_card = driver.find_element_by_id("name")
#    name_on_card.send_keys(u.name_on_card)

#    card_expiry = driver.find_element_by_id("expiry")
#    card_expiry.sendkeys(u.card_exp_month + u.card_exp_year)

#    cvv = driver.find_element_by_id("verification_value")
#    cvv.send_keys(u.card_cvv)

    #click complete order
#    complete_order_button = driver.find_element_by_css_selector("button.step__footer__continue-btn")
#    complete_order_button.click()
password_up()