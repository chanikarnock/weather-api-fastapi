import logging
import os


logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("LOGGER")
VISUAL_CROSSING_API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")