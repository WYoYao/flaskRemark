from flask import Flask

# 
app=Flask(__name__,template_folder='templatesLeo',root_path='root_pathleo')

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__=='__main__':
    app.run(debug=True)
