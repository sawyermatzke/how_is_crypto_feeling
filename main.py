from scheduler.scheduler import start_scheduler
from db.database import create_table

if __name__ == '__main__':
    create_table()  # Ensure the database and table are ready
    start_scheduler()  # Start the scheduling of tasks
