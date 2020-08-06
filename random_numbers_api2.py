import os
import requests
import time

path = 'dataBase.txt'
confirmation_path = 'confirmation.txt'
f = open("io_bound_data.txt", "a")

def random_numbers_api(quant=10,min= 1000000,max= 1000000000):
	start = time.time()
	r = requests.get(f'https://www.random.org/integers/?num={quant}&min={min}&max={max}&col=1&base=10&format=plain&rnd=new')

	with open(path,'w') as db:
		db.write(r.text)
	end = time.time()
	f.write('{:10f} '.format(end - start))

try:
	while(True):
		start = time.time()
		if not os.path.isfile(path):
			random_numbers_api()
			with open(confirmation_path, 'w') as fp: 
				pass
			end = time.time()
	    
		else:
			end = time.time()
		    
except KeyboardInterrupt:
	f.close()

