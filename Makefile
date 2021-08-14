

clean:
	-rm -rf molecule/resources/tests/__pycache__
	-rm -rf molecule/*/tests/__pycache__

test: clean
	molecule test -s vagrant

login: clean
	molecule converge -s vagrant && molecule login -s vagrant

destroy:
	molecule destroy -s vagrant

converge:
	molecule converge -s vagrant

verify:
	molecule verify -s vagrant
