# to import a module
import app13weigh_converters

# the following is used to import a specific function from a module and can use without using the module name
from app13weigh_converters import kg_to_lbs

app13weigh_converters.kg_to_lbs(10)
app13weigh_converters.lbs_to_kg(10)

kg_to_lbs(200)