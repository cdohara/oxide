import binaryninja as bn
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

start = time.time()
file_name = "overapprox.out"

# Opens a binary view (bv) of the provided file
with bn.open_view(file_name) as bv:
    logger.debug(f"Opening {bv.file.filename} which has {len(list(bv.functions))} functions")