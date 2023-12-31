import os
from selenium import webdriver
from selenium.webdriver.common.by import By

directoryPath = r"/Documents/Progamming/Visual Studio/Drivers";
os.environ["PATH"] += directoryPath;
browser = input("Select a browser, {Chrome or Firefox}: ");
if (browser.lower() == "chrome"):
    driver = webdriver.Chrome();
else:
    driver = webdriver.Firefox();

websiteURL = "https://store.epicgames.com/en-US/";
driver.get(websiteURL);
driver.implicitly_wait(2);

for index in range(1, 5):
    title = driver.find_element(By.XPATH, "//*[@id='dieselReactWrapper']/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[" + str(index) + "]/div/div/a/div/div/div[3]/div/div");
    if index == 1:
        print("This week's free games are: ");
    if index == 3:
        print("\n" + "Next week's free games are: ");
    print(f'[{index}] {title.text}');
driver.close();