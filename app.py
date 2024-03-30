from database import create_db_and_tables, create_heroes, create_users

def main():
    create_db_and_tables()
    create_heroes()
    create_users()

if __name__ == "__main__":  
    main()