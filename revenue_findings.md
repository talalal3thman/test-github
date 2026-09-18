# Airbnb revenue investigation

Results from `listings.csv`, covering 22,708 listings. Estimated revenue is available for 19,172 listings. See **Steps 16-23** of `step_by_step_eda.ipynb` for executable calculations, interactive charts, and full comparison tables.

## 1. Why reviews correlate with estimated revenue

The CSV reproduces this calculation:

```text
estimated occupied nights = min(255, 2 x recent reviews x max(3, minimum nights))
estimated revenue = price x estimated occupied nights, rounded
```

The occupancy formula matches all 22,706 rows with complete inputs. The revenue formula matches all 19,172 available revenues within half a currency unit. This is an empirical reconstruction of this export, consistent with [Inside Airbnb's methodology](https://insideairbnb.com/data-assumptions/).

Consequently, the strong correlations partly reflect how the target was created. They do not show how much actual revenue an additional review would generate. The estimator uses review counts without distinguishing good and bad reviews.

| Numerical variable | Spearman association with estimated revenue |
|---|---:|
| Estimated occupied nights | 0.909 |
| Reviews in the last 12 months | 0.892 |
| Lifetime reviews | 0.771 |
| Amenities count | 0.392 |
| Price | 0.355 |
| Guest capacity | 0.327 |
| Beds | 0.256 |
| Minimum nights | -0.235 |
| Bedrooms | 0.163 |
| Overall rating | 0.066 |

These are separate, unadjusted associations. Pair counts are in the notebook. Price and minimum nights are also ingredients in the estimate. Amenities count is a count of described amenities, not a measure of their quality or individual value.

## 2. What makes properties receive reviews?

Review volume depends on both the number of stays and the probability a guest reviews. A property with many reviews may simply host more stays. Shorter stays create more review opportunities for the same occupied nights.

In this file, recent review count is associated with amenities count (Spearman **0.375**), minimum nights (**-0.343**), and capacity (**0.169**). These patterns suggest questions to investigate; they do not isolate causal effects. The notebook also checks listings whose first recorded review was at least a year ago.

To measure whether guests are more likely to review, collect **completed eligible stays and reviews from those same stays**. Dividing reviews by bookings estimated from reviews would merely reproduce the assumed review rate.

**A weak rating correlation does not mean negative reviews are harmless.** The file contains average listing ratings, not separate positive/negative review counts or review text. Ratings are concentrated near the upper end, and missing ratings are not low ratings. The notebook includes rating bands and a sensitivity check requiring at least 10 lifetime reviews.

Practical hypotheses to monitor include cleanliness, accurate descriptions, clear check-in instructions, and responsive communication. Request honest feedback after checkout and review guests promptly. Airbnb describes [these rating dimensions and the role of reviews](https://www.airbnb.com/resources/hosting-homes/a/why-reviews-matter-41); these actions are not effects estimated from this dataset.

## 3. How to compare numerical and categorical data

| Comparison | Method |
|---|---|
| Revenue and another number | Spearman/Pearson |
| Revenue and Superhost (yes/no) | Point-biserial correlation; encode yes=1, no=0 |
| Revenue and neighbourhood, room type, or property type | Group counts, medians, quartiles, box plots, and eta-squared |

Never assign arbitrary neighbourhood codes such as 1, 2, 3 and correlate them with revenue: those numbers have no meaningful order or distance.

**Eta-squared** measures how much observed variation is represented by group-mean differences. It has no positive/negative direction. For example, 0.058 means 5.8% of raw revenue variation in this sample is represented by differences between room-type means. It does not mean that changing room type increases revenue by 5.8%.

| Category | Eta-squared: raw revenue | Eta-squared: log(1 + revenue) |
|---|---:|---:|
| Neighbourhood | 0.0484 | 0.0416 |
| Room type | 0.0580 | 0.0602 |
| Property type | 0.0605 | 0.0688 |
| Superhost status | 0.0469 | 0.0877 |

More categories can inflate in-sample eta-squared. These measures are descriptive, not a ranking of causal importance. Log results describe a different outcome scale. See [eta-squared documentation](https://pingouin-stats.org/generated/pingouin.anova.html) and [point-biserial documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pointbiserialr.html).

For example, this works with the dataframe created in Step 16:

```python
revenue_data.groupby('room_type')[TARGET].agg(['count', 'median', 'mean'])

# Point-biserial coefficient: unknown status remains missing.
pair = revenue_data[['superhost_binary', TARGET]].dropna()
pair.corr(method='pearson').iloc[0, 1]

# Unordered category association: function defined in Step 19.
eta_squared(revenue_data, 'neighbourhood_cleansed', TARGET)
```

For inferential tests, Welch ANOVA compares means with unequal variances; Kruskal-Wallis compares ranks. A p-value does not measure association size. Multiple listings share hosts in this dataset, so inference should account for host clustering rather than assume independent listings.

## 4. Superhost findings

| Status | Listings with recorded revenue | Median estimated annual revenue |
|---|---:|---:|
| Superhost | 5,151 | 18,916 |
| Not Superhost | 13,889 | 5,334 |

Point-biserial correlation is **0.217** with raw revenue, or **0.296** with log(1 + revenue). Unknown statuses are excluded from these coefficients.

The gap is not the gain caused by earning the badge. [Superhost qualification](https://www.airbnb.com/help/article/829) already depends on previous stays and hosting performance. Step 21 compares the two groups within the same neighbourhood, room type, and capacity, while explaining the remaining differences that could account for the gap.

## 5. Candidate segments when you can choose what to buy

Among groups with at least **30 recorded revenues and 10 distinct hosts with recorded revenue**, the leading combinations are **Entire rental unit**, **Entire home/apt**, accommodating **7+ guests**:

| Neighbourhood | Recorded revenues | Distinct hosts | Median estimated annual revenue | Middle 50% of estimated revenues |
|---|---:|---:|---:|---:|
| Sol | 71 | 54 | 69,150 | 27,108-97,707 |
| Cortes | 55 | 32 | 55,957 | 32,202-94,759 |
| Palacio | 59 | 40 | 43,516 | 8,825.5-82,592.5 |

Amounts are in the file's recorded local currency units. Its nonmissing quote currency codes are EUR. The ranks summarize existing listings, including recorded zeros. They are not forecasts for a new listing or evidence that changing neighbourhood causes these differences.

For currently non-Superhost listings in the same segments, medians are **57,962 in Sol** (47 listings), **42,605 in Cortes** (35), and **28,640 in Palacio** (47). Existing non-Superhosts are not necessarily new hosts. The full rankings, including smaller capacities and other property types, are in Step 23.

**Use these as a shortlist for further investigation.** With no purchase budget or cost data, the ranking naturally favours larger properties in this sample. Assess acquisition and operating costs separately to compare returns. The current quoted price is not the average rate earned over the past year, and this constructed target cannot establish an optimal nightly price or minimum-stay rule.

## Validation

All 48 code cells executed without errors or warnings. The existing 60 notebook cells were preserved; 26 cells were added for the revenue investigation. Formula reconstruction, effect-size bounds, and the equivalence of binary correlation squared to eta-squared were checked. The raw CSV was not modified.
