# Taxi insurance quotes prediction

## Project Description

This project implements a machine learning solution for predicting taxi insurance quotes. The system analyzes various factors related to taxi operations and driver profiles to generate accurate insurance premium predictions. 

Key features:
- Data analysis and preprocessing pipeline
- Machine learning model training with experiment tracking
- FastAPI-based serving endpoint for real-time predictions
- Docker containerization for easy deployment
- MLflow integration for model versioning and monitoring

The solution is designed to help insurance companies automate and optimize their taxi insurance quote generation process, providing consistent and data-driven pricing decisions.

## Prerequisites
- Python >=3.12
- uv tool
    - `pip install uv` OR use a [standalone installer](https://docs.astral.sh/uv/getting-started/installation/)

## Launch data analysis and model training
- Run `uv sync` from root of project
- Select the .venv created by uv as your runtime for jupyter file and run it
<br/>**OR**
- Run command `uv run jupyter nbconvert --to script --stdout --execute .\src\insurance-quotes-prediction.ipynb`

## Experiment tracking
- The notebook contains automatic `MLFlow` server launch and best experiment results tracking.

## Model distribution
Model will be saved under `src/app/target` in `model.pkl` file

## Model serving FastAPI endpoint(POC)
- `uv --directory src run fastapi dev`

## Docker build and run
- `docker build -t quote-classifier-app .`
- `docker run -p 8000:80 quote-classifier-app`

## Deployment
TBD
## Monitoring
TBD
## Data drift detection
TBD
## Retraining
TBD