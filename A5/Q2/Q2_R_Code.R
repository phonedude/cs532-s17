library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 3)
colors <- terrain.colors(3, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph if the Club splits into 3 groups"
)

library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 4)
colors <- terrain.colors(4, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph if the Club splits into 4 groups"
)

library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 5)
colors <- terrain.colors(5, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph if the Club splits into 5 groups"
)


