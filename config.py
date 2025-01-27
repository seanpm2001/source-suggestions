import os

# Disable uploads to S3. Useful when running locally or in CI.
NO_UPLOAD = os.getenv('NO_UPLOAD', None)
NO_DOWNLOAD = os.getenv('NO_DOWNLOAD', None)

PCDN_URL_BASE = os.getenv('PCDN_URL_BASE', 'https://pcdn.brave.software')
PUB_S3_BUCKET = os.getenv('PUB_S3_BUCKET', 'brave-today-cdn-development')
# Canonical ID of the public S3 bucket
BRAVE_TODAY_CANONICAL_ID = os.getenv('BRAVE_TODAY_CANONICAL_ID', None)
BRAVE_TODAY_CLOUDFRONT_CANONICAL_ID = os.getenv('BRAVE_TODAY_CLOUDFRONT_CANONICAL_ID', None)

LANG_REGION_MODEL_MAP = os.getenv('LANG_REGION_MODEL_MAP', [
    ('en_US', "sentence-transformers/all-MiniLM-L6-v2"),
    ('en_CA', "sentence-transformers/all-MiniLM-L6-v2"),
    ('en_GB', "sentence-transformers/all-MiniLM-L6-v2"),
    ('es_ES', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ('es_MX', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ('pt_BR', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ('de_DE', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ('fr_FR', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ('en_AU', "sentence-transformers/all-MiniLM-L6-v2"),
    ('en_IN', "sentence-transformers/all-MiniLM-L6-v2"),
    ('ja_JP', "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
])

SOURCES_JSON_FILE = os.getenv('SOURCES_JSON_FILE', 'sources.{LANG_REGION}')
FEED_JSON_FILE = os.getenv('FEED_JSON_FILE', 'feed.{LANG_REGION}')

OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')

ARTICLE_HISTORY_FILE = os.getenv('ARTICLE_HISTORY_FILE', "articles_history.{LANG_REGION}.csv")
# Don't compute the embedding for a source that has less than 30 collected articles
MINIMUM_ARTICLE_HISTORY_SIZE = os.getenv('MINIMUM_ARTICLE_HISTORY_SIZE', 30)
SIMILARITY_CUTOFF_RATIO = os.getenv('SIMILARITY_CUTOFF_RATIO', 0.9)
SOURCE_SIMILARITY_T10 = os.getenv('SOURCE_SIMILARITY_T10', "source_similarity_t10.{LANG_REGION}")
SOURCE_SIMILARITY_T10_HR = os.getenv('SOURCE_SIMILARITY_T10_HR', "source_similarity_t10_hr.{LANG_REGION}")

SOURCE_EMBEDDINGS = os.getenv('SOURCE_EMBEDDINGS', "SOURCE_EMBEDDINGS.{LANG_REGION}")

if SENTRY_URL := os.getenv('SENTRY_URL'):
    import sentry_sdk
    sentry_sdk.init(dsn=SENTRY_URL, traces_sample_rate=0)
