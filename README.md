# Bank Of Zambia Exchange Rate Scraper

This api will pull the dollar rate exchange for all banks in Zambia.

It will get the buy and sell rates for three time periods 9:30, 12:30 and 15:30.

[Check out the website here](https://vast-dusk-59282.herokuapp.com/)

## How to use

Try the interactive documentation [here!](https://vast-dusk-59282.herokuapp.com/docs)

Example request:

```bash
curl --request GET https://vast-dusk-59282.herokuapp.com/banks
```

Response:
```JSON
[{"bank":"ACCESS BANK ZAMBIA","09:30":{"buy":"21.7510","sell":"22.1800"},"12:30":{"buy":"21.7410","sell":"22.1700"},"15:30":{"buy":"21.7510","sell":"22.1800"}},{"bank":"ATLAS MARA BANK","09:30":{"buy":"21.7454","sell":"22.1847"},"12:30":{"buy":"21.7454","sell":"22.1847"},"15:30":{"buy":"21.7454","sell":"22.1847"}},{"bank":"BANK OF CHINA (ZAMBIA)","09:30":{"buy":"21.7400","sell":"22.1650"},"12:30":{"buy":"21.7450","sell":"22.1700"},"15:30":{"buy":"21.7450","sell":"22.1700"}},{"bank":"ABSA BANK ZAMBIA","09:30":{"buy":"21.7624","sell":"22.1796"},"12:30":{"buy":"21.7624","sell":"22.1796"},"15:30":{"buy":"21.7624","sell":"22.1796"}},{"bank":"CAVMONT BANK","09:30":{"buy":"21.7900","sell":"22.1800"},"12:30":{"buy":"21.7900","sell":"22.1800"},"15:30":{"buy":"21.7900","sell":"22.1800"}},{"bank":"CITIBANK ZAMBIA","09:30":{"buy":"21.7305","sell":"22.1695"},"12:30":{"buy":"21.7404","sell":"22.1796"},"15:30":{"buy":"21.7404","sell":"22.1796"}},{"bank":"ECOBANK ZAMBIA","09:30":{"buy":"21.7404","sell":"22.1796"},"12:30":{"buy":"21.7404","sell":"22.1796"},"15:30":{"buy":"21.7404","sell":"22.1796"}},{"bank":"FIRST ALLIANCE BANK ZAMBIA","09:30":{"buy":"21.7255","sell":"22.1600"},"12:30":{"buy":"21.7255","sell":"22.1600"},"15:30":{"buy":"21.7255","sell":"22.1600"}},{"bank":"FIRST CAPITAL BANK ZAMBIA","09:30":{"buy":"21.7409","sell":"22.1758"},"12:30":{"buy":"21.7409","sell":"22.1758"},"15:30":{"buy":"21.7409","sell":"22.1758"}},{"bank":"FIRST NATIONAL BANK ZAMBIA","09:30":{"buy":"21.7480","sell":"22.1820"},"12:30":{"buy":"21.7480","sell":"22.1820"},"15:30":{"buy":"21.7480","sell":"22.1820"}},{"bank":"INDO-ZAMBIA BANK","09:30":{"buy":"21.7300","sell":"22.1600"},"12:30":{"buy":"21.7400","sell":"22.1700"},"15:30":{"buy":"21.7400","sell":"22.1700"}},{"bank":"INVESTRUST BANK","09:30":{"buy":"21.7305","sell":"22.1695"},"12:30":{"buy":"21.7355","sell":"22.1746"},"15:30":{"buy":"21.7355","sell":"22.1746"}},{"bank":"STANBIC BANK ZAMBIA","09:30":{"buy":"21.7437","sell":"22.1763"},"12:30":{"buy":"21.7437","sell":"22.1763"},"15:30":{"buy":"21.7536","sell":"22.1864"}},{"bank":"STANDARD CHARTERED BANK","09:30":{"buy":"21.7270","sell":"22.1580"},"12:30":{"buy":"21.7270","sell":"22.1580"},"15:30":{"buy":"21.7270","sell":"22.1580"}},{"bank":"UNITED BANK FOR AFRICA ZAMBIA ","09:30":{"buy":"21.7500","sell":"22.1750"},"12:30":{"buy":"21.7500","sell":"22.1750"},"15:30":{"buy":"21.7300","sell":"22.1550"}},{"bank":"ZAMBIA INDUSTRIAL COMMERCIAL BANK ","09:30":{"buy":"21.7464","sell":"22.1636"},"12:30":{"buy":"21.7464","sell":"22.1636"},"15:30":{"buy":"21.7464","sell":"22.1636"}},{"bank":"ZAMBIA NATIONAL COMMERCIAL BANK","09:30":{"buy":"21.7498","sell":"22.1630"},"12:30":{"buy":"21.7498","sell":"22.1630"},"15:30":{"buy":"21.7498","sell":"22.1630"}},{"bank":"Market Average","09:30":{"buy":"21.7442","sell":"22.1719"},"12:30":{"buy":"21.7454","sell":"22.1730"},"15:30":{"buy":"21.7454","sell":"22.1731"}}]
```

Single bank example:

```bash
curl --request GET https://vast-dusk-59282.herokuapp.com/bank/china 
```

Response:

```JSON
[{"bank":"BANK OF CHINA (ZAMBIA)",
"09:30":{"buy":"21.7400","sell":"22.1650"},"12:30":{"buy":"21.7450","sell":"22.1700"},"15:30":{"buy":"21.7450","sell":"22.1700"}}]
```