# 3. Exercise
This is a documentation for the thrid exercise from the subject I-PPDS.

For the third exercise I chose Producer-Consumer.

# 1. experiment
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 10
-   Number of Producers: 10
-   Storage size: 10

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/base_setting.png)

If time to produce is increased so is number of products per second. While the number of consumers is increasing the number of products is increasing too so there is more products in storage then there is consumers.

# 2. experiment
Settings:
-   Time to produce: n / x where n = 1-9 and x = 100
-   Tme to consume: randint(0, 10) / x where x = 100
-   Number of Consumers: 20
-   Number of Producers: 10
-   Storage size: 100

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/03/images/experiment2.png)

I increased number of Consumers to max 20 and in the graph we can see that number of products decreased. Interesting is that number of them is 800 which is 300 more then from the previous graph.
