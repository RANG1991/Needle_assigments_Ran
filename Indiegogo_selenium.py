from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def crawl_single_page(link_element, driver):
    d = {"url": link_element.text}
    link_element.click()
    time.sleep(2)
    d["Creators"] = driver.find_element('//div[contains(@class, "campaignOwnerName-tooltip")]')[0].text
    d["Title"] = driver.find_element('//div[contains(@class, "basicsSection-title")]')[0].text
    d["DollarsPledged"] = driver.find_element('//span[contains(@class, "basicsGoalProgress-amountSold")]')[0].text
    d["DollarsGoal"] = driver.find_element('//span[contains[@class, "basicsGoalProgress-progressDetails-detailsGoal")]')[0].text
    d["NumBackers"] = driver.find_element('//span[contains(@class, "basicsGoalProgress-claimedOrBackers")]//span')[0].text
    d["DaysToGo"] = driver.find_element('//span[contains(@class, "basicsGoalProgress-progressDetails-detailsTimeLeft")]//span')[0].text
    time.sleep(3)


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver_path = "C:/Users/Admin/Desktop/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get('https://www.indiegogo.com/explore/home')
    time.sleep(3)
    button = driver.find_element(By.XPATH, '//a[@id="CybotCookiebotDialogBodyButtonAccept"]')
    button.click()
    time.sleep(3)
    for i in range(20):
        button = driver.find_element(By.XPATH, '//a[@ng-click="showMoreCampaigns()"]')
        button.click()
        time.sleep(2)
    links_elements = [element for element in driver.find_elements(By.XPATH,
                                                        '//div[@class="discoverableCard"]/a[@href]')]
    for link_element in links_elements:
        crawl_single_page(link_element, driver)
        time.sleep(1)
    driver.quit()


if __name__ == "__main__":
    main()

