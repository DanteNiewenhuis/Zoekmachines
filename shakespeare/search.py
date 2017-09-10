import os
import re
from collections import Counter
from bs4 import BeautifulSoup

scripts = os.listdir('scripts')
for x in range(len(scripts)):
	#read
	with open('scripts/'+scripts[x], 'r') as script:
		soup = BeautifulSoup(script, 'lxml-xml')

		#cleanup
		soup = soup.get_text()
		soup = re.sub('[^\w\d\s\']', "", soup).strip('\n')
		soup = re.sub(r'\'\W', "", soup)

		#tokenizen
		soup = soup.replace(' ','\n')
		soup = re.sub(r'\n\s*\n', '\n', soup)

	for token in soup:
		if not token.isupper():
			token.lower()	
	with open('tokens/'+scripts[x][:-4]+'.txt', 'w') as text:
		text.write(soup)

