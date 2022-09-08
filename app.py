#Generating html document using Jinja2 tenplate
from jinja2 import Template

indexData={"name":"Satvik Chandrakar","ID":"21f1000344","About Myself":""" Hello! I am from Raipur, Chhattisgarh. 
            I am currently pursuing BS in Data Science and Programming from IIT MADRAS. 
            Data has the power to transform the world and I believe that insights generated 
            from it can deliver great value. I love to read and travel."""}

def main():
   #Read the template file content into a variable 
   template_file=open('template.txt','r')
   TEMPLATE= template_file.read()
   template_file.close()

   #Render the template using Jinja 2
   template = Template(TEMPLATE)
   content=template.render(indexData=indexData)

   #Save the rendered html document 
   my_html_document_file= open('index.html','w')
   my_html_document_file.write(content)
   my_html_document_file.close()

if __name__=="__main__":
    # execute only if run as a script 
    main()    