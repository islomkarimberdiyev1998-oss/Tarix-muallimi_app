import re,glob,math,sys
bad=[]
for f in sorted(glob.glob(sys.argv[1])):
    s=open(f).read()
    cs=[(float(a),float(b),float(r)) for a,b,r in re.findall(r'<circle[^>]*cx="([\d.]+)"[^>]*cy="([\d.]+)"[^>]*r="([\d.]+)"',s)]
    for i in range(len(cs)):
        for j in range(i+1,len(cs)):
            if math.dist(cs[i][:2],cs[j][:2])<cs[i][2]+cs[j][2]+4: bad.append((f,i+1,j+1,round(math.dist(cs[i][:2],cs[j][:2]))))
print(len(glob.glob(sys.argv[1])),bad)
