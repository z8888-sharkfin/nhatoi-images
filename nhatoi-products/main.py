import os
import json
import codecs

template = {
    "brandName": "Nhà Tôi",
    "category": {},
    "endOfEventDate": "0001-01-01T00:00:00",
    "icon": "https://github.com/z8888-sharkfin/nhatoi-images/blob/d78052b80dc206b271ea8b54fd3a3a5d72704c07/nhatoi-products/",
    "id": -1,
    "isCoolPreserve": False,
    "isFresh": False,
    "name": "",
    "productCode": "1012835000472",
    "productPrices": [
        {
            "basePrice": 155000,
            "discountPercent": 35,
            "isCanBuy": True,
            "priceOnBill": 100500,
            "quantityCondition": 0,
            "storeId": 11612,
            "textStatus": "Mua",
            "type": 1
        }
    ],
    "promotionGiftImgs": "",
    "promotionText": "",
    "rateStar": 4.8,
    "totalReview": 0,
    "unit": "chai",
    "url": "",
    "weightUnit": None
}

products = {
    "nuoc-lau-san-green-1-Photoroom.png-Photoroom.png" : {
        "name": "Nước lau sàn Green 3.6L",
        "basePrice": 54900,
        "priceOnBill": 49400,
        "category": {
            "id": 2510,
            "name": "Nước lau sàn",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-giat-dam-dac-max-3.8L-1-Photoroom.png-Photoroom.png" : {
        "name": "Nước giặt Max đậm đặc 3.8L",
        "basePrice": 33900,
        "priceOnBill": 29400,
        "category": {
            "id": 2464,
            "name": "Nước giặt",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-giat-xa-bode-sieu-dam-dac-1-Photoroom.png-Photoroom.png" : {
        "name": "Nước giặt xả Bồ Đề siêu đậm đặc 3.8L",
        "basePrice": 44490,
        "priceOnBill": 42400,
        "category": {
            "id": 2464,
            "name": "Nước giặt",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-green-1.2L-1-Photoroom.png-Photoroom.png" : {
        "name": "Nước rửa chén Green 1.2L",
        "basePrice": 27700,
        "priceOnBill": 25400,
        "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-max-0.8L-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước rửa chén Max 0.8L",
         "basePrice": 23800,
         "priceOnBill": 20600,
         "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-giat-care-3.8L-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước giặt Care 3.8L",
         "basePrice": 43900,
         "priceOnBill": 40400,
         "category": {
            "id": 2464,
            "name": "Nước giặt",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-cao-cap-bode-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước rửa chén Bồ Đề Cao Cấp 1.2L",
         "basePrice": 20900,
         "priceOnBill": 18800,
         "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-green-1.2L-2-Photoroom.png-Photoroom.png" : {
         "name": "Nước rửa chén Green 1.2L",
         "basePrice": 22900,
         "priceOnBill": 19800,
         "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-lau-san-bode-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước lau sàn Bồ Đề",
         "basePrice": 35500,
         "priceOnBill": 34400,
         "category": {
            "id": 2510,
            "name": "Nước lau sàn",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-bat-bode-cong-ghe-sinh-hoc-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước rửa chén công nghệ sinh học",
         "basePrice": 20900,
         "priceOnBill": 19400,
         "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-giat-xa-green-3.8L-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước giặt xả Green 3.8L",
         "basePrice": 60900,
         "priceOnBill": 50400,
         "category": {
            "id": 2464,
            "name": "Nước giặt",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-green-0.8L-1-Photoroom.png-Photoroom.png" : {
         "name": "Nước rửa chén Green 0.8L",
         "basePrice": 21950,
         "priceOnBill": 18400,
         "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
    "nuoc-rua-chen-max-1.2L-1-Photoroom.png-Photoroom.png" : {
        "name": "Nước rửa chén Max 1.2L",
        "basePrice": 24890,
        "priceOnBill": 21400,
        "category": {
            "id": 2387,
            "name": "Nước rửa chén",
            "parentIds": [
                7160
            ]
        },
    },
}

def _list_file():
    files = [f for f in os.listdir("./") if os.path.isfile(f)]
    print(json.dumps(files, indent=2))

def print_json(j):
    print(json.dumps(j, indent=2, ensure_ascii=False, sort_keys=True))

def read_json_utf8(file_name: str):
    """Read json file in utf-8 format"""
    try:
        with codecs.open(file_name, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except: # pylint: disable=W0702
        return None

def write_json_utf8(file_name: str, data):
    """Save json file in utf-8 format"""
    with codecs.open(file_name, "w", "utf-8") as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    out = {}
    p_id = 88000000
    for item in products.items():
        p_id += 1
        filename = item[0]
        data = item[1]
        discountPercent = int(((data["basePrice"] - data["priceOnBill"])/data["basePrice"])*100)
        cat_id = str(data["category"]["id"])
        t = {
            "brandName": "Nhà Tôi",
            "category": data["category"],
            "endOfEventDate": "0001-01-01T00:00:00",
            "icon": f"https://github.com/z8888-sharkfin/nhatoi-images/blob/d78052b80dc206b271ea8b54fd3a3a5d72704c07/nhatoi-products/{filename}?raw=true",
            "id": p_id,
            "isCoolPreserve": False,
            "isFresh": False,
            "name": data["name"],
            "productCode": f"10128{p_id}",
            "productPrices": [
                {
                    "basePrice": data["basePrice"],
                    "discountPercent": discountPercent,
                    "isCanBuy": True,
                    "priceOnBill": data["priceOnBill"],
                    "quantityCondition": 0,
                    "storeId": 11612,
                    "textStatus": "Mua",
                    "type": 1
                }
            ],
            "promotionGiftImgs": "",
            "promotionText": "",
            "rateStar": 4.8,
            "totalReview": 0,
            "unit": "chai",
            "url": "",
            "weightUnit": None
        }
        if cat_id not in out:
            out[cat_id] = []
        out[cat_id].append(t)

    write_json_utf8("./out.json", out)
    print(json.dumps(out, indent=2))

