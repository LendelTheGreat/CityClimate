# -*- coding: utf-8 -*-

from lxml import html
import requests as rqs

def num(string):
  num = ''
  for c in string:
    if ord(c) == 8722:
      num += '-'
    if (c >= '0' and c <= '9') or c == '.' or c == '-':
      num += c

  return float(num)

class City:
  
  def __init__(self, city_name):
    self.city_name = city_name
    self.url = 'https://en.wikipedia.org/wiki/' + city_name
    self.city_name = city_name.split(',')[0]
    
    self.average_high = ['No data']
    self.mean = ['No data']
    self.average_low = ['No data']
    self.sunshine = ['No data']
    
    
  def parse_page(self):
    regexpNS = "http://exslt.org/regular-expressions"
    page = rqs.get(self.url)
    tree = html.fromstring(page.content)
    
    self.average_high = self.filter_list(tree.xpath("//table/tr/th[re:test(., '^.*average high.*$', 'i')]/../td/text()",namespaces={'re':regexpNS}))
    self.mean = self.filter_list(tree.xpath("//table/tr/th[re:test(., '^.*daily mean.*$', 'i')]/../td/text()",namespaces={'re':regexpNS}))
    self.average_low = self.filter_list(tree.xpath("//table/tr/th[re:test(., '^.*average low.*$', 'i')]/../td/text()",namespaces={'re':regexpNS}))
    self.sunshine = tree.xpath("//table/tr/th[re:test(., '^.*monthly sunshine.*$', 'i')]/../td/text()",namespaces={'re':regexpNS})
    if self.sunshine == []:
      self.sunshine = ['-0']
    
  def filter_list(self, list):
    filtered = []
    for i in xrange(0,len(list),2):
      filtered.append(min(num(list[i]), num(list[i+1])))
      
    if filtered == []:
      filtered = ['No data']
    return filtered

  def print_all(self):
    print '###############################'
    print 'Climate for ' + self.city_name
    print 'URL: ' + self.url
    print 'Average high  : Min {}    Max {}'.format(min(self.average_high), max(self.average_high))
    print 'Average       : Min {}    Max {}'.format(min(self.mean), max(self.mean))
    print 'Average low   : Min {}    Max {}'.format(min(self.average_low), max(self.average_low))
    print 'Sunshine hours: ' + str(self.sunshine[-1])
    print '###############################'
    
  def save(self, filename):
    with open(filename, 'a') as file:
      file.write('{}, {}, {}, {}, {}, {}\n'.format(self.city_name, min(self.average_low), max(self.average_low), min(self.average_high), max(self.average_high), num(self.sunshine[-1])))


