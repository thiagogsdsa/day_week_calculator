import streamlit as st
import datetime

st.title("Day of the Week Calculator (Zeller's Congruence)")

date_input = st.date_input("Choose a date")

if date_input:
    d = date_input.day
    m = date_input.month
    y = date_input.year

    if m < 3:
        m += 12
        y -= 1

    K = y % 100
    J = y // 100

    h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    st.markdown(f"### That day is a **{days[h]}**")
    st.latex(r"h = \left(d + \left\lfloor \frac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor + 5J\right) \mod 7")
st.markdown(r"""
This calculator uses **Zeller's Congruence** to find the day of the week for any given date.

**Variables:**

- $d$: Day of the month  
- $m$: Month (with January and February counted as months 13 and 14 of the previous year)  
- $y$: Year (adjusted if month is January or February)  
- $K$: Year of the century ($ y \mod 100 $)  
- $J$: Zero-based century ($ \left\lfloor \frac{y}{100} \right\rfloor $), and 

$$
\left\lfloor \cdot \right\rfloor : \mathbb{R} \longrightarrow \mathbb{Z}
$$

is the floor function that maps a real number $x$ to the greatest integer $n$ less than or equal to $x$.
""")