import aerospike
from aerospike import exception as ex

CONFIG = {
    "hosts": [("127.0.0.1", 3000)]
}

NAMESPACE = "test"
SET_NAME = "users"


def get_client():
    try:
        client = aerospike.client(CONFIG)
        return client
    except ex.AerospikeError as e:
        print(f"Failed to create client: {e}")
        raise


def record_key(user_id: str):
    # (namespace, set, primary_key)
    return (NAMESPACE, SET_NAME, user_id)


def create_user(client, user_id: str, name: str, age: int, city: str):
    key = record_key(user_id)
    bins = {
        "name": name,
        "age": age,
        "city": city,
    }
    client.put(key, bins)
    print(f"Created user {user_id}")


def read_user(client, user_id: str):
    key = record_key(user_id)
    try:
        _, meta, bins = client.get(key)
        print("Record found:")
        print("meta:", meta)
        print("bins:", bins)
    except ex.RecordNotFound:
        print(f"User {user_id} not found")


def update_user(client, user_id: str, name: str = None, age: int = None, city: str = None):
    key = record_key(user_id)

    try:
        _, _, current_bins = client.get(key)
    except ex.RecordNotFound:
        print(f"User {user_id} not found")
        return

    if name is not None:
        current_bins["name"] = name
    if age is not None:
        current_bins["age"] = age
    if city is not None:
        current_bins["city"] = city

    client.put(key, current_bins)
    print(f"Updated user {user_id}")


def delete_user(client, user_id: str):
    key = record_key(user_id)
    try:
        client.remove(key)
        print(f"Deleted user {user_id}")
    except ex.RecordNotFound:
        print(f"User {user_id} not found")


def menu():
    print("\nAerospike CRUD Demo")
    print("1. Create user")
    print("2. Read user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")


def main():
    client = get_client()

    try:
        while True:
            menu()
            choice = input("Choose: ").strip()

            if choice == "1":
                user_id = input("User ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: ").strip())
                city = input("City: ").strip()
                create_user(client, user_id, name, age, city)

            elif choice == "2":
                user_id = input("User ID: ").strip()
                read_user(client, user_id)

            elif choice == "3":
                user_id = input("User ID: ").strip()
                name = input("New name (leave blank to keep): ").strip()
                age_raw = input("New age (leave blank to keep): ").strip()
                city = input("New city (leave blank to keep): ").strip()

                update_user(
                    client,
                    user_id,
                    name=name if name else None,
                    age=int(age_raw) if age_raw else None,
                    city=city if city else None,
                )

            elif choice == "4":
                user_id = input("User ID: ").strip()
                delete_user(client, user_id)

            elif choice == "5":
                print("Goodbye")
                break

            else:
                print("Invalid choice")

    finally:
        client.close()


if __name__ == "__main__":
    main()
