'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process One Package")

package = st.text_input("Enter Package Data")


if package:
    output = parse_packaging(package)
    total = calc_total_units(output)
    units = get_unit(output)
    st.write(f"[{output[0]}, {output[1]}, {output[2]}]")

    for item in output:
        name = list(item.keys())[0]
        value = list(item.values())[0]
        st.info(f"{name} -> {value}")
    st.success(f"Total Size: {total} {units}")

