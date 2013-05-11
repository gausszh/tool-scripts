#coding=utf8
sqlf=open('IPL2.sql','r')
tables=['SYS_TEMPLATE', 'PRIZE_DETAIL', 'GAME_TEAM']
while True and not tables:
    table=raw_input('input the table name(end by -1):\n')
    if table=='-1':
        break
    tables.append(table)
print tables
text=sqlf.readlines()
tmpText=""
for line in text:
    flag=False
    if line.find('INSERT')>=0 :#含这些词
        for table in tables:
            if line.find(table)>=0:
                flag=True
                continue
    if flag:
        tmpText+=line
    elif line.find("*!40")<0 and line.find('LOCK TABLES')<0 and line.find('--')<0 and line.find('INSERT')<0:#不含这些词
        tmpText+=line
toSqlFile=open('newIpl2.sql','w')
toSqlFile.write(tmpText)
toSqlFile.close()
sqlf.close()
