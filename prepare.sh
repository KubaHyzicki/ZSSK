if [[ ! $(ls venv) ]]; then
	python3 -m virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
else
	deactivate &> /dev/null
	source venv/bin/activate
fi