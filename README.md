# Customer Shopping Behavior Analysis

## Overview

This project focuses on analyzing customer shopping behavior data. The primary goal is to ingest raw customer shopping data from CSV files into a PostgreSQL database for efficient querying and analysis.

## Features

- **Data Ingestion**: Automated ingestion of CSV data into PostgreSQL database
- **Logging**: Comprehensive logging of the ingestion process with timestamps
- **Database Setup**: SQL scripts for creating the retail database and customer_shopping table
- **Performance Tracking**: Time tracking for data ingestion operations

## Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **SQLAlchemy**: Database ORM for Python
- **PostgreSQL**: Relational database management system
- **Psycopg2**: PostgreSQL adapter for Python

## Prerequisites

- Python 3.x
- PostgreSQL server running locally
- Required Python packages (see Installation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pravanjankuanr/Customer-Shopping-Behavior.git
   cd Customer-Shopping-Behavior
   ```

2. Install required Python packages:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```

3. Set up PostgreSQL database:
   - Ensure PostgreSQL is installed and running
   - Update the database connection string in `ingestion_db.py` if necessary
   - Run the SQL script to create the database and table:
     ```sql
     -- Execute the contents of SQL Script.sql
     ```

## Usage

1. Place your CSV data files in the `data/` directory

2. Run the data ingestion script:
   ```bash
   python ingestion_db.py
   ```

3. Check the logs in `logs/ingestion_db.log` for process details

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
- `purchase_amount`: Amount spent on purchase
- `purchase_frequency`: How often the customer makes purchases
- `previous_purchases`: Number of previous purchases
- `discount_applied`: Whether a discount was applied
- `promo_code_used`: Whether a promo code was used
- `subscription_status`: Customer's subscription status
- `shipping_type`: Type of shipping selected
- `payment_method`: Payment method used
- `review_rating`: Customer's review rating

## Project Structure

```
Customer-Shopping-Behavior/
├── ingestion_db.py          # Main data ingestion script
├── SQL Script.sql           # Database setup scripts
├── README.md                # Project documentation
├── data/
│   └── customer_shopping_behavior.csv  # Raw data file
└── logs/
    └── ingestion_db.log     # Ingestion logs
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