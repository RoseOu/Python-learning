#!/usr/bin/env python
# coding: utf-8

'''
文本处理。统计一句话中的元音，辅音及单词（以空格分隔）的个数。忽略元音和辅音的特殊情况，
如“h”，“y”，“qu”等。附加题：编写处理这些特殊情况的代码。
'''

sen = raw_input("Input a sencence here:")
vowel = 0
consonant = 0

words = len(sen.split(' '))

for i in sen:
	if i in 'a,e,i,o,u':
		vowel = vowel + 1
	elif i == ' ':
		pass
	else:
		consonant = consonant + 1

print "Vowel:%d, Consonant:%d, Words: %d" % (vowel, consonant, words)