import sys as sys
import os

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	os._exit(0)

	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}

