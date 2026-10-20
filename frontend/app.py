import httpx
import streamlit as st

st.set_page_config(page_title="Agent App", page_icon="🤖", layout="centered")
st.title("Agent App")
st.caption("Streamlit UI talking to the FastAPI backend")

with st.sidebar:
    st.header("API")
    base_url = st.text_input(
        "API base URL",
        value="http://127.0.0.1:8000",
        help="FastAPI server address",
    )
    if st.button("Check API health"):
        url = f"{base_url.rstrip('/')}/health"
        try:
            with httpx.Client(timeout=5.0) as client:
                response = client.get(url)
                response.raise_for_status()
                st.success("API is healthy")
                st.json(response.json())
        except httpx.HTTPError as exc:
            st.error(f"Could not reach API: {exc}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    url = f"{base_url.rstrip('/')}/chat"
    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(url, json={"message": prompt})
            if response.is_error:
                detail = response.text
                try:
                    detail = response.json().get("detail", detail)
                except Exception:
                    pass
                st.error(f"Chat request failed ({response.status_code}): {detail}")
            else:
                reply = response.json()["reply"]
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with st.chat_message("assistant"):
                    st.markdown(reply)
    except httpx.HTTPError as exc:
        st.error(f"Chat request failed: {exc}")
