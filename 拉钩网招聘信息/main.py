import requests
import re
import time
import random
import pandas as pd

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
]
# header = {
#     # 'Host': 'www.lagou.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
#     # 'Accept': 'application/json, text/javascript, */*; q=0.01',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     # 'Accept-Language': 'zh-CN,zh;q=0.9',
#     # 'Connection': 'keep-alive',
#     # 'Content-Length': '55',
#     # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': 'JSESSIONID=ABAAABAAADEAAFI3A615D99261B28EDC8F57E55FB8CA074; _ga=GA1.2.1654363653.1557810466; _gid=GA1.2.1949211889.1557810466; user_trace_token=20190514130747-36c48e7c-7606-11e9-9f4c-5254005c3644; LGUID=20190514130747-36c492eb-7606-11e9-9f4c-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557810466,1557811176,1557811184; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=1f20259328e3144dcb799c4c5650627d; LGSID=20190516081745-0752620c-7770-11e9-a01d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sh_f419d0_af9173_%25E6%258B%2589%25E9%2592%25A9%25E6%258B%259B%25E8%2581%2598%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LG_HAS_LOGIN=1; _putrc=4D4114C59E6B87FF123F89F2B170EADC; login=true; hasDeliver=0; gate_login_token=ffa290fbed0c9381284e5a8e35e72153ffc2be58eb216583e0f21a17f3992bd8; _gat=1; unick=%E9%99%88%E5%BE%B7%E5%A8%81; LG_LOGIN_USER_ID=414009d546d04ae763498a23c2134ee11378966f93e95cb9fda04365020fd8b4; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; SEARCH_ID=a71925b2bed94376aa71a02546b40b56; X_HTTP_TOKEN=3c9c71ff059523be34766975517be75c9ce96640b0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557966742; LGRID=20190516083223-129e9a98-7772-11e9-a01d-5254005c3644',
#     # 'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
#     # 'X-Anit-Forge-Code': '0',
#     # 'X-Anit-Forge-Token': 'None',
#     # 'X-Requested-With': 'XMLHttpRequest'
# }
# proxies = {'https':'103.235.199.46:31611',}
if __name__ == '__main__':
    try:
        for n in range(23,30):
            agent_one = random.sample(agent,1)
            print(agent_one[0])
            header = {
                'User-Agent': agent_one[0],
                'Cookie': 'user_trace_token=20190516183539-7f2f3214-f2c0-400d-842c-0692eda6f8f9; _ga=GA1.2.997830771.1558002939; _gid=GA1.2.1139460829.1558002939; LGUID=20190516183539-5948f420-77c6-11e9-a086-5254005c3644; LG_LOGIN_USER_ID=b61a35889f3e54324dc960d3ed68532d5698e8e3a2814deb7fdae18cbf47409d; LG_HAS_LOGIN=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558002939,1558052276; _gat=1; LGSID=20190517081758-393ee2e3-7839-11e9-a0bc-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=; PRE_SITE=https%3A%2F%2Fsec.lagou.com%2Fverify.html%3Fe%3D2%26f%3Dhttps%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sh_f419d0_19a921_%25E6%258B%2589%25E5%258B%25BE%25E6%25B1%2582%25E8%2581%258C%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc; _putrc=4D4114C59E6B87FF123F89F2B170EADC; JSESSIONID=ABAAABAABEEAAJAB80F4B9AC5A5093A334BF9E8758B214C; login=true; unick=%E9%99%88%E5%BE%B7%E5%A8%81; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=ffa290fbed0c9381284e5a8e35e72153ffc2be58eb216583e0f21a17f3992bd8; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=149ad4d3264c28fa1822508551b118dfe94b74eb4f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558052280; LGRID=20190517081801-3b398c47-7839-11e9-a0bc-5254005c3644; TG-TRACK-CODE=index_search; SEARCH_ID=da010575797c4c2f8045ce4813b8be70',
                'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
                'X-Anit-Forge-Code': '0',
                'X-Anit-Forge-Token': 'None',
                'X-Requested-With': 'XMLHttpRequest',
                'Host': 'www.lagou.com',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': '55',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin':'https://www.lagou.com'
            }
            print('开始爬取第%d页'%n)
            form = {'first': 'false',
                    'kd': '数据分析',
                    'pn': str(n) }
            time.sleep(random.randint(2,5))
            html = requests.post(url, data=form, headers=header, timeout=10).json()
            jobs = html['content']['positionResult']['result']
            # data = re.findall('{"compandyId":.*?,"positionName":"(.*?)",}')

            # data = re.findall(
            #     '{"positionId":.*?,"positionName":"(.*?)","workYear":"(.*?)","education":"(.*?)","city":"(.*?)","jobNature":"(.*?)","financeStage":"(.*?)","companyLogo":".*?","industryField":".*?","city":"(.*?)","salary":"(.*?)","positionId":.*?,"positionAdvantage":"(.*?)","companyShortName":"(.*?)","district"'
            #     , html.text)
            info_list = []
            for job in jobs:
                info = [job['positionId'], job['city'], job['companyFullName'],
                        job['companyLabelList'], job['district'], job['education'],
                        job['firstType'], job['formatCreateTime'], job['positionName'],
                        job['salary'], job['workYear']
                        ]
                info_list.append(info)
            data = pd.DataFrame(info_list)
            data.to_csv('data_1.csv', index=False, mode='a+', encoding='gb2312', header=None)
                        # columns=['','岗位ID', '城市', '公司全名', '福利待遇', '工作地点', '学历'
                        #     , '工作类型', '发布时间', '职位', '薪资', '工作经验'])
            print('第%d页爬取完成'%n)
    except KeyError as e:
        print(e)
        print(html)
