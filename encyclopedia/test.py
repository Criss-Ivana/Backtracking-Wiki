from markdown import markdown

with open("D:\CS50-webdev\project-1\wiki\entries\CSS.md") as file:
    text=file.read()
    html_text=markdown(text)
    print(html_text)

