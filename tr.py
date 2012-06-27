from math import *
# Determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. This fuction

def point_in_poly(pt,poly):
	x=pt.real
	y=pt.imag
	n = len(poly)
	inside = False

    #p1x,p1y = poly[0]
	p1x=poly[0].real
	p1y=poly[0].imag
	for i in range(n+1):
        #p2x,p2y = poly[i % n]
		p2x=poly[i%n].real
		p2y=poly[i%n].imag
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xinters:
						inside = not inside
		p1x,p1y = p2x,p2y

	return inside

def deg2rad(angle):
	tf=[]
	for x in range(0,len(angle)):
		tf=tf+[angle[x]*(pi/180)]
	return tf
def rad2deg(angle):
	tf=[]
	for x in range(0,len(angle)):
		tf=tf+[angle[x]*(180/pi)]
	return tf
def nonreflex_angle(p1,p2,p3):
	f1=atan2(p1.imag-p2.imag,p1.real-p2.real)
	f2=atan2(p3.imag-p2.imag,p3.real-p2.real)
	ang=-(f1-f2)
	#if(ang>pi): ang=2*pi-ang
	return ang
def mesur(p1,p2,p3,poly):
	f1=atan2(p1.imag-p2.imag,p1.real-p2.real)
	f2=atan2(p3.imag-p2.imag,p3.real-p2.real)
	return nonreflex_angle(p1,p2,p3)
def length(side,angle):
	#if(len(angle)==0): return [side[0],0,0]
	pt=[0+0j,side[0]+0j]
	n=len(angle)
	dir=0
	for i in range(0,n):
		dir=dir+(pi-angle[i])
		z=(e**(0+(dir)*(0+1j)))
		pt=pt+[(pt[i+1]+0j)+side[i+1]*z]
	w1=abs(pt[-1])
	w2=mesur(pt[1],pt[0],pt[-1],pt)
	w3=mesur(pt[0],pt[-1],pt[-2],pt)
	return [w1,w2,w3]
def points(side,angle):
	angle=deg2rad(angle)
	pt=[0+0j,side[0]+0j]
	n=len(angle)
	dir=0
	for i in range(0,n):
		#print "angel[i]=",angle[i]
		dir=dir+(pi-angle[i])
		print "dir=",dir
		z=(e**(0+(dir)*(0+1j)))
		#print "side[i+1]=",side[i+1]
		pt=pt+[(pt[i+1])+side[i+1]*z]
	pnt=[]
	for x in pt:
		pnt=pnt+[[x.real,x.imag]]
	return pnt
def occur(array):
	i=0
	g=[]
	for x in range(0,len(array)):
		if((array[x]==0)):
			g=g+[x]
	return g
def cyclic(a,b,n):
	c=[]
	r=a
	while(1):
		c=c+[r]
		if (r==b): break
		r=(r+1)%n
	return c
def poly(side,angle):
	anglef=occur(angle)
	angled=angle
	angle=deg2rad(angle)
	n=len(side)
	sidef=occur(side)
	nside=len(sidef)
	nangle=len(anglef)
	if(nside==0 and nangle==3):
		a1=anglef[0]
		a2=anglef[1]
		a3=anglef[2]
		
		ar=cyclic(a1,a2,n)
		lt=len(ar)
		sid=[]
		ang=[]
		for x in range(0,lt-1):
			if(x==0):
				sid=sid+[side[ar[x]]]
				continue
			sid=sid+[side[ar[x]]]
			ang=ang+[angle[ar[x]]]
		zo=rad2deg(ang)
		print "DSffddf=",sid,zo
		tr1=length(sid,ang)
		ar=cyclic(a2,a3,n)
		lt=len(ar)
		sid=[]
		ang=[]
		for x in range(0,lt-1):
			if(x==0):
				sid=sid+[side[ar[x]]]
				continue
			sid=sid+[side[ar[x]]]
			ang=ang+[angle[ar[x]]]
		print "DSffddf=",sid,rad2deg(ang)
		tr2=length(sid,ang)
		ar=cyclic(a3,a1,n)
		lt=len(ar)
		sid=[]
		ang=[]
		for x in range(0,lt-1):
			if(x==0):
				sid=sid+[side[ar[x]]]
				continue
			sid=sid+[side[ar[x]]]
			ang=ang+[angle[ar[x]]]
		print "DSffddf=",sid,rad2deg(ang)
		tr3=length(sid,ang)
		l1=tr1[0]
		l2=tr2[0]
		l3=tr3[0]
		ub1=(l1*l1+l3*l3-l2*l2)/(float(2*l1*l3))
		if ub1>1 or ub1<-1:
			return ["MATHEMATICAL ERROR"]
		else:
			s1=acos(ub1)
		ub2=(l2*l2+l1*l1-l3*l3)/(float(2*l2*l1))
		if ub2>1 or ub2<-1:
			return ["MATHEMATICAL ERROR"]
		else:
			s2=acos(ub2)
		ub3=(l3*l3+l2*l2-l1*l1)/(float(2*l3*l2))
		if ub3>1 or ub3<-1:
			return ["MATHEMATICAL ERROR"]
		else:
			s3=acos(ub3)
		ans1=s1+tr3[2]+tr1[1]
		ans2=s2+tr1[2]+tr2[1]
		ans3=s3+tr2[2]+tr3[1]
		#print [ans1*180/pi,ans2*180/pi,ans3*180/pi]
		return [[],[ans1*180/pi,ans2*180/pi,ans3*180/pi]]
	if(nside==2 and nangle==1):
		bag=(n-2)*(pi)-(sum(angle))
		angle[anglef[0]]=bag
		if(not(sidef[0]-sidef[1]+1)%n) or (not (sidef[0]-sidef[1]-1)%n):
			if sidef[1]==(n-1) and sidef[0]==0:
				sidef[0],sidef[1]=sidef[1],sidef[0]
			a1=sidef[0]
			a2=(sidef[1]+1)%n
			ar=cyclic(a2,a1,n)
			lt=len(ar)
			sid=[]
			ang=[]
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			tr=length(sid,ang)
			lp=tr[0]
			g0=angle[a1]-tr[2]
			g1=angle[a2]-tr[1]
			g2=angle[sidef[1]]
			a0=lp*((sin(g1))/(sin(g2)))
			b0=lp*((sin(g0))/(sin(g2)))
			if sidef[1]==0 and sidef[0]==n-1:
				a0,b0=b0,a0
			return [[a0,b0],[bag*(180/pi)]]
		un=[]
		sid=[]
		ang=[]
		a1=sidef[0]
		a2=(sidef[0]+1)%n
		b1=sidef[1]
		b2=(sidef[1]+1)%n
		#ar=cyclic(a2,b1,n)[0]
		ar=cyclic(a2,b1,n)
		lt=len(ar)
		for x in range(0,lt-1):
			if(x==0):
				sid=sid+[side[ar[x]]]
				continue
			sid=sid+[side[ar[x]]]
			ang=ang+[angle[ar[x]]]
		tr=length(sid,ang)
		un=un+[tr[0]]
		m3=angle[a2]-tr[1]
		m2=angle[b1]-tr[2]
		sid=[]
		ang=[]
		ar=cyclic(b2,a1,n)
		lt=len(ar)
		for x in range(0,lt-1):
			if(x==0):
				sid=sid+[side[ar[x]]]
				continue
			sid=sid+[side[ar[x]]]
			ang=ang+[angle[ar[x]]]
		tr=length(sid,ang)
		un=un+[tr[0]]
		print "un=",un
		ar=tr[0]
		m1=angle[b2]-tr[1]
		m0=angle[a1]-tr[2]
		print "AAAAAAAAAAAAa:  ",angle[a1],angle[a2],angle[b1],angle[b2]
		A1=-cos(m3)
		B1=-cos(m2)
		C1=un[0]+un[1]*cos(m1+m2)
		A2=-sin(m3)
		B2=sin(m2)
		print "consr angles are",[m0*180/pi,m1*180/pi,m2*180/pi,m3*180/pi]
		print "sum=",sum([m0,m1,m2,m3])*(180/pi)
		C2=-un[1]*(sin(m1+m2))
		cx=(B1*C2-B2*C1)/(A1*B2-A2*B1)
		cy=(C1*A2-C2*A1)/(A1*B2-A2*B1)
		print "cx=",cx,"cy=",cy
		if(cx>1000 or cy>1000): return ["MATHEMATICAL ERROR"]
		if(cx<0.001 or cy<0.001): return ["DATA INSUFFICIENT"]
		return [[cx,cy],[bag*(180/pi)]]
	if(nside==1 and nangle==2):
		chek=0
		i1=sidef[0]
		i2=(sidef[0]+1)%n
		initial=i2
		while(1):
			if(initial==anglef[0]):
				reference=0
				break
			if(initial ==anglef[1]):
				reference=1
				break
			initial=(initial+1)%n
		i3=anglef[reference]
		i4=anglef[1-reference]
		if i4<i3 : chek=1
		print i1,i2,i3,i4
		mor=[]
		if(i2==i3):
			mor=mor+[1]
		else:
			mor=mor+[0]
		if(i4==i1):
			mor=mor+[1]
		else:
			mor=mor+[0]
		if(mor[0]==0 and mor[1]==1):
			i1=i2
		if((mor[0]==1 and mor[1]==0)):
			sid=[]
			ang=[]
			ar=cyclic(i3,i4,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			so1=length(sid,ang)
			sid=[]
			ang=[]
			ar=cyclic(i4,i1,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			#print "sid=",sid
			#print "ang=",ang
			so2=length(sid,ang)
			s1=so1[0]
			s2=so2[0]
			print "i1=",i1,"i3=",i3,"i4=",i4
			a1=angle[i1]-so2[1]
			import numpy
			pl=numpy.poly1d([1.0,-2*(cos(a1))*s2,float(s2*s2-s1*s1)])
			pu=pl.r
			print "pu=",pu
			pu0=pu[0]
			pu1=pu[1]
			if (pu0.imag!=0): return ["MATHMATICAL ERROR"]
			xw=pu1
			if (pu1<0): xw=pu0
			a2=acos((xw*xw+s1*s1-s2*s2)/(2*xw*s1))
			a3=pi-a1-a2
			if(chek==0):
				return [[xw],[(a2+so1[1])*(180/pi),(a3+so1[2]+so2[1])*(180/pi)]]
			else:
				return [[xw],[(a3+so1[2]+so2[1])*(180/pi),(a2+so1[1])*(180/pi)]]
		if((mor[0]==0 and mor[1]==1)):
			print "second  loop"
			sid=[]
			ang=[]
			ar=cyclic(i3,i4,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			so1=length(sid,ang)
			sid=[]
			ang=[]
			ar=cyclic(i2,i3,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			#print "sid=",sid
			#print "ang=",ang
			so2=length(sid,ang)
			s1=so1[0]
			s2=so2[0]
			#print "i1=",i1,"i3=",i3,"i4=",i4
			a1=angle[i2]-so2[1]
			import numpy
			pl=numpy.poly1d([1.0,-2*(cos(a1))*s2,float(s2*s2-s1*s1)])
			pu=pl.r
			print "pu=",pu
			pu0=pu[0]
			pu1=pu[1]
			if (pu0.imag!=0): return ["MATHEMATICAL ERROR"]
			xw=pu1
			if(pu1<=0): xw=pu0
			print xw,s1,s2
			a2=acos((xw*xw+s1*s1-s2*s2)/(2*xw*s1))
			a3=pi-a1-a2
			#print xw,(a2+so1[1])*(180/pi),(a3+so1[2]+so2[1])*(180/pi)
			if(chek==1):
				return [[xw],[(a2+so1[1])*(180/pi),(a3+so1[2]+so2[1])*(180/pi)]]
			else:
				return [[xw],[(a3+so1[2]+so2[1])*(180/pi),(a2+so1[1])*(180/pi)]]
			#return 0
			sid=[]
			ang=[]
			ar=cyclic(i2,i3,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			tr8=length(sid,ang)
			sid=[]
			ang=[]
			ar=cyclic(i3,i4,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			tr9=length(sid,ang)
			sid=[]
			ang=[]
			ar=cyclic(i4,i1,n)
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			tr10=length(sid,ang)
			no1=tr8[0]
			no2=tr9[0]
			no3=tr10[0]
			s2=angle[i2]-tr8[1]
			s3=angle[i1]-tr10[2]
			x3=100
			x3p=0
			sids=[no1,x3,no3]
			angl=[s2,s3]
			lth=(length(sids,angl))[0]
			while(lth!=no2):
				print x3,x3p
				sids=[no1,x3,no3]
				angl=[s2,s3]
				lth=(length(sids,angl))[0]
				j=x3
				if (abs(x3-x3p)<=1): break
				elif(lth>no2):
					if (x3p<x3):
						x3=(x3+x3p)/2
					else:
						x3=x3/2
				elif(lth<no2):
					if(x3p<x3):
						x3=x3+10
					else:
						x3=(x3+x3p)/2
				x3p=j
			sids=[no1,x3,no3]
			angl=[s2,s3]
			lth=(length(sids,angl))
			if(chek==0):
				return [[x3],[(lth[1]+tr9[1]+tr8[2])*(180/pi),(lth[2]+tr9[2]+tr10[1])*(180/pi)]]
			else:
				return [[x3],[(lth[2]+tr9[2]+tr10[1])*(180/pi),(lth[1]+tr9[1]+tr8[2])*(180/pi)]]
		if(mor[0]==1 and mor[1]==1):
			sid=[]
			ang=[]
			ar=cyclic(i2,i1,n)
			print "i1=",i1,"i2=",i2,"ar=",ar,"n=",n
			lt=len(ar)
			for x in range(0,lt-1):
				if(x==0):
					sid=sid+[side[ar[x]]]
					continue
				sid=sid+[side[ar[x]]]
				ang=ang+[angle[ar[x]]]
			print "siddddddddd=",sid
			print "anggggggggg=",ang
			lp=length(sid,ang)
			print   "gggggggggggggggggggggggggggggggggggggggggggggggggg=", [[lp[0]],[lp[2],lp[1]]]
			if(chek==0):
				return [[lp[0]],[lp[2]*(180/pi),lp[1]*(180/pi)]]
			else:
				return [[lp[0]],[lp[1]*(180/pi),lp[2]*(180/pi)]]
	return ["DATA INSUFFICIENT"]