import covid_tier_lookup

covidTierLookup = covid_tier_lookup.CovidTierLookup()

covidTierLookup.lookup("LS1 1UR", lambda x: print("Leeds " + str(x)))
covidTierLookup.lookup("YO10 5DH", lambda x: print("York " + str(x)))
covidTierLookup.lookup("M22 5EJ", lambda x: print("Manchester " + str(x)))
covidTierLookup.lookup("TR11 2PH", lambda x: print("Cornwall " + str(x)))
