# tests/roboflow/modelDownload/py

# Imports
from roboflow import Roboflow
import functions

# Roboflow Model
# API Key
rf = Roboflow(api_key="8UjXP8kvalxT275T5XgN")
# Project Acess
project = rf.workspace("projeto-ic-gcsp").project("pragas-ic-gcsp-m8j84")
resp = int(input(functions.strColored(">> Digite qual versão do modelo deseja baixar: ", 'blue')))

try:
    version = project.version(resp)
    # Dataset
    dataset = version.download("yolov5")
except:
    print(functions.strColored(">> ERRO: Versão não existente do modelo Roboflow", 'red'))
    exit(0)
