import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )

    def create_tables(self):
        """Create necessary tables if they don't exist"""
        with self.engine.connect() as conn:
            # Create input data table
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS customer_data (
                    id SERIAL PRIMARY KEY,
                    TotalCharges FLOAT,
                    Month_to_month VARCHAR(10),
                    One_year VARCHAR(10),
                    Two_year VARCHAR(10),
                    PhoneService VARCHAR(10),
                    tenure INTEGER
                )
            """))
            
            # Create predictions table
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS customer_predictions (
                    id SERIAL PRIMARY KEY,
                    customer_id INTEGER REFERENCES customer_data(id),
                    prediction INTEGER,
                    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            conn.commit()

    def load_data_from_csv(self, csv_path):
        """Load data from CSV into the database"""
        df = pd.read_csv(csv_path)
        df.to_sql('customer_data', self.engine, if_exists='append', index=False)
        return df

    def get_batch_data(self):
        """Get data for prediction"""
        query = "SELECT * FROM customer_data"
        return pd.read_sql(query, self.engine)

    def save_predictions(self, predictions_df):
        """Save predictions to the database"""
        predictions_df.to_sql('customer_predictions', self.engine, 
                            if_exists='append', index=False) 