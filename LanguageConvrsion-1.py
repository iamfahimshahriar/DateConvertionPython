#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from datetime import datetime
strDate='2016-03-20'

objDate = datetime.strptime(strDate, '%Y-%m-%d')
englishResult=datetime.strftime(objDate,'%B %d, %Y')

replaceString=englishResult
banglaDigits = ['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '০', 'জানুয়ারী', 'ফেব্রুয়ারী', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগষ্ট', 'সেপ্টেম্বার', 'অক্টোবার', 'নভেম্বার', 'ডিসেম্বার', ':', ',']
englishDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', ':', ',']
for i,val in enumerate(banglaDigits):
    replaceString=replaceString.replace(englishDigits[i],banglaDigits[i])

print(englishResult)
print(replaceString)	