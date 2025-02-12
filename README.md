# PIB Group Test Solution

## Prerequisites
- Python >=3.12
- uv tool
    - `pip install uv` OR use a [standalone installer](https://docs.astral.sh/uv/getting-started/installation/)

## Launch data analysis and model training
- Run `uv sync` from root of project
- Select the .venv created by uv as your runtime for jupyter file and run it
<br/>**OR**
- Run command`uv run jupyter nbconvert --to script --stdout --execute .\src\pib-group-solution.ipynb`

## Model distribution
Model will be saved under `src/app/target` in `model.pkl` file

## Model serving
- `cd src`
- `uv run fastapi dev`

## Docker build and run
- `docker build -t quote-classifier-app .`
- `docker run -p 8000:80 quote-classifier-app`

## Deployment

## Monitoring

## Data drift detection

## Retraining