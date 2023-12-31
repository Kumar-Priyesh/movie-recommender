mkdir -p ~/.streamlit/
echo "[general]" > ~/.streamlit/credentials.toml
echo "email = \"priyesh708@gmail.com\"" >> ~/.streamlit/credentials.toml
echo "[server]" >> ~/.streamlit/credentials.toml
echo "headless = true" >> ~/.streamlit/credentials.toml
echo "port = $PORT" >> ~/.streamlit/credentials.toml