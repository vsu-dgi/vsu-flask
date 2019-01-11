from flask import Flask, url_for
from flask import render_template
from flask import request
from module_example import some_func

app = Flask(__name__)
app.debug = True

@app.route('/')
def index_page():
	html_template = 'index_ru.html'
	try:
		return render_template(html_template, labname='lab-2', tasks=[1,2,3])
	except Exception as e:
		return e	

@app.route('/task/<tasknum>/', methods=['GET', 'POST'])
def tasks(tasknum):

	output = {'tasknum':tasknum, 'default':'0'}

	if request.method == 'POST':
		input_data = request.form.get('input')
	else:
		input_data = request.args.get('input')

	if input_data is not None and tasknum == '1':
		output['result'] = some_func(float(input_data))
		output['ready'] = True
		output['default'] = input_data
	else:
		output['result'] = 'None'
		output['ready'] = False

	html_template = 'task.html'
	
	return render_template(html_template, output=output)



if __name__ == "__main__":	

	#application.run(debug=True, host='185.72.146.131', port=80)
	#application.run(debug=True, port=80)
	app.run(debug=True, port=8099) # the port number should be changed
	    
