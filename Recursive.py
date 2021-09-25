def okey():
	pw=input("Masukan Password!:")
	if pw=="notbad":
		print("Akses Diterima")
	else:
		print("Akses Tidak Di Terima\n")
		okey()
okey()

import time
def _recurse():
	    string = "Boassnyett"
	    number = 0
	    for i in string:
	    	number += 10
	    	print(i.center(number))
	    	time.sleep (0.4)
	    	if i == string[-1]:
	    		_recurse()
_recurse()