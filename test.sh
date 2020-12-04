if [[ ! $1 == "--raw" ]]; then
	source prepare.sh
fi

python3 main.py --verbose --tasks 3 --processors 1 --durations 2 3 4