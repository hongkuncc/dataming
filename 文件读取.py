f=open(r'write.txt','w')
f.write('hello,world!')
f.close()
f=open('write.txt','r')
p1=f.read(5)
p2=f.read()
print p1,p2
