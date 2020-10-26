import urllib.request
import re

class CovidTierLookup:
	# lookup tier by postcode and return zero indexed tier via callback, -1 if unknown
	def lookup(self, postcode, resultCallback):
		values = {}
		values['postcode-lookup'] = postcode
		data = urllib.parse.urlencode(values)
		data = data.encode('ascii')
		req = urllib.request.Request('https://www.gov.uk/find-coronavirus-local-restrictions', data)

		with urllib.request.urlopen(req) as response:
			html = response.read().decode('utf-8').replace('\n', ' ').replace('\r', '')
			m = re.search('COVID alert level: (.*?)<', html, re.MULTILINE | re.IGNORECASE)
			result = -1;
			if m:
				level = m.group(1).strip().lower();
				if level.startswith('medium'):
					result = 0
				elif level.startswith('high'):
					result = 1
				elif level.startswith('very high'):
					result = 2

				resultCallback(result)

