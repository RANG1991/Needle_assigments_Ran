from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup

MAX_PAGES_TO_CRAWL = 300


def get_single_xpath(driver, str_xpath, convert_to_string=True):
    elements = ""
    try:
        if convert_to_string:
            elements = str(driver.find_element(By.XPATH, str_xpath).text)
        else:
            elements = driver.find_element(By.XPATH, str_xpath)
    except Exception as e:
        print(e)
    finally:
        return elements


def crawl_single_page(url, driver, i):
    print("parsing link: {}".format(url))
    d = {"id": str(i), "url": url}
    driver.get(url)
    time.sleep(2)
    d["Creators"] = get_single_xpath(driver, '//div[contains(@class, "campaignOwnerName-tooltip")]')
    d["Title"] = driver.title

    # get all the text
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    bs = BeautifulSoup(html_source_code, 'html5lib')
    d["Text"] = bs.prettify()

    d["DollarsPledged"] = get_single_xpath(driver, '//span[contains(@class, "basicsGoalProgress-amountSold")]')
    d["DollarsGoal"] = get_single_xpath(driver,
                                        '//span[contains(@class, "basicsGoalProgress-progressDetails-detailsGoal")]')
    backers_elements = get_single_xpath(driver,
                                        '//span[contains(@class, "basicsGoalProgress-claimedOrBackers")]//span')
    d["NumBackers"] = ""
    if backers_elements:
        for element in backers_elements:
            if element.replace(",", "").isnumeric():
                d["NumBackers"] = element
    d["DaysToGo"] = get_single_xpath(driver,
                                     '//div[contains(@class, "basicsGoalProgress-progressDetails-detailsTimeLeft")]//span')
    d["FlexibleGoal"] = "False"
    flexible_goal_element = get_single_xpath(driver,
                                             '//div[contains(@class, "basicsGoalProgress-progressDetails-detailsGoal")]//span[contains(text(), "Flexible Goal")]')
    if "flexible goal" in flexible_goal_element.strip().lower():
        d["FlexibleGoal"] = "True"
    time.sleep(2)
    return d


def main():
    options = webdriver.ChromeOptions()
    options.headless = True
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
    with open("json_all.json", "w", encoding="utf-8") as f:
        f.write("{\n[\n")
        for index in range(min(MAX_PAGES_TO_CRAWL, len(links))):
            d_ret = crawl_single_page(links[index], driver, index + 1)
            for key in d_ret.keys():
                d_ret[key] = d_ret[key].encode("ascii", "ignore").decode('utf8')
            print(d_ret)
            time.sleep(1)
            f.write(json.dumps(d_ret, indent=4) + "\n\n")
            f.flush()
        f.write("\n]\n}")
        driver.quit()


if __name__ == "__main__":
    main()
