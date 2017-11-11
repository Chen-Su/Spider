# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorksInfo(scrapy.Item):
	name = scrapy.Field()			# 作品名称
	category = scrapy.Field()		# 作品类别
	owner = scrapy.Field()			# 著作权人姓名/名称
	nation = scrapy.Field()			# 国籍
	province = scrapy.Field()		# 省份
	city = scrapy.Field()			# 城市
	author = scrapy.Field()			# 作者姓名/名称
	finish_date = scrapy.Field()	# 创作完成日期
	publish_date = scrapy.Field()	# 首次发表日期
	register_id = scrapy.Field()	# 登记号
	register_date = scrapy.Field()	# 登记日期
	post_date = scrapy.Field()		# 发布日期