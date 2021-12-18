import subprocess
from os import path
import sys

dir_abs_path = path.abspath(path.dirname(__file__))
print(dir_abs_path)
sys.path.append(dir_abs_path + "/ScrapeIndiegogo")


def main():
    output = subprocess.check_output(["scrapy", "crawl", "Indiegogo"], cwd=dir_abs_path)
    print(output)


if __name__ == '__main__':
    main()
