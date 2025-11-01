
import pandas as pd
import numpy as np
import pytest
from pipeline.data_enricher import DataEnricher



def test_data_enricher(products_user_df, omnicart_classes):
    data_enr = omnicart_classes[1]
    merged_data = data_enr.data_enrich(products_user_df[0], products_user_df[1])

    assert merged_data.shape[0] == 5

def test_data_enricher_edge_case(products_user_df, omnicart_classes):
    data_enr = omnicart_classes[1]
    merged_data = data_enr.data_enrich(products_user_df[2], products_user_df[1])

    assert merged_data.shape[0] == 6
    assert pd.isna(merged_data["email"].iloc[5])
    assert 6 in data_enr.missing_user_products['id'].values  
    assert merged_data['revenue'].iloc[0] == 13194 