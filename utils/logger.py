from loguru import logger

logger.add("logs/app.log", level="INFO")
logger.add("logs/error.log", level="ERROR")