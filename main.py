ip = input("Ip Address : ").split(".")
#192.168.1.2
def IpToBi(var1,oct):
	var1 = int(var1[oct])
	#Binary digits
	bidg = [128,64,32,16,8,4,2,1]
	#Binary but it's all 1
	bi1 = ["1","1","1","1","1","1","1","1"]
	octate = 0
	
	x = 0
	for i in range(8):
		if (octate+bidg[x]) <= var1:
			octate += bidg[x]
		else:
			bi1[x] = "0"
		x+=1
	
	return "".join(bi1)

print(f"{IpToBi(ip,0)}.{IpToBi(ip,1)}.{IpToBi(ip,2)}.{IpToBi(ip,3)}")
