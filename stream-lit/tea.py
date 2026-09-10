import streamlit as st

st.title("☕ Indian Cafe 24")
st.subheader("Welcome to our Coffee and Tea Shop")

name = st.text_input("Enter your Name")

dob = st.date_input("Enter your DOB")

chai_base = st.selectbox(
    "Pick your Chai Base",
    ["Milk", "Almond Milk", "Water"]
)

selected_flavor = st.radio(
    "Select Flavor",
    ["Adrak", "Elaichi", "Masala", "Special", "All"]
)

cups = st.number_input(
    "How many Cups",
    min_value=1,
    max_value=10,
    step=1
)

add_sugar = st.checkbox("Add Sugar")

sugar_level = 0

if add_sugar:
    sugar_level = st.slider(
        "Sugar Spoons",
        min_value=0,
        max_value=5,
        value=2
    )

@st.dialog("Order Confirmation")
def show_order(name, dob, chai_base, selected_flavor, cups, sugar_level):
    if not name:
        st.error("Please enter your name.")
    else:
        st.success("🎉 Order Placed Successfully!")
        st.write("## 🧾 Order Summary")
    
        st.write(f"**Customer:** {name}")
        st.write(f"**DOB:** {dob}")
        st.write(f"**Chai Base:** {chai_base}")
        st.write(f"**Flavor:** {selected_flavor}")
        st.write(f"**Cups:** {cups}")

        if add_sugar:
            st.write(f"**Sugar:** {sugar_level} spoon(s)")
        else:
            st.write("**Sugar:** No Sugar")
    
        total = cups * 30
    
        st.write(f"### 💰 Total Bill: ₹{total}")

if st.button("Place Order", use_container_width=True):
    show_order(name, dob, chai_base, selected_flavor, cups, sugar_level)