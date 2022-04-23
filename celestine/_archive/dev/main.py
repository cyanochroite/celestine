import hashlib
import os

from element import element


def attribute(name, value):  # {
    return ' {}="{}"'.format(name, value) if (name is not None and value is not None) else ''
# }


print(attribute("pig", "dog"))
print(attribute(None, "dog"))
print(attribute("pig", "dog"))


def attribute():  # {
    bat = 3
# }


def element_text(tag, arg):  # {
    print("<{}{}></{}>".format(tag, arg, tag))
# }


def element_normal(tag, arg):  # {
    print("<{}{}>".format(tag, arg))
    print("</{}>".format(tag))
# }


def element_void(tag, arg):  # {# void element
    print("<{}{} />".format(tag, arg))
# }





def title(text):  # {
    print("<title>")
    print("\t" + text)
    print("</title>")
# }


def body(list):  # {
    body = list.pop(0)
    param = list.pop(0)
    body(param)
# }


def table(list):  # {
    body = list.pop(0)
    param = list.pop(0)
    print("<table>")
    body(param)
    print("</table>")
# }


def tr(list):  # {
    body = list.pop(0)
    param = list.pop(0)
    print("<tr>")
    body(param)
    print("</tr>")
# }


def td(list):  # {
    text = list.pop(0)
    print("<td>")
    print(text)
    print("</td>")
# }


def html(head, body):  # {
    element = head.pop(0)
    attribute = head
    print("<{}{}>".format(element, attribute))
    body = list.pop(0)
    param = list.pop(0)
    body(param)
    print("</{}>".format(element))

# }


def work():  # {
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">")
    title("Create a Working WebSite")
    print("<title>")
    print("Create a Working WebSite")
    print("</title>")
    print("<link href=\"https://edu.mem-dixy.ch/favicon.ico\" rel=\"icon\" type=\"image/x-icon\" />")
    print("<link href=\"index.css\" rel=\"stylesheet\" type=\"text/css\" />")
    print("</head>")
    print("<body>")
    print("<table>")
    print("<tr>")
    print("<td>")
    print("sputter")
    print("</td>")
    print("</tr>")
    print("</table>")
    body(
        [table,
         [tr,
          [td,
           [
               "money"
           ]
           ]
          ]
         ]
    )
    tr([td, ["money"]])
    td(["money"])

    element.canvas([48, 32])
    element.canvas([112, 335])
    print("<script src=\"type.js\" type=\"text/javascript\"></script>")
    print("<script src=\"index.js\" type=\"text/javascript\"></script>")
    print("</body>")
    print("</html>")


# }
work()

cow = []
pig = ["moo"]
cat = ["dog", "bark"]
print(len(cow))
print(len(pig))
print(len(cat))

list = [poop, 1,2,3]
func = list.pop(0)
param = list
func(param)


[

list = [poop, 1,2,3]
func = list.pop(0)
param = list
func(param)


]
