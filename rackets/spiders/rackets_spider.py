import scrapy
from rackets.items import RacketsItem

class RacketsSpider(scrapy.Spider):
	name = "rackets"
	allowed_domains = ["tennis-warehouse.com"]

	#start_urls = ["http://www.tennis-warehouse.com/HeadRacquets.html"]
	#start_urls = ["http://www.tennis-warehouse.com/Babolatracquets.html"]
	start_urls = ["http://www.tennis-warehouse.com/WilsonRacquets.html"]
	#start_urls = ["http://www.tennis-warehouse.com/YonexRacquets.html"]

	
	# There must be a function named 'parse'. Why?
	# Probably because there is a first request with unspecified callback that is not explicitly shown in the code

	def parse(self, response):
		for racket_url in response.xpath('//div[@class="text_wrap"]/a/@href').extract():
			yield scrapy.Request(racket_url, callback = self.parse_racket)
			
	def parse_racket(self, response):
		item = RacketsItem()
			
		item['Racket_Name'] = response.xpath('//div[@class="product_header"]/h1/text()').extract()

		item['Head_Size'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[1]/td[@class="SpecsLt"]/text()').extract()
		item['Length'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[2]/td[@class="SpecsDk"]/text()').extract()
		item['Strung_Weight'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[3]/td[@class="SpecsLt"]/text()').extract()
		item['Balance'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[4]/td[@class="SpecsDk"]/text()').extract()
		item['Swingweight'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[5]/td[@class="SpecsLt"]/text()').extract()
		item['Stiffness'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[6]/td[@class="SpecsDk"]/text()').extract()
		item['Beam_Width'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[7]/td[@class="SpecsLt"]/text()').extract()
		item['Composition'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[8]/td[@class="SpecsDk"]/text()').extract()
		item['Power_Level'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[9]/td[@class="SpecsLt"]/text()').extract()
		item['Stroke_Style'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[10]/td[@class="SpecsDk"]/text()').extract()
		item['Swing_speed'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[11]/td[@class="SpecsLt"]/text()').extract()
		item['Color'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[12]/td[@class="SpecsDk"]/text()').extract()
		item['Grip_Type'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[13]/td[@class="SpecsLt"]/text()').extract()
		item['String_Pattern'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[14]/td[@class="SpecsDk"]/text()').extract()
		item['String_Tension'] = response.xpath('//div[@class="rac_specs"]//tbody/tr[15]/td[@class="SpecsLt"]/text()').extract()
			
		yield item


