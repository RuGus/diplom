import sys

from loguru import logger

from src.settings import LOG_LEVEL

logger.add(sys.stdout, level=LOG_LEVEL, serialize=True)
