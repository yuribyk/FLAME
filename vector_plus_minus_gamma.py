#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:19:18 2019

@author: yuribyk
"""

#a="+----5a+6a-8a+--+++9a"
#a="-5a+6a-8a+9a"
#b="5a+6a-8a+9a"
#b="yuri"
#a="kasporov"

#a="-5a6a8a9a"
print("Caution: Minus sticks to the variable. remaining are deleted")
    
def splitter(a):
    b=""
    """  a-b  =  a+(-b)  """
    for i in range(len(a)):
        if a[i]=="-":
            b+="+"
            b+=a[i]
        else:
            b+=a[i]
    b=b.split("+")
    c=[]
    """Filtering the crap"""
    for i in b:
        if i!="" and i!="-":
            c.append(i)
            
           
    #print(b)
    #print(c)
    return c

def add_vector(a):
    """  helps in removing same vectors   """
    d=len(a)
    #print(d)
    for i in range(d):
        c=a[i][1]
        for j in range(d):
            if i!=j and c==a[j][1]:
                a[j][0]+=a[i][0]
                a[i][0]=0
    b=[]
    for i in a:
      if i[0]!=0:
          b.append(i)
    return b


def prod(a):
    
    try:
        a=int(a)
        #print([a,0]," in prod")
        return [a,'']
        
    except ValueError:
        """ creating required variables """
        numlist=[]
        var_raw_lib=[]
        y=0
        poww=-1
        
        for i in range(len(a),0,-1):
            try:
                x= int(a[i-1])
                poww+=1
                y+=x*(10**poww)
                
                if (i-1)==0:
                    numlist.append(y)
            
            except ValueError:
                
                var_raw_lib.append(a[i-1])
                if y!=0:
                    numlist.append(y)
                """resetting number and power values when char comes"""
                y=0
                poww=-1
        'ASSIGNING MINUS SIGN TO NUMBER'
        try:
            var_raw_lib.remove("-")
            prod=-1
        except ValueError:
            prod=1
            
        for i in numlist:
            prod*=i
            
        var_counter=set(var_raw_lib)
        var_counter=sorted(var_counter)
        #print(var_counter)
    
        data_var=""
        # counter is total num of occurances
        for i in var_counter:
            counter=var_raw_lib.count(i)
            k=(i*counter)
        
            data_var+=k
        #print([prod,data_var]," all sorted")
        return [prod,data_var]

def run_prod(a):
    e=[]
    
    for i in a:
        e.append(prod(i))
    return e

def simplify(a):
    d=splitter(a)
    a=run_prod(d)
    d=add_vector(a)
    #print("simply: ",d)
    return d
def add(b,a):
    return simplify(b+"+"+a)
    
def sub(b,a):
    c=simplify(a)
    for i in c:
        i[0]*=(-1)
    
    d=simplify(b) + c
    e=add_vector(d)
    #print(e)
    return e
    

#c=add(b,a)
#print("a+b= ",c)
#c=sub(b,a)
#print("a-b= ",c)
#c=sub(a,b)
#print("b-a= ",c)
#c=simplify(a)
#print("a= ",c)
#c=simplify(b)
#print("b= ",c)
