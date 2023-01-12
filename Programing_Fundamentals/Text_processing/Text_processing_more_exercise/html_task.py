print("<h1>")
article = input()
print(f"    {article}")
print("</h1>\n<article>")
content = input()
print(f"    {content}")
print("</article>")
while True:
    comment = input()
    if comment == "end of comments":
        break
    print("<div>")
    print(f"    {comment}")
    print("</div>")
