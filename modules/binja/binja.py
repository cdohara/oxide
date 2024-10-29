# You can use https://api.binary.ninja/index.html as a resource.
# Alternatively, you can poke around with pdb and dir() around.
# Currently, this version of the binja module is built for 4.1.5902

import binaryninja as bn
import time
import logging
import json
from capstone import * # to be removed and called by oxide core

logging.basicConfig(level=logging.INFO)

start = time.time()
file_name = "overapprox.out"

output = {
    "disasm": {}
}

# Opens a binary view (bv) of the provided file
# This function raises an exception when a BV can't be created
# TODO: Surround this with try-except to move onto the next module if this one fails
with bn.load(file_name) as bv:

    logging.info(f"Architecture:\t{bv.arch}")

    for func in bv.functions:
        logging.info(f"Function Name:\t{func.name}")
        logging.info(f"Function Start:\t{hex(func.start)}")
        logging.info(f"Function Parameters:\t{func.parameter_vars}")
        logging.info(f"Function Type:\t{func.function_type}")

        for bb in func.basic_blocks:

            for inst in bb.disassembly_text:
                file_offset = bv.get_data_offset_for_address(inst.address)

                # We need to cast to a Python string so we can serialize it later
                output["disasm"][file_offset] = str(inst)

                logging.info(f"{hex(file_offset)}:\t{inst}")

print(json.dumps(output))

end = time.time()
logging.info(f"Time elapsed: {end-start}")