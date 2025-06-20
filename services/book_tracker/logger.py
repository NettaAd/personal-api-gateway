from loguru import logger

logger.add("book_tracker.log", rotation="1 MB", retention="5 days", level="DEBUG")
