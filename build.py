



print ('hello')

top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
index_html = open('content/index_cont.html').read()
sign_up_html = open("content/sign_up_cont.html").read()
connect_html = open("content/connect_cont.html").read()

index_page = top_html + index_html + bottom_html
sign_up_page = top_html + sign_up_html + bottom_html
connect_page = top_html + connect_html + bottom_html

open("docs/index-py.html", "w+").write(index_page)
open("docs/sign-up-py.html", "w+").write(sign_up_page)
open("docs/connect-py.html", "w+").write(connect_page)
