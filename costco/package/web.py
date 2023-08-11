import os
import package.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = input("Please select either Chrome or Firefox browser: ")
# if browser.lower() == "chrome":
#    driver = webdriver.Chrome;
# else:
#    driver = webdriver.Firefox;

class Web(webdriver.Firefox):
    def __init__(this,
                driver_path=r"/Documents/Progamming/Visual Studio/Drivers"):
        this.driver_path = driver_path;
        os.environ["PATH"] += this.driver_path;
        super(Web, this).__init__();

    def open_page(this):
        this.get(const.URL);
        print("[SYSTEM]: The following URL has been opened...");
        this.implicitly_wait(5);
        print("[SYSTEM]: Successfully waited five seconds upon loading...");

    def search(this):
        search_item = input("Enter a product/item to search: ");
        search_box = this.find_element(By.CSS_SELECTOR, "#search-field");
        search_icon = this.find_element(By.CSS_SELECTOR, "button.btn:nth-child(4)");
        search_box.send_keys(search_item);
        print("[SYSTEM]: Product/item entered into the search box...");
        search_icon.click();
        print("[SYSTEM]: Product/item results now displayed upon search...")