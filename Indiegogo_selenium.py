from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json

MAX_PAGES_TO_CRAWL = 10

def crawl_single_page(url, driver):
    print("parsing link: {}".format(url))
    d = {"url": url}
    driver.get(url)
    time.sleep(2)
    try:
        d["Creators"] = driver.find_element(By.XPATH, '//div[contains(@class, "campaignOwnerName-tooltip")]').text
        d["Title"] = driver.find_element(By.XPATH, '//div[contains(@class, "basicsSection-title")]').text
        d["DollarsPledged"] = str(driver.find_element(By.XPATH,
                                                      '//span[contains(@class, "basicsGoalProgress-amountSold")]').text)
        d["DollarsGoal"] = str(driver.find_element(By.XPATH,
                                                   '//span[contains(@class, "basicsGoalProgress-progressDetails-detailsGoal")]').text)
        d["NumBackers"] = driver.find_element(By.XPATH,
                                              '//span[contains(@class, "basicsGoalProgress-claimedOrBackers")]//span').text
        d["DaysToGo"] = driver.find_element(By.XPATH,
                                            '//div[contains(@class, "basicsGoalProgress-progressDetails-detailsTimeLeft")]//span').text
        flexible_goal_element = driver.find_element('//div[contains(@class, "basicsGoalProgress-progressDetails-detailsGoal-goalWording")]'
                                                    '//span[contains(text(), "Flexible Goal")]')
        if flexible_goal_element:
            d["FlexibleGoal"] = "True"
        else:
            d["FlexibleGoal"] = "False"
    except Exception as e:
        print(e)
    time.sleep(2)
    return d


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver_path = "C:/Users/Admin/Desktop/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get('https://www.indiegogo.com/explore/home')
    time.sleep(2)
    button = driver.find_element(By.XPATH, '//a[@id="CybotCookiebotDialogBodyButtonAccept"]')
    button.click()
    time.sleep(2)
    for i in range(20):
        button = driver.find_element(By.XPATH, '//a[@ng-click="showMoreCampaigns()"]')
        button.click()
        time.sleep(2)
    links = [element.get_attribute("href") for element in driver.find_elements(By.XPATH,
                                                        '//div[@class="discoverableCard"]/a[@href]')]
    d = {"records": []}
    with open("json_all.json", "w") as f:
        for index in range(min(MAX_PAGES_TO_CRAWL, len(links))):
            d_ret = crawl_single_page(links[index], driver)
            print(d_ret)
            d["records"].append(d_ret)
            time.sleep(1)
        f.write(json.dumps(d, indent=4))
        f.flush()
        driver.quit()


if __name__ == "__main__":
    main()

