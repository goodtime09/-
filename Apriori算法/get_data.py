import time
from lxml import etree
from selenium import webdriver
import csv
def download(url):
    driver.get(url)
    time.sleep(1)
    html=driver.find_element_by_xpath('//*').get_attribute('outerHTML')
    html = etree.HTML(html)
    movie_lists=html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a')
    name_lists=html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div[1]/div/div[4]')
    num=len(movie_lists)
    if num>15:
        movie_lists=movie_lists[1:]
        name_lists=name_lists
    for (movie,name_list) in zip(movie_lists,name_lists):
        if name_list.text is None:
            continue
        names=name_list.text.split('/')
        print(names)
        if movie.text not in flags :
            if names[0]=='宁浩 ':
                flags.append(movie.text)
                names[0]=movie.text
                csv_write.writerow(names)
            else:
                flags.append(movie.text)
                csv_write.writerow([movie.text] + names)
    print('OK')
    print(num)
    if num >= 14:
        return True
    else:
        return False


if __name__=='__main__':
    driver = webdriver.Chrome()
    start = 0
    url = 'https://movie.douban.com/subject_search?search_text=%E5%AE%81%E6%B5%A9&cat=1002&start={}'.format(start)
    flags = []
    out = open('宁浩.csv', 'w', newline='', encoding='utf-8-sig')
    csv_write = csv.writer(out, dialect='excel')
    while download(url):
        start+=15
        url = 'https://movie.douban.com/subject_search?search_text=%E5%AE%81%E6%B5%A9&cat=1002&start={}'.format(start)
    out.close()
    print('finished')
    driver.close()