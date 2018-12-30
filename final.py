#code by Ashish Goyal(2016ucp1100)
#Date:12 March 2018
import re

inp=open("input.asm","r")
out=open("output.asm","w")
deftab=open("deftab.txt","r+")

nametab=[]
argtab=[]

list1=inp.readlines()
#...................................................................................#
for k in range(len(list1)):
    list1[k]=list1[k].strip('\n')       #remove new line character
    #list1[k]=list1[k].strip('\t')
k=0
while(k<len(list1)):		        #for taking out all the empty spaces created by the above loop                       
    if (not list1[k]):      
    	list1.pop(k)
    	k=k-1
    k+=1
#...................................................................................#   
#for nametab(only without nested is stored that can be called directly)
c=0
index=0
for i in range(len(list1)):         
    if "@@BEGINN" in list1[i]:      #for single line defination
        if "@@ENDD" in list1[i]:
            listtemp=[]
            ind=list1[i].find('(')
            listtemp.append(list1[i][12:ind-4])
            listtemp.append(i+1)
            listtemp.append(i+1)
            index=index+1
            nametab.append(listtemp)
            continue
    if "@@BEGIN" in list1[i]:
        c=c+1
        if(c==1):
            listtemp=[]
            ind=list1[i].find('(')
            listtemp.append(list1[i][11:ind-4])
            listtemp.append(i+1)
    elif "@@END" in list1[i]:
        c=c-1
        if(c==0):
            listtemp.append(i+1)
            index=index+1
            nametab.append(listtemp)
#print(nametab)
            
#for deftab
for q in range(nametab[index-1][2]):          #add new line for the new file that is free of spaces etc
    list1[q]=list1[q]+'\n'
for q in range(nametab[index-1][2]):          #write complete deftab
    deftab.write(list1[q])
#...................................................................................#
for k in range(len(list1)):
    list1[k]=list1[k].strip('\n')               #remove new line character
    #list1[k]=list1[k].strip('\t')
k=0
while(k<len(list1)):		                     
    if (not list1[k]):         
    	list1.pop(k)
    	k=k-1
    k+=1
#....................................................................................#
#for i in range(len(list1)):
#   print(list1[i])


#arguments
def parameter(namtab2,stringg,list1):
    y=stringg.find('...')
    z=stringg.find('(')
    macro1=stringg[y+3:z-4]
    list2=[]            #contain macro name+its dictionary
    list2.append(macro1)
    if "@@BEGIN" in stringg:        #nested macro
        arglist=[]
        dic={}
        arglist=re.split('[,=]',stringg[z+1:len(stringg)-1])
        for v in range(0,len(arglist)-1,2):#dictionary filled
            dic[arglist[v]]=arglist[v+1]
        list2.append(dic)
    else:       #for not nested
        arglist=[]
        arglist=re.split('[,]',stringg[z+1:len(stringg)-1])#here stringg is ...MULTI...(1,2,34)
        for v in range(len(arglist)):#convert into string
            arglist[v]=str(arglist[v])
        for v in range(len(nametab2)):#for starting address
            if macro1==nametab2[v][0]:
                qwerty=nametab2[v][1]#store starting line number
        randstr=list1[qwerty-1]         #store defination first line
        dic={}
        y=randstr.find('...')
        z=randstr.find('(')
        closebracket=randstr.find(')')
        neww=re.split('[,=]',randstr[z+1:closebracket])#store default 
        #for making dictionary
        t=1
        if arglist!=['']:#means there are arguments there see above example
            for v in range(len(arglist)):
                neww[t]=arglist[v]
                t=t+2
        for v in range(0,len(neww)-1,2):#dictionary filled
            dic[neww[v]]=str(neww[v+1])
        list2.append(dic)
    #print(stringg)    
    #print(list2)
    return list2
    

#expansion

def expand(x,y,macro_name,argtab,nametab2,list1):
    counttt=1
    alist=[]
    blist=[]
    dictt={}
    rcount=0
    dictt=argtab[rcount][1]
    #print(dictt)
    #print(argtab)
    alist=list(dictt.keys())
    blist=list(dictt.values())
    #print(alist)
    #print(blist)
    if(x==y):                              #condition for single line defination
        string=list1[x-1]                  #as here the content is in the same line so x-1 i.e line no-1
        if "<#" in list1[x-1]:             #remove comments
            yo=list1[x-1].find("<#")
            yo2=list1[x-1].find("#>")
            yui=string[yo:(yo2+2)]
            string=string.replace(yui,"")

        string=string.replace("@@ENDD","")
        yo=string.find(")")
        str2=string[0:yo+1]
        string=string.replace(str2,"")
        for n in range(0,len(alist)):
            if alist[n] in list1[x-1]:
                string=string.replace(alist[n],blist[n])
        string=string+'\n'
        out.write(string)
    ###
    ######################################################for if-else-enif###############################
    var1,var2,var3,flag=0,0,0,23# set default values
    var3=x
    symbol=";"
    strr="xyz"
    ##
    
    temp=x
    countr=0        #countr=3 for iff,elsee,endif
    while(countr!=3 and temp!=y):
    	if "iff" in list1[temp]:
    		var1=temp
    		countr=countr+1
    		#print('11',temp)
    	if "elsee" in list1[temp]:
    		var2=temp
    		countr=countr+1
    		#print('22',temp)
    	if "endif" in list1[temp]:
    		var3=temp
    		countr=countr+1
    		#print('33',temp)
    	temp=temp+1
    #print(var1,var2,var3)
    if (var1!=0):
    	strr=list1[var1]
    	if "GREATER" in strr:
	    	symbol='>'
    	if "LESS" in strr:
    		symbol='<'
    	if "GREATER_EQUAL" in strr:
    		symbol='>='
    	if "LESS_EQUAL" in strr:
    		symbol='<='
    	if "EQUAL" in strr:
    		symbol='=='
    	if "NOT_EQUAL" in strr:
    		symbol='!='
    	
    
    	newlist=[]
    	#print(var1,var2,var3)
    	for n in range(0,len(alist)):
    		if alist[n] in list1[var1]:
    			newlist.append(alist[n])
    			newlist.append(blist[n])
    	tut1=int(newlist[1])#store first variable for checking comparison
    	tut2=int(newlist[3])#store second variable for checking comparison
    	if (symbol==">"):
    		if tut1>tut2:
    			flag=1
    		else:
    			flag=0
    	if (symbol=="<"):
    		if tut1<tut2:
    			flag=1
    		else:
    			flag=0
    	if (symbol==">="):
    		if tut1>=tut2:
    			flag=1
    		else:
    			flag=0
    	if (symbol=="<="):
    		if tut1<=tut2:
    			flag=1
    		else:
    			flag=0
    	if (symbol=="=="):
    		if tut1==tut2:
    			flag=1
    		else:
    			flag=0
    	if (symbol=="!="):
    		if tut1!=tut2:
    			flag=1
    		else:
    			flag=0

    	if(flag==1):    #when if is true,expand if part
    		var1=var1+1
    		while(var1!=var2):
    			string=list1[var1]
    			if "<#" in list1[var1]:
    				yo=list1[var1].find("<#")
    				yo2=list1[var1].find("#>")
    				yui=string[yo:(yo2+2)]
    				string=string.replace(yui,"")
    			for n in range(0,len(alist)):
    				if alist[n] in list1[var1]:
    					string=string.replace(alist[n],blist[n])
    			string=string+'\n'
    			out.write(string)
    			var1=var1+1
           	
    	
    	elif(flag==0):      #when if is false,expand else part
    		var2=var2+1
    		while(var2!=var3):
    			string=list1[var2]
    			if "<#" in list1[var2]:
    				yo=list1[var2].find("<#")
    				yo2=list1[var2].find("#>")
    				yui=string[yo:(yo2+2)]
    				string=string.replace(yui,"")
    			for n in range(0,len(alist)):
    				if alist[n] in list1[var2]:
    					string=string.replace(alist[n],blist[n])
    			string=string+'\n'
    			out.write(string)
    			var2=var2+1
    	x=var3+1#only in iff case next line should be after index of endif
    	#print(list1[x])
    #####
    ######################################################for while###############################
    
    if "WHILEE" in list1[x]:
        
        temp=x
        strr=list1[x]
        if "GREATER" in strr:
            symbol='>'
        if "LESS" in strr: 
            symbol='<'
        if "GREATER_EQUAL" in strr:
            symbol='>='
        if "LESS_EQUAL" in strr: 
            symbol='<='
        if "NOT_EQUAL" in strr:
            symbol='!='
    	
        newlist=[]
        loopcount=0
        for n in range(0,len(alist)):
            if alist[n] in list1[x]:
                newlist.append(alist[n])
                newlist.append(blist[n])
        tut1=int(newlist[1])
        tut2=int(newlist[3])
        #print(tut1,tut2)
        if (symbol==">"):
            if tut1>tut2:
                loopcount=tut1-tut2
                flag=1
            else:
                flag=0
        if (symbol=="<"):
            if tut1<tut2:
                loopcount=tut2-tut1
                flag=1
            else:
                flag=0
        if (symbol==">="):
            if tut1>=tut2:
                loopcount=tut1-tut2+1
                flag=1
            else:
                flag=0
        if (symbol=="<="):
            if tut1<=tut2:
                loopcount=tut2-tut1+1
                
                flag=1
            else:
                flag=0
        if (symbol=="!="):
            if tut1!=tut2:
                if(tut1>tut2):
                    loopcount=tut1-tut2
                elif(tut2>tut1):
                    loopcount=tut2-tut1
                flag=1
            else:
                flag=0
        x=x+1
        #print(loopcount)
        #print(flag)
        listwhile=[]        #list containg the statements inside while for repetition
        if(flag==0):#while's inside condition is not solvable so no expansion
            while(1):
                if "ENDWHIL" in list1[x]:
                    x=x+1
                    break
                x=x+1
        else:
            while(1):
                if "ENDWHIL" in list1[x]:
                    x=x+1
                    break
                if "INRR" in list1[x]:
                    pass
                elif "DCRR" in list1[x]:
                    pass
                else:
                    listwhile.append(list1[x])
                    #print(listwhile)
                x=x+1
    
        #print(listwhile)
        templen=len(listwhile)
        #print(loopcount)
        for i in range(loopcount):#loop the listwhile the number of times we calculate the while loop run i.e loopcount times
            mrp=0
            for j in range(templen):
                string=listwhile[mrp]
                if "<#" in list1[mrp]:
                    yo=listwhile[mrp].find("<#")
                    yo2=listwhile[mrp].find("#>")
                    yui=string[yo:(yo2+2)]
                    string=string.replace(yui,"")
                for n in range(0,len(alist)):
                    if alist[n] in listwhile[mrp]:
                        string=string.replace(alist[n],blist[n])
                string=string+'\n'
                out.write(string)
                mrp=mrp+1
    
            
     
    #########################################for normal expansion without conditional or single line defination
    while(counttt!=0 and x!=y):#countt take care of nested 
        '''if "///" in list1[x]:
            x=x+1
            continue'''
        if 'BEGIN' in list1[x]:
            rcount=rcount+1
            x=x+1
            counttt=counttt+1
            alist=[]
            blist=[]
            dictt={}
            dictt=argtab[rcount][1]
            alist=list(dictt.keys())
            blist=list(dictt.values())
            #change acc to new macro name a and b list
            continue
        elif 'END' in list1[x]:
            counttt=counttt-1
            x=x+1
        else:
            string=list1[x]
            if "<#" in list1[x]:
                yo=list1[x].find("<#")
                yo2=list1[x].find("#>")
                yui=string[yo:(yo2+2)]
                string=string.replace(yui,"")
            for n in range(0,len(alist)):
                if alist[n] in list1[x]:
                    string=string.replace(alist[n],blist[n])
            string=string+'\n'
            out.write(string)
            x=x+1
#________________________________________________________________         
        

#from here start reading and expanding

f=nametab[index-1][2]                               #reading start
nametab2=nametab                                    #for updation of nested macro
mcroname=[]                                         #for macro names
for h in range(len(nametab2)):
    mcroname.append(nametab[h][0])
#print(mcroname)#store only macro name
#print(nametab2)
while(f<len(list1)):
    countt=0
    argtab=[]                   #argtab new for every new call therefore its index always start with 0 in expand  #null agian as new macro call arrives
    if "(" in list1[f]:                             #if there is macro call
        countt=1
        z=list1[f].find('...')
        ind=list1[f].find('(')
        tempo=list1[f][z+3:ind-4]                   #take macro name
        #print(tempo)
        for h in range(len(nametab2)):
            if tempo==nametab2[h][0]:               #macro found
                
                arg=parameter(nametab2,list1[f],list1)   #for not nested
                argtab.append(arg)
                x=nametab2[h][1]-1                  #as index is 1 less than line number
                y=nametab2[h][2]
                x=x+1
                while(countt!=0 and x!=y):          #countt take care of nested
                    '''if ("/**" or "**/") in list1[x]:
                        x=x+1
                        pass'''
                    if 'BEGIN' in list1[x]:
                        arg=parameter(nametab2,list1[x],list1)       ##for nested
                        argtab.append(arg)
                        countt=countt+1
                        tempolist=[]                #for making list of new macro
                        z=list1[x].find('...')
                        ind=list1[x].find('(')
                        macro_name=list1[x][z+3:ind-4]
                        if macro_name in mcroname:
                            pass
                        else:
                        
                            tempolist.append(macro_name)    #tempolist for new macro
                            mcroname.append(macro_name)
                            tempolist.append(x+1)
                        
                            qwer=0
                            tempp=x+1
                            while(qwer!=-1):
                                if 'BEGIN' in list1[tempp]:
                                    qwer=qwer+1
                                elif 'END' in list1[tempp]:
                                    qwer=qwer-1
                                tempp=tempp+1
                            tempolist.append(tempp)
                            nametab2.append(tempolist)
                        
                    elif 'END' in list1[x]:
                        countt=countt-1
                       
                    x=x+1
                expand(nametab2[h][1],nametab2[h][2],nametab2[h][0],argtab,nametab2,list1)
            else:
                pass
        f=f+1
    else:           #if there is no macro call then as it write to outfile
        #print(list1[f])
        list1[f]=list1[f]+'\n'
        out.write(list1[f])
        f=f+1;
inp.close()
out.close()
deftab.close()
