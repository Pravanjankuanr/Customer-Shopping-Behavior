# Customer Shopping Behavior Analysis

## Overview

This project focuses on analyzing customer shopping behavior data. The primary goal is to ingest raw customer shopping data from CSV files into a PostgreSQL database for efficient querying and analysis, followed by exploratory data analysis to uncover insights on revenue optimization without increasing discounts.

## Features

- **Data Ingestion**: Automated ingestion of CSV data into PostgreSQL database
- **Logging**: Comprehensive logging of the ingestion process with timestamps
- **Database Setup**: SQL scripts for creating the retail database and customer_shopping table
- **Performance Tracking**: Time tracking for data ingestion operations
- **Exploratory Data Analysis**: Analysis of discount impact, category performance, repeat customer behavior, and revenue metrics

## Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **SQLAlchemy**: Database ORM for Python
- **PostgreSQL**: Relational database management system
- **Psycopg2**: PostgreSQL adapter for Python
- **Jupyter Notebook**: For interactive data analysis

## Prerequisites

- Python 3.x
- PostgreSQL server running locally
- Jupyter Notebook (for running the EDA notebook)
- Required Python packages (see Installation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pravanjankuanr/Customer-Shopping-Behavior.git
   cd Customer-Shopping-Behavior
   ```

2. Install required Python packages:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary jupyter
   ```

3. Set up PostgreSQL database:
   - Ensure PostgreSQL is installed and running
   - Update the database connection string in `ingestion_db.py` and `Exploratory Data Analysis.ipynb` if necessary
   - Run the SQL script to create the database and table:
     ```sql
     -- Execute the contents of SQL Script.sql
     ```

## Usage

### Data Ingestion

1. Place your CSV data files in the `data/` directory

2. Run the data ingestion script:
   ```bash
   python ingestion_db.py
   ```

3. Check the logs in `logs/ingestion_db.log` for process details

### Exploratory Data Analysis

1. Ensure the data is ingested into the database

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook "Exploratory Data Analysis.ipynb"
   ```

3. Run the cells in order to perform the analysis

## Data Description

The dataset contains customer shopping behavior information with the following columns:

- `customer_id`: Unique identifier for each customer
- `age`: Age of the customer
- `gender`: Gender of the customer
- `location`: Customer's location
- `category`: Product category purchased
- `item_purchased`: Specific item bought
- `size`: Size of the item
- `color`: Color of the item
- `season`: Season of purchase
- `purchase_amount`: Amount spent on purchase (USD)
- `purchase_frequency`: How often the customer makes purchases
- `previous_purchases`: Number of previous purchases
- `discount_applied`: Whether a discount was applied (Yes/No)
- `promo_code_used`: Whether a promo code was used (Yes/No)
- `subscription_status`: Customer's subscription status (Yes/No)
- `shipping_type`: Type of shipping selected
- `payment_method`: Payment method used
- `review_rating`: Customer's review rating (1-5 scale)

Dataset size: 3900 rows, 18 columns. Missing values in `review_rating` were filled with the mean value.

## Exploratory Data Analysis Insights

The EDA notebook addresses the key business question: "How can the business increase revenue without increasing discounts?"

### Key Analyses Performed:

1. **Discount Impact Analysis**:
   - Compares average purchase amounts, total revenue, and order counts between discounted and non-discounted purchases

2. **Category Performance**:
   - Analyzes revenue by product category for non-discounted purchases

3. **Repeat Customer Behavior**:
   - Examines how repeat customers (those with previous purchases) interact with discounts
   - Calculates repeat purchase rate

4. **Revenue Metrics**:
   - Overall average purchase amount
   - Total revenue comparison between discount and non-discount segments

### Sample Findings (based on code structure):
- Average purchase amount across all transactions
- Repeat purchase rate percentage
- Revenue breakdowns by discount status and categories

*Note: Actual numerical results depend on running the notebook with your data.*

## Project Structure

```
Customer-Shopping-Behavior/
├── Exploratory Data Analysis.ipynb  # Jupyter notebook for data analysis
├── ingestion_db.py                  # Main data ingestion script
├── SQL Script.sql                   # Database setup scripts
├── README.md                        # Project documentation
├── data/
│   ├── customer_shopping_behavior.csv       # Primary raw data file
│   └── customer_shopping_behavior_data2.csv # Additional data file
├── images/                          # Directory for analysis visualizations
└── logs/
    └── ingestion_db.log             # Ingestion logs
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or suggestions, please open an issue on GitHub.