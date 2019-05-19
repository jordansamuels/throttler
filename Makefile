SYSTEM_PYTHON=python3
VENV=venv
RUNNER=env PYTHONPATH=src $(VENV)/bin/python

demo: .deps
	$(RUNNER) src/throttler/harness.py regression/in/sample1.txt

test: .deps
	$(VENV)/bin/nosetests tests/unit

$(VENV):
	$(SYSTEM_PYTHON) -m venv $@

.deps: $(VENV) requirements.txt
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
	touch $@

clean:
	rm -rf $(VENV) .deps

run_notebooks: .deps
	env PYTHONPATH=../src venv/bin/jupyter notebook --notebook-dir=notebooks

