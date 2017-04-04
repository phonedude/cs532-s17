import sys
import recommendations as rec

if len(sys.argv) < 2:
        print "Usage: python findrecommended.py <user_id>"
        print "e.g: python findrecommended.py 182"
        exit()

pref= rec.loadMovieLens()
ranks = rec.getRecommendations(pref, sys.argv[1])

print "Five Most recommended Movies for My Substitute: " + sys.argv[1]
print "--------------------------------------------------------"
for movie in ranks[:5]:
        print movie[1]

print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

print "Five Least Recommended Movies for My Substitute: " + sys.argv[1]
print "--------------------------------------------------------"
for movie in ranks[-5:]:
        print movie[1]

print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

