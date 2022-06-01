***************** CREATE CONDA ENV *****************

conda create -n mlops python=3.7 -y

activate mlops

pip install -r requirements.txt


***************** DVC Initialization *****************

git init

dvc init

dvc add data_git/winequality.csv

git add .

git commit -m "Initialize File Structure"


***************** Load Data Stage *****************

create src/get_data.py
create src/load_data.py
update dvc.yaml
dvc repro
