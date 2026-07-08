import json

from processing.extract_data import get_reponse, get_data
from processing.transform_data import transform_clean_data
from processing.load_clean_data import create_new_data


def lambda_handler(event, context):
    # text = "Desde AWS!!!"
    
    raw_data = get_data()
    data_clean= transform_clean_data(raw_data)
    csv_buffer = data_clean.to_csv(index=False).encode("utf-8")
    new_data = create_new_data(csv_buffer)

    # TODO implement
    return {
        'statusCode': 200,
        'data1': data_clean.head(5).to_dict(orient="records"),
        "data2": json.dumps(new_data)
    }