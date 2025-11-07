import streamlit as st

st.title("THE CHAI POOLING BOOTH")
col1 ,col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("maasala.jpg",width=200 )
    vote1=st.button("Masala Chai")
       

with col2:
    st.header("Adrak Chai")
    st.image("adrak.jpg",width=200)
    vote2=st.button("Adrak chai")
  

if vote1:
 st.success("thanks for voting masala chai")
elif vote2:
  st.success("Thanks for voting Adrak chai")

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water in a pot.
    2. Add tea leaves and let it simmer.
    3. Add milk and sugar to taste.
    4. For Masala Chai, add spices like cardamom, cinnamon, and cloves.
    5. For Adrak Chai, add freshly grated ginger.
    6. Let it boil for a few minutes.
    7. Strain the tea into cups and serve hot.
    """)
st.markdown("## enjoy your chai! ☕")
st.markdown('>blockquote')
          