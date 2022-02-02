"""
Insta485 index (main) view.
URLs include:
/
"""
import flask
import wangoliver_com
@wangoliver_com.app.route('/')
def show_index():
    """Display / route."""
    # context = {}
    # return flask.render_template("orig_index.html", **context)
    return "<p>Hello, World!</p>"
