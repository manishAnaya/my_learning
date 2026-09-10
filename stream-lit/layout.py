import streamlit as st

st.title("Chai taste Poll")
col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaCMIYhn5Z5rm1aU4i6jgNCoJse-exDqOSVtzNQaXO6Q&s=10", use_container_width=True)
    v1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsfx2C7yUFB0ujriC6E26Q53cTwPxZBmIhiBFK9Uc6Ce5lvQcUe_8qjxP9&s=10", use_container_width=True)
    v2 = st.button("Vote for Adrak Chai")

if v1:
    st.success("Thank you for voting Masala Chai")
elif v2:
    st.success("Thank you for voting Adrak Chai")

st.sidebar.header("Please Fill This before Voting")
st.sidebar.text_input("Enter your name")

exp = st.expander("How to vote")

with exp:
    st.write(
        """
        1. Fill the form
        2. Select your fav option by clicking on buttons
        3. Congratulation Voting done
        """
    )

st.markdown("# Thank you.")
st.write("# Thank you.")