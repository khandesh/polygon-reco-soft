def rsw(file='d7.png'):
	C=2
	import math
	from numpy import math
	import Image;
	im=Image.open(file);
	#Image.open("d3.png").show()
	im=im.convert("1");
	t=im.size;
	t1=t[0];
	t2=t[1];
	flag=0
	orient=0;
	import math
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
	index=0
	while flag==1:
		index=index+1
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
	
#	print p
		#if(p==s) or (math.sqrt((p[0][0]-s[0][0])**2+(p[0][1]-s[0][1])**2)<5 and index>90):
		#if(p==s) or ((p==ds) and math.sqrt((p[0][0]-s[0][0])**2+(p[0][1]-s[0][1])**2)<10):
		if(p==s):
			flag=0

	import numpy as np
	#import matplotlib.pyplot as plt
	#for d in bc:
		#plt.plot(d[0],d[1],'r.')
#plt.show()
	

	print "START POINT WAS" ,s
#import numpy as np
	import ImageDraw
	out=Image.open("d1.png")
	draw=ImageDraw.Draw(out)
	for r in range (0,len(bc)):
		draw.line((bc[r][0],bc[r][1],bc[(r+1)%len(bc)][0],bc[(r+1)%len(bc)][1]),fill=128)
	out.save('output.jpg')
	corner=[]
	k=[]
	w=len(bc)
	for i in range(0,len(bc)):
		a1=(bc[(i+1)%w][0]-bc[(i-1)%w][0])/2
	#print a1
		a2=(bc[(i+1)%w][1]-bc[(i-1)%w][1])/2
		a3=((bc[(i+2)%w][0]-bc[i][0])-(bc[i][0]-bc[(i-2)%w][0]))/2
		a4=((bc[(i+2)%w][1]-bc[i][1])-(bc[i][1]-bc[(i-2)%w][1]))/2
	#print (a1*a4-a3*a2)/((a1*a1+a2*a2)**(1.5))
		if a1 or a2:
			k=k+[[bc[i][0],bc[i][1],(a1*a4-a3*a2)/((a1*a1+a2*a2)**(1.5))]]
		else:
			corner=corner+[[bc[i][0],bc[i][1]]]
	
	for g in k:
		if g[2]:
			corner=corner+[[g[0],g[1]]]
#for g in k:
#	if g[2]:
#		print g
#for g in corner:
#	print g
	


	thr=[];
	dg=len(k)
	L1=[]
	L2=[]
	f=lambda a,b:a+b
	dg=len(k)
	for i in range(0,len(k)):
		s=0
		while k[(i-s)%dg][2]>k[(i-s-1)%dg][2]:
			s=s+1
#	L1=L1+[(i-s)%dg]
		L1=L1+[15]
		s=0
		while k[(i+s)%dg][2]>k[(i+s+1)%dg][2]:
			s=s+1
#	L2=L2+[(i+s)%dg]
		L2=L2+[15]
	thr=[]
	fc=[]
	for t in range(0,dg):
#	u1=((L1[t])%dg)
#	u2=(L2[t]+1)%dg
		u1=(t-15)%dg
		u2=(t+15)%dg
		y=0
		for q in k[u1:u2]:
			y=y+q[2]
		thr=thr+[[k[t][0],k[t][1],(1.5*y)/(L1[t]+L2[t]+1)]]
		A1=k[u1][0]
		B1=k[u1][1]
		A2=k[(u1+t)/2][0]
		B2=k[(u1+t)/2][1]
		A3=k[t][0]
		B3=k[t][1]
		if (A1*(B2-B3)+A2*(B3-B1)+A3*(B1-B2))==0:
			theta=math.atan2(B1-B3,A1-A3)
		
		
		else :
			A0=((((A1*A1)+(B1*B1))*(B2-B3))+(((A2*A2)+(B2*B2))*(B3-B1))+(((A3*A3)+(B3*B3))*(B1-B2)))/(2*(A1*(B2-B3)+A2*(B3-B1)+A3*(B1-B2)))
			B0=((((B1*B1)+(A1*A1))*(A2-A3))+(((B2*B2)+(A2*A2))*(A3-A1))+(((B3*B3)+(A3*A3))*(A1-A2)))/(2*(B1*(A2-A3)+B2*(A3-A1)+B3*(A1-A2)))
			theta=math.atan2(B0-k[t][1],A0-k[t][0])
		phi=math.atan2(B2-B3,A2-A3)
		xi1=theta+(sgn(math.sin(phi-theta)))*(math.pi/2)
		A4=k[u2][0]
		B4=k[u2][1]
		A5=k[(u2+t)/2][0]
		B5=k[(u2+t)/2][1]
		A3=k[t][0]
		B3=k[t][1]
		if (A4*(B5-B3)+A5*(B3-B4)+A3*(B4-B5))==0:
			theta=math.atan2(B4-B3,A4-A3)
		else :
			A0=((((A4*A4)+(B4*B4))*(B5-B3))+(((A5*A5)+(B5*B5))*(B3-B4))+(((A3*A3)+(B3*B3))*(B4-B5)))/(2*(A4*(B5-B3)+A5*(B3-B4)+A3*(B4-B5)))
			B0=((((B4*B4)+(A4*A4))*(A5-A3))+(((B5*B5)+(A5*A5))*(A3-A4))+(((B3*B3)+(A3*A3))*(A4-A5)))/(2*(B4*(A5-A3)+B5*(A3-A4)+B3*(A4-A5)))
			theta=math.atan2(B0-B3,A0-A3)
		phi=math.atan2(B5-B3,A5-A3)
		xi2=theta+((sgn(math.sin(phi-theta)))*(math.pi/2))
		xi1=xi1*(180/math.pi)
		xi2=xi2*(180/math.pi)
		if(abs(xi1-xi2)<(180)):
			tu=abs(xi1-xi2)
		else:
			tu=360-(abs(xi1-xi2))
		fc=fc+[[k[t][0],k[t][1],tu]]
	
	coner=[]
	for r in range(0,dg):
		if fc[r][2]<145:
			coner=coner+[[fc[r][0],fc[r][1]]]

	q=[]
			#	Finding start corner
	n=0			
	for d in range(0,len(coner)):
			if ((math.sqrt((coner[d][0]-coner[(d+1)%len(coner)][0])**2+(coner[d][1]-coner[(d+1)%len(coner)][1])**2)<10) and math.sqrt((coner[d][0]-coner[(d-1)%len(coner)][0])**2+(coner[d][1]-coner[(d-1)%len(coner)][1])**2)>10):
				n=d
				break
	import math
	x=[]

	for f in range(n,len(coner)+n):
		d=f%len(coner)
		if((math.sqrt((coner[d][0]-coner[(d+1)%len(coner)][0])**2+(coner[d][1]-coner[(d+1)%len(coner)][1])**2)) > 10)and (math.sqrt((coner[d][0]-coner[(d-1)%len(coner)][0])**2+(coner[d][1]-coner[(d-1)%len(coner)][1])**2)) > 10:
			q=q+[[coner[d][0],coner[d][1]]]
			continue
		if(math.sqrt((coner[d][0]-coner[(d+1)%len(coner)][0])**2+(coner[d][1]-coner[(d+1)%len(coner)][1])**2)) > 10:
			if  (len(x)):
				v=len(x)
				q=q+[[x[v/2][0],x[v/2][1]]]
				x=[]
		else:
			x=x+[[coner[d][0],coner[d][1]]]
#for r in fc[200:300]:
#	if(r[2]>5):
#		print r

#for i in range(0,len(k)):
#	print i-(L1[i])
#print len(fc)
	t=[]
	xz=len(q)
	b=0
	flag=1
	while(b<xz):
		if(flag==1):
			c1=q[(b-1)%len(q)][0]
			c2=q[(b-1)%len(q)][1]
		else:
			c1=t[-1][0]
			c2=t[-1][1]
		f=math.atan2(q[(b+1)%len(q)][1]-q[b][1],q[(b+1)%len(q)][0]-q[b][0])
		g=math.atan2(c2-q[b][1],c1-q[b][0])
		h=abs(f-g)
		h=h*(180/math.pi)
		if(h<180):
			i=h
		else:
			i=360-h
		if i<162 and i>5:
			t=t+[[q[b][0],q[b][1]]]
			flag=0
		print i
		b=b+1
	q=t
	coner=[]
	side=[]
	wz=len(q)
	for vf in range(0,wz):
		p1=q[vf]
		p2=q[(vf+1)%wz]
		side=side+[math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)]
	thre=(max(side))*0.1
	cand=[]
	for vf in range(0,wz):
		if side[vf]<(thre):
			cand=cand+[q[vf],q[(vf+1)%wz]]
	cb=[]
	for rg in q:
		if not(rg in cand):
			cb=cb+[rg]
	q=cb
	print "q=",len(q)
	for cx in q:
		print cx
	import ImageDraw
	return q
	#out1=Image.open("l.png")	
	#draw=ImageDraw.Draw(out1)

	#for r in range (0,len(q)):
		#draw.line((q[r][0],q[r][1],q[(r+1)%len(q)][0],q[(r+1)%len(q)][1]),fill=128)
	#draw.line((q[r][0],200-(q[r][1]),q[(r+1)%len(q)][0],200-(q[(r+1)%len(q)][1])),fill=128)
	#out1.save('output1.jpg')
	#Image.open("output1.jpg").show()
def sgn(t):
	if t>0: return 1
	if t<0: return -1
	return 0