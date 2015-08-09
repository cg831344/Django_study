#!/bin/env python
#coding=utf-8

def try_int(arg,default):
    try:
        arg = int(arg)
    except BaseException,e:
        arg = default
    return arg