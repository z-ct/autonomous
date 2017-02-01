# Market Sizing

There are a few approaches we can take with market sizing, we consider two: 
- an analysis the market size of each industry that we hope to automate the transactions in;
- an analysis of the size of the payments market, with an estimate on what percentage of payments we would be able to automate.

Since our system is meant to be industry agnostic (at least, in the long term vision), we are starting with the second approach.

| Flat fees | source | numbers |
| --- | --- | ---: |
| Number of non-cash consumer transactions | [Capgemini](https://www.worldpaymentsreport.com/sites/all/themes/wpr_theme/frontend/dist/images/other/infograph.jpg) | 426 Bn (increasing at ~10% p/a) |
| Projected number of non-cash consumer payments in 2020\* | (conservative assumption of non-increasing growth) | ~ 686 Bn |
| Average flat transaction fee per transaction | [Merchant Maverick](https://www.merchantmaverick.com/the-complete-guide-to-credit-card-processing-rates-and-fees/)\*\* | 0.10 |
| Projected flat transaction fees chargeable worldwide in 2020 | *math* | 68.6 Bn |

\*this may be useful if we choose to have a flat, per transaction fee, but we will analyse the potential business plans at a later date.
\*\*note, this is a US sum, we should average across the world.

| Percentage fees | source | numbers |
| --- | --- | ---: |
| Volume of non-cash consumer transactions | [Capgemini](https://www.worldpaymentsreport.com/sites/all/themes/wpr_theme/frontend/dist/images/other/infograph.jpg) | 426 Bn (increasing at ~10% p/a) |
| Projected volume of non-cash consumer payments in 2020\* | (conservative assumption of non-increasing growth) | ~ 686 Bn |
| Average percentage transaction fee per transaction | [Merchant Maverick](https://www.merchantmaverick.com/the-complete-guide-to-credit-card-processing-rates-and-fees/)\*\* | 2.10% |
| Projected percentage transaction fees chargeable worldwide in 2020 | *math* | 68.6 Bn |


## Other sources to consider:
* https://www.helcim.com/us/pricing/visa-mastercard-interchange-rates/
* http://www.creditcards.com/credit-card-news/payment-method-statistics-1276.php
* https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiO9ruKp-_RAhXpy4MKHUOvALQQFggaMAA&url=http%3A%2F%2Fwww.mckinsey.com%2F~%2Fmedia%2Fmckinsey%2Fdotcom%2Fclient_service%2Ffinancial%2520services%2Flatest%2520thinking%2Fpayments%2Fglobal_payments_2015_a_healthy_industry_confronts_disruption.ashx&usg=AFQjCNHZZURTZAB4YymVOrUzCIY_2nQXqg&sig2=BpG70lYmwY7jH6oC77sctw&bvm=bv.145822982,d.amc
* http://www.mckinsey.com/~/media/mckinsey/dotcom/client_service/financial%20services/latest%20thinking/payments/global_payments_2015_a_healthy_industry_confronts_disruption.ashx
