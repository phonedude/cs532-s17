library(igraph)
library(igraphdata)
data(karate)
plot.igraph(karate,
            vertex.color="yellow",
            vertex.size = 10,
            main="Karate Club Social Interaction Graph Before Club Fission"
)

library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 2)
colors <- cm.colors(2, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph if the Club splits into 2 groups"
)