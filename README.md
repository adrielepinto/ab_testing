# A/B Testing

![image](https://user-images.githubusercontent.com/97919969/186538073-7365c477-0243-4f16-8ed5-200ffe2a6411.png)

 # 1.0 PA James

 The UX Designers team is working on a new sales page, with the objective of increasing the conversion rate from 13% to 15%, that is, a 2% increase in conversion for the product 'Bluetooth Keyboard'. The product has a retail price of $4,500.00. However, the manager would like to test the effectiveness of the new page on a smaller group of customers, in order to run less risk of dropping conversions, if the new page shows a smaller conversion than the old one.
 
# Challenge:

1. Is the conversion of the new page really better than the old one?
 
    Wasn't impossible to see the effect on the new page

 2. What potential sales figures can the new page bring?
 
Wasn't impossible to see the effect on the new page


3. What is the total revenue from the sale of the new page's bluetooth keyboard?
   
  Wasn't impossible to see the effect on the new page

  # Data Frame Descriptions
  

  <img width="225" alt="Screen Shot 2023-08-29 at 11 53 17 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/261c26ac-17ad-4243-9d58-1054fc99dad8">
  
  This dataset has 294478 lines and 5 columns.
  

  <img width="192" alt="Screen Shot 2023-08-29 at 11 56 41 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/c61f7ebc-173b-4831-bac1-7a71329929c6">

  However, was needed a sample of  4720 from the datase to run the teste.

# Conclusion

<img width="460" alt="Screen Shot 2023-08-29 at 12 33 17 PM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/e949c732-3d5c-4e52-b225-ca0ee76cc21d">

A failed to reject the null hypothesis, that mean, the null hypothesis is true. Unfortunately with the sample size, it wasn't possible to conclude that the new page designer made by the UX Designers team IS or IS NOT better than the current page. It was impossible to identify an action with the data present in the dataset. The next step to improve the result of this test would be to collect more data that better explain the effect to take more samples.




<img width="368" alt="Screen Shot 2023-08-29 at 12 03 25 PM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/82999ffd-1d8c-41e1-9886-47ae5f667d3d">


However, in a hypothetical scenario, where the new page conversion actually went from 13% to 15%, the company would have a lift of $25,803,000.00 in the company's revenue.



# 2.0 P A Bound

Electronic House is a company that sells products online. The product director would like to develop a new way of filling out credit cards that isn't done manually. A solution was delivered where 90% of payments were filled in automatically. However, the design team would like to measure the effectiveness of the new product, to conclude whether the new payment method was really better than the old one.
  The two pages were put online by someone, and a label was assigned to each customer, showing which page the customer was viewing.

  # Challenge:
  
  What is the best payment method? Manual or automatic?

  # Data Frame Descriptions


  <img width="256" alt="Screen Shot 2023-08-30 at 8 36 26 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/98392862-5bba-4b20-b291-378093d20b50">


This dataset has 45883 lines and 8 columns.

 <img width="331" alt="Screen Shot 2023-08-30 at 8 40 47 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/3cf9fae3-037c-4fc4-bafa-fcd6fda87bde">

  However, was needed a sample of 6588 from the datase to run the teste.

  <img width="844" alt="Screen Shot 2023-08-30 at 8 55 21 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/01ef52a3-f698-4c58-8298-aed438429eee">

 Analyzing the data, was possible to verify that the purchases don't have a distorting difference between group A and group B. The behavior of groups are very similar to each other.


# Conclusion

<img width="842" alt="Screen Shot 2023-08-30 at 9 28 44 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/ddef2d86-0eff-444f-b6b4-b7bf73cfdfe3">


After run the tests, it is concluded that the design team needs to rethink the strategy of the automatic filling device.

# 3.0  A | B | N Testing
The Montana library has a page that has a university banner, a search bar, three main access categories and a sidebar on the right. During the period from April 3, 2013 to April 10, 2013, the library 'home' page received 10,819 visitors. Analyzing the page access data, the IT team and the University noticed a big difference between the accesses of the page category. The click-through rate for 'Find' was 35%, 'Request' was 6%, and 'Interect' was 2%.
Looking at the click-through rates, the IT team wondered why interest category conversion was so low. Therefore, an A/B/N test needs to be defined to validate which of the category variations is most attractive to students.

# Challenge:

Is any of the conversions really better than the current one? What would the name of the variation be?

 # Data Frame Descriptions
 <img width="867" alt="Screen Shot 2023-08-30 at 9 56 23 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/e2d310de-8749-464e-aafe-fa19eddf67be">


 Data collection was done according to information from each page.

 # Conclusion

 <img width="839" alt="Screen Shot 2023-08-30 at 11 48 15 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/3e93610e-ecca-4351-942b-2e1805d4c399">


From a statistical point of view, the results of the tests showed that the Connect, Services and Help pages didn't have any differ from each other. The  IT team can use any of them, however it is recommended to use them according to the lowest P_Value of each page.

## Interact x Connect == There is a correlation = p_value == 5.3676772349808135
## Interact x Service == There is a correlation = p_value == 1.798089447385411
## Interact x Help== There is a correlation  = p_value == 0.0031030587017400212


# 4.0 A | B Bayesian Test

ISketch company manufactures software focused on 3D development of civil construction projects. To acquire customers, the company uses email capture in exchange for a Newsletter with weekly content on civil construction. The Marketing coordinator asked the Designer team to create a new page with a modification of the red 'Sign-Up' button that has the blue button. Therefore, the company's data scientist team needs to test the effectiveness of the button's color.

# Challenge:

The Marketing team expects the Data Science team to complete the test in less than 7 days.

 # Solution Infrastructure

 <img width="577" alt="Screen Shot 2023-08-30 at 1 11 52 PM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/c1615ba2-556a-4597-ba41-7a2ab5ff5913">

In a simple structure, two HTML pages will be exposed on the internet. A Reinforcement Learning agent ( App.py ) will be responsible for choosing which of the two pages to show, the page with the Blue rumor or the page with the red button, according to the determined criteria. However, it is necessary to choose the page that maximizes the return for the company, simulating that the chosen page was shown to the consumer/client, and the probability of that client leaving the email to receive information will be calculated. 

## A | B Bayesian

<img width="1106" alt="Screen Shot 2023-08-31 at 10 32 59 AM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/a7a505df-3483-4250-9dad-210c2f2f026c">


- The graph on the right shows that on day 25 the probability of page B being better than page A is approximately 97%.
- The graph on the left shows that the risk associated with choosing page B, saying it is better than A is less than 0.01%.
  
Given that, we can end the experiment by saying that page B with the red button, is better than page A with the blue button.

# Experiment in Production





https://github.com/adrielepinto/ab_testing/assets/97919969/303952fe-f3ca-40b3-a340-527c861db7c4





https://github.com/adrielepinto/ab_testing/assets/97919969/6150d43b-1338-401d-a2ca-d41b3fc118ec

# 5.0 Mult Armed bandit - MAB 

A person enters a casino to have fun with slot machines. Each machine has a different probability of return totally unknown, some have higher chances of winnings while others smaller. The player allocates some machines next to each other, and after a few rounds the player needs to make a decision: he continues playing with the machines that had the highest return or he can choose random machines to play.

# Challenge:
 How the player can make the best decision in order to maximize the final result?

   # Solution Infrastructure

   <img width="833" alt="Screen Shot 2023-08-31 at 2 07 19 PM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/cb844124-b1e5-4b8a-8553-70bc5df28446">

In the first structure, there are two pages that will receive visitors, where data will be collected for a certain time of the experiment.

<img width="512" alt="Screen Shot 2023-08-31 at 2 16 14 PM" src="https://github.com/adrielepinto/ab_testing/assets/97919969/c9e0e4ea-3676-4a9a-908b-b7831fb00da9">


