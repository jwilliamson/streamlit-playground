import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title('Sine Wave')

    # Generate a range of x values
    x = np.linspace(0, 2*np.pi, 400)

    # Compute the corresponding y values
    y = np.sin(x)

    # Create a DataFrame
    df = pd.DataFrame({
        'x': x,
        'y': y
    })

    # Plot the data
    st.line_chart(df)

if __name__ == "__main__":
    main()