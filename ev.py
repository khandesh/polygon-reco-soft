import cv
import math
def average(a):
	s1=0
	s2=0
	l=len(a)
	if(l==0): return [0,0]
	for y in a:
		s1=s1+y[0]
		s2=s2+y[1]
	return [float(s1/l),float(s2/l)]
def bq(im,n):
	f=[]
	for j in range(0,480,8):
		for k in range(0,640,9):
			l=cv.Get2D(im,j,k)
			b=float(l[0])
			g=float(l[1])
			r=float(l[2])
			if(b and g and r):
				if((b/g)>((103.32-n)/66.34)) and ((b/g)<((103.32+n)/66.34)):
					if((g/r)>((66.34-n)/46.55)) and ((g/r)<((66.34+n)/46.55)):
						f=f+[[j,k]]
			#if(g/r<0.5):
				#print (b/g,g/r)
	return [average(f)]
#27.7567:36.8925:110.77
#r=46.55:g=66.34:b=103.32