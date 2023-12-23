import os
import zpackage.constants as const
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
        print("The following URL has been opened.");
        this.implicitly_wait(3);
        print("Successfully waited three seconds upon loading.")

    def close_page(this):
        this.close()

    def search(this):
        user_search_text = input("Enter an address, neighborhood, city, or ZIP code: ");
        search_box = this.find_element(By.CSS_SELECTOR, "#search-box-input");
        search_box.click();
        search_box.send_keys(user_search_text);
        print("Inputted user specified location in the search box.");
        # search_box.send_keys(Keys.ENTER);
        search_icon_button = this.find_element(By.CSS_SELECTOR, "#search-icon");
        search_icon_button.click();
        print("Searching...")

    def first_time_pop_up_preferences(this):
        skip_button = this.find_element(By.CSS_SELECTOR, ".fccQKC");
        print("Pop-up enabled.");
        skip_button.click();
        print("Skipping pop-up...");
