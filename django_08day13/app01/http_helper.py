#!/bin/env python
#coding=utf-8
from django.utils.safestring import mark_safe  #这个方法是帮助将html标签当成html标签，不然django通过render_to_response返回时字符串

class PageInfo():
    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
        
   
    
    #第一页：0 - 5： page=1.
    #第二页: 5- 10: page=2
    #第三页: 10 -15: page=3
    #(page-1)*per_item page*per_item
    
    
    def start(self):
        return (self.CurrentPage-1) * self.PerItem
    
    def end(self):
        return self.CurrentPage * self.PerItem
    
    def all_page_count(self):
        '''
        temp = divmod(count, per_item) #divmod取得总的页数，看有没有余数
        if temp[1] == 0:
            all_pages_count = temp[0]
        else:
            all_pages_count = temp[0] + 1
        '''
        temp = divmod(self.AllCount, self.PerItem) #divmod取得总的页数，看有没有余数
        if temp[1] == 0:
            all_pages_count = temp[0]
        else:
            all_pages_count = temp[0] + 1
        
        return all_pages_count



def Pager(page,all_pages_count):
    '''
    page:当前页
    all_page_count:总页数
    '''
    page_html = []
    first_html = "<li><a href='/index/%d'>%s</a></li>" %(1,'首页')
    page_html.append(first_html)
    
    if page <= 1:
        prev_html = "<li><a href=#>%s</a></li>" %('上一页')
    else:
        prev_html = "<li><a href='/index/%d'>%s</a></li>" %(page-1,'上一页')
    page_html.append(prev_html)
    
 #   begin = page - 5
 #   end = page + 6
    
    if all_pages_count < 11:
        begin = 0
        end = all_pages_count
    else:
        if page < 6:
            begin = 0
            end = 12
        else:
            if page + 6 > all_pages_count:
                begin = all_pages_count - 11
                end = all_pages_count
            else:
                begin = page -6
                end = page + 5
    
    for i in range(begin,end):
        if page == i+1:
            a_html = "<li><a style='color:red' href='/index/%d'>%d</a></li>" %(i+1,i+1)
        else:
            a_html = "<li><a href='/index/%d'>%d</a></li>" %(i+1,i+1)
        page_html.append(a_html)
    
    if page == all_pages_count:
        next_html = "<li><a href='#'>%s</a></li>" %('下一页')
    else:
        next_html = "<li><a href='/index/%d'>%s</a></li>" %(page+1,'下一页')
    page_html.append(next_html)
    
    end_html = "<li><a href='/index/%d'>%s</a></li>" %(all_pages_count,'尾页')
   
    page_html.append(end_html)
    page_string = mark_safe(''.join(page_html))
    return page_string
