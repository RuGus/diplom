from loguru import logger
from settings import LOG_LEVEL

logger.add(level=LOG_LEVEL, serialize=True)
