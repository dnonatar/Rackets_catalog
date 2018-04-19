# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RacketsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    Racket_Name = scrapy.Field()
    Head_Size = scrapy.Field()
    Length = scrapy.Field()
    Strung_Weight = scrapy.Field()
    Balance = scrapy.Field()
    Swingweight = scrapy.Field()
    Stiffness = scrapy.Field()
    Beam_Width = scrapy.Field()
    Composition = scrapy.Field()
    Power_Level = scrapy.Field()
    Stroke_Style = scrapy.Field()
    Swing_speed = scrapy.Field()
    Color = scrapy.Field()
    Grip_Type = scrapy.Field()
    String_Pattern = scrapy.Field()
    String_Tension = scrapy.Field()
    pass
