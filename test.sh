if [[ ! $1 == "--raw" ]]; then
	source prepare.sh
fi

python3 main.py --verbose --strategy dummy --arbitration random --expropriation --processors 1 --tasks 3 --durations 2 3 4
