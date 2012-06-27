import wx
import Image
import ImageDraw
import cv
from ev import *
from math  import *
from vf1 import *
from tc import *
from ay import *
import tr
global fram
global box
global dataside
global dat
global dataangle
global flag2
global n1
global n2
n1=[]
n2=[]
flag2=0
global numberofsides
def num2strside(i,total):
	r1=chr(ord('A')+i)
	if i!=(total-1):
		r2=chr(ord('A')+i+1)
	else:
		r2='A'
	return r1+r2+'='
dataangle=[]
class DrawPane(wx.PyScrolledWindow):
	VSIZE = (1000, 700)
	global numberofsides
	global dataside
	global dataangle
	def __init__(self,de):
		wx.PyScrolledWindow.__init__(self,de)
		self.flag2=0
		self.flag9=0
        #self.SetScrollbars(10, 10, 100, 100)
		self.prepare_buffer()
		self.Bind(wx.EVT_PAINT, self.on_paint)
		self.Bind(wx.EVT_MOTION,self.cal)
		self.Bind(wx.EVT_LEFT_DOWN,self.star)
		self.sett()
		self.dod()
	def cal(self,evt):
		global numberofsides
		if (self.flag9==0): return
		if(evt.Moving()):
				newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				self.flag2=0
				ln1=len(self.n1)
				ln2=len(self.n2)
				for rf in range(0,ln2):
					tn=self.kg[self.n2[rf]]
					if (abs(newpos[0]-tn[0])+abs(newpos[1]-tn[1]))<10:
						self.index=rf
						self.flag2=1
						break
				for rf in range(0,ln1):
					pnt1=self.kg[self.n1[rf]]
					pnt2=self.kg[(self.n1[rf]+1)%numberofsides]
					tq=[(pnt1[0]+pnt2[0])/2,(pnt1[1]+pnt2[1])/2]
					if (abs(newpos[0]-tq[0])+abs(newpos[1]-tq[1]))<10:
						self.flag2=2
						self.index=rf
						break
				if(self.flag2): self.SetCursor(wx.StockCursor(wx.CURSOR_POINT_LEFT))
				else:
					self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
					self.flag2=0
	def star(self,event):
		if(self.flag2==0): return
		if(self.flag2==1):
			init=float(self.datangle[self.n2[self.index]])
			vaus=init
			print "vaus=",vaus
			jk=self.n2[self.index]
			self.m2.pop(self.index)
			while(vaus<=(float(init*2))):
				self.dataa[self.index]=vaus
				self.dod2()
				self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				print  "done"
				vaus=vaus+0.2
			while(vaus>=(float(init))):
				self.dataa[self.index]=vaus
				self.dod2()
				self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				print "done"
				vaus=vaus-0.8
			self.dataa[self.index]=0
			self.m1=[]+self.n1
			self.m2=[]+self.n2
				
	def sett(self):
		global dataside
		global dataangle
		self.dc.Clear()
		self.datas=[]
		self.dataa=[]
		for i in range(0,numberofsides):
			valueangle=dataangle[i].GetValue()
			valueside=dataside[i].GetValue()
			if(valueangle!=''):
				valueangle=float(valueangle)
			else: valueangle=0
			if(valueside!=''): valueside=int(valueside)
			else: valueside=0
			self.datas=self.datas+[valueside]
			self.dataa=self.dataa+[valueangle]
	def dod2(self):
		global dataside
		global dataangle
		self.dc.Clear()
		ase=tr.poly(self.datas,self.dataa)
		if(len(ase)==1):
			if(ase[0]!="DATA INSUFFICIENT"):
				self.dc.SetTextForeground(wx.Colour(255,0,0))
				self.dc.DrawLabel(ase[0],(10,10,150,150))
				self.dc.SetTextForeground(wx.Colour(0,0,0))
				self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				return
		
		flag3=0
		z1=len(n1)
		z2=len(n2)
		debit=z1+z2-3
		flag2=1
		self.datside=[]+self.datas
		self.datangle=[]+self.dataa
		print "earlyside=",self.datside
		print "early angle=",self.datangle
		for iterate in self.m2:
			self.datangle[iterate]=50
			nominate=tr.poly(self.datside,self.datangle)
			if(len(nominate)>1): break
		if(len(nominate)==1):
			for iterate in self.m1:
				self.datside[iterate]=100
				nominate=tr.poly(self.datside,self.datangle)
				if(len(nominate)>1):break
		sis=[]
		angs=[]
		count1=0
		count2=0
		for g in range(0,numberofsides):
			if self.datside[g]==0:
				sis=sis+[nominate[0][count1]]
				count1=count1+1
			else:
				sis=sis+[self.datside[g]]
			if self.datangle[g]==0:
				angs=angs+[nominate[1][count2]]
			else:
				angs=angs+[self.datangle[g]]
		self.datside=[]+sis
		self.datangle=[]+angs
		print "sis=",sis
		print "angs=",angs
		for g in range(0,numberofsides):
			self.kk=tr.points(sis[:-1],angs[1:-1])
		self.kg=[]
		for g in range(0,numberofsides):
			t1=200+int(self.kk[g][0])
			t2=200+int(self.kk[g][1])
			t3=200+int(self.kk[(g+1)%numberofsides][0])
			t4=200+int(self.kk[(g+1)%numberofsides][1])
			self.kg=self.kg+[[t1,t2]]
			x1=(t1+t3)/2
			y1=(t2+t4)/2
			self.dc.DrawLine(t1,t2,t3,t4)
			if(g in self.n1):
				self.dc.SetTextForeground(wx.Colour(255,0,0))
			self.dc.DrawLabel(str(int(sis[g])),(x1-5,y1-5,x1+5,y1+5))
			self.dc.SetTextForeground(wx.Colour(0,0,0))
			if(g in self.n2):
				self.dc.SetTextForeground(wx.Colour(255,0,0))
			self.dc.DrawLabel(str(int(angs[g])),(t1-5,t2-5,t1+5,t2+5))
			self.dc.SetTextForeground(wx.Colour(0,0,0))
		self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
		return
	def dod(self):
		global dataside
		global dataangle
		self.dc.Clear()
		print "self.dataa=",self.dataa
		print "self.datas=",self.datas
		ase=tr.poly(self.datas,self.dataa)
		if(len(ase)==1):
			if(ase[0]!="DATA INSUFFICIENT"):
				self.dc.SetTextForeground(wx.Colour(255,0,0))
				self.dc.DrawLabel(ase[0],(10,10,150,150))
				self.dc.SetTextForeground(wx.Colour(0,0,0))
				self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				return
			else:
				self.flag9=1
				flag3=0
				self.n1=tr.occur(self.datas)
				self.n2=tr.occur(self.dataa)
				z1=len(n1)
				z2=len(n2)
				debit=z1+z2-3
				flag2=1
				self.datside=[]+self.datas
				self.datangle=[]+self.dataa
				for iterate in self.n2:
					self.datangle[iterate]=50
					nominate=tr.poly(self.datside,self.datangle)
					if(len(nominate)>1): break
				if(len(nominate)==1):
					for iterate in self.n1:
						self.datside[iterate]=100
						nominate=tr.poly(self.datside,self.datangle)
						if(len(nominate)>1):break
				print "nominate=",nominate
				print "self.datside=",self.datside
				print "self.datangle=",self.datangle
				sis=[]
				angs=[]
				count1=0
				count2=0
				for g in range(0,numberofsides):
					if self.datside[g]==0:
						sis=sis+[nominate[0][count1]]
						count1=count1+1
					else:
						sis=sis+[self.datside[g]]
					if self.datangle[g]==0:
						angs=angs+[nominate[1][count2]]
						count2=count2+1
					else:
						angs=angs+[self.datangle[g]]
						print "yeahhhh"
				self.datside=[]+sis
				self.datangle=[]+angs
				print "yahhhhhhhhh"
				print "sis=",sis
				print "angs=",angs
				for g in range(0,numberofsides):
					self.kk=tr.points(sis[:-1],angs[1:-1])
				self.kg=[]
				print "self.kk=",self.kk
				for g in range(0,numberofsides):
					t1=200+int(self.kk[g][0])
					t2=200+int(self.kk[g][1])
					t3=200+int(self.kk[(g+1)%numberofsides][0])
					t4=200+int(self.kk[(g+1)%numberofsides][1])
					self.kg=self.kg+[[t1,t2]]
					x1=(t1+t3)/2
					y1=(t2+t4)/2
					self.dc.DrawLine(t1,t2,t3,t4)
					if(g in self.n1):
						self.dc.SetTextForeground(wx.Colour(255,0,0))
					self.dc.DrawLabel(str(int(sis[g])),(x1-5,y1-5,x1+5,y1+5))
					self.dc.SetTextForeground(wx.Colour(0,0,0))
					if(g in self.n2):
						self.dc.SetTextForeground(wx.Colour(255,0,0))
					self.dc.DrawLabel(str(int(angs[g])),(t1-5,t2-5,t1+5,t2+5))
					self.dc.SetTextForeground(wx.Colour(0,0,0))
				self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				self.m1=[]+self.n1
				self.m2=[]+self.n2
				return
				
		sis=[]
		angs=[]
		count1=0
		count2=0
		print "self.datas=",self.datas
		print "self.dataa=",self.dataa
		for g in range(0,numberofsides):
			if self.datas[g]==0:
				sis=sis+[ase[0][count1]]
				count1=count1+1
			else:
				sis=sis+[self.datas[g]]
			if self.dataa[g]==0:
				angs=angs+[ase[1][count2]]
				count2=count2+1
			else:
				angs=angs+[self.dataa[g]]
		print "sis=",sis
		print "angs=",angs
		kk=tr.points(sis[:-1],angs[1:-1])
		model=kk
		for g in range(0,numberofsides):
            #self.dc.DrawLine(10,10,100,100)
			t1=200+int(model[g][0])
			t2=200+int(model[g][1])
			t3=200+int(model[(g+1)%numberofsides][0])
			t4=200+int(model[(g+1)%numberofsides][1])
			self.dc.DrawLine(t1,t2,t3,t4)
			x1=(t1+t3)/2
			y1=(t2+t4)/2
			self.dc.DrawLabel(str(int(sis[g])),(x1-5,y1-5,x1+5,y1+5))
		self.dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
	def prepare_buffer(self):
		self.buffer = wx.EmptyBitmap(*DrawPane.VSIZE)
		self.dc = wx.BufferedDC(None, self.buffer)
		self.dc.Clear()
       # dc.DrawLine(0, 0, 999, 999) # Draw something to better show the flicker problem

	def on_paint(self, evt):
		self.dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)
class construction(wx.Frame):
	global fram
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'My app')
		self.Maximize()
		s = wx.BoxSizer(wx.VERTICAL)
		pn=wx.Panel(self,-1)
		wx.Button(pn,4321,"GO BACK")
		wx.Button(pn,4422,"CONSTRUCT ANOTHER POLYGON",pos=(100,0))
		pn.Bind(wx.EVT_BUTTON,self.did,id=4321)
		pn.Bind(wx.EVT_BUTTON,self.dp,id=4422)
		s.Add(pn,0.1,wx.EXPAND)
		s.Add(DrawPane(self), 1, wx.EXPAND)
		self.SetSizer(s)
	def did(self,event):
		global fram
		fram=MainFrame()
		fram.Show()
		self.Close()
	def dp(self,event):
		global box
		global numberofsides
		box=wx.TextEntryDialog(self,'ENTER NO. OF SIDES IN POLYGON','NO. OF SIDES=?','')
		box.Show()
		tn=box.ShowModal()
		print "tnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn=",tn
		pan.im=Image.open("l.png")
		imeg=ImageDraw.Draw(pan.im)
		if(tn==5100):
			numberofsides=int(box.GetValue())
			kk=query(None,-1,'ENTER DIMENSIONS',numberofsides)
			kk.Show()
			self.Close()
class query(wx.Frame):
	global dataside
	global dataangle
	def __init__(self,par,id,title,sides):
		global dataside
		global dataangle
		wx.Frame.__init__(self,par,id,title)
		dataside=[]
		dataangle=[]
		self.Maximize()
		b=wx.BoxSizer(wx.VERTICAL)
		b1=wx.BoxSizer(wx.HORIZONTAL)
		pan1=wx.Panel(self,-1)
		pan2=wx.Panel(self,-1)
		wx.Button(pan2,532,'SUBMIT')
		pan2.Bind(wx.EVT_BUTTON,self.submit,id=532)
		p1=wx.Panel(pan1,-1)
		p2=wx.Panel(pan1,-1)
		for i in range(0,sides):
			#father is p1
			tex=num2strside(i,sides)
			wx.StaticText(p1,-1,tex,((20,10+(30*i))))
			tex2=chr(ord('A')+i)
			wx.StaticText(p2,-1,tex2,((20,10+(30*i))))
			t1=wx.TextCtrl(p1,-1,"",pos=((80,10+30*i)),size=(40,20))
			t2=wx.TextCtrl(p2,-1,"",pos=((80,10+30*i)),size=(40,20))
			dataside=dataside+[t1]
			dataangle=dataangle+[t2]
		b1.Add(p1,1,wx.EXPAND)
		b1.Add(p2,1,wx.EXPAND)
		pan1.SetSizer(b1)
		b.Add(pan1,5,wx.EXPAND)
		b.Add(pan2,1,wx.EXPAND)
		self.SetSizer(b)
		#panel1=wx.Panel(self,-1)
		#text1=wx.TextCtrl(panel1,-1,"",size=(10,10))
		#text3=wx.StaticText(self,-1,str(ang),((20,40)))
	def submit(self,event):
		global dataside
		global dataangle
		datas=[]
		dataa=[]
		for i in range(0,numberofsides):
			valueangle=dataangle[i].GetValue()
			valueside=dataside[i].GetValue()
			if(valueangle!=''):
				valueangle=int(valueangle)
			else: valueangle=0
			if(valueside!=''):
				valueside=int(valueside)
			else: valueside=0
			datas=datas+[valueside]
			dataa=dataa+[valueangle]
		#print "datas=",datas
		#print "dataa=",dataa
		#print tr.poly(datas,dataa)
		h=tr.poly(datas,dataa)
		construction().Show()
		self.Close()
def construct(event):
	global fram
	global box
	global numberofsides
	box=wx.TextEntryDialog(fram,'ENTER NO. OF SIDES IN POLYGON','NO. OF SIDES=?','')
	box.Show()
	tn=box.ShowModal()
	print "tnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn=",tn
	pan.im=Image.open("l.png")
	imeg=ImageDraw.Draw(pan.im)
	if(tn==5100):
		numberofsides=int(box.GetValue())
		kk=query(None,-1,'ENTER DIMENSIONS',numberofsides)
		kk.Show()
		fram.Close()
flag=[0]
flg=[0]
dlg=[0]
ptt=[3,4]
global ang
ang=[]
global sid
global arm
global counter
global imge
counter=7
arm=[]
#global number
#number=6
sid=[]
from shutil import *
global pi
global inc
global check
check=-300
inc=-1
po=[]
def video(event):
	global dc
	global pan
	dc.Clear()
	dc = wx.BufferedDC(wx.ClientDC(pan), pan.buffer)
	global check
	global capture
	global camera_index
	global capture
	global imeg
	global j
	pan.im=Image.open("l.png")
	imeg=ImageDraw.Draw(pan.im)
	camera_index = 0
	capture = cv.CaptureFromCAM(camera_index)
	flg[0]=0
	dlg[0]=0
		#while(check<30):
	while(check<=30):
		print "capture=",capture
		repeat()
	check=-300
	del(capture)
	#filerefresh(pan.im)
	pan.prep(23)
def repeat():
  global check
  global inc
  global capture #declare as globals since we are assigning to them now
  global camera_index
  global gram
  global po
  global pan
  global imeg
  frame = cv.QueryFrame(capture)
  #y=bq(frame,4)
  global dc
  #for ht in y: 
#	dc.DrawPoint(ht[1],ht[0])
  ny=process(frame)
  if(ny==[0,0]):
	check=check+1
  else:
	check=0
	po=po+[ny]
	li=len(po)
	if(len(po)>1):
		dc.DrawLine(640-po[li-2][0],po[li-2][1],640-po[li-1][0],po[li-1][1])
		imeg.line(((640-po[li-2][0],po[li-2][1]),(640-po[li-1][0],po[li-1][1])),fill=20)
		#print "aaa=",po[li-2][0],po[li-2][1],po[li-1][0],po[li-1][1]
  #dc.DrawPoint(tq[1],tq[0])
		dc = wx.BufferedDC(wx.ClientDC(pan), pan.buffer)
  c = cv.WaitKey(20)
  if(c=="n"): #in "n" key is pressed while the popup window is in focus
    camera_index += 1 #try the next camera index
    capture = cv.CaptureFromCAM(camera_index)
    if not capture: #if the next camera index didn't work, reset to 0.
        camera_index = 0
        capture = cv.CaptureFromCAM(camera_index)
def previ(event):
	global counter
	global but1
	global but3
	counter=counter-1
	if(counter<7):
		but3.Enable()
	if(counter==1): 
		but1.Disable()
	strin='d'+str(counter)+'.png'
	imge.SetBitmap(wx.BitmapFromImage(wx.Image(strin, wx.BITMAP_TYPE_ANY)))
	imge.Refresh()
	but3.Refresh()
	but1.Refresh()
def next(event):
	global counter
	global but1
	global but3
	counter=counter+1
	if(counter>1):but1.Enable()
	if(counter==7):
		but3.Disable()
	strin='d'+str(counter)+'.png'
	imge.SetBitmap(wx.BitmapFromImage(wx.Image(strin, wx.BITMAP_TYPE_ANY)))
	imge.Refresh()
	but3.Refresh()
	but1.Refresh()
def compute(event):
	global pan
	string='d'+str(counter)+'.png'
	copyfile(string,'no.png')
	if(flag[0]==0):
			cx=rsw('no.png')
	if(flag[0]==2):
			#print "number=",number
		g=int(number)
			#cx=ast(int(number))
			#print "g=",g
		cx=ast(g,'no.png')
	#self.h=cx
	#self.d=[]
	im=Image.open("l.png")
        #self.d=[]
	draw=ImageDraw.Draw(im)
        #wx.MessageBox("successfully saved")
	dc.Clear()
	l=len(cx)
	text=ord('A')
	global ang
	global sid
	xw="Angle:"
	bt="SIDE:"
	for r in range(0,l):
		dc.DrawLine(cx[r][0],cx[r][1],cx[(r+1)%l][0],cx[(r+1)%l][1])
		su=atan2(cx[(r+1)%l][1]-cx[r][1],cx[(r+1)%l][0]-cx[r][0])
		si=atan2(cx[(r-1)%l][1]-cx[r][1],cx[(r-1)%l][0]-cx[r][0])
		sc=abs(su-si)
		if(sc>pi): sc=(2*pi-sc)
		ang=ang+[sc*180/pi]
		sid=sid+[sqrt((cx[(r+1)%l][1]-cx[r][1])**2+(cx[(r+1)%l][0]-cx[r][0])**2)]
		xw=xw+chr(text)+"="+str("{0:.1f}".format(ang[r]))+"  "
		if(r!=(l-1)):
			bt=bt+chr(text)+chr(text+1)+"="+str("{0:.1f}".format(sid[r]))+"  "
		else:
			bt=bt+chr(text)+"A"+"="+str("{0:.1f}".format(sid[r]))+"  "
		dc.DrawLabel(chr(text)+str("{0:.2f}".format(ang[r])),(cx[r][0],cx[r][1],10,10))
		text=text+1
	text3.SetLabel(xw)
	ang=[]
	text4.SetLabel(bt)
	sid=[]
	pan.Refresh()
def filerefresh(k):
	copyfile('d7.png','p.png')
	k.save('d7.png')
	copyfile('d6.png','q.png')
	copyfile('p.png','d6.png')
	copyfile('d5.png','p.png')
	copyfile('q.png','d5.png')
	copyfile('d4.png','q.png')
	copyfile('p.png','d4.png')
	copyfile('d3.png','p.png')
	copyfile('q.png','d3.png')
	copyfile('d2.png','q.png')
	copyfile('p.png','d2.png')
	copyfile('q.png','d1.png')
def upgrade(event):
	global counter
	i=counter
	for r in range(i-1,0,-1):
		copyfile('d'+str(r)+'.png','d'+str(r+1)+'.png')
	copyfile('l.png','d1.png')
	strin='d'+str(counter)+'.png'
	imge.SetBitmap(wx.BitmapFromImage(wx.Image(strin, wx.BITMAP_TYPE_ANY)))
class My(wx.Panel):
	#global number
	def __init__(self,par):
		wx.Panel.__init__(self,par,-1)
		global text3
		text3=wx.StaticText(self,-1,str(ang),((20,40)))
		text3.SetFont(wx.Font(12,wx.DEFAULT,wx.ITALIC,wx.NORMAL))
		global text4
		text4=wx.StaticText(self,-1,str(sid),((20,60)))
		text4.SetFont(wx.Font(12,wx.DEFAULT,wx.ITALIC,wx.NORMAL))
		global text5
		text5=wx.StaticText(self,-1,"NUMBER OF SIDES",((2,10)))
		text5.SetFont(wx.Font(8,wx.DEFAULT,wx.ITALIC,wx.NORMAL))
class por(wx.Panel):
	def __init__(self,par):
		wx.Panel.__init__(self,par,-1)
		global imge
		global but1
		global but3
		global but2
		img = wx.Image('d7.png', wx.BITMAP_TYPE_ANY)
		#self.imageCtrl= wx.StaticBitmap(self, wx.ID_ANY,
        #                                wx.BitmapFromImage(img))
		imge= wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.BitmapFromImage(img))
		#imge.Resize((20,20),Image.ANTIALIAS)
		but1 = wx.Button(self, id=32, label='Previous', pos=(160, 550), size=(110, 28))
		self.Bind(wx.EVT_BUTTON,previ,id=32)
		but2 = wx.Button(self, id=33, label='Draw', pos=(280, 550), size=(110, 28))
		self.Bind(wx.EVT_BUTTON,compute,id=33)
		but3 = wx.Button(self, id=34, label='Next', pos=(400, 550), size=(110, 28))
		but3.Disable()
		self.Bind(wx.EVT_BUTTON,next,id=34)
		self.button4 = wx.Button(self, id=35, label='Delete', pos=(280, 510), size=(110, 28))
		self.Bind(wx.EVT_BUTTON,upgrade,id=35)
		#self.Refresh()
class MainFrame(wx.Frame):
	""" Just a frame with a DrewPane """
	global pan
	global number
	global valu
	global arm
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'POLYGON RECOGNITION AND DRAGGING APP')
		self.Maximize()
		#self.SetBackgroundColour("#000000")
		#t=wx.Panel()
		self.Maximize()
		s=wx.BoxSizer(wx.HORIZONTAL)
		self.pa=wx.Panel(self,-1)
		ry=wx.BoxSizer(wx.VERTICAL)
		global fd
		fd=por(self)
		self.SetSizer(s)
		self.Bind(wx.EVT_KEY_DOWN,self.drag)
		menubar=wx.MenuBar()
		mode=wx.Menu()
		#tio=wx.MenuItem(mode,101,'&SMOOTHEN','USE THIS MODE WHEN YOU DO NOT WANT TO GIVE NO OF SIDES AS INPUT',wx.ITEM_RADIO)
		#print self.tio
		mode.Append(101,'&SMOOTHEN','USE THIS MODE WHEN YOU DO NOT WANT TO GIVE NO OF SIDES AS INPUT',wx.ITEM_RADIO)
		mode.Append(103,'&BEST FIT POLYGON','USE THIS MODE WHEN YOU WILL GIVE NO. OF SIDES AS INPUT',wx.ITEM_RADIO)
		mode.Append(102,'&DRAG','USE THIS MODE WHEN YOU WANT TO ADJUST DIMENSIONS BY DRAWING POLYGON',wx.ITEM_RADIO)
		mode.Append(104,'&ROTATE',"TO ROTATE A SIDE OF THE POLYGON",wx.ITEM_RADIO)
		mode.Append(105,'&TRANSLATE',"KEEPING ANGLE CONSTANT",wx.ITEM_RADIO)
		#mode.Append(106,'&WEBCAM',"TAKE VIDEO INPUT",wx.ITEM_RADIO)
		wx.EVT_MENU(self,101,self.changes)
		wx.EVT_MENU(self,102,self.changed)
		wx.EVT_MENU(self,103,self.bestfit)
		wx.EVT_MENU(self,104,self.rotate)
		#wx.EVT_MENU(self,106,self.construct)
		wx.EVT_MENU(self,105,self.translate)
		#wx.EVT_MENU(self,106,self.video)
		self.CreateStatusBar()
		menubar.Append(mode,'&MODES')
		self.SetMenuBar(menubar)
		self.pa.SetSizer(ry)
		global pan
		pan=DrewPane(self.pa)
		ry.Add(pan, 6, wx.EXPAND)
		global h
		h=My(self.pa)
		sam=[]
		for tuo in range(26,0,-1):
			sam=sam+[str(tuo)]
		self.cb=wx.ComboBox(h,100,"default value",(100,10),(100,-1),sam,wx.CB_DROPDOWN)
		global butt
		butt = wx.Button(h, id=50, label='WEBCAM', pos=(100, 120), size=(70, 20))
		global buts
		buts=wx.Button(h,id=60,label="CONSTRUCT", pos=(172,120),size=(80,20))
		h.Bind(wx.EVT_BUTTON,video,id=50)
		h.Bind(wx.EVT_BUTTON,construct,id=60)
		ry.Add(h,2,wx.EXPAND)
		s.Add(self.pa,1.1,wx.EXPAND)
		s.Add(fd,1,wx.EXPAND)
	def bestfit(self,event):
		global h
		flag[0]=2
		flg[0]=0
		dlg[0]=0
		#but2=wx.Button(h,5,'APPROXIMATE',(180,0))
		h.Bind(wx.EVT_COMBOBOX,self.fun,self.cb)
	def rotate(self,event):
		flag[0]=3
		flg[0]=0
		dlg[0]=0
	def translate(self,event):
		flag[0]=4
		flg[0]=0
		dlg[0]=0
	def fun(self,event):
		self.cb = event.GetString()
		#global h
		global number
		#self.valu = wx.TextCtrl(h, -1, "", size=(175, -1))
		number=self.cb
	def changes(self,event):
		flag[0]=0
		flg[0]=0
		dlg[0]=0
	def changed(self,event):
		flag[0]=1
		flg[0]=0
		dlg[0]=0
	def drag(self,event):
		dr=event.GetKeyCode()
		if(dr==ord('D')):
			flag[0]=1
			flg[0]=0
			#wx.MessageBox('Drag Mode Activated')
		if(dr==ord('S')):
			flag[0]=0
			flg[0]=0
		if(dr==ord('F')):
			flag[0]=2
			flg[0]=0
class DrewPane(wx.PyScrolledWindow):
	global number
	global dc
	#VSIZE = (819,460)
	VSIZE=(640,480)
	#VSIZE=(480,640)

	def __init__(self,de):
		self.d=[]
		self.im=Image.open("l.png")
		self.draw=ImageDraw.Draw(self.im)
		wx.PyScrolledWindow.__init__(self,de)
		self.show_bmp=wx.StaticBitmap(self)
		self.prepare_buffer()
		#self.dr=wx.EmptyBitmap(480,640)
		self.Bind(wx.EVT_LEFT_UP,self.prep)
		self.Bind(wx.EVT_PAINT, self.on_paint)
		self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
		self.Bind(wx.EVT_MOTION, self.on_motion)
		self.Bind(wx.EVT_RIGHT_DOWN,self.lolz)
            #self.Bind(wx.EVT_KEY_DOWN,self.dr)
	def lolz(self,event):
		dc.Clear()
		self.Refresh()
	def prepare_buffer(self):
		global dc
		self.buffer = wx.EmptyBitmap(*DrewPane.VSIZE)
		dc = wx.BufferedDC(None, self.buffer)
		dc.Clear()
	def prep(self,event):
		if(flag[0]==0 or flag[0]==2):
			filerefresh(self.im)
		global arm
		global fd
		global imge
		global dc
		if(flag[0]==0 or flag[0]==2):
			imge.SetBitmap(wx.BitmapFromImage(wx.Image('d7.png', wx.BITMAP_TYPE_ANY)))
			imge.Refresh()
			#fd.Refresh()
		#global number
		if(flg[0]==1 and dlg[0]==1):
			dlg[0]=0
			self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
			return
		if(flag[0]==1): return
		#Image.open("d3.png").show()
        #Image.open("d3.png").show()
        #Image.open("d3.png").show()
		if(flag[0]==3):
			if(len(arm)==2):
				arm=[]
				self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
			return
		if(flag[0]==4):
			if(len(arm)==2):
				arm=[]
				self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
			return
		if(flag[0]==0):
			cx=rsw()
		if(flag[0]==2):
			#print "number=",number
			g=int(number)
			#cx=ast(int(number))
			#print "g=",g
			cx=ast(g)
		self.h=cx
		self.d=[]
		self.im=Image.open("l.png")
        #self.d=[]
		self.draw=ImageDraw.Draw(self.im)
        #wx.MessageBox("successfully saved")
		dc.Clear()
		#self.Refresh()
		l=len(cx)
		text=ord('A')
		global ang
		global sid
		xw="Angle:"
		bt="SIDE:"
		for r in range(0,l):
			dc.DrawLine(cx[r][0],cx[r][1],cx[(r+1)%l][0],cx[(r+1)%l][1])
			su=atan2(cx[(r+1)%l][1]-cx[r][1],cx[(r+1)%l][0]-cx[r][0])
			si=atan2(cx[(r-1)%l][1]-cx[r][1],cx[(r-1)%l][0]-cx[r][0])
			sc=abs(su-si)
			if(sc>pi): sc=(2*pi-sc)
			ang=ang+[sc*180/pi]
			sid=sid+[sqrt((cx[(r+1)%l][1]-cx[r][1])**2+(cx[(r+1)%l][0]-cx[r][0])**2)]
			xw=xw+chr(text)+"="+str("{0:.1f}".format(ang[r]))+"  "
			if(r!=(l-1)):
				bt=bt+chr(text)+chr(text+1)+"="+str("{0:.1f}".format(sid[r]))+"  "
			else:
				bt=bt+chr(text)+"A"+"="+str("{0:.1f}".format(sid[r]))+"  "
			dc.DrawLabel(chr(text)+str("{0:.2f}".format(ang[r])),(cx[r][0],cx[r][1],10,10))
			text=text+1
		text3.SetLabel(xw)
		ang=[]
		text4.SetLabel(bt)
		sid=[]
		dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
		print "done"
        
		#wx.MessageBox('Done')
        #dc.DrawLine(0, 0, 999, 999) # Draw something to better show the flicker problem
	def on_paint(self, evt):
		global dc
		dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)
		global fram
	def on_mouse_down(self, evt):
		global dc
		if(flag[0]==1):
			if(flg[0]==0):return
			else:
				dlg[0]=1
				self.pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				u=self.h.index(ptt)
				(self.h)[u][0]=self.pos[0]
				self.h[u][1]=self.pos[1]
				ptt[0]=self.pos[0]
				ptt[1]=self.pos[1]
				dc.Clear()
				tv=len(self.h)
				text=ord('A')
				for li in range(0,tv):
					dc.DrawLine(self.h[li][0],self.h[li][1],self.h[(li+1)%tv][0],self.h[(li+1)%tv][1])
					dc.DrawLabel(chr(text),(self.h[li][0],self.h[li][1],20,20))
					text=text+1
				#self.Refresh()
				return
		global arm
		if(flag[0]==3):
			if(len(arm)<2 and flg[0]==1):
				arm=arm+[ptt[0]]
				return
			else: return
		if(flag[0]==4):
			if(len(arm)<2 and flg[0]==1):
				arm=arm+[ptt[0]]
				return
			else: return
		dc.Clear()
		self.Refresh()
		self.mouse_pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()

	def on_motion(self, evt):
		global dc
		if(flag[0]==1 and dlg[0]==0):
			if(evt.Moving()):
				newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				ant=0
				for ty in self.h:
					if (abs(newpos[0]-ty[0])+abs(newpos[1]-ty[1]))<10:
						ant=1
						ptt[0]=ty[0]
						ptt[1]=ty[1]
						break
				if(ant==1):
					self.SetCursor(wx.StockCursor(wx.CURSOR_POINT_LEFT))
					ant=0
					flg[0]=1
				else: 
					flg[0]=0
					self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
				#self.Refresh()
			return
		if(flag[0]==3 and len(arm)<2):
			if(evt.Moving()):
				newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				ant=0
				for ty in self.h:
					if (abs(newpos[0]-ty[0])+abs(newpos[1]-ty[1]))<10:
						ant=1
						ptt[0]=ty
						#print "ptt=",ptt
						break
				if(ant==1):
					self.SetCursor(wx.StockCursor(wx.CURSOR_POINT_LEFT))
					ant=0
					flg[0]=1
				else: 
					flg[0]=0
					self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
			return
		if(flag[0]==4 and len(arm)<2):
			if(evt.Moving()):
				newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				ant=0
				for ty in self.h:
					if (abs(newpos[0]-ty[0])+abs(newpos[1]-ty[1]))<10:
						ant=1
						ptt[0]=ty
						#print "ptt=",ptt
						break
				if(ant==1):
					self.SetCursor(wx.StockCursor(wx.CURSOR_POINT_LEFT))
					ant=0
					flg[0]=1
				else: 
					flg[0]=0
					self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
			return
		if(flag[0]==3 and len(arm)==2 and evt.LeftIsDown() and evt.Dragging()):
			global ang
			global sid
			#print "(self.h)=",(self.h)
			newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
			a1=(self.h).index(arm[0])
			a2=(self.h).index(arm[1])
			do=ort(newpos,arm[0],arm[1])
			dc.Clear()
			(self.h)[a2]=do
			arm[1]=do
			tv=len(self.h)
			ang=[]
			sid=[]
			text=ord('A')
			ct="angle:"
			bt="SIDE:"
			for li in range(0,tv):
				dc.DrawLine(self.h[li][0],self.h[li][1],self.h[(li+1)%tv][0],self.h[(li+1)%tv][1])
				su=atan2(self.h[(li+1)%tv][1]-self.h[li][1],self.h[(li+1)%tv][0]-self.h[li][0])
				si=atan2(self.h[(li-1)%tv][1]-self.h[li][1],self.h[(li-1)%tv][0]-self.h[li][0])
				sc=abs(su-si)
				if(sc>pi): sc=(2*pi-sc)
				ang=ang+[sc*180/pi]
				sid=sid+[sqrt((self.h[(li+1)%tv][1]-self.h[li][1])**2+(self.h[(li+1)%tv][0]-self.h[li][0])**2)]
				ct=ct+chr(text)+"="+str("{0:.1f}".format(ang[li]))+"  "
				if(li !=(tv-1)):
					bt=bt+chr(text)+chr(text+1)+"="+str("{0:.1f}".format(sid[li]))+"  "
				else:
					bt=bt+chr(text)+"A"+"="+str("{0:.1f}".format(sid[li]))+"  "
				dc.DrawLabel(chr(text)+str("{0:.0f}".format(ang[li])),(self.h[li][0],self.h[li][1],20,20))
				dc.DrawLabel(str("{0:.0f}".format(sid[li])),(((self.h[li][0]+self.h[(li+1)%tv][0])/2),(self.h[li][1]+self.h[(li+1)%tv][1])/2,20,20))
				text=text+1
			text3.SetLabel(ct)
			text3.Refresh()
			ang=[]
			text4.SetLabel(bt)
			text4.Refresh()
			sid=[]
				#dc.DrawLabel("MOAZZAM",(0,0,20,20))
			#self.Refresh()
			dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
			return
		if(flag[0]==4 and len(arm)==2 and evt.LeftIsDown() and evt.Dragging()):
			#global ang
			#global sid
			#print "(self.h)=",(self.h)
			newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
			a1=(self.h).index(arm[0])
			a2=(self.h).index(arm[1])
			
			do=trans(newpos,arm[0],arm[1])
			dc.Clear()
			(self.h)[a2]=do
			arm[1]=do
			tv=len(self.h)
			ang=[]
			sid=[]
			text=ord('A')
			ct="angle:"
			bt="SIDE:"
			for li in range(0,tv):
				dc.DrawLine(self.h[li][0],self.h[li][1],self.h[(li+1)%tv][0],self.h[(li+1)%tv][1])
				su=atan2(self.h[(li+1)%tv][1]-self.h[li][1],self.h[(li+1)%tv][0]-self.h[li][0])
				si=atan2(self.h[(li-1)%tv][1]-self.h[li][1],self.h[(li-1)%tv][0]-self.h[li][0])
				sc=abs(su-si)
				if(sc>pi): sc=(2*pi-sc)
				ang=ang+[sc*180/pi]
				sid=sid+[sqrt((self.h[(li+1)%tv][1]-self.h[li][1])**2+(self.h[(li+1)%tv][0]-self.h[li][0])**2)]
				ct=ct+chr(text)+"="+str("{0:.1f}".format(ang[li]))+"  "
				if(li !=(tv-1)):
					bt=bt+chr(text)+chr(text+1)+"="+str("{0:.1f}".format(sid[li]))+"  "
				else:
					bt=bt+chr(text)+"A"+"="+str("{0:.1f}".format(sid[li]))+"  "
				dc.DrawLabel(chr(text)+str("{0:.0f}".format(ang[li])),(self.h[li][0],self.h[li][1],20,20))
				dc.DrawLabel(str("{0:.0f}".format(sid[li])),(((self.h[li][0]+self.h[(li+1)%tv][0])/2),(self.h[li][1]+self.h[(li+1)%tv][1])/2,20,20))
				text=text+1
			text3.SetLabel(ct)
			text3.Refresh()
			ang=[]
			text4.SetLabel(bt)
			text4.Refresh()
			sid=[]
				#dc.DrawLabel("MOAZZAM",(0,0,20,20))
			#self.Refresh()
			dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
			return
		if(flag[0]==1 and dlg[0]==1):
			if evt.Dragging() and evt.LeftIsDown():
				self.pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
				u=self.h.index(ptt)
				(self.h)[u][0]=self.pos[0]
				(self.h)[u][1]=self.pos[1]
				ptt[0]=self.pos[0]
				ptt[1]=self.pos[1]
				dc.Clear()
				tv=len(self.h)
				text=ord('A')
				#global ang
				#global sid
				bt="SIDE:"
				ct="angle:"
				tv=len(self.h)
				for li in range(0,tv):
					dc.DrawLine(self.h[li][0],self.h[li][1],self.h[(li+1)%tv][0],self.h[(li+1)%tv][1])
					su=atan2(self.h[(li+1)%tv][1]-self.h[li][1],self.h[(li+1)%tv][0]-self.h[li][0])
					si=atan2(self.h[(li-1)%tv][1]-self.h[li][1],self.h[(li-1)%tv][0]-self.h[li][0])
					sc=abs(su-si)
					if(sc>pi): sc=(2*pi-sc)
					ang=ang+[sc*180/pi]
					sid=sid+[sqrt((self.h[(li+1)%tv][1]-self.h[li][1])**2+(self.h[(li+1)%tv][0]-self.h[li][0])**2)]
					ct=ct+chr(text)+"="+str("{0:.1f}".format(ang[li]))+"  "
					if(li !=(tv-1)):
						bt=bt+chr(text)+chr(text+1)+"="+str("{0:.1f}".format(sid[li]))+"  "
					else:
						bt=bt+chr(text)+"A"+"="+str("{0:.1f}".format(sid[li]))+"  "
					dc.DrawLabel(chr(text)+str("{0:.0f}".format(ang[li])),(self.h[li][0],self.h[li][1],20,20))
					dc.DrawLabel(str("{0:.0f}".format(sid[li])),(((self.h[li][0]+self.h[(li+1)%tv][0])/2),(self.h[li][1]+self.h[(li+1)%tv][1])/2,20,20))
					text=text+1
				text3.SetLabel(ct)
				text3.Refresh()
				ang=[]
				text4.SetLabel(bt)
				text4.Refresh()
				sid=[]
				#dc.DrawLabel("MOAZZAM",(0,0,20,20))
				#pan.Refresh()
				dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
				return
				
		if evt.Dragging() and evt.LeftIsDown():
			dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
			newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
			self.d=self.d+[[newpos[0],newpos[1]]]
			coords = self.mouse_pos + newpos
			dc.DrawLine(*coords)
			self.draw.line(coords,fill=0)
			self.mouse_pos = newpos
def ort(p,p1,p2):
	x1=p1[0]
	y1=p1[1]
	x=p[0]
	y=p[1]
	x2=p2[0]
	y2=p2[1]
	l=sqrt((x-x1)**2+(y-y1)**2)
	u=[(x-x1)/l,(y-y1)/l]
	dist=sqrt((x1-x2)**2+(y1-y2)**2)
	w=u[0]*dist+x1
	q=u[1]*dist+y1
	t=[w,q]
	return t
def trans(p,p1,p2):
	x1=p1[0]
	y1=p1[1]
	x=p[0]
	y=p[1]
	x2=p2[0]
	y2=p2[1]
	A=(y1-y2)
	B=(x2-x1)
	if (not A and not B): return p1
	C=(x1*y2-x2*y1)
	x0=(float(B*B*x-A*B*y-A*C))/(A*A+B*B)
	y0=(float(A*A*y-A*B*x-B*C))/(A*A+B*B)
	return [x0,y0]
if __name__ == "__main__":
	app = wx.PySimpleApp()
	wx.InitAllImageHandlers()
	global fram
	fram=MainFrame()
	fram.Show()
	app.MainLoop()