# E-commerce-Funnel-Analysis (User Journey)
## Behaviour vs Strict Funnel Analysis

This project analyses **e-commerce user journeys** using two contrasting funnel definitions —  
**Behaviour Funnel** and **Strict Funnel** — to uncover **category-level purchase behaviour differences**.

'How do users actually purchase products and when does the funnel break?'

The result is a **dashboard-style analysis** that moves beyond simple conversion rates and focuses on  
**how structured (or unstructured) purchase journeys really are.**

## Key Questions

- Do all product categories follow a sequential purchase funnel?
- How much does enforcing funnel order change purchase rate interpretation?
- Which categories **bypass the funnel entirely**?

## Tech Stack

- Python (pandas, numpy)
- matplotlib
- GridSpec (dashboard layout)

## Core Concepts

### Behaviour Funnel
- No enforced event order
- Allows purchases without cart or view
- Reflects **real-world, non-linear behaviour**

### Strict Funnel
- Enforces `View → Add to Cart → Purchase`
- Suitable for **drop-off analysis**
- Represents an **idealised purchase journey**

### Funnel Adherence Ratio
```text
Adherence Ratio = Strict Purchase Rate / behaviour Purchase Rate
≈ 1.0	Structured, sequential purchase
≪ 1.0	Funnel bypass (impulsive / habitual)

-- This is not a performance metric — it is a behavioural structure metric.
```

## Data Processing Flow

1. Load raw event-level data
2. Standardise timestamps and funnel stages
3. Map events into funnel stages
4. Funnel computation:
    - Behaviour funnel summary
    - Strict funnel summary
5. Metric Derivation:
    - Purchase rate (purchase / view)
    - Funnel adherence ratio


## Key Insights & Business Value

1. Funnel enforcement significantly alters purchase rate interpretation
- **Value**: Moving beyond strict linear paths allows for a more accurate calculation of true conversion potential.

2. Some categories naturally bypass the cart stage
- **Value**: Identifying 'Direct-to-Buy' patterns helps in optimising the UI for faster checkout in specific product lines.

3. Applying a single strict funnel to all categories can distort user behaviour
- **Value**: Recognising non-linear journeys prevents the misidentification of friction points where none exist.

4. Funnel definitions should be category-aware
- **Value**:Tailoring conversion metrics to specific category behaviours enables more precise, data-driven marketing strategies.


## Dashboard Preview


## Dashboard Key Features

1. Overall E-commerce behaviour Funnel (log scale)
    - Captures actual user actions
    - Log scale used due to extreme imbalance between View and downstream events

2. Overall E-commerce Strict Funnel (log scale)

    - Enforces sequential logic
    - Enables meaningful drop-off interpretation
    - Serves as contrast to behaviour funnel

3. Purchase Rate by Category
    - Behaviour vs Strict Funnel
        - Grouped bar chart (purchase / view)
        - Same metric, different funnel definitions
        - Shows how funnel enforcement changes interpretation

4. Funnel Adherence Ratio by Category (Key Insight)
    - Horizontal, sorted bar chart across all categories
        - Includes categories with ≥ 100 viewers
        - Sorted by adherence ratio (lowest first)
        - Color-coded:
            - 🔴 Low adherence → funnel bypass
            - 🔵 Normal adherence
        - Reference line at 1.0 (perfect adherence)
        - This chart represents the final analytical conclusion of the project.


## Project Structure
```text
├── data/
│   └── sample_ecommerce.csv
│ 
├── scripts/
│   └── sampling.py
│ 
├── src/
│   ├── funnel_analysis.py 
│   └── preprocess.py
│
├── utils/
│   ├── utility.py          # category label helpers
│   └── color_utility.py    # adherence-based color mapping
├── README.md
└── analysis.py             # main dashboard script
```
