import sys
import recommendations as rec

if len(sys.argv) < 2:
	print "Usage: python findcorrelated.py <user_id>"
	print "e.g: python findcorrelated.py 182"
	exit()

pref= rec.loadMovieLens()
correlated_users = rec.topMatches(1, pref, sys.argv[1])
noncorrelated_users =  rec.topMatches(0, pref, sys.argv[1])
print "Five Most Correlated Users to My Substitute: " + sys.argv[1]
print "--------------------------------------------------------"
for user in correlated_users:
	print user[1]

print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

print "Five Least Correlated Users to My Substitute: " + sys.argv[1]
print "--------------------------------------------------------"
for user in noncorrelated_users:
	print user[1]
