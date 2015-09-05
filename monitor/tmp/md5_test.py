#!/bin/env python
#coding=utf-8
import md5

passwd = 'cgcgcg'

a =  md5.md5(passwd).hexdigest()
b =  md5.md5()
b.update('cgcgcg')
print a 
print b.hexdigest()