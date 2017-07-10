---
layout: single
title:  "Algorithm"
date:   2016-07-16 16:10:44 +0530
categories: algorithm
tags: 
    - algorithm
    - machine-learning
author: Natendra Dubey
header:
  teaser: /assets/site-images/thumb-sphare-vector.jpg
---
**What is an Algorithm?**

Since there is no universally agreed-on wording to describe this notion, there is general agreement about what the concept means:

“*An algorithm is a sequence of unambiguous instructions for obtaining a required output for any legitimate input in a finite amount of time*”

There is a wide range of problems from sorting to sequence matching for which we already have a solutions available. Algorithm design is a field of study which existed even before computers where invented. In this series of blogs we will look at some of the most popular problems and algorithms.

The two motivating forces for any problem is its practical importance and some specific characteristics. The different types of problems are:
- Sorting
- Searching
- String processing
- Graph problems
- Combinatorial problems
- Geometric problems
- Numerical problems

We use these problems to illustrate different algorithm design techniques and methods of algorithm analysis.

**Sorting:**

Sorting problem is one which rearranges the items of a given list in ascending order. We usually sort a list of numbers, characters, strings and records similar to college  information about their students, library information and company information is chosen for guiding the sorting technique. For eg in student’s information, we can sort it either based on student’s register number or by their names. Such pieces of information is called a key. The most important when we use the searching of records. There are different types of sorting algorithms. There are some algorithms that sort an arbitrary of size n using nlog2n comparisons, On the other hand, no algorithm that sorts by key comparisons can do better than that. Although some algorithms are better than others, there is no algorithm that would be the best in all situations. Some algorithms are simple but relatively slow while others are faster but more complex. Some are suitable only for lists residing in the fast memory while others can be adapted for sorting large files stored on a disk, and so on.

**Searching:**

The searching problem deals with finding a given value, called a search key, in a given set. The searching can be either a straightforward algorithm or binary search algorithm which is a different form. These algorithms play a important role in real-life applications because they are used for storing and retrieving information from large databases. Some algorithms work faster but require more memory, some are very fast but applicable only to sorted arrays. Searching, mainly deals with addition and deletion of records. In such cases, the data structures and algorithms are chosen to balance among the required set of operations.

**String processing:**

A String is a sequence of characters. It is mainly used in string handling algorithms. Most common ones are text strings, which consists of letters, numbers and special characters. Bit strings consist of zeros and ones. The most important problem is the string matching, which is used for searching a given word in a text. For e.g. sequential searching and brute- force string matching algorithms.

**Graph problems:**

One of the interesting area in algorithmic is graph algorithms. A graph is a collection of points called vertices which are connected by line segments called edges. Graphs are used for modeling a wide variety of real-life applications such as transportation and communication networks. It includes graph traversal, shortest-path and topological sorting algorithms. Some graph problems are very hard, only very small instances of the problems can be solved in realistic amount of time even with fastest computers. There are two common problems: the traveling salesman problem, finding the shortest tour through n cities that visits every city exactly once. The graph-coloring problem is to assign the smallest number of colors to vertices of a graph so that no two adjacent vertices are of the same color. It arises in event-scheduling problem, where the events are represented by vertices that are connected by an edge if the corresponding events cannot be scheduled in the same time, a solution to this graph gives an optimal schedule.

**Combinatorial problems:**

The traveling salesman problem and the graph-coloring problem are examples of combinatorial problems. These are problems that ask us to find a combinatorial object such as permutation, combination or a subset that satisfies certain constraints and has some desired (e.g. maximizes a value or minimizes a cost). These problems are difficult to solve for the following facts. First, the number of combinatorial objects grows extremely fast with a problem’s size. Second, there are no known algorithms, which are solved in acceptable amount of time.

**Geometric problems:**

Geometric algorithms deal with geometric objects such as points, lines and polygons. It also includes various geometric shapes such as triangles, circles etc. The applications for these algorithms are in computer graphic, robotics etc.

The two problems most widely used are the closest-pair problem, given ‘n’ points in the plane, find the closest pair among them. The convex-hull problem is to find the smallest convex polygon that would include all the points of a given set.

**Numerical problems:**

This is another large special area of applications, where the problems involve mathematical objects of continuous nature: solving equations computing definite integrals and evaluating functions and so on. These problems can be solved only approximately. These require real numbers, which can be represented in a computer only approximately. If can also lead to an accumulation of round-off errors. The algorithms designed are mainly used in scientific and engineering applications.