# SuperBenchmark

## Setup

1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
uvicorn superbenchmark.main:app --reload
```

## Configuration
- Set `SUPERBENCHMARK_DEBUG` in `.env` file
- `True`: Use test database
- `False`: Disable endpoints

## Endpoints
- GET `/results/average`: All results
- GET `/results/average/{start_time}/{end_time}`: Time-windowed results

## Code Quality
Run checks:
```bash
# Run linting, formatting, and type checking
./check.sh
