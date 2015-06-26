import requests
import json

page = requests.get('https://www.rescuetime.com/anapi/data?key=B63iJ8U5nu0UAjrr7FBA5W3BzfSUWMzYWO9a04aY&perspective=interval&interval=hour&format=json');

arr = json.loads(page.text);
totalsld = 0;
totalink = 0;
totaleag = 0;
for key in arr['rows']:

	if key[3]=='sldworks':
		totalsld = totalsld + key[1];
	if (key[3]=='x11' or key[3]=='inkscape'):
		totalink = totalink + key[1];
	if key[3]=='eagle':
		totaleag = totaleag + key[1];

print totalsld