

import  os as p
import  re
#-*-coding:utf-8 -*-
if __name__ == '__main__':



 count=0
 filepath=raw_input('input file path')
 if p.path.exists(filepath):

     file=open(filepath,'r')
     patter=raw_input('input your str')
     for x in file.readlines():
         st=re.findall(patter,x)
         if len(st)<>0:
            count=count+len(st)
     else:
      print count

 else:
     print  'error file not exit'











