import os

# Set to INFO to see some output during long-running steps.
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')

# Disable uploads to S3. Useful when running locally or in CI.
NO_UPLOAD = os.getenv('NO_UPLOAD', None)
NO_DOWNLOAD = os.getenv('NO_DOWNLOAD', None)

PCDN_URL_BASE = os.getenv('PCDN_URL_BASE', 'https://pcdn.brave.software')
PUB_S3_BUCKET = os.getenv('PUB_S3_BUCKET', 'brave-today-cdn-development')
# Canonical ID of the public S3 bucket
BRAVE_TODAY_CANONICAL_ID = os.getenv('BRAVE_TODAY_CANONICAL_ID', None)
BRAVE_TODAY_CLOUDFRONT_CANONICAL_ID = os.getenv('BRAVE_TODAY_CLOUDFRONT_CANONICAL_ID', None)

LANG_REGION = os.getenv('LANG_REGION', 'en_US')

SOURCES_JSON_FILE = os.getenv('SOURCES_JSON_FILE', f'sources.{LANG_REGION}')
FEED_JSON_FILE = os.getenv('FEED_JSON_FILE', f'feed.{LANG_REGION}')

OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')

ARTICLE_HISTORY_FILE = os.getenv('ARTICLE_HISTORY_FILE', f"articles_history.{LANG_REGION}.csv")
SOURCE_SIMILARITY_T10 = os.getenv('SOURCE_SIMILARITY_T10', f"source_similarity_t10.{LANG_REGION}")
SOURCE_SIMILARITY_T10_HR = os.getenv('SOURCE_SIMILARITY_T10_HR', f"source_similarity_t10_hr.{LANG_REGION}")

SOURCE_EMBEDDINGS = os.getenv('SOURCE_EMBEDDINGS', f"SOURCE_EMBEDDINGS.{LANG_REGION}")
