from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

# Custom titles for specific routes
custom_titles = {
    "/": "Home",
    "/admin/": "Admin Dashboard",
    "/api/users": "Users",
    "/api/sectors": "Sectors",
}

def generate_sitemap(app):
    links = ['/admin/']
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    # Create HTML list items with custom titles
    links_html = "".join([
        f"<li><a href='{url}'>{custom_titles.get(url, url)}</a></li>" 
        for url in links
    ])

    return """
    <style>
        body {
            background-color: #7D8087;
            margin: 0px; 
            padding:0px;
        }
    </style>
    <body>
        <nav style="background-color: #1B3255; color: #056FAA; font-weight: 400; font-size: 30px; margin-bottom: 12px;">
        <br/>
            <h1 style="text-align: center;">Welcome to your dasboard!!</h1>
            <br/>
        </nav>
        <br/>
        <ul style="text-align: left; margin-left: 30px;">"""+links_html+"""</ul>
    </body>"""
