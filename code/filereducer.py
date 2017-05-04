# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:46:29 2016

@author: test
"""
import numpy as np
import shutil as sh


fp_i = open('./wikiextractor-master/output.npy', 'rb')
arr = np.load(fp_i);  


for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(str(arr[i,j]+1))
        sh.copy("./dataset_HTML/AA/wiki_"+str(arr[i,j]+1)+".html","./dataset_HTML/reduced_files/")

for i in range(len(arr)):
    myfile= open("./dataset_HTML/reduced_files/wiki_"+str(arr[i,0]+1)+".html", "a")
    count=1
    for j in range(1,len(arr[i])):        
        myfile.write("<br/><a href='http://spanky.rutgers.edu/reduced_files/wiki_"+str(arr[i,j]+1)+".html'>Reference "+str(count)+"</a><br/>")
        count=count+1
    myfile.close();

fp=open("./dataset_HTML/index2.html","w")
fp.write("<html><title>List of Topics</title><body>")
count=1
pagecount=1
fp.write("<h1>List of Topics</h1><div class='div"+str(pagecount)+"'>")
for num in arr[:,0]:
    if count==30:
        pagecount=pagecount+1;
        fp.write("</div><br/>")
        fp.write("<div class='div"+str(pagecount)+"'>")
        count=0
    with open("./dataset_HTML/reduced_files3/wiki_"+str(num+1)+".html", encoding='utf8') as f1:
        for line in f1.readlines():
            if "<h1>" in line:
                title=line[4:len(line)-6]
                fp.write("<a href='http://localhost/reduced_files/wiki_"+str(num+1)+".html'>"+title+"</a><br/>")
    count=count+1;
fp.write("</div></body></html>")


