### Bachelorthesis of Simon Weickert

# Detection and Analysis of Communities in a large-scale bibliographic Graph Database

### Abstract:

> This thesis addresses different approaches to handle large graphical data collections using the bibliographic database DBLP. These approaches aim at reducing the data. One reduction takes place by focusing on the top 200 conferences and those articles that were presented at one of them. Through the Louvain algorithm distinct communities are detected which then allows to further narrow the focus on a subset such as the top 10 communities. This work moreover presents an approach to determine representative articles of the communities. Selecting these is made possible through the generated document-topic probability distribution Theta(d) from the Latent Dirichlet Allocation model. This approach allows to achieve a significant reduction depending on the number of topics and the specification of the representative data quantity. The implementation of this technique leads to lower data density and therefore to an easier management of continuing analyses and better understanding of visualizations. It is assumed that the information content will remain stable as long as the latent topics cover all the important areas of a community. However, to fully validate this approach more research needs to be done in the future. Descriptive visualizations subsequently assist to give an overview of the representative data. In the  final part of this work the individual titles are transformed into a high dimensional vector space using a combination of fastText embedding and weighting by inverse document frequency. The representation in a 2D and 3D scatter plot is made possible through the t-SNE dimensionality reduction algorithm and shows how the titles compare to each other.

To install the packages run 

pip install -r requirements.txt
