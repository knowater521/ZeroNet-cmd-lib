import json, sqlite3

def getWrapperkey(data_directory, address):
	with open("%s/sites.json" % data_directory) as f:
		sites = json.loads(f.read())
		if address in sites:
			return sites[address]["wrapper_key"]
		else:
			raise KeyError("No site %s" % address)

def findByWrapperkey(data_directory, wrapper_key):
	with open("%s/sites.json" % data_directory) as f:
		sites = json.loads(f.read())

		for address, site in sites.iteritems():
			if site["wrapper_key"] == wrapper_key:
				return address

		raise KeyError("No wrapper key %s" % wrapper_key)

def sqlQuery(path, query):
	conn = sqlite3.connect(path)
	cursor = conn.cursor()
	return cursor.execute(query)


def getDomains(path, address):
	with open(path, "r") as f:
		names = json.loads(f.read())

		domains = []
		for domain, result in names.iteritems():
			if result == address:
				domains.append(domain)

		if len(domains) == 0:
			raise KeyError("%s has no domains" % address)
		else:
			return domains

def findByDomain(path, domain):
	with open(path, "r") as f:
		names = json.loads(f.read())
		if domain in names:
			return names[domain]
		else:
			raise KeyError("No domain %s" % domain)