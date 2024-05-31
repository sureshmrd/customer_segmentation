# CUSTOMER SEGMENTATION USING MACHINE LEARNING (Clustering using KMeans)

## Introduction
- This Machine Learning Project is related to the **UnSupervised Machine Learning** using KMeans Clustering.
- The Main idea is to cluster the similar customers of a mall based on their Annual Income & Spending Scores.
- The dataset is taken from the kaggle , and dataset contains attributes like customer id , gender , age , annual income and spending score.
- Customer segmentation using machine learning involves dividing a customer base into groups of individuals who are similar in specific ways relevant to marketing, such as  behavior, or preferences.
- The goal is to identify patterns and trends within the customer data that allow businesses to better understand and target their customers.

## Objective 
- The main objective of this project is to group the customers of small mall , into different groups.
- Using this ,we can get start with the UnSupervised Machine learning , because clustering is one of the important topic in the UnSupervised learning.

## Methodology
- This Customer segmentation is done using the **KMeans** clustering algorithm of the Machine Learning.
- For the functionality of the algorithm , here **Scikit Learn** is used , which is a python library to implement machine learning models.

  ### KMeans Algorithm
  - KMeans clustering is one of the most popular unsupervised machine learning algorithms used for clustering data points into groups or clusters based on similarity.
  - The algorithm starts by randomly initializing K cluster centroids. These centroids represent the centers of the clusters that will be formed. K is the number of clusters.
  - Each data point is then assigned to the nearest centroid based on some distance metric, typically Euclidean distance. The data points are assigned to the cluster whose centroid is closest to them.
  -  Once all data points are assigned to clusters, the centroids are recalculated based on the mean of all the data points assigned to each cluster. This step effectively moves the centroids to the center of their respective clusters.
  -  Convergence occurs when the centroids no longer change significantly or when a specified number of iterations is reached.
  -  Once convergence is reached, the algorithm produces K clusters, where each cluster contains a group of data points that are more similar to each other than to data points in other clusters.
    #### How to select the 'k' value???
    - The Answer is : using **Elbow Method (WCCS)**.
    - The Elbow Method is a common technique used to determine the optimal number of clusters (K) in a KMeans clustering algorithm.
    - It involves plotting the within-cluster sum of squares (WCSS) against the number of clusters and looking for the "elbow" point where the rate of decrease in WCSS slows down significantly.
    - ![image](https://github.com/sureshmrd/cust_seg/assets/123853377/9c95f3ef-4a06-41d3-b1f4-548af11f8165)
  ```python
     Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    - Inside the loop, a new KMeans clustering model is initialized with the current value of i as the number of clusters.
    - n_clusters=i specifies the number of clusters for the KMeans model.
    - init='k-means++' specifies the initialization method for the centroids. 'k-means++' is a smart initialization method that helps to speed up convergence.

  
 


### Results
- Formed 5 Clusters and grouped the customers of the mall into different clusters.
- ![image](https://github.com/sureshmrd/cust_seg/assets/123853377/c5e1b1fa-2bac-4cea-abac-50a81a217409)

 
### Advantages:
- **Personalized Marketing**: Customer segmentation allows for targeted marketing strategies tailored to the needs and preferences of different customer groups.
- **Improved Customer Satisfaction**: By understanding different segments, businesses can offer more personalized experiences, leading to higher customer satisfaction.
- **Enhanced Decision Making**: Data-driven segmentation provides insights that can guide strategic decision-making processes, such as product assortment, pricing strategies, and promotional campaigns.
- **Competitive Advantage**: Implementing machine learning-based customer segmentation can give businesses a competitive edge by staying ahead of market trends and customer preferences.

### Conclusions
- **Cluster 1** : Customers in this cluster have moderate annual income and moderate spending scores. They might be considered average customers who spend moderately compared to others. Businesses can focus on understanding their preferences better to tailor marketing strategies and product offerings that resonate with this segment.
- **Cluster 2** : Customers in this cluster have high annual income but relatively low spending scores. They might be considered as cautious spenders who are financially well-off but prefer to save rather than spend extravagantly. Businesses can target them with personalized offers or incentives to encourage higher spending.
- **Cluster 3** : This cluster consists of customers with relatively low annual income and low spending scores. They might be budget-conscious customers who prioritize saving over spending. Businesses can consider offering discounts or promotions to attract these customers and increase their spending.
- **Cluster 4** : This cluster represents customers with moderate to low annual income and high spending scores. They are likely to be impulse buyers or individuals who enjoy shopping and are willing to spend more on products or services they desire. Businesses can focus on providing a seamless shopping experience and personalized recommendations to enhance their satisfaction and loyalty.
- **Cluster 5** : This cluster contains customers with relatively high annual income and high spending scores. These customers are likely high-value customers who have the financial capacity to spend more on products or services. Businesses can target them with premium offerings or loyalty programs to retain their high spending levels.




