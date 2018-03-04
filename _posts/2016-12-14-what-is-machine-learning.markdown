---
layout: single
title:  "What is Machine Learning?"
date:   2016-12-14 16:10:44 +0530
categories: machine-learning
tags:
    - machine-learning
header:
    teaser: /assets/site-images/thumb-sphare-vector.jpg
---
> Machine learning is a field of study that provides computers with the ability to learn without being explicitly programmed - Arthur Samuel.

Machine learning is a part of computer science which focuses on the development of computer programs that can teach themselves to grow and change based on the data it is exposed to. 

Machine learning algorithms are used heavily in mining large data sets like click stream data, flight data, engineering data, sensor data etc. Machine learning programs detect patterns in data and adjust program actions accordingly. For example, Facebook's News Feed changes according to the user's personal interactions with other users. If a user frequently tags a friend in photos, writes on his wall or "likes" his links, the News Feed will show more of that friend's activity in the user's News Feed due to presumed closeness.

Machine learning algorithms plays  a big role solving complex problems which cannot be programmed like flying an Aircraft, DNA sequencing, Genome Analysis.

The machine learning algorithms can be classified into two main categories:

* Supervised Learning Algorithms
* Unsupervised Learning Algorithms

### Supervised learning algorithms

The majority of practical machine learning uses supervised learning. In a supervised machine learning algorithm we start with a data set which contains both the inputs and the corresponding correct answer and we train the algorithm to learn a function good enough to predict the correct or approximate correct output for a new given input value which it have not seen before.

The supervised learning algorithms can be further grouped under **Regression** and **Classification** problems.

**Regression** All the algorithms used to predict a continuous number as output for a given input, then its a Regression algorithm. 

e.g: if we are trying to predict the price of a house, based on history of real state transaction data its a Regression problem since the price is continuous number. 

**Classification** All the algorithms where we try to predict a the group in which a given input falls in is a Classification problem.

e.g. if we are trying to predict if the given email is spam or not, its a classification problem, since there the two groups span and not-spam and we are trying to put the given input in one of there,  the number of groups can be two or more then two. let take another example let say given a bunch of images we want to predict of there is a cat, dog, horse or a tiger 


### Unsupervised  learning algorithms

In this type of learning algorithms we use to only have input data, the corresponding output is unknown and the algorithms are left to their own to discover and present the interesting structure in the data, The goal for unsupervised learning is to model the underlying structure  
or distribution in the data in order to learn more about the data.

Unsupervised learning problems can be further grouped into **Clustering** and **Association** problems.

**Clustering**: A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behaviour.

**Association**:  An association rule learning problem is where you want to discover rules that describe large portions of your data, such as people that buy X also tend to buy Y
