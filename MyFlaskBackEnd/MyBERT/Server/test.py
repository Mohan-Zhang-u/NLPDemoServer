import os
import codecs
import csv

# mew=""
# with codecs.open("../To_Be_Clean/CoLA/mew", "r", encoding="utf-8") as fp:
#     mew=fp.read()
# print(mew)

#
# sentence1 = "PCCW 's chief operating officer , Mike Butcher , and Alex Arena , the chief financial officer , will report directly to Mr So ."
# sentence2 = "Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So ."
# sentence3 = "Johnny is reading a book."
# sentence4 = "A book is read by Johnny."
#
# # with codecs.open("../To_Be_Clean/MRPC/test.tsv", "w", encoding="utf-8") as fp:
# #     tsv_writer = csv.writer(fp, delimiter='\t')
# #     tsv_writer.writerow(["index","#1 ID","#2 ID","#1 String","#2 String"])
# #     tsv_writer.writerow(["0","1089874","1089925",sentence1,sentence2])
# #     tsv_writer.writerow(["0","1089874","1089925",sentence3,sentence4])
#
# with codecs.open("../To_Be_Clean/MRPC/output/test_results.tsv", "r", encoding="utf-8") as fp:
#     tsv_reader = csv.reader(fp, delimiter='\t')
#     for row in tsv_reader:
#         print(row)
a="basdfvbq--wfhoiuwer das'\";h bf sdj nvl iu% we gr#$eghj~h !"

regular="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "
b=set(list(a))

for i in b:
    if i not in regular:
        print(i)
        a=a.replace(i, ' '+i+' ')
print(a)

# i=0
# while i < len(a):
#
#     if a[i] in "as":
#         a=a[:i-1]+' '+a[i]+' '+a[i:]
#         i+=2
#     i += 1
# print(a)
