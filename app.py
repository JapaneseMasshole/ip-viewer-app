import streamlit as st
import requests

def get_client_ip():
    try:
        # Using ipify API to get the client's IP
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
        return "Could not fetch IP"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Client IP Address Viewer")
    
    # Create a button
    if st.button("Show My IP"):
        client_ip = get_client_ip()
        st.markdown(f"### Your IP Address is: **{client_ip}**")

if __name__ == "__main__":
    main() 