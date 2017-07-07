---
layout: single
title:  "Discovery of Hadoop"
date:   2015-03-03 16:10:44 +0530
categories: Hadoop
tags: hadoop
header:
    teaser: /assets/images/banner.jpg
---
Back in the early 2000's Dough Cutting was attempting to build an Open Source Search engine called Nutch. They were facing trouble managing their distributed system even when they were running on very few computers. Nutch was stuck with its two half time developers.At the same time Google was facing band problem because they were ingesting the entire internet frequently,they needed to process all the data available on the entire World Wide Web in every couple of days, and it was practically impossible to build an index over the entire internet in a reasonable amount of time by using any commercial tool available. They had documents that were web pages and also their own logs that they had generated, they needed a system which can readout the whole data in time and the problem was they couldn't go buy a document maintenance system which can do their job because there were none available. So they designed and developed their new infrastructure at home which was MapReduce.


MapReduce was a pretty simple idea, you can use some commodity servers with some memory disk attached and every server had a regional amount of CPU. The data were distributed among all the servers with a safe number of replication so that in case you lose a server you got another copy the data somewhere. Now you have stored all your data very cheaply in pretty reliably and the best part is you've got CPU's attached to the disks so if you want to do some indexing or transformation you can use the local CPU to chew over the data and you get this huge parallelism in your data processing. You don’t have to funnel the whole data through a single processer and this basic idea worked and changed the old world where everything was centralized.

 
After Google published its papers on GFS and MapReduce in 2004. Nutch got its route clear they implemented the same their system was not perfect but somehow they managed to run on 20 systems. Very soon they realized that it wasn't something two half timers (Dough Cutting and Mike Cefarella) can handle because they needed to run their processes on thousand of machines and they needed more peoples.

 
Around that time Yahoo got interested in their work Yahoo folks were looking into these projects to add more capabilities to their search engine.   They left out the search engine part of Nutch and developed the distributed computing part of it and named Hadoop.


[embed]https://www.youtube.com/watch?v=ebgXN7VaIZA[/embed]