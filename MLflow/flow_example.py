import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
import mlflow
import mlflow.sklearn
from prefect import task, flow
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

@task(name="Extraer Datos", tags=["data"], description="Extrae los datos de la base de datos Iris.")
def extraer_datos():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df

@task(name="Preparar Datos", tags=["data"], description="Divide los datos en conjuntos de entrenamiento y testeo.")
def preparar_datos(df):
    X = df.drop(columns=['target'])
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

@task(name="Entrenar Modelo", tags=["training", "model"], description="Entrena un modelo de regresión lineal con los datos de entrenamiento.")
def entrenar_modelo(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

@task(name="Testear Modelo", tags=["testing", "model"], description="Testea el modelo entrenado y calcula el error cuadrático medio.")
def testear_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def regresion_iris():
    mlflow.set_experiment("regresion_iris_prefect")
    print(f"tracking URI: '{mlflow.get_tracking_uri()}'")
    with mlflow.start_run():
        df = extraer_datos()
        X_train, X_test, y_train, y_test = preparar_datos(df)
        
        # Registrar parámetros
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        
        model = entrenar_modelo(X_train, y_train)
        
        mse = testear_modelo(model, X_test, y_test)
        
        # Registrar métricas
        mlflow.log_metric("mse", mse)
        
        # Registrar el modelo
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Mean Squared Error: {mse}")

        print(f"default artifact location: '{mlflow.get_artifact_uri()}'")

# Ejecutar el flujo
regresion_iris()