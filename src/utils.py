from . import TOWN_REGION_MAPPING, TOWN_MATURITY_MAPPING

import pandas as pd

from typing import Tuple

def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Loads training and testing data."""

    train = pd.read_csv('data/train.csv')
    test = pd.read_csv('data/test.csv')

    return train, test

def impute_additional_features(train: pd.DataFrame,
                               test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Imputes additional features as such region, maturity and area_sqm
    for testing data.
    """
    # Computing average flat area from training data
    avg_area_by_flat_type = train.groupby("flat_type")["area_sqm"].mean()
    
    # Imputing calculated features into testing data
    test['region'] = test['town'].apply(lambda x:
        "".join([k for k, v in TOWN_REGION_MAPPING.items() if x in v]))
    test["maturity"] = test["town"].apply(lambda x:
        "".join([k for k, v in TOWN_MATURITY_MAPPING.items() if x in v]))
    test["area_sqm"] = test.apply(lambda x:
        avg_area_by_flat_type[x['flat_type']], axis=1)

    return train, test

def preprocess_dataset(train: pd.DataFrame,
                       test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Combines training and testing data to preprocess together."""

    train, test = impute_additional_features(train, test)
    train['train_set'] = 1
    test['train_set'] = 0

    combined = pd.concat([train, test], ignore_index=True)

    # Preprocessing
    n_lat_bins = 3
    n_lng_bins = 4

    lat_labels = [f"Lat{i}" for i in range(n_lat_bins)]
    lng_labels = [f"Lng{i}" for i in range(n_lng_bins)]
    combined["lat_bins"] = pd.cut(combined["latitude"], bins=n_lat_bins, include_lowest=True, labels=lat_labels)
    combined["lng_bins"] = pd.cut(combined["longitude"], bins=n_lng_bins, include_lowest=True, labels=lng_labels)
    combined["lat_x_lng"] = combined.apply(lambda x: str(x["lat_bins"]) + str(x["lng_bins"]), axis=1)
    combined["type_x_maturity"] = combined.apply(lambda x: str(x["flat_type"]) + str(x["maturity"]), axis=1)
    combined["maturity"] = combined["maturity"].apply(lambda x: 1 if "Mature" else 0)

    combined = pd.concat([combined, pd.get_dummies(combined["month"], prefix="Month", drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["region"], drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["lat_bins"], drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["lng_bins"], drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["flat_type"], drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["lat_x_lng"], drop_first=True)], axis=1)
    combined = pd.concat([combined, pd.get_dummies(combined["type_x_maturity"], drop_first=True)], axis=1)

    combined = combined.drop(["month", "town", "region", "latitude", "lat_bins", "longitude", "lng_bins", "flat_type", "lat_x_lng", "type_x_maturity"], axis=1)

    train = combined.loc[combined['train_set'] == 1, :].reset_index(drop=True)
    test = combined.loc[combined['train_set'] == 0, :].reset_index(drop=True)

    return train, test