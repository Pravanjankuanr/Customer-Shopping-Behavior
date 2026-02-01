# Customer Shopping Behavior Analysis

## 📋 Overview

This project provides a comprehensive analysis of customer shopping behavior data to uncover insights on revenue optimization without increasing discounts. The solution includes automated data ingestion from CSV files into a PostgreSQL database, coupled with exploratory data analysis to identify key trends, patterns, and business opportunities.

**Project Goal**: Extract actionable insights from customer shopping behavior to optimize revenue while maintaining or reducing discount rates.

## ✨ Features

- **Data Ingestion**: Fully automated ingestion of CSV data into PostgreSQL database with error handling
- **Comprehensive Logging**: Detailed logging of all ingestion operations with timestamps and row counts
- **Database Setup**: SQL scripts for creating the retail database and customer_shopping table schema
- **Performance Tracking**: Automatic time tracking and reporting for data ingestion operations
- **Exploratory Data Analysis**: Deep-dive analysis including:
  - Discount impact assessment on customer behavior and revenue
  - Category performance analysis
  - Repeat customer patterns and retention metrics
  - Revenue optimization opportunities
  - Customer segmentation insights

## 🛠 Technologies & Tools

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation, cleaning, and analysis |
| **SQLAlchemy** | Database ORM for Python |
| **PostgreSQL** | Relational database management system |
| **Psycopg2** | PostgreSQL adapter for Python |
| **Jupyter Notebook** | Interactive data analysis and visualization |
| **Matplotlib/Seaborn** | Data visualization (optional) |

## 📦 Project Structure

```
Customer-Shopping-Behavior/
├── data/                                    # CSV data files
│   ├── customer_shopping_behavior.csv
│   └── customer_shopping_behavior_data2.csv
├── logs/                                    # Ingestion and application logs
│   └── ingestion_db.log
├── images/                                  # Analysis visualizations and charts
├── Exploratory Data Analysis.ipynb         # Main analysis notebook
├── SQL Script.sql                          # Database schema and setup
├── ingestion_db.py                         # Data ingestion script
├── README.md                               # Project documentation
├── Business Problem.rtf                    # Business requirements
└── Analysis Report.docx                    # Final analysis report
```

## ⚙️ Prerequisites

- **Python 3.7** or higher
- **PostgreSQL** server (running locally or accessible)
- **Jupyter Notebook** (for interactive analysis)
- **pip** package manager
- 50 MB+ disk space for database and logs

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Pravanjankuanr/Customer-Shopping-Behavior.git
cd Customer-Shopping-Behavior
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas sqlalchemy psycopg2-binary jupyter
```

### 3. Configure Database Connection

Update the database connection string in `ingestion_db.py`:
```python
engine = create_engine("postgresql+psycopg2://username:password@localhost:port/database_name")
```

**Default Configuration**:
- Host: localhost
- Port: 5432 (or 5434 in this project)
- Username: postgres
- Database: retail

### 4. Initialize Database

Execute the SQL script to create database schema:
```bash
psql -U postgres -f "SQL Script.sql"
```

Or in PostgreSQL client:
```sql
-- Execute contents of SQL Script.sql
```

## 🚀 Usage

### Running Data Ingestion

1. **Place CSV files** in the `data/` directory
2. **Execute the ingestion script**:
   ```bash
   python ingestion_db.py
   ```
3. **Monitor logs** for ingestion status:
   ```bash
   tail -f logs/ingestion_db.log
   ```

**Output**: 
- Data ingested into `customer_shopping` table
- Execution time logged
- Row and column counts tracked

### Running Exploratory Data Analysis

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open** `Exploratory Data Analysis.ipynb`

3. **Execute cells** sequentially to:
   - Load data from database
   - Perform statistical analysis
   - Generate visualizations
   - Extract business insights

## 📊 Dataset Information

### Data Schema

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | Integer | Unique customer identifier |
| `age` | Integer | Customer age |
| `gender` | String | Customer gender |
| `location` | String | Customer's geographic location |
| `category` | String | Product category purchased |
| `item_purchased` | String | Specific item description |
| `size` | String | Item size |
| `color` | String | Item color |
| `season` | String | Season of purchase |
| `purchase_amount` | Float | Transaction amount (USD) |
| `purchase_frequency` | String | How often customer purchases |
| `previous_purchases` | Integer | Count of prior purchases |
| `discount_applied` | String | Discount status (Yes/No) |
| `promo_code_used` | String | Promo code status (Yes/No) |
| `subscription_status` | String | Subscription status (Yes/No) |
| `shipping_type` | String | Shipping method selected |
| `payment_method` | String | Payment method used |
| `review_rating` | Float | Review score (1-5 scale) |

### Dataset Statistics

- **Total Records**: 3,900 rows
- **Columns**: 18
- **Data Quality**: Missing values in `review_rating` filled with mean value
- **Time Period**: [Add if known]

## 🔍 Key Analysis Areas

1. **Discount Impact Analysis**: How discounts affect customer behavior and revenue
2. **Category Performance**: Which product categories drive revenue
3. **Customer Segmentation**: Identifying high-value and repeat customers
4. **Revenue Optimization**: Strategies to increase revenue without increased discounts
5. **Payment & Shipping Trends**: Preferences affecting conversion rates

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **PostgreSQL connection error** | Verify PostgreSQL is running; check connection string in `ingestion_db.py` |
| **Module not found (pandas, sqlalchemy)** | Run `pip install -r requirements.txt` |
| **Permission denied on logs/** | Ensure write permissions; create directory if missing: `mkdir logs` |
| **CSV file not found** | Verify CSV files are in `data/` directory |
| **Database already exists** | Drop existing database: `DROP DATABASE retail;` |

## 📈 Expected Outcomes

After running the analysis, you should obtain:
- Key metrics on discount effectiveness
- Revenue per customer segment
- Product category performance rankings
- Customer retention patterns
- Actionable recommendations for revenue optimization

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

For questions or issues, please open an issue on GitHub or contact the project maintainer.

---

**Last Updated**: February 2, 2026  
**Version**: 1.0

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