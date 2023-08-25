import webbrowser

def firefox(url):
    webbrowser.get('firefox').open_new_tab(url)
    
websites = {
    "Google" : "https://www.google.com/",
    "Facebook" : "https://ar-ar.facebook.com/",
    "Twitter" : "https://twitter.com/?lang=ar",
    "Whatsapp" : "https://web.whatsapp.com/",
    "GitHub" : "https://github.com/"
}

