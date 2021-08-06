

clean:
	-rm -rf molecule/resources/tests/__pycache__
	-rm -rf molecule/*/tests/__pycache__

test: clean
	molecule test -s vagrant
