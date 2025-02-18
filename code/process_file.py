'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import json
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process File of Packages")

data = st.file_uploader("Upload Package File", type = ["txt"])

if data:
   packages = []
   file_contents = data.read().decode("utf-8").splitlines()
   for line in file_contents:
      line = line.strip()
      if line:
         package = parse_packaging(line)
         total_units = calc_total_units(package)
         unit = get_unit(package)
         st.info(f"{line} -> total units: {total_units} {unit}")
         packages.append(package)
      with open("data/pacaking1.json", "w") as f:
         json.dump(packages, f, indent=4)
   with open("data/pacaking1.json", "r") as f:
      info = json.load(f)
   entry_count = len(info)
   st.success(f"{entry_count} packages written to packaging1.json")