from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from models import Base

# Database URL
DATABASE_URL = 'sqlite:///Restuarants.db'  

# Creating the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Creating Alembic configuration
alembic_cfg = Config("alembic.ini")
alembic_cfg.set_main_option('script_location', 'alembic')

# Running the migration
command.upgrade(alembic_cfg, "head")

print("Migration completed.")