import lights
import covid_tier_lookup
import sys

from time import sleep

lights = lights.Lights()
covidTierLookup = covid_tier_lookup.CovidTierLookup()

def callback(tier):
	print("callback with tier " + str(tier))
	lights.set(tier)

print("lookup " + sys.argv[1])
while (True):
	covidTierLookup.lookup(sys.argv[1], callback)
	sleep(1800)
