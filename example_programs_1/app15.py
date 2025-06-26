# Packages - used to organize module
# Package should have __init__.py file

#Importing entire module from packages
import Utility.weight_converter
#importing the specific module method from package
from Utility.weight_converter import kg_to_lbs
#importing the module from package
from Utility import weight_converter

Utility.weight_converter.kg_to_lbs(100)

kg_to_lbs(100)

weight_converter.lbs_to_kg(100)