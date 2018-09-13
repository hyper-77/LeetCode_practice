import glob
count=0
for file in glob.glob('*.*.py'):

    count+=1


print('I have solved '+str(count)+' problems')