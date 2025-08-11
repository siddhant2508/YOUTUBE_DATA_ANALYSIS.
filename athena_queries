-- Create external table from cleansed data in S3
CREATE EXTERNAL TABLE IF NOT EXISTS youtube_data (
    video_id STRING,
    title STRING,
    channel_title STRING,
    category_id INT,
    views BIGINT,
    likes BIGINT,
    dislikes BIGINT,
    comment_count BIGINT,
    thumbnail_link STRING,
    comments_disabled BOOLEAN,
    ratings_disabled BOOLEAN,
    video_error_or_removed BOOLEAN,
    description STRING,
    region STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
) LOCATION 's3://your-bucket/cleansed/youtube_data/'
TBLPROPERTIES ('has_encrypted_data'='false');
