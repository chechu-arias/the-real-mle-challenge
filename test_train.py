
import config as config
from src.features.build_features import build_training
from src.models.train import train_model

if __name__ == '__main__':

    df = build_training()
    train_model(df)
