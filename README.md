# 3. Exercise
This is a documentation for the thrid exercise from the subject I-PPDS.

For the third exercise I chose Producer-Consumer.

In the first experiment I declared base setting that I will edit in the following experiments.

# 1. experiment - Base Settings
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 10
-   Number of Producers: 10
-   Storage size: 10

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/base_setting.png)

If time to produce is decrease so is number of products per second. While the number of consumers is increasing the number of products is increasing too so there is more products in storage then there is consumers.

# 2. experiment - Increase number of Consumers
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 20
-   Number of Producers: 10
-   Storage size: 10

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/experiment2.png)

I increased number of Consumers to max 20 and in the graph we can see that number of products decreased. Interesting is that number of them is 800 which is 300 more then from the previous graph.

# 3. experiment - Increase Storage size
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 10
-   Number of Producers: 10
-   Storage size: 20

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/experiment3.png)

I increased the Storage size to 20. Diffrence from the last graph is that data are more consistent.

# 4. experiment - Decrease time to Produce and time to Consume
Settings:
-   Time to produce: n / x where n = 1-9 and x = 200
-   Tme to consume: randint(0, 10) / x where x = 200
-   Number of Consumers: 10
-   Number of Producers: 10
-   Storage size: 10

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/experiment4.png)

I decrease time to produce and time to consume. In this graph we can best see that with decreased time to produce products the more productes are produced.

# 5. experiment - Increase number of Producers
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 10
-   Number of Producers: 20
-   Storage size: 10

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/experiment5.png)

I increase the number of producers. We can see on the graph that there is sudden incerease in number of products based on the time.
