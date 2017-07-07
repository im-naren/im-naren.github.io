---
layout: single
title:  "Hadoop Vs Relational Database Management System"
date:   2015-03-07 16:10:44 +0530
categories: Hadoop
tags: 
    - hadoop
    - big-data
header:
    teaser: /assets/images/banner.jpg
---
Hadoop or RDBMS? There are a lot of different opinions out there among these two technologies. Few people think Hadoop is a replacement of RDBMS, few say Hadoop is the future, and few thinks Hadoop have just got hype. So I have tried to find out what is the reality what Hadoop is really meant for.


**Let talk about the History**

RDBMS was developed with intent of storing and analyzing data, it was developed at a point on timeline when the computation was slow and logical disks were expensive, the whole idea behind this technology was to store data in a structured (tabular) and logical manner so that alot of data can be stored in a small space and since the size is small it can be analyzed with very less computational effort. The unstructured data were not getting much of response; generally unstructured data were getting dumped by the IT giants and other systems. RDBMS evolved as a great technology over time and its capabilities grown to the heights of advancement. RDBMS is a really a phenomenal ETL tool even after 40-50 years from its origin.  But RDBMS have its own limitations.

In the current world when computation is ridiculously fast, Disks are ridiculously cheap and different advanced technologies are producing huge amount of unstructured data. The Devels (developers) of the new advanced world started thinking beyond the limitations of RDBMS capabilities and realizes the importance of this huge data which were getting dumped by different systems. Time was the moment Hadoop came in existence. It is a technology which is deals with unstructured data very efficiently and reliably.

**Differences in capabilities**

**Filtering and Aggregating** – RDBMS is good at filtering and aggregating things quickly. RDBMS will spit out the records in a reasonably small time if you want to find out some specific data from a huge database based on some specific scenario.

**Interactive applications** – if you have data warehouse and you used to fly into your cubes very interactively and very quickly getting answers to questions which are sort of pre-computed then Hadoop would be a bad choice. On the other hand RDBMS are bad with problem like “how many or which are the new customers who have visited you store first time ever last one year?”  Something where you need to process each line of you database. RDBMS always takes time in founding out counts other thing where the RDBMS always eat up time is COURSERS where you loop through rows.

**Orientation of Data** – Hadoop is best suited for raw data and RDBMS for structural data. Hadoop is a “schema on read” technology but RDBMS is a “Schema on write” technologies i.e.  Before writing the data in a transactional database you need to have a hand full of information like Structure of the tables and data types, and you need to convert your data to fit in the tables. But in case to Hadoop you just need to distribute the data across the cluster and then read in whatever structure you want to.

**Failures** – Hadoop handles the failure of nodes internally. MapReduce queries don’t hold up results even in case of failures, because of data replication mechanism the delivered results are reliable and consistent against the no failure scenario. On the other hand a Relational database management system (RDBMS) does not release any results to the user in case of failure because it doesn’t have the complete dataset which is called two phases commit.

**Scalability** – Hadoop solutions are something scalable to 1000 servers or even beyond that it’s very cheap and reliable. RDBMS starts giving problem when it need to scale. Scaling for a RDBMS system is very expensive, with

**Objective of solution** – RDBMS and star schema is fundamentally about transaction. Where we are doing the financial planning but they are not really grateful for marketing stuffs because in market planning we are not really seeking answers about transactions we are asking questions about peoples and customers. RDBMS is good for simple things whatever that fits in a table RDBMS is a great analyzing tool but when things starts exceeding out of tables like Customers who are using your website, Hadoop is the better option.

**Expert’s Opinion**

According to a joint report from Cloudera and Teradata – “Hadoop and the data warehouse will often work together in a single information supply chain. When it comes to Big Data, Hadoop excels in handling raw, unstructured and complex data with vast programming flexibility. Data warehouses also manage big structured data, integrating subject areas and providing interactive performance through BI tools.”

**When to Use Which**

REQUIREMENT | DATA WAREHOUSE | HADOOP
----------- | ---------------|----------
Low latency, interactive reports, and OLAP | ✔ | ✘
ANSI 2003 SQL compliance is required | ✔ | ✘
Preprocessing or exploration of raw unstructured data | ✘ | ✔
Online archives alternative to tape | ✘ | ✔
High-quality cleansed and consistent data | ✔ | ✘
100s to 1000s of concurrent users | ✔ | ✔
Discover unknown relationships in the data | ✔ | ✔
Parallel complex process logic | ✘ | ✔
CPU intense analysis | ✔ | ✔
System, users, and data governance | ✔ | ✘
Many flexible programming languages running in parallel | ✘ | ✔
Unrestricted, ungoverned sand box explorations | ✘ | ✔
Analysis of provisional data | ✘ | ✔
Extensive security and regulatory compliance | ✔ | ✘
Real time data loading and 1 second tactical queries | ✔ | ✔

**Conclusions**

Hadoop is different in Quality from the RDBMS systems. Hadoop is good in exhaustive batch processing deep analysis. If you’ve got an existing enterprise data warehouse problem then Hadoop is gonna map poorly. Where Hadoop will really shine is the new data sources which are online, if you want to understand them digest them and maybe even load summary of them into your cube. Hadoop is not a replacement of RDBMS but it is a technology which needs to run parallel to your RDBMS infrastructure. RDBMS is still unequivocally a good tool to run the ETL process Hadoop is entirely a different perspective in the world of database which deals with a different kind of problems.