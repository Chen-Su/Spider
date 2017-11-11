from firstcrawl.items import WorksInfo
import scrapy


class WorksSpider(scrapy.Spider):
    name = "works"
    def start_requests(self):
        base_url = "http://203.207.196.210:8080/registerinfo/worksDetail.do?id="
        for i in range(50):
            yield scrapy.Request(url=base_url+str(i+1), callback=self.parse)

    def parse(self, response):
        item_list = ['name', 'category', 'owner', 'nation', 'province',
            'city', 'author', 'finish_date', 'publish_date',
            'register_id', 'register_date', 'post_date']
        
        item = WorksInfo()
        
        for table in response.xpath('//*[@id="text_real"]/table'):
            datas = table.xpath('tr/td')
            cnt = 0
            isodd = True
            first = True
            for data in datas:
                if isodd:
                    if first:
                        first = False
                    else:
                        res = data.xpath('text()').extract_first()
                        item[item_list[cnt]] = res;
                        # print item_list[cnt], item[item_list[cnt]]
                        cnt += 1
                isodd = not isodd

        yield item