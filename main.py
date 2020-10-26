#import lights
import covid_tier_lookup

from time import sleep

lights = lights.Lights()
covidTierLookup = covid_tier_lookup.CovidTierLookup()

def callback(tier):
	print("callback with tier " + str(tier))

while (True):
	covidTierLookup.lookup(argv[0] callback)
	sleep(1800)
