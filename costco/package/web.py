import os
import package.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable

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

    def result(this):
        print("[SYSTEM]: Simplifying results...");

        cart = [];
        product_names = this.find_elements(By.CLASS_NAME, "description");
        product_prices = this.find_elements(By.CLASS_NAME, "price");

        # for product_name in product_names:
        #   print(product_name.find_element(By.TAG_NAME, "a").get_attribute("innerText"));
        # for product_price in product_prices:
        #   print(product_price.get_attribute("innerText"));
        # print(len(product_names));

        for i in range(0, len(product_names)):
            product_name = product_names[i].find_element(By.TAG_NAME, "a").get_attribute("innerText");
            product_price = product_prices[i].get_attribute("innerText");
            cart.append([product_name, product_price]);

        table = PrettyTable(["Product Name", "Price"]);
        table.add_rows(cart);

        print("[SYSTEM]: Results shown below...");
        print(table);

    def close_page(this):
        print("[SYSTEM]: Closing page...");
        this.implicitly_wait(3);
        this.close();
        print("[SYSTEM]: Page has been closed...");