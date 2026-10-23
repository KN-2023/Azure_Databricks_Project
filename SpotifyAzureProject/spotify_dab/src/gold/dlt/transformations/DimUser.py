import dlt 
@dlt.table
def dimuser_stg():
    df = spark.readStream.table("spotify_cata.silver.dimuser")
    return df
