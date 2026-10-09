import os,sys
from terminal_ui import run
original=os.dup(1)
tty=os.open('/dev/tty',os.O_RDWR)
try:
 os.dup2(tty,0);os.dup2(tty,1)
 title,back,*rows=sys.argv[1:]
 keys=[];labels=[]
 for row in rows:
  key,_,label=row.partition('\t');keys.append(key);labels.append(label)
 result=[back]
 def session(ui):
  n=ui.menu(title,labels)
  if n is not None:result[0]=keys[n]
 code=run(title,session)
 os.write(original,(result[0]+'\n').encode())
finally:os.close(tty)
os.close(original)
raise SystemExit(code)
