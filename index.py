
# Import modules for CGI handling 
import cgi, cgitb

#from __future__ import print_function
b=''
x='Hello World'
y=x.split()
t=len(y)
for i in range(0,t):
        a=y[i]
        n=len(a)-1
        while n>=0:
            if a[n]=='g' and a[n-1]=='n':
                b=b+'ng'
                n=n-2
            else:
                b=b+a[n]
                n=n-1    
        b=b+' '

        
print("""Content-type:text/html\r\n\r\n
    <html>
    <head>
      <title>Hello CGI</title>
    </head>
    <body>
    <h1>""")
print(x+"""</h1>
    Halaman ini dibuat menggunakan Python
    </body>
    </html>""")

    #return b
print(b)

