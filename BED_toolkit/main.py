import sys
from Class.bed_class import Bed


# The input
user_input = sys.argv[1]
bed_data = Bed.read_bed(user_input)
print(bed_data)
print(len(bed_data))