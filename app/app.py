import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # Fetch TENANT_NAME from environment variables with a safe fallback
    tenant_name = os.environ.get("TENANT_NAME", "Default Tenant")
    return f"Demo environment for {tenant_name}\n"

if __name__ == "__main__":
    # Host on 0.0.0.0 to allow container/network binding
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)