import dagshub
import mlflow
mlflow.set_tracking_uri("https://dagshub.com/rakesh-kumar-22/mlops-mini-project.mlflowhttps://dagshub.com/rakesh-kumar-22/mlops-mini-project.mlflow")
dagshub.init(repo_owner='rakesh-kumar-22', repo_name='mlops-mini-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)