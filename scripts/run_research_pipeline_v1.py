from pprint import pprint

from triton_labs.services.research_pipeline_v1 import (
    run_equity_intelligence,
)

result = run_equity_intelligence("MSFT")

pprint(result)