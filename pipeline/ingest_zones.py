import pandas as pd
from sqlalchemy import create_engine


def run():
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

    zones_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
    df_zones = pd.read_csv(zones_url)

    df_zones.to_sql(
        name='zones',
        con=engine,
        if_exists='replace',
        index=False
    )

    print('Zones table created')


if __name__ == '__main__':
    run()