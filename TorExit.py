import urllib2, os

url = 'https://check.torproject.org/exit-addresses'

def GetExit(url):
	response = urllib2.urlopen(url)
	if response.getcode() == 200:
		#print response.info()
		f = open('torexit','w')
		for line in response.readlines():
			if line.startswith('ExitAddress'):
				f.write(line.split()[1] + '\n')
		f.close
#Main 
def main():
	GetExit(url)

# call main
if __name__ == '__main__':
	main()

