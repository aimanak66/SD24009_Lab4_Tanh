import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function", page_icon="📈", layout="centered")
st.title("Hyperbolic Tangent (Tanh) Activation Function")
st.write("Tanh maps input values to an output between -1 and 1.")
st.latex(r"\\tanh(x) = \\frac{e^x - e^{-x}}{e^x + e^{-x}}")

x_min = st.slider("Minimum input value", -20, 0, -10)
x_max = st.slider("Maximum input value", 1, 20, 10)
if x_min >= x_max:
    st.error("The maximum input must be greater than the minimum input.")
else:
    x = np.linspace(x_min, x_max, 400)
    y = np.tanh(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Tanh")
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlabel("Input (x)")
    ax.set_ylabel("Output tanh(x)")
    ax.set_title("Hyperbolic Tangent Activation Function")
    ax.set_ylim(-1.1, 1.1)
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)
    value = st.number_input("Try an input value", value=0.0, step=0.5)
    st.metric("Tanh output", f"{np.tanh(value):.4f}")
    st.caption("Interpretation: negative inputs approach -1, positive inputs approach 1, and tanh(0) = 0.")
