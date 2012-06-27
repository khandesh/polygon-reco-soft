#file:///C:/Users/Administrator/Desktop/d.htm
#A Split/Merge Method with Ranking Selection
#for Polygonal Approximation of Digital Curve
#vertic=input("enter the no. of vertices in the polygon\n")
def ast(A,file="d7.png"):
	vertic=A
	C=2
	import random
	import math
	from numpy import math
	import Image;
	im=Image.open(file);
	#Image.open("d3.png").show()
	im=im.convert("1");
	import ImageFilter
#im.show()
#kernel=[1.0/273,4.0/273,7.0/273,4.0/273,1.0/273,4.0/273,16.0/273,26.0/273,16.0/273,4.0/273,7.0/273,26.0/273,41.0/273,26.0/273,7.0/273,4.0/273,16.0/273,26.0/273,16.0/273,4.0/273,1.0/273,4.0/273,7.0/273,4.0/273,1.0/273]
#fv=ImageFilter.Kernel((5,5), kernel, scale=None, offset=0)
#im=im.filter(fv)
#im.show()
	t=im.size;
	print im.size
	t1=t[0];
	t2=t[1];
	flag=0
	orient=0;

	for i in range(0,t1):
		for j in range(0,t2):
			if ((im.getpixel((i,j)))==0):
				if((im.getpixel((i-1,j)))and(im.getpixel((i-1,j+1)))and(im.getpixel((i+1,j+1)))and((not(im.getpixel((i-1,j-1))))or(not(im.getpixel((i,j-1))))or(not(im.getpixel((i+1,j-1)))))):
					orient=0
					flag=1
					break
				elif((im.getpixel((i,j-1)))and(im.getpixel((i-1,j-1)))and(im.getpixel((i-1,j+1)))and((not(im.getpixel((i+1,j-1))))or(not(im.getpixel((i+1,j))))or(not(im.getpixel((i+1,j+1)))))):
					orient=1
					flag=1
					break
				elif((im.getpixel((i+1,j)))and(im.getpixel((i+1,j-1)))and(im.getpixel((i-1,j-1)))and((not(im.getpixel((i,j+1))))or(not(im.getpixel((i-1,j+1))))or(not(im.getpixel((i+1,j+1)))))):
					orient=2
					flag=1
					break
				elif((im.getpixel((i,j+1)))and(im.getpixel((i+1,j+1)))and(im.getpixel((i+1,j-1)))and((not(im.getpixel((i-1,j+1))))or(not(im.getpixel((i-1,j))))or(not(im.getpixel((i-1,j-1)))))):
					orient=3
					flag=1
					break
		
		if flag==1:
			break
	




	bc=[]
	s=[(i,j)]
	p=s
	flag==1
	while flag==1:
		i=p[0][0]
		j=p[0][1]
		if(orient==0):
			if(im.getpixel((i-1,j-1))==0):
				bc=bc+[(i-1,j-1)]
				p=[(i-1,j-1)]
				orient =3
			
			elif(im.getpixel((i,j-1))==0):
				bc=bc+[(i,j-1)]
				p=[(i,j-1)]
				orient=0
			
			elif(im.getpixel((i+1,j-1))==0):
				bc=bc+[(i+1,j-1)]
				p=[(i+1,j-1)]
				orient =0
			
			else:
				orient=orient+1
				orient=orient%4
				continue
	
		elif(orient==1):
			if(im.getpixel((i+1,j-1))==0):
				bc=bc+[(i+1,j-1)]
				p=[(i+1,j-1)]
				orient =0
			
			elif(im.getpixel((i+1,j))==0):
				bc=bc+[(i+1,j)]
				p=[(i+1,j)]
				orient=1
			
			elif(im.getpixel((i+1,j+1))==0):
				bc=bc+[(i+1,j+1)]
				p=[(i+1,j+1)]
				orient =1
			else:
				orient=orient+1
				orient=orient%4
				continue
	
		elif(orient==2):
			if(im.getpixel((i+1,j+1))==0):
				bc=bc+[(i+1,j+1)]
				p=[(i+1,j+1)]
				orient =1
			
			elif(im.getpixel((i,j+1))==0):
				bc=bc+[(i,j+1)]
				p=[(i,j+1)]
				orient=2
			
			elif(im.getpixel((i-1,j+1))==0):
				bc=bc+[(i-1,j+1)]
				p=[(i-1,j+1)]
				orient =2
			
			else:
				orient=orient+1
				orient=orient%4
				continue
		elif(orient==3):
			if(im.getpixel((i-1,j+1))==0):
				bc=bc+[(i-1,j+1)]
				p=[(i-1,j+1)]
				orient =2
			elif(im.getpixel((i-1,j))==0):
				bc=bc+[(i-1,j)]
				p=[(i-1,j)]
				orient=3
			elif(im.getpixel((i-1,j-1))==0):
				bc=bc+[(i-1,j-1)]
				p=[(i-1,j-1)]
				orient =3
			else:
				orient=orient+1
				orient=orient%4
				continue
	
	
		if(p==s):
			flag=0	
	print "len(bc)=",len(bc)
	def select(m,a):
		z=[]
		t=1
		for d in range(1,m+1):
			z=z+[t]
			t=t*((math.e)**(-2/d))
			#t=d+1
		p=random.uniform(0,sum(z))
		for c in range(1,m+1):
			p=p-z[c-1]
			if (p<0): break
		if(a>0):return (a%m)
		return ((c-1)%m)
	#return 0
	#return random.choice(range(0,m))
	def line(p1,p2):
		x1=p1[0]
		y1=p1[1]
		x2=p2[0]
		y2=p2[1]
		c1=(y1-y2)
		c2=(x2-x1)
		c3=(x1*y2-x2*y1)
		return [c1,c2,c3]
	def dist(point,lin):
		x=point[0]
		y=point[1]
		A=lin[0]
		B=lin[1]
		C=lin[2]
		if not A and not B:
			return 100000000000000000000000000000000000
		return ((abs(A*x+B*y+C))/(math.sqrt(A*A+B*B)))
	def criteria(f):
		return -f[1]
	def split(poly,bc,a):
		k=len(poly)
		split_index=[]
		i1=0
		i2=poly[0]
		p1=bc[i1]
		p2=bc[i2]
		l=line(p1,p2)
		for cou in range(i1,i2):
			p=bc[cou]
			d=dist(p,l)
			split_index=split_index+[[cou,d]]
		for v in range(0,k-2):
			i1=poly[v]
			i2=poly[v+1]
			p1=bc[i1]
			p2=bc[i2]
			l=line(p1,p2)
			for cou in range(i1+1,i2):
				p=bc[cou]
				d=dist(p,l)
				split_index=split_index+[[cou,d]]
		i1=poly[-1]
		i2=len(bc)-1
		p1=bc[i1]
		p2=bc[i2]
		p1=bc[i1]
		p2=bc[i2]
		l=line(p1,bc[0])
		for cou in range(i1,i2+1):
			p=bc[cou]
			d=dist(p,l)
			split_index=split_index+[[cou,d]]
		split_index=sorted(split_index,key=criteria)
		num=select(len(split_index),a)
		splitted=split_index[num][0]
		poly=poly+[splitted]
		poly=sorted(poly)
		return poly
	#print "poly returned after splitting=",poly
	def merge(poly,bc,a):
		arr=[]
		o=len(poly)
		for index in range(0,o):
			p1=bc[poly[(index-1)%o]]
			p2=bc[poly[(index+1)%o]]
			l=line(p1,p2)
			d=dist(bc[poly[index]],l)
			arr=arr+[[poly[index],1/(d+0.001)]]
		arr=sorted(arr,key=criteria)
		n=select(len(arr),a)
		arr.pop(n)
		poly=[]
		for tj in arr:
			poly=poly+[tj[0]]
		poly=sorted(poly)
		return poly
	#print "poly returned after merging=",poly
#program starts now
	def error(poly,bc):
		k=len(poly)
		error=0
		i1=0
		i2=poly[0]
		p1=bc[i1]
		p2=bc[i2]
		l=line(bc[poly[-1]],bc[poly[0]])
		for cou in range(0,i2):
			p=bc[cou]
			d=dist(p,l)
			error=error+(d*d)
		for v in range(0,k-1):
			i1=poly[v]
			i2=poly[v+1]
			p1=bc[i1]
			p2=bc[i2]
			l=line(p1,p2)
			for cou in range(i1,i2):
				p=bc[cou]
				d=dist(p,l)
				error=error+(d*d)
		i1=poly[-1]
		i2=len(bc)-1
		p1=bc[i1]
		p2=bc[i2]
		l=line(bc[poly[-1]],bc[poly[0]])
		for cou in range(i1,i2):
			p=bc[cou]
			d=dist(p,l)
			error=error+(d*d)
		return error
	s=[]
	bc1=[]
	for xy in range (0,len(bc),2):
		bc1=bc1+[bc[xy]]
	bc=bc1
	for r in range(1,300):
		V=sorted(random.sample(range(0,len(bc)),vertic))
		#print "startingV=",error(V,bc)
		k=0
		count=0
		a=0
		flag=0
		u=[]
		while(k<=100):
			if(k>=0 and k<3):
				u=u+[V]
			if(k==3):
				if u[2][1]>(0.3*(u[0][1])):break
			B=[]
			if(flag==1):
				a=a+1
			else:
				a=0
			B=B+V
			V=split(V,bc,a)
			V=merge(V,bc,a)
			errorv=error(V,bc)
			errorb=error(B,bc)
			if (V==B): flag=1
			elif errorv>errorb:
#			print error(V,bc)
				V=[]
				V=V+B
			else:
				if (errorb>(errorv+2000)) or (errorv<2000):
					flag=0
			k=k+1
		s=s+[[V,error(V,bc)]]
	#	print V,"error:",error(V,bc)
	def de(ce):
		return ce[1]
	s=sorted(s,key=de)

	V=s[0][0]
#print "finally V=",V
#print "length of bc=",len(bc)
	#import ImageDraw
	#draw=ImageDraw.Draw(im)
	xc=len(V)
	pr=[]
	for g in range(0,len(V)):
		pr=pr+[[bc[V[g]][0],bc[V[g]][1]]]	
	#print pr
	return pr
	#im.save('best.jpg')
	#print error(V,bc)
	#Image.open('best.jpg').show()
#ast(4)