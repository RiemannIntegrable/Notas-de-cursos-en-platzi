from src.utils.utils import Utils

if __name__ == "__main__":
    
    utils = Utils()

    data = utils.load_from_csv('/root/Platzi/Cur_M_L_SKlearn/data/external/felicidad.csv')

    print(data)