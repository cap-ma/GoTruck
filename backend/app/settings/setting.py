from dotenv import load_dotenv
import os 

path="backend\app\.env"
load_dotenv(path)
DATABASE_URL=os.environ.get("DATABASE_URL")

