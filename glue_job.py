from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import sys

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket/raw/youtube_data.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

# Basic transformation: Convert to DataFrame and drop nulls
df = datasource.toDF().dropna()

# Convert back to DynamicFrame and write to cleansed path
cleansed_frame = DynamicFrame.fromDF(df, glueContext, "cleansed_frame")
glueContext.write_dynamic_frame.from_options(
    frame=cleansed_frame,
    connection_type="s3",
    connection_options={"path": "s3://your-bucket/cleansed/youtube_data"},
    format="parquet"
)

job.commit()
