#
# @lc app=leetcode.cn id=195 lang=bash
#
# [195] 第十行
#
# Read from the file file.txt and output the tenth line to stdout.

awk '{if (NR==10) print $0}' file.txt

