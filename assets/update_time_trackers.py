import requests
import json

page = requests.get('https://www.rescuetime.com/anapi/data?key=B63iJ8U5nu0UAjrr7FBA5W3BzfSUWMzYWO9a04aY&perspective=interval&interval=hour&format=json');

arr = json.loads(page.text);
totalsld = 0
for key in arr['rows']:

	if key[3]=='sldworks':
		totalsld = totalsld + key[1];
		print key

print totalsld