# Aerospike CRUD Demo (Python)

This project is a command-line CRUD system for user records using **Aerospike** as the database.  
It shows how to connect from Python to Aerospike and perform:
- Create user
- Read user
- Update user
- Delete user

Default app configuration (`app.py`):
- Host: `127.0.0.1:3000`
- Namespace: `test`
- Set: `users`

## Dependencies

- Git
- Python 3.8+ (recommended)
- Aerospike Python client: `aerospike`
- Aerospike server (running locally or reachable by network)

## Complete Setup And Run Process

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependency

```bash
pip install aerospike
```

### 4. Run the app

```bash
python3 app.py
```

### 5. Use the menu

- `1` Create user
- `2` Read user
- `3` Update user
- `4` Delete user
- `5` Exit

## Git Commands (Common Workflow)

### Pull latest changes

```bash
git pull origin main
```

### Push your changes

```bash
git add .
git commit -m "Describe your update"
git push origin main
```

## Notes

- Make sure Aerospike is running before starting `app.py`.
- If your Aerospike host/port/namespace/set are different, update `CONFIG`, `NAMESPACE`, and `SET_NAME` in `app.py`.
