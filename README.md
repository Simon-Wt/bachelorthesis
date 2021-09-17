### Bachelorthesis of Simon Weickert

# Detection and Analysis of Communities in a large-scale bibliographic Graph Database

### Abstract:

> This thesis addresses different approaches to handling large graphical data collectionsusing the bibliographic database DBLP. These approaches aim at reducing the data.One reduction takes place by specializing on the top 200 conferences and those articlesthat were presented at one of them.Through the Louvain algorithm distinct communities are detected which enables to fur-ther narrow the focus on a subset such as the top 10 communities. With this workI further present an approach to determine representative articles of the communities.The selection of these is possible thanks to the generated ”document to topic” probabil-ity distributionθdfrom the Latent Dirichlet Allocation model. This approach allows toobtain a significant reduction depending on the number of topics and the specificationof the representative data quantity. Thus, continuing analyses can be more easily man-aged and visualizations can be better understood due to the lower data density. Theassumption here is that the information content will remain stable as long as the latenttopics cover all the important areas of a community. However, more research needs tobe done in the future to validate this.Descriptive visualizations subsequently assist to give an overview of the representativedata. Finally, the work is concerned with transforming the individual titles into a highdimensional vector space using a combination of fastText embedding and weighting byinverse document frequency. The representation in 2D and 3D scatter plot is possiblethrough the dimensionality reduction of t-SNE and shows that the titles are spreadthroughout the space and that the communities can be partially recognized.

To install the packages run 

pip install -r requirements.txt
