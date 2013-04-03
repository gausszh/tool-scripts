#coding=utf8
for directory,subdir,filennames in os.walk('D:\\project\\app'):#path
	for filename in filennames:
		afilename=os.path.join(directory,filename)
		f=open(afilename,'r')
		text=f.read()
		f.close()
		if text[:3]=='\xef\xbb\xbf':# with bom
			f=open(afilename,'w')
			f.write(text[3:])
			f.close()

