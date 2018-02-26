def hd():
    flag1=0
    flag2=0
    flag3=0
    resultstr=''
    
    while flag1!=1:
        a=list(input("enter first binary string:"))
        flag1=cheakbinary(a)
        
    while flag2!=1 or flag3!=1:
        b=list(input("enter second binary string:"))
        flag2=cheakbinary(b)
        flag3=cheaklenth(b,a)
        
    x,y=0,0
    for i in range(len(a)):
        if a[i]=='1':
            x=x+1
        if b[i]=='1':
            y=y+1
            
    #adding the parity of 1 bit at the end of string    
    z=int(input("enter 1 for even parity and enter 0 for odd :"))
    if z==1:
        if x%2==0:
            a.append('0')
        else:
            a.append('1')

        if y%2==0:
            b.append('0')
        else:
            b.append('1')
    else:
        if x%2==0:
            a.append('1')
        else:
            a.append('0')

        if y%2==0:
            b.append('1')
        else:
            b.append('0')
            
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count=count+1
            resultstr=resultstr+'1'
        else:
            resultstr=resultstr+'0'
            
    stra=''.join(a)
    strb=''.join(b)
    print(stra)
    print(strb)
    print(resultstr)
    print(count)
# cheak if the lenth of both the string is equal or not   
def cheaklenth(sample1,sample2):
    if len(sample1)==len(sample2):
        return 1
    else:
        print('lenth of string b should be equal to a')
        return 0
#cheak if the string is in binary or not
def cheakbinary(sample):
    count1=0
    for i in sample:
        if i=='0' or i=='1':
            count1=count1+1
    if count1==len(sample):
        return 1
    else:
        print('string is not in binary please enter again')
        return 0
#calling hamming distance function
hd()        
    
    
