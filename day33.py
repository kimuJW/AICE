import warnings
warnings.filterwarnings(action='ignore') 
from aicentro.session import Session
from aicentro.framework.keras import Keras as AiduFrm

aidu_session = Session(verify=False)
aidu_framework = AiduFrm(session=aidu_session)
aidu_framework.config.data_dir