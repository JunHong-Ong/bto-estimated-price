# Built-to-Order (BTO) Flat Price Prediction

## Executive Summary
 Purchasing a BTO in Singapore is a major decision. For most young couples, a BTO would likely be their first home in Singapore. However, prospective applicants for BTO sales launch have access to limited information prior to the announcement by the Housing and Development Board (HDB).

 In particular, applicants would only have access to basic project-related information such as the location of the BTO site and the number of units and flat types which would be offered. Crucuially, the estimated prices for such BTOs are not provided.

 As many applicants, first-time applicants in particular, are young couples who have recently started their careers, they may not have the income to afford an expensive first home. By providing information relating the the estimated prices of the BTO, applicants would be able to make a more informed judgement on which BTO site they may wish to compete for.

 Therefore, a regression model has been developed to predict the estimated prices of such BTO sales launch. The model was trained on estimated BTO prices, provided by HDB, from 2019 to 2022 ($n$=241). Using K-folds cross-validation, the model achieved a RMSE score of 53.953 (SD: 17.221).

![training](demo\training.png)

## Comparison of Results
 For further evaluation, the model was used to predict BTO sales launch prices for the Feb 2023 and May 2023 BTO sales launch.

### May 2023 BTO Sales Launch
 For the May 2023 Sales Launch, as HDB has not yet made the official announcement, we would be comparing our predictions with predictions of SRX.
 | Town/Estate | Flat Type | Predicted Price | SRX's Estimation |
 | ----------- | --------- | --------------- | ---------------- |
 | Bedok | 2-room Flexi Type 1 | $187,000 - $225,000 | - |
 | Bedok | 2-room Flexi Type 2 | $238,000 - $290,000 | - |
 | Bedok | 3-room | $339,000 - $418,000 | $330,000 - $400,000 |
 | Bedok | 4-room | $478,000 - $599,000 | $450,000 - $550,000 |
 | Bedok | 5-room | $377,000 - $463,000 | $590,000 - $680,000 |
 | Bedok | 3 Gen | $330,000 - $406,000 | - |
 | Kallang / Whampoa | 3-room | $378,000 - $469,000 | $360,000 - $460,000 |
 | Kallang / Whampoa | 4-room | $538,000 - $679,000 | $490,000 - $640,000 |
 | Serangoon | 4-room | $413,000 - $513,000 | $350,000 - $430,000 |
 | Serangoon | 5-room | $543,000 - $683,000 | $470,000 - $560,000 |
 | Tengah | 2-room Flexi Type 1 | $120,000 - $147,000 | - |
 | Tengah | 2-room Flexi Type 2 | $141,000 - $171,000 | - |
 | Tengah | 3-room | $219,000 - $268,000 | $210,000 - $280,000 |
 | Tengah | 4-room | $297,000 - $366,000 | $310,000 - $415,000 |
 | Tengah | 5-room | $405,000 - $501,000 | $420,000 - $550,000 |

### February 2023 BTO Sales Launch
 As the Feb 2023 Sales Launch has been completed, we can evalute the predictions of the model with actual prices estimated by HDB. Below is a comparison of the predictions.

 | Project Name | Town/Estate | Flat Type | Predicted Price | HDB's Estimation |
 | ------------ | ----------- | --------- | --------------- | ---------------- |
 | Jurong West Crystal | Jurong West | 3-room | $209,000 - $255,000 | $187,000 - $249,000 |
 | Jurong West Crystal | Jurong West | 4-room | $295,000 - $363,000 | $288,000 - $372,000 |
 | Brickland Weave | Tengah | 2-room Flexi Type 1 | $117,000 - $143,000 | $97,000 - $118,000 |
 | Brickland Weave | Tengah | 2-room Flexi Type 2 | $140,000 - $169,000 | $122,000 - $158,000 |
 | Brickland Weave | Tengah | 3-room | $209,000 - $255,000 | $190,000 - $248,000 |
 | Brickland Weave | Tengah | 4-room | $296,000 - $364,000 | $291,000 - $375,000 |
 | Brickland Weave | Tengah | 5-room | $412,000 - $11,0050 | $401,000 - $503,000 |
 | Rajah Summit | Kallang / Whampoa | 3-room | $355,000 - $440,000 | $326,000 - $443,000 |
 | Rajah Summit | Kallang / Whampoa | 4-room | $489,000 - $615,000 | $459,000 - $631,000 |
 | Farrer Park Fields | Kallang / Whampoa | 2-room Flexi Type 1 | $144,000 - $174,000 | $185,000 - $229,000 |
 | Farrer Park Fields | Kallang / Whampoa | 2-room Flexi Type 1 | $143,000 - $173,000 | $233,000 - $297,000 |
 | Farrer Park Fields | Kallang / Whampoa | 3-room | $355,000 - $440,000 | $356,000 - $449,000 |
 | Farrer Park Fields | Kallang / Whampoa | 4-room | $489,000 - $615,000 | $484,000 - $631,000 |
 | Ulu Pandan Glades | Queenstown | 3-room | $370,000 - $458,000 | $372,000 - $498,000 |
 | Ulu Pandan Glades | Queenstown | 4-room | $518,000 - $653,000 | $541,000 - $711,000 |

 ![testing](demo\testing.png)

## Discussion
 From the comparison on results, we can see that the model generally performs well for BTO sites with frequent activity in the past few years (Tengah and Kallang / Whampoa). However, for BTO sites which did not appear in the training set, such as Bedok and Serangoon, the model's predictions differ quite substantailly from SRX's estimates. However, this issue can likely be alleviated by the following:
 - Augmenting the training data with current market prices of similar flats around the BTO site and;
 - Gathering more data to feed into the model

 Currently, the model does not have enough datapoints to afford a more granular binning of the latitudes and longitudes. The number of bins used for the current model is 3 and 4 respectively, which means the model is only able to divide the whole of Singapore into 12 segments and learn 1 parameter for each segment. However, 12 segments is relatively small number to subdivide the whole area of Singapore. Looking specifically at the predictions for 2-room Flexi flats in Bedok for the May 2023 launch, out model has predicted prices of $187,000 to $290,000 which is significantly more expensive than 2-room Flex flats in the East (Pasir Ris: $135,000 - $170,000; Tampines: $150,000 - $180,000). This is likely caused by the low resolution of binning; grouping together large areas of Singapore, and could lead to a very general estimate.