# Rezepte

## Request

```
http://127.0.0.1:8000/food/recipe
```

## Response

```
[
    {
        "id": 4,
        "hints": [
            {
                "id": 2,
                "createdAt": "2022-08-29T17:10:21.312000+02:00",
                "updatedAt": "2022-08-29T17:50:27.477000+02:00",
                "name": "mehr Gewicht",
                "description": "",
                "value": 300.0,
                "hintLevel": "warn",
                "minMax": "min",
                "parameter": "weight_g"
            },
            {
                "id": 5,
                "createdAt": "2022-08-29T23:20:25.463000+02:00",
                "updatedAt": "2022-08-29T23:20:25.463000+02:00",
                "name": "Nicht gesund genug",
                "description": "",
                "value": 2.0,
                "hintLevel": "warn",
                "minMax": "max",
                "parameter": "nutri_class"
            }
        ],
        "tags": [],
        "createdAt": "2022-08-27T19:18:21.446000+02:00",
        "updatedAt": "2022-08-29T23:20:54.532000+02:00",
        "energyKj": 1971.0,
        "proteinG": 26.0,
        "fatG": 25.0,
        "fatSatG": 12.0,
        "sugarG": 3.0,
        "sodiumMg": 522.0,
        "saltG": 0.0,
        "fruitFactor": 0.0,
        "carbohydrateG": 39.0,
        "fibreG": 2.0,
        "fructoseG": 0.0,
        "lactoseG": 0.0,
        "name": "Einfache Käsespätzle",
        "description": "",
        "mealType": "lunch",
        "nutriClass": 3.0,
        "nutriPoints": 5.0,
        "weightG": 246.0
    },
    {
        "id": 2,
        "createdAt": "2022-08-27T19:11:35.084000+02:00",
        "updatedAt": "2022-08-30T07:27:06.635424+02:00",
        "energyKj": 2832.0,
        "proteinG": 38.0,
        "fatG": 4.0,
        "fatSatG": 1.0,
        "sugarG": 35.0,
        "sodiumMg": 88.0,
        "saltG": 0.0,
        "fruitFactor": 0.0,
        "carbohydrateG": 125.0,
        "fibreG": 7.0,
        "fructoseG": 0.0,
        "lactoseG": 0.0,
        "name": "Reis mit Süß Saurer Soße",
        "description": "",
        "mealType": "lunch",
        "nutriClass": 2.0,
        "nutriPoints": 1.0,
        "weightG": 465.0,
        "tags": [],
        "hints": []
    }
]
```

# Zutaten:

## Reqeust

```
http://127.0.0.1:8000/food/portion?search=Nu
```

## Response

```
[
    {
        "id": 68,
        "ingredient": {
            "id": 81,
            "createdAt": "2022-08-20T20:09:58.079000+02:00",
            "updatedAt": "2022-08-30T07:26:18.322716+02:00",
            "energyKj": 2587.0,
            "proteinG": 23.99124,
            "fatG": 49.43,
            "fatSatG": 8.415,
            "sugarG": 0.0,
            "sodiumMg": 220.7,
            "saltG": 0.0,
            "fruitFactor": 0.0,
            "carbohydrateG": 22.70376,
            "fibreG": 6.323,
            "fructoseG": 0.0,
            "lactoseG": 0.0,
            "nutriPointsEnergyKj": 7.0,
            "nutriPointsProteinG": -5.0,
            "nutriPointsFatSatG": 8.0,
            "nutriPointsSugarG": 0.0,
            "nutriPointsSaltG": 2.0,
            "nutriPointsFibreG": -5.0,
            "name": "Erdnussbutter",
            "description": "",
            "physicalDensity": 1.0,
            "physicalViscosity": "solid",
            "fdcId": 2262072,
            "majorClass": "Legumes and Legume Products",
            "nutriPoints": 7,
            "nutriClass": 3.0,
            "ndbNumber": 16098,
            "tags": []
        },
        "measuringUnit": {
            "id": 3,
            "createdAt": null,
            "updatedAt": null,
            "name": "g",
            "description": "Gramm",
            "quantity": 1.0,
            "unit": "g"
        },
        "createdAt": "2022-08-20T20:10:00.742000+02:00",
        "updatedAt": "2022-08-20T20:10:00.742000+02:00",
        "energyKj": 25.87,
        "proteinG": 0.24,
        "fatG": 0.49,
        "fatSatG": 0.08,
        "sugarG": 0.0,
        "sodiumMg": 2.21,
        "saltG": 0.0,
        "fruitFactor": 0.0,
        "carbohydrateG": 0.23,
        "fibreG": 0.06,
        "fructoseG": 0.0,
        "lactoseG": 0.0,
        "name": "Erdnussbutter in g",
        "quantity": 1.0,
        "rank": 1,
        "weightG": 1.0
    },
    {
        "id": 110,
        "ingredient": {
            "id": 14,
            "createdAt": null,
            "updatedAt": "2022-08-30T07:26:18.248936+02:00",
            "energyKj": 1521.0,
            "proteinG": 13.04,
            "fatG": 1.51,
            "fatSatG": 0.277,
            "sugarG": 2.67,
            "sodiumMg": 6.0,
            "saltG": 0.0,
            "fruitFactor": 0.0,
            "carbohydrateG": 74.67,
            "fibreG": 3.2,
            "fructoseG": 0.0,
            "lactoseG": 0.0,
            "nutriPointsEnergyKj": 4.0,
            "nutriPointsProteinG": -5.0,
            "nutriPointsFatSatG": 0.0,
            "nutriPointsSugarG": 0.0,
            "nutriPointsSaltG": 0.0,
            "nutriPointsFibreG": -3.0,
            "name": "Nudeln, roh",
            "description": "",
            "physicalDensity": 1.5,
            "physicalViscosity": "solid",
            "fdcId": 169736,
            "majorClass": "Cereal Grains and Pasta",
            "nutriPoints": -4,
            "nutriClass": 1.0,
            "ndbNumber": 20120,
            "tags": []
        },
        "measuringUnit": {
            "id": 3,
            "createdAt": null,
            "updatedAt": null,
            "name": "g",
            "description": "Gramm",
            "quantity": 1.0,
            "unit": "g"
        },
        "createdAt": "2022-08-20T22:07:41.075000+02:00",
        "updatedAt": "2022-08-20T22:07:41.075000+02:00",
        "energyKj": 15.21,
        "proteinG": 0.13,
        "fatG": 0.02,
        "fatSatG": 0.0,
        "sugarG": 0.03,
        "sodiumMg": 0.06,
        "saltG": 0.0,
        "fruitFactor": 0.0,
        "carbohydrateG": 0.75,
        "fibreG": 0.03,
        "fructoseG": 0.0,
        "lactoseG": 0.0,
        "name": "Nudeln in g",
        "quantity": 1.0,
        "rank": 1,
        "weightG": 1.0
    }
]
```
