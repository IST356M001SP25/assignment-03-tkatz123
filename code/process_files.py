'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import json
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process Package Files")


data = st.file_uploader("Upload Package File", type = ["txt"])

if "stats" not in st.session_state:
        st.session_state.stats = {"file": [], "values": []}

entry_count = 0
json_name = ""
total_files = 0
total_packages = 0

if data:
   packages = []
   file_name = data.name
   json_name = file_name.replace("txt", "json")
   file_contents = data.read().decode("utf-8").splitlines()
   for line in file_contents:
      line = line.strip()
      if line:
         package = parse_packaging(line)
         total_units = calc_total_units(package)
         unit = get_unit(package)
         packages.append(package)
   with open(f"data/{json_name}", "w") as f:
        json.dump(packages, f, indent=4) 
   with open(f"data/{json_name}", "r") as f:
        info = json.load(f)  

   entry_count = len(info)
   st.session_state.stats["file"].append(json_name)
   st.session_state.stats["values"].append(entry_count)
   
for i in range(len(st.session_state.stats['file'])):
    st.info(f"{st.session_state.stats['values'][i]} packages written to {st.session_state.stats['file'][i]}")
total_files = len(st.session_state.stats['file'])
total_packages = sum(st.session_state.stats['values'])
st.success(f"{total_files} files processed, {total_packages} total lines processed")

