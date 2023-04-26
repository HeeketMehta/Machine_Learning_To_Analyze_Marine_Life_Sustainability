# A Machine Learning Approach to Analyze Marine Life Sustainability

```
Proceedings of International Conference on Intelligent Computing, Information and Control Systems, 2021, Volume 1272 <br />
ISBN : 978-981-15-8442-8<br />
Danish Jain, Shanay Shah, Heeket Mehta, Ayushi Lodaria, Lakshmi Kurup<br />
https://link.springer.com/chapter/10.1007/978-981-15-8443-5_53<br />
```

## Problem Statement <br />

In this project, we implement the task of analyzing the water quality containing various attributes and characteristics of numerous rivers and water bodies in multiple states of India since the water is highly polluted.
To do so, we develop a model to calculate and categorize the quality of water based on parameters like ‘pH’, ‘Temp’, ‘D. O.’ by determining an attribute Water Quality Index (WQI) using supervised machine learning algorithms.
Results of this model will be extrapolated to calculate sustainable water quality for marine life salubriousness.
Moreover, our aim is to categorize the freshness of fish based on fish tissues using image processing and computer vision.

## Overview <br />
In this project, we have made an attempt to study the quality of water. There are many quality parameters like  ‘pH’, ‘Temperature’, ‘Dissolved Oxygen (DO)’, etc. which plays a key role in determining the Water quality index (WQI). 
The WQI values range from 19.3 to 99.8 which are then scaled down and classified into five categories using Random Forest Algorithm, K- Nearest Neighbors (KNN) and Support Vector Machine. By taking the WQI into consideration.
The results obtained by the Random Forest Algorithm provides 92.127% accuracy in classifying the water quality. 
The results were visualized on the basis of various years and states in India.<br />


## Getting Started 

We mostly use Python in the project and hence, we used libraries that can be installed using - <br />
```
pip install pandas
pip install numpy
pip install seaborn
pip install matplotlib
pip install sklearn
```

## Proposed Architecture / Flow Diagram
We propose the flow diagram below and execute the methodology in the following sense, to obtain results of water quality analysis, to understand various trends, and build machine learning models to understand how polluted water quality may be and its effect on marine life.<br />
![BAR_GRAPH_STATE](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/System_Architecture.png)<br />

## Exploratory Data Analysis


![BAR_GRAPH_STATE](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/DATA_VISUALIZATION/BAR_GRAPH_STATE.JPG)<br />
![Year_vs_wqi](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/DATA_VISUALIZATION/Year_vs_wqi%20line%20chart.JPG)<br />
![State_VS_Fish](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/DATA_VISUALIZATION/STATE%20VS%20FISH%20Water.JPG)<br />


## Machine Learning Results

Random Forest algorithm performs the best, to classify the water quality into various classes, with the segragation being on the quality of water, for both being potable and for the marine life present in the waterbodies.<br />

The results - in terms of confusion matrix/ cross tab are mentioned below - 
### Random Forest Implementation -
![Random Forest Implementation](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/Random%20Forest%20Output.JPG)<br />

### Support Vector Machine Implementation -
![Support Vector Machine Implementation](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/SVM_OUTPUT.JPG)
<br />

### K-Nearest Neigbors Implementation -
![K-Nearest Neigbors Implementation](https://github.com/HeeketMehta/Marine-Life-Sustainability-using-ML/blob/master/OUTPUT/KNN_OUTPUT.JPG)<br />

## Conclusion
Please check out the paper we published at the following URL - 
```
https://link.springer.com/chapter/10.1007/978-981-15-8443-5_53
```
We really appreciate your interest

## Authors
```
Heeket Mehta
Ayushi Lodaria
Shanay Shah
Danish Jain
```

## Mentorship -
```
Prof. Lakshmi Kurup
```





