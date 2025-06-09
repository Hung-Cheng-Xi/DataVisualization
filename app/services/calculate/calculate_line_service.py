import pandas as pd
from app.schema import LifeLineRecord


def get_life_records() -> list[LifeLineRecord]:
    """Load and process birth and death data, return list of LifeRecord for years Minguo 103–113."""
    data = {
        "year": list(range(96, 114)),
        "deaths": [
            140371,
            143594,
            143513,
            145804,
            153206,
            155239,
            155686,
            163327,
            163822,
            172829,
            172028,
            172700,
            175546,
            173162,
            184457,
            208129,
            205202,
            201313,
        ],
        "births": [
            203711,
            196486,
            192133,
            166473,
            198348,
            234599,
            194939,
            211399,
            213093,
            207600,
            194616,
            180656,
            175074,
            161288,
            157019,
            137413,
            133895,
            134769,
        ],
    }
    df = pd.DataFrame(data)
    # Filter year >= 103
    df = df[df["year"] >= 103]
    # Calculate natural change
    df["natural_change"] = df["births"] - df["deaths"]

    # Create Pydantic models
    return [LifeLineRecord(**row) for row in df.to_dict(orient="records")]
