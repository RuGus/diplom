"""Модуль логгирования"""
from loguru import logger

from src.settings import LOG_LEVEL

logger.level(LOG_LEVEL)
