pages = [
         {
            "filename": "content/index_cont.html",
            "output": "docs/index.html",
            "title": "Homer",
         },
         {
            "filename": "content/connect_cont.html",
            "output": "docs/connect.html",
            "title": "Connect",
         },
         {
            "filename": "content/sign_up_cont.html",
            "output": "docs/sign_up.html",
            "title": "Sign Up",
         }
    ]
    
#dictionary is common to prevent scoping issues

def main():
    for page in pages:
        content =  ( page["filename"])
        location =  ( page["output"])
        #place info into variable which will change as we loop. call the writepage function to name each file as it is being looped
        writepage(content, location)
    
def writepage(content, location):
    #import template files. place in variables
    top_html = open('templates/top.html').read()
    bottom_html = open('templates/bottom.html').read()
    
    #combine with changing content variable 
    finished_index_page = top_html + content + bottom_html
    
    template = open('templates/base.html').read()
    content = open(content).read()
    
    #replace content with the content being called during the loop
    finished_index_page = template.replace("{{content}}", content)
    open(location, 'w+').write(finished_index_page)


#call maine function
if __name__ == "__main__":
    main()
