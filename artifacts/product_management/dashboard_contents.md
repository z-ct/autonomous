# Version 1 of Dashboard
*We intended to show flow as the primary detail, with subsidiary columns being components to revenue, components to trust, and components to market health (from left to right respectively).*
![Dashboard v1](https://github.com/z-ct/autonomous/blob/master/artifacts/product_management/Dashboard%20v1.jpg "Dashboard v1")


# Dashboard Contents
*This is a rich list, certain datapoints from it will be extracted for the visual dashboard*

## Sales Data

| What | Unit | Formula | Window | Baseline | Example |
| ---- | ---- | ------- | ------ | -------- | ------- |
| Devices on network | Int | N/A | Daily | Weekly | 1.49 million devices on network |
| % Devices Active | % | # Deevices active that day / # of devices on network | Weekly | Quarterly | 89 % of the devices on the network were active today |
| Users | Int | N/A | Weekly | Quarterly | There are 1 million users on the network |
| Devices per user | Int | Average (devices / user) | Weekly | Quarterly | The average user has 2 devices | 
| Median time until second device | Time | Median (time until second device) | Weekly | Quarterly | Median user with a second device bought it 8 weeks after the first device | 
| Money saved | $ | N / A | Monthly | Month - 1 | How much money did your car saved last month |
| Transactions per vendor | # | aggregate | Weekly | Month - 1 | How many transactions did you took part of as a vendor |



## Revenue Data

| What | Unit | Formula | Window | Baseline | Example |
| ---- | ---- | ------- | ------ | -------- | ------- |
| Revenue | $ | N/A | Weekly | Quarterly | $3,000,000 revenue this week |
| $ Flowing through Z-CT | $ | N/A | Daily | Daily | 
| Number of transactions | Int | N/A | Daily | Daily (during growth phase) | 111,650 transactions occurred today |
| Volume of transactions | $ | N/A | Daily | Daily (during growth phase) |  $1,502,601 transacted today |
| Descriptive Statistics of  transaction amount | $ Int | Mean, Median, Mode, Std Dev | Daily | Daily (during growth phase) |  Transaction amount: mean = 15, median = 17, mode 20, std dev = 3 |
| Descriptive statistics of transactions per device | Int | Mean, Median, Mode, Std Dev | Daily | Daily (during growth period | Trns / User: mean = 3, median = 3, mode = 1, std dev = 0.8 |
| Descriptive statistics of budget per user |$| Mean, Median, Mode, Std Dev | Daily | Daily (during growth period | Budget / User: mean = 300, median = 312, mode = 190, std dev = 80 |
| Number of seller nodes | Int | N/A | Daily | Daily | 3,000 seller nodes |
| Descriptive statistics of transactions / seller | Int | Mean, Median, Mode, Std Dev | Daily | Daily (during growth period | Trns / Seller: mean = 3, median = 3, mode = 1, std dev = 0.8 |

## Network Health Data
| What | Unit | Formula | Window | Baseline | Example |
| ---- | ---- | ------- | ------ | -------- | ------- |
| Descriptive statistics of number of bids per transaction (split by industry) | Int | Mean, Median, Mode, Std Dev | Daily | Daily (during growth period | Bids / Transaction: mean = 3, median = 3, mode = 1, std dev = 0.8 |
| % transactions disputed |%| Transactions disputed / transactions | Weekly | Quarterly | 0.8 % of transactions were disputed |
| % of users w/ transactions disputed |%| Users w/ transactions disputed / Tot Users (with >0 transactions) | Weekly | Quarterly | 0.2 % of users had transactions disputed |
| Pie chart - type of auction triggered | % | Auction type / total number of auctions | Weekly | Quarterly | 14% of auctions were second price auctions |
| Pie cha1rt - industry | % | Industry / total number of auctions | Weekly | Quarterly | 24% of transactions were auto-related |
| Perception of fairness | score | N / A | Weekly | Quarterly | 4.8 |
| Perception of value | score | N / A | Weekly | Quarterly | 4.3 |


## Extract of data on first adopters
All of the same data, but for the subset of users whose first device was an autonomous vehicle.
