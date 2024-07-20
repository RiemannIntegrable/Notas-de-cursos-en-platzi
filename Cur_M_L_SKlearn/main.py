from src.utils.utils import Utils
from src.models.models import Models

if __name__ == "__main__":
    
    utils = Utils()
    models = Models()

    data = utils.load_from_csv('/home/riemannintegrable/Platzi/Cur_M_L_SKlearn/data/external/felicidad.csv')
    X, y = utils.features_target(data, ['country', 'rank', 'score'], 'score')

    models.grid_training(X, y)

    print(data)