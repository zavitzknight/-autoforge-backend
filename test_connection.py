import psycopg2

# Database connection settings
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "testdb"
DB_USER = "postgres"
DB_PASSWORD = "Steph420!"  # <-- replace with your actual password

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def ensure_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def list_people():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM people ORDER BY id;")
    rows = cur.fetchall()
    if rows:
        print("\nPeople in the database:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}")
    else:
        print("\n⚠️ No people found in the database.")
    cur.close()
    conn.close()

def add_person(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO people (name) VALUES (%s);", (name,))
    conn.commit()
    print(f"✅ Added '{name}' to the database.")
    cur.close()
    conn.close()

def delete_person(person_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM people WHERE id = %s;", (person_id,))
    if cur.rowcount > 0:
        print(f"🗑️ Deleted person with ID {person_id}.")
    else:
        print(f"⚠️ No person found with ID {person_id}.")
    conn.commit()
    cur.close()
    conn.close()

def main():
    ensure_table()
    while True:
        print("\n--- People Database Menu ---")
        print("1. List all people")
        print("2. Add a new person")
        print("3. Delete a person by ID")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_people()
        elif choice == "2":
            name = input("Enter the name to add: ").strip()
            if name:
                add_person(name)
            else:
                print("⚠️ Name cannot be empty.")
        elif choice == "3":
            try:
                person_id = int(input("Enter the ID to delete: ").strip())
                delete_person(person_id)
            except ValueError:
                print("⚠️ Please enter a valid numeric ID.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    try:
        main()
    except psycopg2.OperationalError as e:
        print("❌ Could not connect to the database.")
        print("Error details:", e)
    except Exception as e:
        print("❌ An error occurred.")
        print("Error details:", e)