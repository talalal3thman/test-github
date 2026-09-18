# Understanding and presenting the Airbnb case

## The case in one sentence

You are a prospective host choosing what to buy in Madrid, and the EDA helps you shortlist property segments with higher estimated annual revenue before investigating actual costs and bookings.

## The logic, in plain English

1. **The business problem is uncertainty.** You have many possible neighbourhoods and property types, and you do not know which is most suitable for your objective.
2. **The analysis compares existing listings.** It checks numerical features, compares categorical groups, and looks at reviews and Superhost status.
3. **The strongest review relationship is partly built into the estimate.** The data creator uses reviews to estimate occupied nights, then multiplies nights by a quoted price. A strong correlation therefore does not prove that asking for one more review produces extra real income.
4. **The shortlist identifies candidates.** Entire rental units for 7+ guests in Sol and Cortes lead the selected comparison groups. Their medians describe existing listings. A new property's results can differ.
5. **The next decision needs more evidence.** Compare actual properties, purchase and operating costs, rental eligibility, and booking evidence. After launch, track real revenue and the share of completed stays that receive reviews.

## A simple example of the estimate

Suppose a listing has 20 reviews in the last year. If the model assumes that half of stays receive a review, it estimates 40 stays. At three nights per stay, that becomes 120 occupied nights. At a quoted price of EUR 100 per night, the estimate is EUR 12,000.

Those assumptions explain the estimate. They do not verify that the property actually earned EUR 12,000. The CSV also caps estimated nights at 255, and uses the larger of three nights and the listing's minimum stay in the calculation.

## Terms you should be able to explain

| Term | Plain meaning |
|---|---|
| Problem statement | Why the project is needed: the uncertainty or opportunity facing the prospective host. |
| Project objective | A specific task the analysis will perform to address that problem. |
| Median | The middle observation after sorting the values. |
| Spearman correlation | Whether two numerical measures tend to rank listings similarly. It ranges from -1 to +1. |
| Point-biserial correlation | Correlation between a true yes/no variable and a number. Here, Superhost is 1 and non-Superhost is 0. |
| Eta-squared | The share of observed variation represented by differences between categorical group means. It is not the gain from changing categories. |
| Middle 50% | The observations between the 25th and 75th percentiles. This is not a forecast or confidence interval. |
| Review rate | Reviews divided by eligible completed stays from the same checkout cohort, after the review window. |
| Association | Variables occur together in a pattern. It does not by itself establish cause. |

## How to use the speaker notes

Open the deck in PowerPoint and select **Notes** below a slide. Each slide contains:

- **SAY:** a short script you can adapt into your own words.
- **UNDERSTAND:** the reasoning behind the slide.
- **IF ASKED:** explanations for likely questions, where useful.
- **SOURCES:** references for facts and calculations.

The scripts total roughly nine minutes at a conversational pace. The longer explanations are for preparation; you do not need to read all of them aloud. During the presentation, use Presenter View to see your notes while the audience sees the slides.

## Slide-by-slide speaking guide

### Slide 1: Choosing an Airbnb property in Madrid

SAY (about 30 seconds)
Imagine I can buy a property anywhere in Madrid. My question is which type of property deserves further investigation, and which hosting practices I should focus on. I used the Airbnb listings dataset to compare estimated annual revenue. The result is a shortlist for investigation, with clear limits on what the estimates can tell us.

UNDERSTAND
You are presenting as a prospective owner or investor. Your business ambition is higher actual revenue. Your available measurement is estimated_revenue_l365d, an estimate for the preceding 365 days. We can screen existing property groups with this measure, but we cannot promise the income of a new property.

TRANSITION
First, I will separate the business problem from the objectives of the analysis.

SOURCES
Main notebook: step_by_step_eda.ipynb, Steps 16-23. Data: listings.csv, Madrid snapshot collected 20 June-2 July 2026.

Cover illustration: AI-generated with the built-in ImageGen tool. It represents a hypothetical apartment, not an observed or recommended listing. Image embedded in the deck.
Prompt: A refined editorial illustration of a bright Spanish apartment with tall balcony doors, a pale oak floor, cream sofa and muted teal accent. Soft daylight, white and ivory palette with restrained terracotta detail. Portrait 2:3 composition. A conceptual apartment, not a real listing. No text, logos, people, data or borders. Simple, softly textured architectural illustration.

### Slide 2: Problem statement and project objectives

SAY (about 55 seconds)
The problem is investment uncertainty. A prospective host has to choose a property before knowing its earning potential. Our snapshot covers 22,708 listings, and the estimated revenues vary substantially. We also need to understand the connection between reviews and revenue before using it to guide a purchase. My objectives are to compare property and host characteristics, explain the role of reviews, and identify three property segments with enough observations to support further investigation.

UNDERSTAND
The problem statement explains WHY the project exists. The objectives explain WHAT the analysis will measure. We do not claim that an existing business has lost money, because no evidence of a revenue decline or financial loss appears in the data. The number of listings describes the scale of the decision, not a measured loss. The analysis period is the June-July 2026 snapshot, with annual estimates referring to each listing's preceding 365 days.

OBJECTIVE DETAILS
1. Compare numerical attributes and four categorical factors: neighbourhood, room type, property type, and Superhost status.
2. Investigate recent review activity, average ratings, and the target's calculation.
3. Deliver a shortlist of three segments, requiring at least 30 recorded revenues and 10 distinct hosts with recorded revenue per segment. These are screening rules, not significance tests.

SOURCES
User-provided Case Statement Guide.pptx, slides 2-6. Problem Statement vs. Objectives Guideline.pdf, sections 1-3. Presentation Components.pptx, slide 3. Main notebook, Steps 16-23.

### Slide 3: The revenue estimate starts with reviews

SAY (about 65 seconds)
This is the most important finding. The revenue field is an estimate. In this file, recent reviews help calculate occupied nights, and occupied nights multiplied by the quoted price produce estimated revenue. For an illustration, 20 reviews imply 40 stays under a 50 percent review-rate assumption. At three nights per stay, that becomes 120 occupied nights. At a quoted price of 100 euros per night, estimated annual revenue is 12,000 euros. That is a calculation, not a verified booking history.

UNDERSTAND
The exact reconstruction is: occupied nights = min(255, 2 x number_of_reviews_ltm x max(3, minimum_nights)). Revenue = price x estimated occupied nights, rounded to a whole currency unit. It matches all 22,706 rows with complete occupancy inputs and all 19,172 available revenue values within rounding. The occupancy column measures nights, not a percentage. The factor 2 assumes that half of stays receive a review. The cap is 255 nights in this export.

IF ASKED
An extra review increases the estimate mechanically if the other inputs stay fixed and the cap has not been reached. This does not establish an increase in real income. Similarly, raising price or minimum nights in the formula cannot reveal how real demand will respond.

SOURCES
Main notebook, Step 16, formula_results and revenue_error. Inside Airbnb methodology: https://insideairbnb.com/data-assumptions/ . Data dictionary: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit .

### Slide 4: Reviews lead the numerical correlations

SAY (about 55 seconds)
The chart shows how strongly each variable tends to rise with estimated revenue. Occupancy and recent reviews have the strongest relationships, around 0.91 and 0.89, which fits the formula we just saw. Lifetime reviews also have a strong association. Among other characteristics, amenities count and guest capacity have positive associations worth investigating. The overall rating has a weak relationship in this snapshot.

UNDERSTAND
Spearman correlation compares ranks. It ranges from minus one to plus one. A positive value means listings with more of one measure tend to have more of the other. It does not prove a cause, a percentage increase, or a forecast. The notebook also calculates Pearson correlations and reports the number of complete pairs. Amenities count is the number of listed amenities, not their quality or economic value. Price is itself an input to estimated revenue.

IF ASKED
A rating correlation of 0.066 does not mean negative reviews are harmless. The dataset only contains listing-level averages, many ratings are near the top of the scale, and other differences between properties can obscure the relationship.

SOURCES
Main notebook, Step 17, formula_associations and property_associations. Eligible pair counts: occupancy, recent reviews, lifetime reviews, amenities, price, and capacity n=19,172; beds n=17,888; rating n=16,464.

### Slide 5: Categories separate groups, with wide overlap

SAY (about 65 seconds)
For categories such as neighbourhood or room type, ordinary numerical correlation is inappropriate because the labels do not have a numerical order. I compare group medians and distributions, and use eta-squared to summarize differences between group means. Room type has a value of about 5.8 percent. That means between-group mean differences account for 5.8 percent of the observed variation in raw estimated revenue. Considerable variation remains within each group.

UNDERSTAND
Eta-squared ranges from zero to one and has no positive or negative sign. It equals the between-group sum of squared deviations divided by the total sum of squared deviations. It does NOT mean that changing room type increases revenue by 5.8 percent. Do not encode neighbourhood names as arbitrary values such as one, two, and three and correlate those codes with revenue. For Superhost, a genuine yes/no variable, coding yes=1 and no=0 allows point-biserial correlation. The next slide shows that comparison.

IF ASKED
The category effects overlap and cannot be added. More categories can inflate in-sample eta-squared, so the chart does not establish a ranking of causal importance. Property type and room type are particularly related. The notebook also checks log-transformed revenue and displays counts and spreads.

SOURCES
Main notebook, Step 19, category_associations. Raw eta-squared: property type 0.0604734; room type 0.0579868; neighbourhood 0.0483884; Superhost 0.0468866. n=19,172 for the first three, n=19,040 for known Superhost status. Method: https://pingouin-stats.org/generated/pingouin.anova.html .

### Slide 6: Superhosts show higher estimated revenue

SAY (about 55 seconds)
Superhost listings have a median estimated annual revenue of 18,916 euros, compared with 5,334 euros for non-Superhosts. The point-biserial correlation is positive at 0.217. This is a useful benchmark, but it does not tell us how much income the badge itself produces. Superhosts already have a track record of completed stays and hosting performance, and their properties may differ in other ways.

UNDERSTAND
The median is the middle listing after sorting the revenues. Half the observations are below it and half above it, apart from ties. The correlation here uses a binary variable: Superhost=1, non-Superhost=0. Unknown statuses remain missing. A coefficient of 0.217 is not a 21.7 percent revenue increase. The chart presents group medians while the correlation summarizes the binary-numeric association.

IF ASKED
Step 21 compares listings within the same neighbourhood, room type, and guest capacity. That improves comparability, but it still cannot isolate the badge's causal impact. A stronger investigation would follow future actual revenue around changes in status and account for prior trends and property differences.

SOURCES
Main notebook, Steps 20-21, revenue_group_summaries['superhost_status'] and superhost_associations. Counts: Superhost 5,151; non-Superhost 13,889. Airbnb qualification: https://www.airbnb.com/help/article/829 . Point-biserial: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pointbiserialr.html .

### Slide 7: Review volume and review probability differ

SAY (about 65 seconds)
Ten reviews can come from different situations. A host with 20 stays and a 50 percent review rate gets ten reviews. A host with ten stays and a 100 percent review rate also gets ten. Counts alone cannot tell us who is better at getting guests to review. In our data, more amenities and shorter minimum stays are associated with more recent reviews. These are useful hypotheses, but completed-stay counts are missing.

UNDERSTAND
The table is an illustrative example, not observations from the CSV. Expected review volume is approximately completed eligible stays multiplied by review probability. Shorter stays can create more review opportunities for the same number of occupied nights. To measure review probability, collect reviews and completed stays from the same checkout cohort, allowing the review window to finish. Do not divide reviews by bookings estimated from those same reviews, because that would just reproduce the assumed review rate.

POSITIVE REVIEWS
Average listing ratings cannot separate the effects of positive and negative individual reviews. Cleanliness, accurate descriptions, clear arrival instructions, and communication are service priorities to monitor. Request honest feedback without incentives or pressure. The effect of these actions was not measured by this CSV.

SOURCES
Main notebook, Step 18, review_associations. Recent-review Spearman coefficients: amenity_count 0.3753 (n=22,708), minimum_nights -0.3430 (n=22,706). Airbnb ratings: https://www.airbnb.com/resources/hosting-homes/a/why-reviews-matter-41 . Review window: https://www.airbnb.com/help/article/995 . Reviews policy: https://www.airbnb.com/help/article/2673 .

### Slide 8: Sol leads the screened property segments

SAY (about 65 seconds)
When I combine neighbourhood, room type, property type, and guest capacity, Sol has the highest median among groups that meet the screening rules. Its median estimated annual revenue is 69,150 euros, followed by Cortes at 55,957 and Palacio at 43,516. The ranges on the right show substantial differences between properties inside each group. These results justify researching those segments more closely. They are not guaranteed earnings for a new listing.

UNDERSTAND
Every eligible segment needs at least 30 recorded revenues and ten distinct hosts with recorded revenue. Sol has 71 such listings and 54 hosts; Cortes 55 and 32; Palacio 59 and 40. The middle 50 percent means the 25th to 75th percentiles, not a confidence interval or forecast range. Sol's range is 27,108 to 97,707; Cortes 32,202 to 94,759; Palacio 8,825.5 to 82,592.5. Zero estimates remain in the calculations.

IF ASKED
The ranking is among groups that pass these thresholds in this snapshot. The 7+ capacity band includes different property sizes. No budget constraint was supplied, so larger properties can lead the gross-revenue ranking. In the same segments, non-Superhost medians are 57,962 for Sol, 42,605 for Cortes, and 28,640 for Palacio. Existing non-Superhosts are not necessarily new hosts. Purchase prices and costs could change the investment preference.

SOURCES
Main notebook, Step 23, purchase_segments_by_capacity and purchase_segments_non_superhost. Recorded price-quote currency codes indicate EUR.

### Slide 9: Recommendations

SAY (about 60 seconds)
My recommendation is to investigate entire rental units for seven or more guests in Sol and Cortes first, while comparing smaller-capacity alternatives against the available budget. For each real property, I would verify rental eligibility, obtain purchase and operating costs, and compare actual booking evidence from similar listings. After launch, I would test pricing and minimum-stay rules, focus on a reliable guest experience, and track actual revenue and review rates.

UNDERSTAND
The data supports a shortlist, not immediate purchase approval. The estimate's formula cannot find an optimal price, because it holds bookings fixed when price changes. In reality, raising price may reduce bookings. Equally, shortening stays may create more reviews but also more cleaning and turnover costs. Service improvements are reasonable hypotheses to monitor, rather than effects established by this analysis.

MEASUREMENT PLAN
Track actual revenue, occupied nights, average realized nightly rate, nights offered, and contribution after variable costs. For reviews, track the share of eligible stays reviewed and average rating from matching checkout cohorts after the review window. Use a proposed initial 90-day operating review, with a longer period needed to assess seasonality. This is a plan, not a completed pilot or guaranteed result.

SOURCES
Main notebook, Steps 22-23. Recommendations synthesize the EDA and proposed data collection. Guest-experience guidance: https://www.airbnb.com/resources/hosting-homes/a/why-reviews-matter-41 . No investment costs or legal eligibility findings are supplied by the dataset.

### Slide 10: Limitations and decision conditions

SAY (about 60 seconds)
There are four main limits. First, the target is a review-based estimate. Second, 15.6 percent of listings lack revenue values, and this is a snapshot rather than a record of actual performance over time. Third, property and host characteristics overlap, so the comparisons do not prove cause and effect. Finally, the dataset has no acquisition costs, operating costs, or verified rental eligibility for a property. My conclusion is to proceed to targeted property research, then decide using real costs and booking evidence.

UNDERSTAND
Missing revenue is concentrated differently by scrape source, so the observed sample may not represent the full market. A scraped quote is not the rate actually earned across the year. Average ratings cannot reconstruct positive and negative individual reviews. Actual completed stays are absent, which prevents a genuine review-rate calculation. Multiple listings share hosts, so independent-listing statistical tests can understate uncertainty. Response time, response rate, acceptance rate, and Instant Book are entirely missing in this export.

IF ASKED
Why not simply buy the highest-ranked segment? Because the analysis ranks estimated gross revenue rather than investment return. A property with higher revenue may cost much more to buy and operate. The decision requires a budget, financing and operating assumptions, applicable rental permissions, and subsequent actual performance.

CLOSING LINE
The EDA gives us a focused starting point and a clear list of evidence needed for the next decision.

SOURCES
Main notebook, Steps 16, 18, 19, and 22-23. Presentation Components.pptx, slide 6.

## Three answers to practise

**Does the analysis prove that more reviews cause higher revenue?**

No. Reviews help construct this revenue estimate, and more stays create more reviews. We would need later actual booking/revenue data and a stronger design to measure a causal effect.

**Why would I aim for positive reviews if the rating correlation is weak?**

The dataset cannot compare the effects of individual positive and negative reviews. A weak correlation among average listing ratings does not establish that review quality is irrelevant. Guest-experience improvements should be monitored using actual feedback and future performance.

**Why do we stop at a shortlist?**

Because estimated gross revenue leaves out purchase price, operating costs, financing, and property eligibility. Those inputs can change which property offers the better return.

## Cover illustration

The cover uses the built-in ImageGen tool for a hypothetical apartment illustration. It does not depict a property in the dataset. The image is embedded in the PPTX, so the deck does not depend on an external image file.

Workspace asset: `C:/Users/TALAL ALOTHMAN/Documents/GitHub/.airbnb_presentation_work/cover_illustration.png`

Generation prompt:

> Use case: illustration-story. Asset type: a single cover illustration for a light, minimal business PowerPoint about choosing an Airbnb property in Madrid. Create a refined editorial illustration of a bright, welcoming Spanish apartment interior with tall balcony doors, a pale oak floor, a cream sofa and a small muted teal accent. Soft natural daylight, white and warm ivory palette, restrained warm terracotta detail. Portrait composition, approximately 2:3 aspect ratio. This is a conceptual apartment, not a real listing. No text, no logos, no people, no data, no borders. Keep the scene simple with generous light surfaces; hand-painted or softly textured architectural illustration rather than a photograph.
