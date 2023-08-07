import os
import hpackage.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = input("Please select either Chrome or Firefox browser: ")
# if browser.lower() == "chrome":
#    driver = webdriver.Chrome;
# else:
#    driver = webdriver.Firefox;

class Web(webdriver.Firefox):
    def __int__(this,
                driver_path=r"/Documents/Progamming/Visual Studio/Drivers"):
        this.driver_path = driver_path;
        os.environ["PATH"] += this.driver_path;
        super(Web, this).__init__();

    def open_page(this):
        this.get(const.URL);
        print("[SYSTEM]: The following URL has been opened...");
        this.implicitly_wait(5);
        print("[SYSTEM]: Successfully waited five seconds upon loading...")
    
    def location(this):
        user_location_text = input("Please enter a location (>2 chars): ");
        location_button = this.find_element(By.CSS_SELECTOR, ".Input-element");
        location_button.send_keys(user_location_text);
        print("[SYSTEM]: The following location has been inputted...");

    def price(this):
        price_button = this.find_element(By.CSS_SELECTOR, "div.styles__AutocompleteHItem-h5ukh3-4:nth-child(1) > div:nth-child(1) > button:nth-child(1)");
        price_button.click();
        print("[SYSTEM]: Clicked price button for drop down menu...")
        user_min_price = input("Please enter a minimum price bound: ");
        user_max_price = input("Please enter a maximum price bound: ");
        min_price = this.find_element(By.CSS_SELECTOR, "#min-price-input");
        max_price = this.find_element(By.CSS_SELECTOR, "#max-price-input");
        min_price.send_keys(user_min_price);
        max_price.send_keys(user_max_price);
        print("[SYSTEM]: Price range values inputted...");

    def bed_count(this):
        bed_filter_button = this.find_element(By.CSS_SELECTOR, "div.styles__AutocompleteHItem-h5ukh3-4:nth-child(2) > div:nth-child(1) > button:nth-child(1)");
        bed_filter_button.click();
        exact_button = this.find_element(By.CSS_SELECTOR, ".styles__StyledCheckbox-sc-6kwpq3-2");
        user_exact = input("Do you want exact number of bed count (Y/N): ");
        if (user_exact.lower() == "y"):
            exact_button.click();
            print("[SYSTEM]: Exact button checked...");
            user_bed_count = input("Enter the number of beds [1-4] or 0 for studio: ");

            if (user_bed_count == "1"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(2) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 1 bed has been checked...");
            
            elif (user_bed_count == "2"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(3) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 2 beds has been checked...");
            
            elif (user_bed_count == "3"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(4) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 3 beds has been checked...");
            
            elif (user_bed_count == "4"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(5) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 4 beds has been checked...");
            
            else:
                print("[SYSTEM]: studio (default) has been checked...");
        
        else:
            print("[SYSTEM]: Exact button unchecked...");
            user_bed_count = input("Enter the number of beds [1-4] or 0 for any: ");
            if (user_bed_count == "1"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(2) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 1 bed has been checked...");
            
            elif (user_bed_count == "2"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(3) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 2 beds has been checked...");
            
            elif (user_bed_count == "3"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(4) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 3 beds has been checked...");
            
            elif (user_bed_count == "4"):
                bed_number_button = this.find_element(By.CSS_SELECTOR, "li.styles__FlexListItem-sc-1h02zis-1:nth-child(5) > button:nth-child(1)");
                bed_number_button.click();
                print("[SYSTEM]: 4 beds has been checked...");
            
            else:
                print("[SYSTEM]: any beds has been checked...");

    def search(this):
        search_button = this.find_element(By.CSS_SELECTOR, "button.styles__Button-mwrmpo-0:nth-child(2)");
        search_button.click();
        print("[SYSTEM]: Searched and results are displayed...");